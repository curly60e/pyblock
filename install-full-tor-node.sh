#!/bin/sh

###############################################################################

REPO_URL="https://github.com/bitcoinknots/bitcoin.git"

VERSION=28.1.knots20250305

TARGET_DIR=$HOME/bitcoin-knots
PORT=8333

BUILD=0
UNINSTALL=0

BLUE='\033[94m'
GREEN='\033[32;1m'
YELLOW='\033[33;1m'
RED='\033[91;1m'
RESET='\033[0m'

ARCH=$(uname -m)
SYSTEM=$(uname -s)
MAKE="make"
if [ "$SYSTEM" = "FreeBSD" ]; then
    MAKE="gmake"
fi
SUDO=""

usage() {
    cat <<EOF

This is the install script for Bitcoin full node based on Bitcoin KNOTS.

Usage: $0 [-h] [-v <version>] [-t <target_directory>] [-p <port>] [-b] [-u]

-h
    Print usage.

-v <version>
    Version of Bitcoin KNOTS to install.
    Default: $VERSION

-t <target_directory>
    Target directory for source files and binaries.
    Default: $HOME/bitcoin-knots

-p <port>
    Bitcoin KNOTS listening port.
    Default: $PORT

-b
    Build and install Bitcoin KNOTS from source.
    Default: $BUILD

-u
    Uninstall Bitcoin KNOTS.

EOF
}

print_info() {
    printf "$BLUE$1$RESET\n"
}

print_success() {
    printf "$GREEN$1$RESET\n"
    sleep 1
}

print_warning() {
    printf "$YELLOW$1$RESET\n"
}

print_error() {
    printf "$RED$1$RESET\n"
    sleep 1
}

print_start() {
    print_info "Start date: $(date)"
}

print_end() {
    print_info "\nEnd date: $(date)"
}

print_readme() {
    cat <<EOF

# README

To stop Bitcoin KNOTS:

    cd $TARGET_DIR/bin && ./stop.sh

To start Bitcoin KNOTS again:

    cd $TARGET_DIR/bin && ./start.sh

To use bitcoin-cli program:

    cd $TARGET_DIR/bin && ./bitcoin-cli -conf=$TARGET_DIR/.bitcoin/bitcoin.conf getnetworkinfo

To view Bitcoin KNOTS log file:

    tail -f $TARGET_DIR/.bitcoin/debug.log

To uninstall Bitcoin KNOTS:

    ./install-full-tor-node.sh -u

EOF
}

program_exists() {
    type "$1" > /dev/null 2>&1
    return $?
}

create_target_dir() {
    if [ ! -d "$TARGET_DIR" ]; then
        print_info "\nCreating target directory: $TARGET_DIR"
        mkdir -p $TARGET_DIR
    fi
}

init_system_install() {
    if [ $(id -u) -ne 0 ]; then
        if program_exists "sudo"; then
            SUDO="sudo"
            print_info "\nInstalling required system packages.."
        else
            print_error "\nsudo program is required to install system packages. Please install sudo as root and rerun this script as normal user."
            exit 1
        fi
    fi
}

install_miniupnpc() {
    print_info "Installing miniupnpc from source.."
    $SUDO rm -rf miniupnpc-2.2.4 miniupnpc-2.2.4.tar.gz &&
        wget -q http://miniupnp.free.fr/files/miniupnpc-2.2.4.tar.gz -O miniupnpc-2.2.4.tar.gz && \
        tar xzf miniupnpc-2.2.4.tar.gz && \
        cd miniupnpc-2.2.4 && \
        $SUDO $MAKE install > build.out 2>&1 && \
        cd .. && \
        $SUDO rm -rf miniupnpc-2.2.4 miniupnpc-2.2.4.tar.gz
}

install_debian_build_dependencies() {
    $SUDO apt-get update
    $SUDO apt-get install -y \
        automake \
        autotools-dev \
        build-essential \
        curl \
        git \
        libboost-all-dev \
        libevent-dev \
        libminiupnpc-dev \
        libssl-dev \
        libtool \
        pkg-config
}

