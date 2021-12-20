<img src="./pybitblock/resources/images/Logo.PNG" width="80%" />

   
    ----------------------
    CPU Usage: X% 
    Memory Usage: X% 
    ----------------------
	
    Local: PyBLOCK
    Node:  XxXxXxX
    Block: XxXxXxX
    Version: X.x.X
    
    A. PyBLOCK
    B. Bitcoin Core
    L. Lightning Network
    P. Platforms
    S. Settings
    X. Donate
    Q. Exit
    
    Select option:     


<br />

<img src="https://pbs.twimg.com/media/Entgg9HXEAI6yea.jpg" width="50%" />

<br />

<img src="https://pbs.twimg.com/media/EpYxp_oWEAE88s-.jpg" width="50%" />

<br />

<img src="https://pbs.twimg.com/media/E5VnuZYXIAAVlVh.jpg" width="50%" />

<br />

<img src="https://pbs.twimg.com/media/FDBefZPWQAQDEVo.jpg" width="50%" />

<br />

<img src="https://pbs.twimg.com/media/FAskRpLXIAgC-fC.jpg" width="50%" />

<br />

<img src="https://pbs.twimg.com/media/FADnL4DXoAIlkwR.jpg" width="50%" />

# PyBlock v1.1.9
ℙ𝕪𝔹𝕃𝕆ℂ𝕂 𝕚𝕥𝕤 𝕒 𝔹𝕚𝕥𝕔𝕠𝕚𝕟 𝔻𝕒𝕤𝕙𝕓𝕠𝕒𝕣𝕕 𝕨𝕚𝕥𝕙 ℂ𝕪𝕡𝕙𝕖𝕣𝕡𝕦𝕟𝕜 𝕒𝕖𝕤𝕥𝕙𝕖𝕥𝕚𝕔.

