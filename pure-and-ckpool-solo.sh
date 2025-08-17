#!/bin/bash
#chmod +x pure-and-ckpool-solo.sh
#sudo ./pure-and-ckpool-solo.sh

# Exit on errors
set -e

# Function to detect distro and set package manager
detect_distro() {
    if [ -f /etc/os-release ]; then
        . /etc/os-release
        DISTRO=$ID
    else
        echo "Unsupported distribution. Exiting."
        exit 1
    fi
    case $DISTRO in
        ubuntu|debian)
            PKG_MANAGER="apt"
            INSTALL_CMD="apt install -y"
            UPDATE_CMD="apt update"
            ;;
        fedora|centos|rhel)
            PKG_MANAGER="dnf"  # or yum for older CentOS
            INSTALL_CMD="dnf install -y"
            UPDATE_CMD="dnf check-update"
            ;;
        *)
            echo "Unsupported distribution: $DISTRO. Exiting."
            exit 1
            ;;
    esac
}

# Check if sudo
if [ "$EUID" -ne 0 ]; then
    echo "Please run with sudo or as root."
    exit 1
fi

# Detect previous installation
PREVIOUS_INSTALL=false
if [ -f /etc/systemd/system/bitcoind.service ] || [ -f /etc/systemd/system/ckpool.service ] || [ -d /opt/ckpool ] || [ -d /etc/ckpool ] || [ -d /var/log/ckpool ] || [ -f /usr/local/bin/wait-for-bitcoind-sync.sh ]; then
    PREVIOUS_INSTALL=true
fi

if $PREVIOUS_INSTALL; then
    read -p "Previous installation detected. Overwrite existing files and services(no blockchain data will be deleted)? (y/N, default: no): " overwrite_answer
    if [[ ! "$overwrite_answer" =~ ^[Yy]$ ]]; then
        echo "Installation aborted."
        exit 0
    fi
    echo "Overwriting previous installation..."
    # Stop and disable services if they exist
    systemctl stop ckpool 2>/dev/null || true
    systemctl stop bitcoind 2>/dev/null || true
    systemctl disable ckpool 2>/dev/null || true
    systemctl disable bitcoind 2>/dev/null || true
    # Remove old files
    rm -f /etc/systemd/system/ckpool.service /etc/systemd/system/bitcoind.service
    rm -rf /opt/ckpool /etc/ckpool /var/log/ckpool
    rm -f /usr/local/bin/wait-for-bitcoind-sync.sh
    # Reload systemd
    systemctl daemon-reload
fi

# Main installation
echo "Starting installation of Bitcoin PURE and CKPool-Solo. This requires sudo privileges."
echo "Warning: Bitcoin PURE will download up to ~700GB of blockchain data (or less if pruned). Ensure sufficient disk space."
echo "Important: You cannot mine with CKPool-Solo until the Bitcoin PURE blockchain is fully synchronized, which may take days depending on your hardware and network speed."

# Prompt for service user (default to current sudo user)
current_user=${SUDO_USER:-root}
echo "Optionally, choose a user to run Bitcoin PURE and CKPool as (instead of $current_user)."
echo "Any existing blockchain data in the user's .bitcoin directory will be used."
read -p "Enter existing username, or 'create' to make a new 'ckpool' user (leave blank for $current_user): " input_user
if [ "$input_user" = "create" ]; then
    useradd -m -s /bin/bash ckpool
    service_user="ckpool"
elif [ -z "$input_user" ]; then
    service_user="$current_user"
else
    if id "$input_user" >/dev/null 2>&1; then
        service_user="$input_user"
    else
        echo "User $input_user does not exist. Exiting."
        exit 1
    fi
fi
if [ "$service_user" != "root" ]; then
    HOME_DIR="/home/$service_user"
else
    HOME_DIR="/root"
fi

# Prompt for max disk space
echo "Bitcoin blockchain full size is approximately 700 GB as of August 2025."
read -p "Enter maximum disk space for Bitcoin data in GB (0 for full chain, default: 0): " max_gb
if [ -z "$max_gb" ]; then max_gb=0; fi
if [ "$max_gb" -eq 0 ]; then
    prune_line=""
    required_space=675
else
    prune_mb=$((max_gb * 1024))
    if [ $prune_mb -lt 550 ]; then
        echo "Minimum prune size is 550 MB. Setting to 550 MB."
        prune_mb=550
        max_gb=$((prune_mb / 1024))
    fi
    prune_line="prune=$prune_mb"
    required_space=$max_gb
fi

# Disk space check (add 10% buffer to required_space)
required_space=$((required_space * 110 / 100))
available_space=$(df -k --output=avail "$HOME_DIR" | tail -n 1)
available_space_gb=$((available_space / 1024 / 1024))
if [ "$available_space_gb" -lt "$required_space" ]; then
    echo "Warning: Insufficient disk space. Required: ~${required_space} GB, Available: ${available_space_gb} GB in $HOME_DIR."
    read -p "Continue anyway? (y/N, default: no): " continue_answer
    if [[ ! "$continue_answer" =~ ^[Yy]$ ]]; then
        echo "Installation aborted due to insufficient disk space."
        exit 1
    fi
    echo "Proceeding with installation despite low disk space. This may cause issues."