install_centos_build_dependencies() {
    $SUDO yum install -y \
        automake \
        boost-devel \
        curl \
        gcc-c++ \
        git \
        libevent-devel \
        libtool \
        make \
        openssl-devel \
        wget
    install_miniupnpc
    echo '/usr/lib' | $SUDO tee /etc/ld.so.conf.d/miniupnpc-x86.conf > /dev/null && $SUDO ldconfig
}

install_archlinux_build_dependencies() {
    $SUDO pacman -S --noconfirm \
        automake \
        boost \
        curl \
        git \
        libevent \
        libtool \
        miniupnpc \
        openssl
}

install_alpine_build_dependencies() {
    $SUDO apk update
    $SUDO apk add \
        autoconf \
        automake \
        boost-dev \
        build-base \
        curl \
        git \
        libevent-dev \
        libtool \
        openssl-dev
    install_miniupnpc
}

install_mac_build_dependencies() {
    if ! program_exists "gcc"; then
        print_info "When the popup appears, click 'Install' to install the XCode Command Line Tools."
        xcode-select --install
    fi

    if ! program_exists "brew"; then
        /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
    fi

    brew install \
        --c++11 \
        automake \
        boost \
        libevent \
        libtool \
        miniupnpc \
        openssl \
        pkg-config
}

install_freebsd_build_dependencies() {
    $SUDO pkg install -y \
        autoconf \
        automake \
        boost-libs \
        curl \
        git \
        gmake \
        libevent \
        libtool \
        miniupnpc \
        openssl \
        pkgconf \
        wget
}

install_build_dependencies() {
    init_system_install
    case "$SYSTEM" in
        Linux)
            if program_exists "apt-get"; then
                install_debian_build_dependencies
            elif program_exists "yum"; then
                install_centos_build_dependencies
            elif program_exists "pacman"; then
                install_archlinux_build_dependencies
            elif program_exists "apk"; then
                install_alpine_build_dependencies
            else
                print_error "\nSorry, your system is not supported by this installer."
                exit 1
            fi
            ;;
        Darwin)
            install_mac_build_dependencies
            ;;
        FreeBSD)
            install_freebsd_build_dependencies
            ;;
        *)
            print_error "\nSorry, your system is not supported by this installer."
            exit 1
            ;;
    esac
}

build_bitcoin_knots() {
    cd $TARGET_DIR

    if [ ! -d "$TARGET_DIR/bitcoin" ]; then
        print_info "\nDownloading Bitcoin KNOTS source files.."
        git clone --quiet $REPO_URL
    fi

    cxxflags=""
    ldflags=""
    if [ "$SYSTEM" = "Linux" ]; then
        ram_kb=$(grep MemTotal /proc/meminfo | awk '{print $2}')
        if [ $ram_kb -lt 1500000 ]; then
            # Tune gcc to use less memory on single board computers.
            cxxflags="--param ggc-min-expand=1 --param ggc-min-heapsize=32768"
        fi
    fi
    if [ "$SYSTEM" = "FreeBSD" ]; then
        cxxflags="-I/usr/local/include"
        ldflags="-L/usr/local/lib"
    fi

    print_info "\nBuilding Bitcoin KNOTS v$VERSION"
    print_info "Build output: $TARGET_DIR/bitcoin/build.out"
    print_info "This can take up to an hour or more.."
    rm -f build.out
    cd bitcoin &&
        tor &&
        git fetch > build.out 2>&1 &&
        git checkout "v$VERSION" 1>> build.out 2>&1 &&
        git clean -f -d -x 1>> build.out 2>&1 &&
        ./autogen.sh 1>> build.out 2>&1 &&
        ./configure \
            CXXFLAGS="$cxxflags" \
            LDFLAGS="$ldflags" \
            --disable-maintainer-mode \
            --without-gui \
            --with-miniupnpc \
            --disable-wallet \
            --disable-tests \
            1>> build.out 2>&1 &&
        $MAKE 1>> build.out 2>&1

    if [ ! -f "$TARGET_DIR/bitcoin/src/bitcoind" ]; then
        print_error "Build failed. See $TARGET_DIR/bitcoin/build.out"
        exit 1
    fi
}