- This will fully work on a Node that has Bitcoin Core and LND installed.
- We fully tested and worked perfect on [MyNodeBTC](https://twitter.com/_PyBlock_/status/1402516068959199233)
- We fully tested and worked perfect on [RaspiBlitz](https://twitter.com/_PyBlock_/status/1405788110458441728)
- We fully tested and worked perfect on [BitcoinMachines](https://twitter.com/_PyBlock_/status/1365757861217861632)
- We fully tested and worked perfect on [Umbrel](https://twitter.com/_PyBlock_/status/1405574038320201733)

# First Start

- You will need to find the path of the files tls.cert and admin.macaroon to do the REST connection to have access to LND.
- [Poetry](https://python-poetry.org/) is needed to ensure every user has the same python dependencies installed.

    ### From LOCAL Node

    Open the Terminal.

    -- Easy mode:
    * a@A:~> sudo apt install hexyl
    * a@A:~> pip3 install pybitblock
    * a@A:~> pyblock
    
    -- Manual mode:
    * a@A:~> sudo apt install hexyl
    * a@A:~> pip3 install poetry
    * a@A:~> git clone https://github.com/curly60e/pyblock.git
    * a@A:~> cd pyblock
    * a@A:~> poetry install
    * a@A:~> poetry run python3 PyBlock.py

    -- Upgrade:
    * a@A:~> pip3 install pybitblock -U
    * a@A:~> pyblock

    <br />

    - This is how we continue.

    <br />

    <img src="./pybitblock/resources/images/REST1.PNG" width="30%" />

    <br />

    - It will ask you for the IP:PORT (REST PORT) in this case use: localhost instead of the IP.

    <br />

    <img src="./pybitblock/resources/images/REST2.PNG" width="30%" />

    <br />

    - Then it will ask you for the path to the tls.cert.

    <br />

    <img src="./pybitblock/resources/images/REST3.PNG" width="30%" />

    <br />

    - Then it will ask you for the path to the admin.macaroon.

    <br />

    <img src="./pybitblock/resources/images/REST4.PNG" width="30%" />

    <br />  

    - Then it will ask you for the path to bitcoin-cli or if you have already installed just put: bitcoin-cli.

    <br />

    <img src="./pybitblock/resources/images/bitcoin-cli.PNG" width="30%" />

    <br />

    - And you are in.

    <br />

    <img src="./pybitblock/resources/images/main.PNG" width="30%" />

    <br />

    ### From REMOTE Computer

    * You will need to have tls.cert and admin.macaroon already downloaded from your LND node.
    * [Poetry](https://python-poetry.org/) is needed to ensure every user has the same python dependencies installed.

     - Open the Terminal
     
	    -- Easy mode:
	    * a@A:~> sudo apt install hexyl
	    * a@A:~> pip3 install pybitblock
	    * a@A:~> pyblock

	    -- Manual mode:
	    * a@A:~> sudo apt install hexyl
	    * a@A:~> pip3 install poetry
	    * a@A:~> git clone https://github.com/curly60e/pyblock.git
	    * a@A:~> cd pyblock
	    * a@A:~> poetry install
	    * a@A:~> poetry run python3 PyBlock.py

	    -- Upgrade:
	    * a@A:~> pip3 install pybitblock -U
	    * a@A:~> pyblock

        <br />

        - This is how we continue.

        <br />

        <img src="./pybitblock/resources/images/REST1.PNG" width="30%" />

        <br />

        - It will ask you for the IP:PORT (REST PORT).

        <br />

        <img src="./pybitblock/resources/images/REST1REMOTE.PNG" width="30%" />

        <br />

        - Then it will ask you for the path to the tls.cert.

        <br />

        <img src="./pybitblock/resources/images/REST2REMOTE.PNG" width="30%" />

        <br />

        - Then it will ask you for the path to the admin.macaroon.

        <br />

        <img src="./pybitblock/resources/images/REST3REMOTE.PNG" width="30%" />

        <br />  

        - Then it will ask you for the path to bitcoin-cli or if you have already installed just put: bitcoin-cli.

        <br />

        <img src="./pybitblock/resources/images/bitcoin-cli.PNG" width="30%" />

        <br />

        - And you are in.

        <br />

        <img src="./pybitblock/resources/images/main.PNG" width="30%" />

        <br />


## Dependencies

  - Install Curl on Debian based type:
    - sudo apt install curl

## How to execute

  - python3 PyBlock.py


### Created by

[@Curly60e](https://twitter.com/curly60e) ⚡️ curly60e@bitrefill.com

### Testing and contribution by

[@SatoshiNakamoto](https://twitter.com/__B__T__C__)

### Contributor

[@Danvergara...](https://twitter.com/__danvergara__)

### Tools by

[@SamouraiDev,](https://twitter.com/SamouraiDev)
[@Korynewton,](https://twitter.com/kn3wt)
[@Tippin_Me,](https://twitter.com/tippin_me)
[@TallyCoinApp,](https://twitter.com/tallycoinapp)
[@DJBooth007,](https://twitter.com/djbooth007)
[@MemPool,](https://twitter.com/mempool)
[@CoinGecko,](https://twitter.com/coingecko)
[@Igor_Chubin,](https://twitter.com/igor_chubin)
[@Shesek,](https://twitter.com/shesek)
[@LNBits,](https://twitter.com/lnbits)
[@LNPAYco,](https://twitter.com/LNPAYco)
[@OpenNodeCo,](https://twitter.com/OpenNodeCo)
[@BlockStream,](https://twitter.com/Blockstream)
[@Gwidion,](https://twitter.com/gwidion)
[@AlphaaZeta,](https://twitter.com/alphaazeta)
[@Hampus_S,](https://twitter.com/hampus_s)
[@Mutatrum,](https://twitter.com/mutatrum)
[@RoboHash,](https://twitter.com/Robohash)
[@C_Otto83,](https://twitter.com/c_otto83)
[@BashCo_,](https://twitter.com/BashCo_)
[@JamesOb,](https://twitter.com/jamesob)
[@BenTheCarman,](https://twitter.com/benthecarman)
[@Whale_Alert,](https://twitter.com/whale_alert)
[@BitcoinExplorer,](https://twitter.com/BitcoinExplorer)
[@JanoSide,](https://twitter.com/janoside)

SUPPORT PyBLØCK.

Bitcoin Address: bc1qjzaz34nv2ev55vfdu9m5qh0zq0fwcn6c7pkcrv

<img src="/pybitblock/images/bitcoin-donation.png" width="30%" />

Samourai Wallet Paynym: PM8TJhNTTq3YVocXuPtLjKx7pKkdUxqwTerWJ2j2a7dNitgyMmBPN6gK61yE17N2vgvQvKYokXktt6D6GZFTmocvDJhaUJfHt7ehEMmthjsT3NQHseFM

<img src="/pybitblock/images/codeimage.png" width="30%" />

Monero: 42jtb4dAfm6BQ8h6x56qGyAMMHVXGRwRMTSb2LwsBg1jVqD4TxfpD1pTK56tkrTMGhEKipZdDHfJrB1g8iQfvSyC7gZ9M8M

<img src="/pybitblock/images/qrcode.png" width="20%" />