fi

# Prompt for assumevalid block hash
read -p "To speed up blockchain sync, enter a trusted recent block hash for assumevalid (default: 00000000000000000001e6a5aec8788183793b27370ef638b152b4d02f9f0787 at block 907465, or 0 to disable): " assumevalid_hash
if [ "$assumevalid_hash" = "0" ]; then
    assumevalid_line=""
    echo "Assumevalid disabled. Full blockchain verification will be performed."
elif [ -n "$assumevalid_hash" ]; then
    echo "Warning: Using assumevalid skips signature verification up to this block, reducing security. Ensure the hash is from a trusted source."
    assumevalid_line="assumevalid=$assumevalid_hash"
else
    assumevalid_line="assumevalid=00000000000000000001e6a5aec8788183793b27370ef638b152b4d02f9f0787"
fi

# Prompt for donation to CKPool author
read -p "Support CKPool author with a 0.5% donation on mined blocks? (y/N, default: no): " donation_answer
if [[ "$donation_answer" =~ ^[Yy]$ ]]; then
    donation_line='"donation" : 0.5,'
    echo "Donation of 0.5% enabled. Thank you for supporting CKPool development!"
else
    donation_line=""
    echo "Donation disabled. You can enable it later in /etc/ckpool/ckpool.conf."
fi

# Prompt for coinbase signature
read -p "Enter an optional signature string to include in the coinbase of mined blocks (leave blank for none): " btcsig
if [ -n "$btcsig" ]; then
    btcsig_line="\"btcsig\" : \"$btcsig\","
    echo "Coinbase signature '$btcsig' will be included in mined blocks."
else
    btcsig_line=""
    echo "No coinbase signature set. You can add one later in /etc/ckpool/ckpool.conf."
fi

detect_distro
$UPDATE_CMD

# Install dependencies (for Bitcoin PURE, CKPool build, rpcauth.py, tarball verification, and jq for sync check)
$INSTALL_CMD build-essential git autoconf automake libtool pkg-config yasm libzmq3-dev curl screen libevent-dev libssl-dev bsdmainutils python3 gnupg jq

# Enable persistent journald storage
echo "Enabling persistent journal storage for easier log access..."
mkdir -p /var/log/journal
systemd-tmpfiles --create --prefix /var/log/journal 2>/dev/null || true

# Download and verify Bitcoin PURE tarball
ARCH=$(uname -m)
if [ "$ARCH" = "x86_64" ]; then
    BITCOIN_TAR="archive/refs/tags/PURE.tar.gz"
elif [ "$ARCH" = "aarch64" ]; then
    BITCOIN_TAR="archive/refs/tags/PURE.tar.gz"
else
    echo "Unsupported architecture: $ARCH. Exiting."
    exit 1
fi
BASE_URL="https://github.com/SatoshiNakamotoBitcoin/The-Bitcoin-Pure"
curl -O ${BASE_URL}/${BITCOIN_TAR}

# Extract tarball
tar -zxvf ${BITCOIN_TAR}

# Generate rpcauth using included script
cd The-Bitcoin-Pure-PURE
rpc_output=$(python3 ./share/rpcauth/rpcauth.py ckpooluser)
rpcauth_line=$(echo "$rpc_output" | grep '^rpcauth=')
rpc_password=$(echo "$rpc_output" | tail -1 | sed 's/Your password://' | tr -d '[:space:]')
cd ..