get_bin_url() {
    url="https://bitcoinknots.org/files/28.x/$VERSION"
    case "$SYSTEM" in
        Linux)
            if program_exists "apk"; then
                echo ""
            elif [ "$ARCH" = "armv7l" ]; then
                url="$url/bitcoin-$VERSION-arm-linux-gnueabihf.tar.gz"
                echo "$url"
            else
                url="$url/bitcoin-$VERSION-$ARCH-linux-gnu.tar.gz"
                echo "$url"
            fi
            ;;
        Darwin)
            url="$url/bitcoin-$VERSION-$ARCH-apple-darwin.tar.gz"
            echo "$url"
            ;;
        FreeBSD)
            echo ""
            ;;
        *)
            echo ""
            ;;
    esac
}

download_bin() {
    checksum_url="https://bitcoinknots.org/files/28.x/$VERSION/SHA256SUMS"

    cd $TARGET_DIR

    rm -f bitcoin-$VERSION.tar.gz checksum.asc

    print_info "\nDownloading Bitcoin KNOTS binaries.."
    if program_exists "wget"; then
        wget -q "$1" -O bitcoin-$VERSION.tar.gz &&
            wget -q "$checksum_url" -O checksum.asc &&
            mkdir -p bitcoin-$VERSION &&
            tar xzf bitcoin-$VERSION.tar.gz -C bitcoin-$VERSION --strip-components=1
    elif program_exists "curl"; then
        curl -s "$1" -o bitcoin-$VERSION.tar.gz &&
            curl -s "$checksum_url" -o checksum.asc &&
            mkdir -p bitcoin-$VERSION &&
            tar xzf bitcoin-$VERSION.tar.gz -C bitcoin-$VERSION --strip-components=1
    else
        print_error "\nwget or curl program is required to continue. Please install wget or curl as root and rerun this script as normal user."
        exit 1
    fi

    if program_exists "shasum"; then
        checksum=$(shasum -a 256 bitcoin-$VERSION.tar.gz | awk '{ print $1 }')
        if grep -q "$checksum" checksum.asc; then
            print_success "Checksum passed: bitcoin-$VERSION.tar.gz ($checksum)"
        else
            print_error "Checksum failed: bitcoin-$VERSION.tar.gz ($checksum). Please rerun this script to download and validate the binaries again."
            exit 1
        fi
    fi

    rm -f bitcoin-$VERSION.tar.gz checksum.asc
}

install_bitcoin_knots() {
    cd $TARGET_DIR

    print_info "\nInstalling Bitcoin KNOTS v$VERSION"

    if [ ! -d "$TARGET_DIR/bin" ]; then
        mkdir -p $TARGET_DIR/bin
    fi

    if [ ! -d "$TARGET_DIR/.bitcoin" ]; then
        mkdir -p $TARGET_DIR/.bitcoin
    fi

    if [ "$SYSTEM" = "Darwin" ]; then
        if [ ! -e "$HOME/Library/Application Support/Bitcoin" ]; then
            ln -s $TARGET_DIR/.bitcoin "$HOME/Library/Application Support/Bitcoin"
        fi
    else
        if [ ! -e "$HOME/.bitcoin" ]; then
            ln -s $TARGET_DIR/.bitcoin $HOME/.bitcoin
        fi
    fi

    if [ -f "$TARGET_DIR/bitcoin/src/bitcoind" ]; then
        # Install compiled binaries.
        cp "$TARGET_DIR/bitcoin/src/bitcoind" "$TARGET_DIR/bin/" &&
            cp "$TARGET_DIR/bitcoin/src/bitcoin-cli" "$TARGET_DIR/bin/" &&
            print_success "Bitcoin KNOTS v$VERSION (compiled) installed successfully!"
    elif [ -f "$TARGET_DIR/bitcoin-$VERSION/bin/bitcoind" ]; then
        # Install downloaded binaries.
        cp "$TARGET_DIR/bitcoin-$VERSION/bin/bitcoind" "$TARGET_DIR/bin/" &&
            cp "$TARGET_DIR/bitcoin-$VERSION/bin/bitcoin-cli" "$TARGET_DIR/bin/" &&
                rm -rf "$TARGET_DIR/bitcoin-$VERSION"
            print_success "Bitcoin KNOTS v$VERSION (binaries) installed successfully!"
    else
        print_error "Cannot find files to install."
        exit 1
    fi

    cat > $TARGET_DIR/.bitcoin/bitcoin.conf <<EOF
### IPv4/IPv6 mode ###
# This mode requires uPnP feature on your router to allow Bitcoin KNOTS to accept incoming connections.
#bind=0.0.0.0
upnp=0

### Tor mode ###
# This mode requires tor (https://www.torproject.org/download/) to be running at the proxy address below.
# No configuration is needed on your router to allow Bitcoin KNOTS to accept incoming connections.
proxy=127.0.0.1:9050
bind=127.0.0.1
onlynet=onion

listen=1
port=$PORT
maxconnections=64
datacarrier=0
permitbaremultisig=0

dbcache=5555
par=4
checkblocks=24
checklevel=0

disablewallet=1
uacomment=PyBLOCK Crew
txindex=0
prune=1000
server=1

rpccookiefile=$TARGET_DIR/.bitcoin/.cookie
rpcbind=127.0.0.1
rpcport=8332
rpcallowip=127.0.0.1
EOF
    chmod go-rw $TARGET_DIR/.bitcoin/bitcoin.conf

    cat > $TARGET_DIR/bin/start.sh <<EOF
#!/bin/sh
if [ -f $TARGET_DIR/bin/bitcoind ]; then
    $TARGET_DIR/bin/bitcoind -conf=$TARGET_DIR/.bitcoin/bitcoin.conf -datadir=$TARGET_DIR/.bitcoin -daemon
fi
EOF
    chmod ugo+x $TARGET_DIR/bin/start.sh

    cat > $TARGET_DIR/bin/stop.sh <<EOF
#!/bin/sh
if [ -f $TARGET_DIR/.bitcoin/bitcoind.pid ]; then
    kill \$(cat $TARGET_DIR/.bitcoin/bitcoind.pid)
fi
EOF
    chmod ugo+x $TARGET_DIR/bin/stop.sh
}

start_bitcoin_knots() {
    if [ ! -f $TARGET_DIR/.bitcoin/bitcoind.pid ]; then
        print_info "\nStarting Bitcoin KNOTS.."
        cd $TARGET_DIR/bin && ./start.sh

        timer=0
        until [ -f $TARGET_DIR/.bitcoin/bitcoind.pid ] || [ $timer -eq 5 ]; do
            timer=$((timer + 1))
            sleep $timer
        done

        if [ -f $TARGET_DIR/.bitcoin/bitcoind.pid ]; then
            print_success "Bitcoin KNOTS is running!"
        else
            print_error "Failed to start Bitcoin KNOTS."
            exit 1
        fi
    fi
}

stop_bitcoin_knots() {
    if [ -f $TARGET_DIR/.bitcoin/bitcoind.pid ]; then
        print_info "\nStopping Bitcoin KNOTS.."
        cd $TARGET_DIR/bin && ./stop.sh

        timer=0
        until [ ! -f $TARGET_DIR/.bitcoin/bitcoind.pid ] || [ $timer -eq 120 ]; do
            timer=$((timer + 1))
            sleep $timer
        done

        if [ ! -f $TARGET_DIR/.bitcoin/bitcoind.pid ]; then
            print_success "Bitcoin KNOTS stopped."
        else
            print_error "Failed to stop Bitcoin KNOTS."
            exit 1
        fi
    fi
}