cp -r The-Bitcoin-Pure-PURE/bin/* /usr/local/bin/
rm -rf The-Bitcoin-Pure-PURE ${BITCOIN_TAR}

# Calculate dbcache: 25% of total memory in MB, capped at 8192 MB
total_mem=$(free -m | awk '/Mem:/ {print $2}')
dbcache=$((total_mem * 25 / 100))
if [ $dbcache -gt 8192 ]; then
    dbcache=8192
fi

# Set up Bitcoin PURE config and datadir
DATADIR="$HOME_DIR/.bitcoin"
mkdir -p "$DATADIR"
chown -R $service_user:$service_user "$DATADIR"
cat << EOF > "$DATADIR/bitcoin.conf"
$rpcauth_line
server=1
$prune_line
$assumevalid_line
rpcallowip=127.0.0.1
rpcbind=127.0.0.1
zmqpubhashblock=tcp://127.0.0.1:28332
blockmaxweight=3900000
checkblocks=6
blockreconstructionextratxn=1000
dbcache=$dbcache
EOF

# Install CKPool-Solo
git clone https://bitbucket.org/ckolivas/ckpool.git /opt/ckpool
chown -R $service_user:$service_user /opt/ckpool
cd /opt/ckpool
./autogen.sh
./configure
make
make install

# Set up CKPool config (minimal, per README-SOLOMINING)
mkdir -p /etc/ckpool
cat << EOF > /etc/ckpool/ckpool.conf
{
  $donation_line
  $btcsig_line
  "btcd" : [
    {
      "url" : "127.0.0.1:8332",
      "auth" : "ckpooluser",
      "pass" : "$rpc_password",
      "notify" : true
    }
  ],
  "startdiff" : 1000000,
  "logdir" : "/var/log/ckpool"
}
EOF
mkdir -p /var/log/ckpool
chown -R $service_user:$service_user /etc/ckpool /var/log/ckpool

# Create wait script for bitcoind sync with block progress
cat << EOF > /usr/local/bin/wait-for-bitcoind-sync.sh
#!/bin/bash

echo "Starting wait for bitcoind sync at \$(date)"
echo "Using config file: $DATADIR/bitcoin.conf"
while true; do
    if ! bitcoin-cli -conf="$DATADIR/bitcoin.conf" getblockchaininfo >/dev/null 2>&1; then
        echo "Waiting for bitcoind to start... at \$(date)"
        sleep 60
        continue
    fi
    info=\$(bitcoin-cli -conf="$DATADIR/bitcoin.conf" getblockchaininfo 2>/dev/null)
    if [ \$? -ne 0 ]; then
        echo "Error querying bitcoind: RPC failure at \$(date)"
        sleep 60
        continue
    fi
    synced=\$(echo "\$info" | jq '.initialblockdownload' 2>/dev/null)
    blocks=\$(echo "\$info" | jq '.blocks' 2>/dev/null)
    headers=\$(echo "\$info" | jq '.headers' 2>/dev/null)
    if [ -z "\$synced" ] || [ -z "\$blocks" ] || [ -z "\$headers" ]; then
        echo "Error parsing bitcoind info at \$(date)"
        sleep 60
        continue
    fi
    if [ "\$synced" = "false" ]; then
        echo "Blockchain synced: \$blocks blocks at \$(date)"
        break
    fi
    if [ "\$blocks" -gt 0 ] && [ "\$headers" -gt 0 ]; then
        progress=\$(echo "scale=2; \$blocks * 100 / \$headers" | bc)
        echo "Syncing: \$blocks/\$headers blocks (\${progress}%) at \$(date)"
    else
        echo "Waiting for bitcoind to start syncing... at \$(date)"
    fi
    sleep 60
done
EOF
chmod +x /usr/local/bin/wait-for-bitcoind-sync.sh
chown $service_user:$service_user /usr/local/bin/wait-for-bitcoind-sync.sh

# Create systemd services
cat << EOF > /etc/systemd/system/bitcoind.service
[Unit]
Description=Bitcoin Daemon
After=network.target

[Service]
User=$service_user
ExecStart=/usr/local/bin/bitcoind -conf="$DATADIR/bitcoin.conf" -datadir="$DATADIR" -printtoconsole
Restart=always

[Install]
WantedBy=multi-user.target
EOF

cat << EOF > /etc/systemd/system/ckpool.service
[Unit]
Description=CKPool Solo
After=bitcoind.service

[Service]
User=$service_user
ExecStart=/bin/bash -c '/usr/local/bin/wait-for-bitcoind-sync.sh && exec /usr/local/bin/ckpool -B -q -c /etc/ckpool/ckpool.conf'
StandardOutput=journal
StandardError=journal
Restart=always

[Install]
WantedBy=multi-user.target
EOF

systemctl daemon-reload
systemctl enable bitcoind ckpool
systemctl start bitcoind ckpool

echo "Installation complete! CKPool-Solo is set to start on port 3333 after blockchain sync."
echo "Important: You cannot mine until the Bitcoin PURE blockchain is fully synchronized, which may take days."
echo "Check sync progress with:"
echo "  - journalctl -u ckpool -f (block progress until CKPool starts)"
echo "  - journalctl -u bitcoind -f (detailed sync logs)"
echo "  - tail -f $DATADIR/debug.log (detailed sync logs)"
echo "CKPool startup is delayed until sync completes (monitor with: journalctl -u ckpool -f)."
echo "Connect miners using: stratum+tcp://[machine IP]:3333 with your Bitcoin address as username and 'x' as password. Replace [machine IP] with the IP address of this machine (use ifconfig or ip addr to find it)."
echo "Monitor logs:"
echo "  - CKPool: tail -f /var/log/ckpool/ckpool.log (full logs) or journalctl -u ckpool -f (block progress, then reduced CKPool logs)"
echo "  - Bitcoin PURE: tail -f $DATADIR/debug.log or journalctl -u bitcoind -f"
echo "Edit configs in $DATADIR/bitcoin.conf and /etc/ckpool/ckpool.conf if needed, then restart services with: systemctl restart bitcoind ckpool"