check_bitcoin_knots() {
    if [ -f $TARGET_DIR/.bitcoin/bitcoind.pid ]; then
        if [ -f $TARGET_DIR/bin/bitcoin-cli ]; then
            print_info "\nChecking Bitcoin KNOTS in 30 seconds.."
            sleep 30 
            $TARGET_DIR/bin/bitcoin-cli -conf=$TARGET_DIR/.bitcoin/bitcoin.conf -datadir=$TARGET_DIR/.bitcoin getnetworkinfo
        fi

        reachable=$(curl -I https://bitnodes.io/api/v1/nodes/me-$PORT/ 2> /dev/null | head -n 1 | cut -d ' ' -f2)
        if [ $reachable -eq 200 ]; then
            print_success "Bitcoin KNOTS is accepting incoming connections at port $PORT!"
        else
            print_warning "Bitcoin KNOTS is not accepting incoming connections at port $PORT. You may need to configure port forwarding on your router."
        fi
    fi
}

uninstall_bitcoin_knots() {
    stop_bitcoin_knots

    if [ -d "$TARGET_DIR" ]; then
        print_info "\nUninstalling Bitcoin KNOTS.."
        rm -rf $TARGET_DIR

        # Remove stale symlink.
        if [ "$SYSTEM" = "Darwin" ]; then
            if [ -L "$HOME/Library/Application Support/Bitcoin" ] && [ ! -d "$HOME/Library/Application Support/Bitcoin" ]; then
                rm "$HOME/Library/Application Support/Bitcoin"
            fi
        else
            if [ -L $HOME/.bitcoin ] && [ ! -d $HOME/.bitcoin ]; then
                rm $HOME/.bitcoin
            fi
        fi

        if [ ! -d "$TARGET_DIR" ]; then
            print_success "Bitcoin KNOTS uninstalled successfully!"
        else
            print_error "Uninstallation failed. Is Bitcoin KNOTS still running?"
            exit 1
        fi
    else
        print_error "Bitcoin KNOTS not installed."
    fi
}

while getopts ":v:t:p:bu" opt
do
    case "$opt" in
        v)
            VERSION=${OPTARG}
            ;;
        t)
            TARGET_DIR=${OPTARG}
            ;;
        p)
            PORT=${OPTARG}
            ;;
        b)
            BUILD=1
            ;;
        u)
            UNINSTALL=1
            ;;
        h)
            usage
            exit 0
            ;;
        ?)
            usage >& 2
            exit 1
            ;;
    esac
done

WELCOME_TEXT=$(cat <<EOF

Welcome Cypherpunk!

You are about to install a Bitcoin full node based on Bitcoin KNOTS v$VERSION.

All files will be installed under $TARGET_DIR directory.

Your node will be configured to accept incoming connections from other nodes in
the Bitcoin network by using uPnP feature on your router.

For security reason, wallet functionality is not enabled by default.

After the installation, it may take several hours for your node to download a
full copy of the blockchain.

If you wish to uninstall Bitcoin KNOTS later, you can download this script and
run "sh install-full-tor-node.sh -u".

EOF
)

print_start

if [ $UNINSTALL -eq 1 ]; then
    echo
    read -p "WARNING: This will stop Bitcoin KNOTS and uninstall it from your system. Uninstall? (y/n) " answer
    if [ "$answer" = "y" ]; then
        uninstall_bitcoin_knots
    fi
else
    echo "$WELCOME_TEXT"
    if [ -t 0 ]; then
        # Prompt for confirmation when invoked in tty.
        echo
        read -p "Install? (y/n) " answer
    else
        # Continue installation when invoked via pipe, e.g. curl .. | sh
        answer="y"
        echo
        echo "Starting installation in 15 seconds.."
        sleep 15
    fi
    if [ "$answer" = "y" ]; then
        if [ "$BUILD" -eq 0 ]; then
            bin_url=$(get_bin_url)
        else
            bin_url=""
        fi
        stop_bitcoin_knots
        create_target_dir
        if [ "$bin_url" != "" ]; then
            download_bin "$bin_url"
        else
            install_build_dependencies && build_bitcoin_knots
        fi
        install_bitcoin_knots && start_bitcoin_knots && check_bitcoin_knots
        print_readme > $TARGET_DIR/README.md
        cat $TARGET_DIR/README.md
        print_success "If this is your first install, Bitcoin KNOTS may take several hours/days to download a full copy of the blockchain."
        print_success "\nMeanwhile you can install PyBLOCK to Manage your Bitcoin Node copying and pasting this commands:"
        print_success "\nCopy and save this route before proceeding: ./../../../..$TARGET_DIR/bin/bitcoin-cli"
        print_success "\ngit clone https://github.com/curly60e/pyblock.git \ncd pyblock \npip3 install -r requirements.txt \ncd pybitblock \npython3 PyBlock.py"
        print_success "\nSelect the Option B."
        print_success "\nLeave in BLANK ip:port, rpcuser, rpcpass and paste this Path to Bitcoin-cli: ./../../../..$TARGET_DIR/bin/bitcoin-cli"
        print_success "\nPyBLOCK Crew!"
        print_success "\nInstallation completed!"
    fi
fi

print_end
