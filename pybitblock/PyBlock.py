#Developer: Curly60e
#Tester: __B__T__C__
#ℙ𝕪𝔹𝕃𝕆ℂ𝕂 𝕚𝕥𝕤 𝕒 𝔹𝕚𝕥𝕔𝕠𝕚𝕟 𝔻𝕒𝕤𝕙𝕓𝕠𝕒𝕣𝕕 𝕨𝕚𝕥𝕙 ℂ𝕪𝕡𝕙𝕖𝕣𝕡𝕦𝕟𝕜 𝕒𝕖𝕤𝕥𝕙𝕖𝕥𝕚𝕔.

import codecs
import os
import os.path
import time as t
import psutil
import html2text
import qrcode
import random
import xmltodict
import sys
import subprocess
import requests
import json
import lastblockdetail
import block_visualizer
import mempool_monitor
import asyncio
import peers_monitor
import tx_search
from block_explorer import call_blocks
from node_monitor import run_display_node_info
from imgterminal import createimagebitaxe, set_terminal_background
from datetime import datetime, timedelta
from sha256 import ex
from cfonts import render, say
from clone import gitclone, satnode
from donation import donationAddr, donationPayNym, donationLN, donationAddrTst, donationLNTst, decodeQR
from feed import readFile
from logos import logoA, logoB, logoC
from sysinf import sysinfoDetail
from pblogo import blogo, tick
from apisnd import apisender, apisenderFile
from ppi import (
    opreturnOnchainONLY, opreturn, opreturn_view, opretminer, gameroom,
    statsConn, pgpConn, mtConn, satoshiConn, whalalConn, bwtConn,
    datesConn, quotesConn, miningConn, stalnConn, ranConn, CoingeckoPP,
    OwnNodeMinerComputer, OwnNodeMinerRaspberry, wttrDataV1, wttrDataV2,
    rateSXList, rateSXGraph, lnbitCreateNewInvoice, lnbitPayInvoice,
    lnbitCreatePayWall, lnbitDeletePayWall, lnbitsLNURLw, lnbitsLNURLwList,
    lnbitListPawWall, createFileConnOpenNode, OpenNodecreatecharge,
    OpenNodeiniciatewithdrawal, OpenNodelistfunds, OpenNodeListPayments,
    OpenNodeCheckStatus, tippinmeGetInvoice, blocks, fee,
)
from termcolor import colored, cprint
from nodeconnection import (
    remoteHalving, remotegetblock, remotegetblockcount, remoteconsole,
    runthenumbersConn, consoleLN, localaddinvoice, localpayinvoice,
    localkeysend, localnewaddress, locallistinvoices, localchannelbalance,
    locallistchannels, localrebalancelnd, locallistpeersQQ, localconnectpeer,
    localbalanceOC, locallistchaintxns, localgetinfo, localgetnetworkinfo,
    localchatsendA, localchatnewA, localchatlistA, localchatsendB,
    localchatnewB, localchatlistB, localchatsendC, localchatnewC,
    localchatlistC, getnewinvoice, payinvoice, getnewaddress, listinvoice,
    getinfo, channels, channelbalance, listonchaintxs, balanceOC,
)
from terminal_matrix.matrix import doit
from PIL import Image
from robohash import Robohash
from binascii import unhexlify
from embit import bip39
from embit.wordlists.bip39 import WORDLIST
from config import cfg
from menu import select_color
from log import get_logger
from shared.display import clear, close, sysinfo, rectangle, delay_print
from shared.formatting import get_ansi_color_code, get_color
from shared.ui import status_bar, show_error, loading
from shared.rich_ui import (
    console, rich_status_bar, rich_header, rich_menu, rich_error, rich_prompt
)
logger = get_logger("PyBlock")


version = "4.0"

def rpc(method, params=None):
    if params is None:
        params = []
    payload = json.dumps({
        "jsonrpc": "2.0",
        "id": "minebet",
        "method": method,
        "params": params
    })
    return requests.post(cfg.path['ip_port'], auth=(cfg.path['rpcuser'], cfg.path['rpcpass']), data=payload).json()['result']

def pathexec():
    global path
    path = cfg.path

def lndconnectexec():
    global lndconnectload
    lndconnectload = cfg.lndconnectload
#-----------------------------Slush--------------------------------

def counttxs():
    try:
        bitcoinclient = f'{path["bitcoincli"]} getblockcount'
        block = subprocess.run(str(bitcoinclient).split(), capture_output=True, text=True).stdout # 'getblockcount' convert to string
        b = block
        a = b
        pathexec()
        clear()
        getrawmempool = " getrawmempool"
        gnaa = subprocess.run([path['bitcoincli']] + getrawmempool.split(), capture_output=True, text=True).stdout
        gna1 = str(gnaa)
        d = json.loads(gna1)
        e = len(d)
        n = e / 10
        nn = n
        getrawmempool = " getrawmempool"
        while True:
            x = a
            bitcoinclient = f'{path["bitcoincli"]} getblockcount'
            block = subprocess.run(str(bitcoinclient).split(), capture_output=True, text=True).stdout # 'getblockcount' convert to string
            b = block
            pathexec()
            gnaa = subprocess.run([path['bitcoincli']] + getrawmempool.split(), capture_output=True, text=True).stdout
            gna1 = str(gnaa)
            d = json.loads(gna1)
            e = len(d)
            n = e / 10
            if e > nn:
                clear()
                outputtxs = render(
                    f'{e} txs',
                    colors=[settingsClock['colorA'], settingsClock['colorB']],
                    align='center',
                    font='tiny',
                )

                print("\x1b[?25l" + outputtxs)
                shq = int(n)
                ss = str(rectangle(shq))
                qq = ss.replace("None","")
                print(f"\033[A{qq}\033[A")
                nn = e
            if b > a:
                print("\n\n\n")
                output = render(str(b), colors=[settingsClock['colorA'], settingsClock['colorB']], align='center', font='tiny')
                print("\a\x1b[?25l" + output)
                bitcoinclient = f'{path["bitcoincli"]} getbestblockhash'
                bb = subprocess.run(str(bitcoinclient).split(), capture_output=True, text=True).stdout
                ll = bb
                bitcoinclientgetblock = f'{path["bitcoincli"]} getblock {ll}'
                qq = subprocess.run(bitcoinclientgetblock.split(), capture_output=True, text=True).stdout
                yy = json.loads(qq)
                mm = yy
                outputtxs = render(str(mm['nTx']) + " txs", colors=[settingsClock['colorA'], settingsClock['colorB']], align='center', font='tiny')
                print("\x1b[?25l" + outputtxs)
                sh = int(mm['nTx']) / 10
                shq = int(sh)
                ss = str(rectangle(shq))
                print(ss.replace("None",""))
                t.sleep(5)
                txs = str(mm['nTx'])
                if txs == "1":
                    try:
                        p = subprocess.Popen(['curl', 'https://ascii.live/forrest'])
                        p.wait(5)
                    except subprocess.TimeoutExpired:
                        p.kill()
                print("\033[0;37;40m\x1b[?25l")
                clear()
                a = b
                nn = e
    except Exception as e:
        show_error(str(e))
        logger.debug("Suppressed error: %s", e)

def slDIFFConn():
    try:
        conn = """curl -s https://insights.braiins.com/api/v1.0/difficulty-stats"""
        a = subprocess.run(conn.split(), capture_output=True, text=True).stdout
        clear()
        blogo()
        closed()
        output = render("difficulty", colors=['yellow'], align='left', font='tiny')
        print(output)
        b = json.loads(a)
        print(f"""\n

            Block epoch: {b['block_epoch']}
            Difficulty: {b['difficulty']}
            Epoch block time: {b['epoch_block_time']}
            Estimated adjustment: {b['estimated_adjustment']}
            Estimated adjustemnt date: {b['estimated_adjustment_date']}
            Estimated next differece: {b['estimated_next_diff']}
            Previous adjustment: {b['previous_adjustment']}

        """)
        input("\a\nContinue...")
    except Exception as e:
        show_error(str(e))
        logger.debug("Suppressed error: %s", e)

def slPOOLConn():
    try:
        conn = """curl -s https://insights.braiins.com/api/v1.0/pool-stats?json=1 | jq -C '.[]' | tr -d '{|}|]|,' | xargs -L 1 | grep -E " " """
        a = subprocess.run(conn.split(), capture_output=True, text=True).stdout
        clear()
        blogo()
        closed()
        output = render("pool", colors=['yellow'], align='left', font='tiny')
        print(output)
        print(a)
        input("\a\nContinue...")
    except Exception as e:
        show_error(str(e))
        logger.debug("Suppressed error: %s", e)

def getPoolSlushCheck():

    s = ""
    sq = s

    api = ""
    try:
        if os.path.isfile("config/braiinsAPI.conf"):
            apiv = json.load(open("config/braiinsAPI.conf", "r"))
            api = apiv
        else:
            clear()
            blogo()
            api = input("Insert Braiins API KEY: ")
            with open("config/braiinsAPI.conf", "w") as f: json.dump(api, f, indent=2)
    except Exception as e:
        show_error(str(e))
        logger.debug("Suppressed error: %s", e)

    while True:
        try:
            slushpoolbtc = f"curl https://pool.braiins.com/accounts/profile/json/btc/ -H 'SlushPool-Auth-Token:{api}' 2>/dev/null"

            slushpoolbtcblock = f"curl https://pool.braiins.com/stats/json/btc/ -H 'SlushPool-Auth-Token:{api}' 2>/dev/null"


            c = subprocess.run(slushpoolbtc.split(), capture_output=True, text=True).stdout
            d = json.loads(c)
            f = d['btc']

            cblock = subprocess.run(slushpoolbtcblock.split(), capture_output=True, text=True).stdout
            dblock = json.loads(cblock)
            fblock = dblock['btc']
            eblock = fblock['blocks']
            for i in eblock:
            	qnq = sorted(eblock)
            	for n in qnq:
            		s = n

            if s > sq:
                newblock = f"\a\n\n\t\t\u001b[31;1m    New Block Mined \u001b[38;5;27m{s}\u001b[31;1m! \u001b[38;5;202mFresh sats for you!\033[0;37;40m"

                sq = s
            else:
                newblock = s

            clear()
            blogo()
            print("""\033[A

    --------------------------------------------------------------------------------------------

                        \033[0;37;40mBraiins Pool

                        Username: {}
                        All Time reward: \u001b[38;5;40m{}\033[0;37;40m BTC
                        Today reward: \u001b[33;1m{}\033[0;37;40m BTC
                        Estimated reward: {} BTC
                        All Time reward: {} BTC
                        Hash Rate 5m: {} Gh/s
                        Hash Rate 60m: {} Gh/s
                        Hash Rate 24h: {} Gh/s
                        Hash Rate Scoring: \u001b[38;5;27m{}\033[0;37;40m Gh/s
                        Hash Rate Yesterday: {} Gh/s
                        Connected Workers: {}
                        Disconnected Workers: {}
                        Last Block discovered: {}

    --------------------------------------------------------------------------------------------

            \033[A""".format(d['username'], f['all_time_reward'], f['today_reward'], f['estimated_reward'], f['all_time_reward'], f['hash_rate_5m'], f['hash_rate_60m'], f['hash_rate_24h'], f['shares_yesterday'], f['hash_rate_yesterday'], f['ok_workers'], f['off_workers'],newblock))

            t.sleep(10)

        except Exception as e:
            logger.debug("Loop interrupted: %s", e)
            break


#-----------------------------END Slush--------------------------------

def ckpoolpoolLOCALOnchainONLY():

    s = ""
    sq = s

    api = ""
    try:
        if os.path.isfile("config/CKPOOLAPI.conf"):
            apiv = json.load(open("config/CKPOOLAPI.conf", "r"))
            api = apiv
        else:
            clear()
            blogo()
            api = input("Insert CKPool Wallet.Worker: ")
            with open("config/CKPOOLAPI.conf", "w") as f: json.dump(api, f, indent=2)
    except Exception as e:
        show_error(str(e))
        logger.debug("Suppressed error: %s", e)

    while True:
        try:
            ckpool = f"curl https://solo.ckpool.org/users/{api} 2>/dev/null"


            c = subprocess.run(ckpool.split(), capture_output=True, text=True).stdout
            d = json.loads(c)
            f = d['worker']
            e = f[0]

            clear()
            blogo()
            print("""\033[A

    --------------------------------------------------------------------------------------------

                        \033[0;37;40mCKPool BTC

                        Username: {}
                        Hash Rate 1m: {}
                        Hash Rate 5m: {}
                        Hash Rate 1h: {}
                        Hash Rate 1d: {}
                        Hash Rate 7d: {}
                        Last Share: \u001b[38;5;27m{}\033[0;37;40m
                        Shares: {}
                        Best Share: {}
                        Best Ever: {}
                        Workers: {}

    --------------------------------------------------------------------------------------------

            \033[A""".format(e['workername'], e['hashrate1m'], e['hashrate5m'], e['hashrate1hr'], e['hashrate1d'], e['hashrate7d'], e['lastshare'], e['shares'], e['bestshare'], e['bestever'], d['workers']))

            t.sleep(10)

        except Exception as e:
            logger.debug("Loop interrupted: %s", e)
            break

def callMemL():
    try:
        clear()
        blogo()
        output = render(
            "Mempool-cli", colors=['yellow'], align='left', font='tiny'
        )
        if os.path.isdir ('mempoolcli'):
            subprocess.run(["rm", "-rf", "mempool-cli_2.0.4_Linux_x86_64.tar.gz"], cwd="mempoolcli")
            subprocess.run(["wget", "https://github.com/mempool/mempool-cli/releases/download/v2.0.4/mempool-cli_2.0.4_Linux_x86_64.tar.gz"], cwd="mempoolcli")
        else: # Check if the file 'bclock.conf' is in the same folder
            os.makedirs("mempoolcli", exist_ok=True)
            subprocess.run(["wget", "https://github.com/mempool/mempool-cli/releases/download/v2.0.4/mempool-cli_2.0.4_Linux_x86_64.tar.gz"], cwd="mempoolcli")
            subprocess.run(["tar", "-xvf", "mempool-cli_2.0.4_Linux_x86_64.tar.gz"], cwd="mempoolcli")
        clear()
        blogo()
        print(output)
        subprocess.run(["./mempool-cli"], cwd="mempoolcli")
    except Exception as e:
        logger.debug("Menu error: %s", e)
        menuSelection()

def callMemR():
    try:
        clear()
        blogo()
        output = render(
            "Mempool-cli", colors=['yellow'], align='left', font='tiny'
        )
        if os.path.isdir ('mempoolcli'):
            subprocess.run(["rm", "-rf", "mempool-cli_2.0.4_Linux_arm64.tar.gz"], cwd="mempoolcli")
            subprocess.run(["wget", "https://github.com/mempool/mempool-cli/releases/download/v2.0.4/mempool-cli_2.0.4_Linux_arm64.tar.gz"], cwd="mempoolcli")
        else: # Check if the file 'bclock.conf' is in the same folder
            os.makedirs("mempoolcli", exist_ok=True)
            subprocess.run(["wget", "https://github.com/mempool/mempool-cli/releases/download/v2.0.4/mempool-cli_2.0.4_Linux_arm64.tar.gz"], cwd="mempoolcli")
            subprocess.run(["tar", "-xvf", "mempool-cli_2.0.4_Linux_arm64.tar.gz"], cwd="mempoolcli")
        clear()
        blogo()
        print(output)
        subprocess.run(["./mempool-cli"], cwd="mempoolcli")
    except Exception as e:
        logger.debug("Menu error: %s", e)
        menuSelection()

def MemShellMenu(menunos):
    if menunos in ["A", "a"]:
        callMemL()
    elif menunos in ["B", "b"]:
        callMemR()
    elif platf in ["R", "r"]:
        menuSelection()

def SHS():
    try:
        clear()
        blogo()
        output = render("SHS - Symbolic Hash Satoshi", colors=['yellow'], align='left', font='tiny')
        print(output)
        subprocess.run(["python3", "SHS.py"])
        input("\a\nContinue...")
    except Exception as e:
        logger.debug("Menu error: %s", e)
        menuSelection()

def MemShell():
    clear()
    blogo()
    sysinfo()
    pathexec()
    #lndconnectexec()
    if path['bitcoincli']:
        n = "Local" if path['bitcoincli'] else "Remote"
        bitcoincli = " getblockchaininfo"
        a = subprocess.run([path['bitcoincli']] + bitcoincli.split(), capture_output=True, text=True).stdout
        b = json.loads(a)
        d = b
    else:
        a = "Local" if path['bitcoincli'] else "Remote"
        blk = rpc('getblockchaininfo')
        d = blk

        cert_path = lndconnectload["tls"]
        macaroon = codecs.encode(open(lndconnectload["macaroon"], 'rb').read(), 'hex')
        headers = {'Grpc-Metadata-macaroon': macaroon}
        url = f'https://{lndconnectload["ip_port"]}/v1/getinfo'
        r = requests.get(url, headers=headers, verify=cert_path)
        alias = r.json()
    print("""\t\t
    \033[1;37;40m{}\033[0;37;40m: \033[1;31;40mPyBLOCK\033[0;37;40m
    \033[1;37;40mBlock\033[0;37;40m: \033[1;32;40m{}\033[0;37;40m
    \033[1;37;40mVersion\033[0;37;40m: {}

    \u001b[38;5;202mA.\033[0;37;40m Linux
    \u001b[38;5;202mB.\033[0;37;40m Raspberry-Pi
    \u001b[33;1mEnter.\033[0;37;40m Return
    \n\n\x1b[?25h""".format(n if path['bitcoincli'] else a, d['blocks'], version ))
    MemShellMenu(input("\033[1;32;40mSelect option: \033[0;37;40m"))


def pyblockpoolpoolLOCALOnchainONLY():

    s = ""
    sq = s

    api = ""
    try:
        if os.path.isfile("config/PYBLOCKPOOLAPI.conf"):
            apiv = json.load(open("config/PYBLOCKPOOLAPI.conf", "r"))
            api = apiv
        else:
            clear()
            blogo()
            api = input("Insert your PyBLOCK Pool Wallet: ")
            with open("config/PYBLOCKPOOLAPI.conf", "w") as f: json.dump(api, f, indent=2)
    except Exception as e:
        show_error(str(e))
        logger.debug("Suppressed error: %s", e)

    while True:
        try:
            pyblockpool = f"curl https://pyblock.xyz:8443/users/{api} 2>/dev/null"


            c = subprocess.run(pyblockpool.split(), capture_output=True, text=True).stdout
            d = json.loads(c)
            f = d['worker']
            e = f[0]

            clear()
            blogo()
            print("""\033[A

    --------------------------------------------------------------------------------------------

                        \033[0;37;40mPYBLOCK Pool Miner Stats

                        Username: {}
                        Hash Rate 1m: {}
                        Hash Rate 5m: {}
                        Hash Rate 1h: {}
                        Hash Rate 1d: {}
                        Hash Rate 7d: {}
                        Last Share: \u001b[38;5;27m{}\033[0;37;40m
                        Shares: {}
                        Best Share: {}
                        Best Ever: {}
                        Workers: {}

    --------------------------------------------------------------------------------------------

            \033[A""".format(e['workername'], e['hashrate1m'], e['hashrate5m'], e['hashrate1hr'], e['hashrate1d'], e['hashrate7d'], e['lastshare'], e['shares'], e['bestshare'], e['bestever'], d['workers']))

            t.sleep(10)

        except Exception as e:
            logger.debug("Loop interrupted: %s", e)
            break

def getblock(): # get access to bitcoin-cli with the command getblockchaininfo
    while True:
        try:
            bitcoincli = " getblockchaininfo"
            a = subprocess.run([path['bitcoincli']] + bitcoincli.split(), capture_output=True, text=True).stdout
            b = json.loads(a)
            d = b
            print(d)
            clear()
            blogo()
            close()
            output = render("CHAIN INFO", colors=['yellow'], align='left', font='tiny')
            print(output)
            print("""
            ----------------------------------------------------------------------------
            Chain: {}
            Blocks: {}
            Best BlockHash: {}
            Difficulty: {}
            Verification Progress: {}
            Size on Disk: {}
            Pruned: {}
            ----------------------------------------------------------------------------
            """.format(d['chain'], d['blocks'], d['bestblockhash'], d['difficulty'], d['verificationprogress'], d['size_on_disk'], d['pruned']))
            t.sleep(10)
        except Exception as e:
            logger.debug("Loop interrupted: %s", e)
            break

def searchTXS():
    try:
        gettxout = " gettxout "

        while True:
            clear()
            blogo()
            closed()
            output = render("search txs", colors=['yellow'], align='left', font='tiny')
            print(output)
            tx = input("Search Tx ID: ")
            gnta = subprocess.run([path['bitcoincli']] + (gettxout + tx + " 1").split(), capture_output=True, text=True).stdout
            gnt1 = str(gnta)
            gnt2 = json.loads(gnt1)
            if gnt2['bestblock']:
                clear()
                blogo()
                closed()
                output = render("search txs", colors=['yellow'], align='left', font='tiny')
                print(output)
                scriptPubKey = gnt2['scriptPubKey']
                print("""
    -------------------------------------------------------------------------------
    Tx: \u001b[38;5;40m{} \033[0;37;40m
    -------------------------------------------------------------------------------
    \u001b[31;1mBestblockhash: \u001b[31;1m{}
    \u001b[31;1mConfirmations: \u001b[38;5;27m{}
    \u001b[31;1mAmount: \u001b[38;5;202m{} BTC
    \u001b[31;1mAddress: \u001b[33;1m{}\033[0;37;40m
    -------------------------------------------------------------------------------
                    """.format(tx, gnt2['bestblock'], gnt2['confirmations'], gnt2['value'], scriptPubKey['address']))
            else:
                print("Is this a \u001b[38;5;40m Coinbase\033[0;37;40m tx?")

            input("\n\033[?25l\033[0;37;40m\n\033[AContinue...\033[A")
    except Exception as e:
        show_error(str(e))
        logger.debug("Suppressed error: %s", e)

def untxsConn():
    try:
        while True:
            clear()
            blogo()
            closed()
            output = render(
                "unconfirmed txs", colors=['yellow'], align='left', font='tiny'
            )

            print(output)
            getrawmempool = " getrawmempool"
            gnaa = subprocess.run([path['bitcoincli']] + getrawmempool.split(), capture_output=True, text=True).stdout
            gna1 = str(gnaa)
            d = json.loads(gna1)
            getrawtrans = " getrawtransaction "
            for b in d:
                n = "".join(map(str, b))
                m = getrawtrans + n + " 1"
                gnba = subprocess.run([path['bitcoincli']] + m.split(), capture_output=True, text=True).stdout
                gnb1 = str(gnba)
                abc = json.loads(gnb1)
                ab = abc['vout']
                knz = 'address'
                for value in ab:
                    knx = value['scriptPubKey']
                    if knz in knx:
                        print(
                            f"TxID: \u001b[38;5;40m{b} \033[0;37;40m| \u001b[31;1mAmount: \u001b[38;5;202m{value['value']} BTC \033[0;37;40m| \u001b[31;1mAddress: \u001b[33;1m{knx['address']}\033[0;37;40m | \u001b[31;1mType: \u001b[31;1m{knx['type']}\u001b[33;1m"
                        )

                    else:
                        print(
                            f"TxID: \u001b[38;5;40m{b} \033[0;37;40m| \u001b[31;1mAmount: \u001b[38;5;202m{value['value']} BTC \033[0;37;40m| \u001b[31;1mOP_RETURN: \u001b[38;5;27m{knx['asm']}\033[0;37;40m | \u001b[31;1mType: \u001b[31;1m{knx['type']}\u001b[33;1m"
                        )

                        decodeTX = (
                            path['bitcoincli']
                            + f" getrawtransaction {b}"
                            + " | xxd -r -p | hexyl -n 256"
                        )

                        print("OP_RETURN Hex: ")
                        subprocess.run(decodeTX, shell=True)
                input("\n\033[?25l\033[0;37;40m\n\033[AContinue...\033[A")
    except Exception as e:
        show_error(str(e))
        logger.debug("Suppressed error: %s", e)

def getnewaddressOnchain():
    try:
        clear()
        blogo()
        close()
        qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
        )
        getadd = " getnewaddress"
        getbal = " getbalance"
        getfeemempool = " getmempoolinfo"
        getunconfirm = " getunconfirmedbalance"
        gnaa = subprocess.run([path['bitcoincli']] + getadd.split(), capture_output=True, text=True).stdout
        gna1 = str(gnaa)
        gnbb = subprocess.run([path['bitcoincli']] + getbal.split(), capture_output=True, text=True).stdout
        gnb1 = str(gnbb)
        gnua = subprocess.run([path['bitcoincli']] + getunconfirm.split(), capture_output=True, text=True).stdout
        gnub = str(gnua)
        output = render(
            str(f'{gnb1} BTC'), colors=['yellow'], align='left', font='tiny'
        )

        print("""---------------------------------------------------------------
            {}
---------------------------------------------------------------""".format(output))
        print("Unconfrmed: \u001b[31;1m{} BTC\033[0;37;40m".format(gnub.replace("\n","")))
        print("---------------------------------------------------------------")
        print("\033[1;30;47m")
        qr.add_data(gna1.replace("\n",""))
        qr.print_ascii()
        print("\033[0;37;40m")
        qr.clear()
        print("\x1b[?25l" + "Bitcoin Address: " + gna1)
        gna.close()
        a = gnub
        b = gnb1
        getbal = " getbalance"
        while True:
            x = a
            z = b
            gnbb = subprocess.run([path['bitcoincli']] + getbal.split(), capture_output=True, text=True).stdout
            gnb1 = str(gnbb)
            gnaaq = subprocess.run([path['bitcoincli']] + getfeemempool.split(), capture_output=True, text=True).stdout
            gna1q = str(gnaaq)
            gnua = subprocess.run([path['bitcoincli']] + getunconfirm.split(), capture_output=True, text=True).stdout
            gnub = str(gnua)
            d = json.loads(gna1q)
            if gnub > a or gnb1 > b:
                clear()
                blogo()
                close()
                getadd = " getnewaddress"
                gnaa = subprocess.run([path['bitcoincli']] + getadd.split(), capture_output=True, text=True).stdout
                gna1 = str(gnaa)
                output = render(
                    str(f'{gnb1} BTC'),
                    colors=['yellow'],
                    align='left',
                    font='tiny',
                )

                print("""---------------------------------------------------------------
                    {}
---------------------------------------------------------------""".format(output))
                print("Unconfrmed: \u001b[31;1m{} BTC\033[0;37;40m".format(gnub.replace("\n","")))
                print("---------------------------------------------------------------")
                getfeemempool = " getmempoolinfo"
                gnaaq = subprocess.run([path['bitcoincli']] + getfeemempool.split(), capture_output=True, text=True).stdout
                gna1q = str(gnaaq)
                d = json.loads(gna1q)
                print("\033[1;30;47m")
                qr.add_data(gna1.replace("\n",""))
                qr.print_ascii()
                print("\033[0;37;40m")
                qr.clear()
                print("\x1b[?25l" + "Bitcoin Address: " + gna1)
                gna.close()
                a = gnub
                b = gnb1
            nn = float(d['total_fee']) / float(d['bytes']) * float(100000000)
            print(f"\n\033[ALive Fee: ~{nn} sat/vB \033[A")
            t.sleep(10)
    except Exception as e:
        logger.debug("Wallet menu error: %s", e)
        walletmenuLOCALOnchainONLY()

def gettransactionsOnchain():
    try:
        listtxs = " listunspent"
        while True:
            clear()
            blogo()
            close()
            gnaa = subprocess.run([path['bitcoincli']] + listtxs.split(), capture_output=True, text=True).stdout
            gna1 = str(gnaa)
            d = json.loads(gna1)
            gnbb = subprocess.run([path['bitcoincli'], 'getbalance'], capture_output=True, text=True).stdout
            gnb1 = str(gnbb)
            sort_order = sorted(d, key=lambda x:x['confirmations'], reverse=True)
            output = render("transactions", colors=['yellow'], align='left', font='tiny')
            print(output)
            for q in sort_order:
                print(
                    (
                        (
                            (
                                (
                                    f"TxID: \u001b[38;5;40m{str(q['txid'])}\033[0;37;40m | Amount: "
                                    + f"\u001b[38;5;202m{str(q['amount'])} BTC\033[0;37;40m"
                                )
                                + " | "
                            )
                            + "Conf: "
                        )
                        + f"\u001b[33;1m{str(q['confirmations'])}\033[0;37;40m"
                    )
                )



            print("\nTotal Balance: \u001b[38;5;202m{} BTC \033[0;37;40m".format(gnb1.replace("\n", "")))
            input("\nRefresh...")
    except Exception as e:
        logger.debug("Wallet menu error: %s", e)
        walletmenuLOCALOnchainONLY()

def dumppk(): #
    try:
        clear()
        blogo()
        output = render("Dumpprivkey", colors=['yellow'], align='left', font='tiny')
        print(output)
        responseC = input("Bitcoin Address: ")
        bitcoincli = " dumpprivkey "
        subprocess.run([path['bitcoincli']] + (bitcoincli + responseC).split())
        input("\a\nContinue...")
    except Exception as e:
        logger.debug("Wallet menu error: %s", e)
        walletmenuLOCALOnchainONLY()

def wallmenu(): #
    try:
        clear()
        blogo()
        output = render("Your Wallet info", colors=['yellow'], align='left', font='tiny')
        print(output)
        bitcoincli = " getwalletinfo"
        subprocess.run([path['bitcoincli']] + bitcoincli.split())
        input("\a\nContinue...")
    except Exception as e:
        logger.debug("Wallet menu error: %s", e)
        walletmenuLOCALOnchainONLY()

def inffmenu(): #
    try:
        clear()
        blogo()
        output = render("Address info", colors=['yellow'], align='left', font='tiny')
        print(output)
        responseC = input("Bitcoin Address: ")
        bitcoincli = " getaddressinfo "
        subprocess.run([path['bitcoincli']] + (bitcoincli + responseC).split())
        input("\a\nContinue...")
    except Exception as e:
        logger.debug("Wallet menu error: %s", e)
        walletmenuLOCALOnchainONLY()

def miningmenu(): #
    try:
        clear()
        blogo()
        output = render("Minning info", colors=['yellow'], align='left', font='tiny')
        print(output)
        bitcoincli = " getmininginfo"
        subprocess.run([path['bitcoincli']] + bitcoincli.split())
        input("\a\nContinue...")
    except Exception as e:
        logger.debug("Wallet menu error: %s", e)
        walletmenuLOCALOnchainONLY()

def getblockcount(): # get access to bitcoin-cli with the command getblockcount
    bitcoincli = " getblockcount"
    subprocess.run([path['bitcoincli']] + bitcoincli.split())

def getbestblockhash(): # get access to bitcoin-cli with the command getblockcount
    bitcoincli = " getbestblockhash"
    subprocess.run([path['bitcoincli']] + bitcoincli.split())

def getgenesis(): # get and decode Genesis block
    output = render("genesis", colors=['yellow'], align='left', font='tiny')
    print(output)
    bitcoincli = " getblock 000000000019d6689c085ae165831e934ff763ae46a2a6c172b3f1b60a8ce26f 0 | xxd -r -p | hexyl -n 256"
    subprocess.run([path['bitcoincli']] + bitcoincli.split())

def readHexBlock(): # Hex Decoder using Hexyl on local node
    hexa = input("Add the Block Hash you want to decode: ")
    blocknumber = input("Add the Block number: ")
    decodeBlock = (
        path['bitcoincli']
        + f" getblock {hexa} {blocknumber}"
        + " | xxd -r -p | hexyl -n 256"
    )

    subprocess.run(decodeBlock, shell=True)

def readHexTx(): # Hex Decoder using Hexyl on an external node
    hexa = input("Add the Transaction ID. you want to decode: ")
    decodeTX = (
        path['bitcoincli']
        + f" getrawtransaction {hexa}"
        + " | xxd -r -p | hexyl -n 256"
    )

    subprocess.run(decodeTX, shell=True)

def tmp():
    t.sleep(15)

def console(): # get into the console from bitcoin-cli
    print("\t\033[0;37;40mThis is \033[1;33;40mBitcoin-cli's \033[0;37;40mconsole. Type 'help' for more information.\n\n")
    while True:
        cle = input("\u001b[38;5;202m₿ console >: \033[0;37;40m")
        if cle == "clear":
            clear()
            blogo()
            sysinfo()
            close()
            console()
        lsd0 = subprocess.run([path['bitcoincli']] + cle.split(), capture_output=True, text=True).stdout
        lsd1 = str(lsd0)
        print(lsd1)

def screensv():
    try:
        doit()
    except (KeyboardInterrupt, SystemExit):
        matrix.close()
        clear()
        blogo()
        menu()

#------------------------------------------------------


def some_other_function():
    # Aquí puedes llamar a la función de node_monitor
    run_display_node_info()

def execute_visualizer():
    block_visualizer.run_visualizer()

def artist():
    """Launch the enhanced block clock."""
    from clock import run_clock
    mode = "remote" if not path.get("bitcoincli") else "local"
    run_clock(mode, path, cfg.settings_clock)


#--------------------------------- Hex Block Decoder Functions -------------------------------------

def getrawtx(): # show confirmatins from transactions
    while True:
        try:
            clear()
            blogo()
            close()
            tx = input("Insert your TxID: ")
            if tx == "4a5e1e4baab89f3a32518a88c31bc87f618f76673e2cc77ab2127b7afdeda33b":
                print("""\t\t\n\033[1;35;40mThis transaction it's the first one of the Bitcoin Blockchain on Block 0 by Satoshi Nakamoto.
You can decode that block in HEX and see what's inside.\033[0;37;40m""")
            else:
                bitcoincli = " getrawtransaction "
                lsd0 = subprocess.run([path['bitcoincli']] + (bitcoincli + tx + " 1").split(), capture_output=True, text=True).stdout
                lsd1 = str(lsd0)
                lsda = lsd1.split(',')
                lsdb = lsda[-3]
                lsdc = str(lsdb)
                print(
                    "\033[0;37;40mTransaction "
                    + f"\033[1;31;40m{tx}\033[0;37;40m"
                    + " has:\n"
                    + f"\033[1;31;40m{lsdc}\033[0;37;40m"
                )

                tmp()
                lsd.close()
            input("Continue...")
        except Exception as e:
            logger.debug("Loop interrupted: %s", e)
            break

def runthenumbers():
    bitcoincli = " gettxoutsetinfo"
    subprocess.run([path['bitcoincli']] + bitcoincli.split())
    input("\nContinue...")

def countdownblock():
    bitcoinclient = f'{path["bitcoincli"]} getblockcount'
    block = subprocess.run(str(bitcoinclient).split(), capture_output=True, text=True).stdout # 'getblockcount' convert to string
    b = block
    try:
        a = input("Insert your block target: ")
        clear()
        blogo()
        print("""
        --------------------- BLOCK {} COUNTDOWN ---------------------

         """.format(a))
        n = int(b)
        print("\nCountDown:", b)
        q = int(a) - int(b)
        print(f'Remaining: {str(q)}' + " Blocks\n")
        while a > b:
            try:
                bitcoinclient = f'{path["bitcoincli"]} getblockcount'
                block = subprocess.run(str(bitcoinclient).split(), capture_output=True, text=True).stdout # 'getblockcount' convert to string
                b = block
                if a == b:
                    break
                elif n != int(b):
                    print("CountDown: ", b)
                    q = int(a) - int(b)
                    print(f'Remaining: {str(q)}' + " Blocks\n")
                    n = int(b)
            except Exception as e:
                logger.debug("Loop interrupted: %s", e)
                break
        print(f'#RunTheNumbers {str(a)} PyBLOCK')
        input("\nContinue...")
    except Exception as e:
        logger.debug("Menu error: %s", e)
        menuSelection()

def countdownblockConn():
    b = rpc('getblockcount')
    c = str(b)
    try:
        a = int(input("Insert your block target: "))
        clear()
        blogo()
        print("""
        --------------------- BLOCK {} COUNTDOWN ---------------------

         """.format(a))
        print("\nCountDown:", int(c))
        n = int(c)
        q = a - int(c)
        print(f'Remaining: {str(q)}' + " Blocks\n")
        while a > int(c):
            try:
                b = rpc('getblockcount')
                c = str(b)
                if a == c:
                    break
                elif n != int(c):
                    print("CountDown: ", c)
                    q = a - int(c)
                    print(f'Remaining: {str(q)}' + " Blocks\n")
                    n = int(c)
            except Exception as e:
                logger.debug("Loop interrupted: %s", e)
                break
        print(f'#RunTheNumbers {a} PyBLOCK')
        input("\nContinue...")
    except Exception as e:
        logger.debug("Menu error: %s", e)
        menuSelection()


def localHalving():
    bitcoincli = f'{path["bitcoincli"]} getblockcount'
    block_count = int(subprocess.run(bitcoincli.split(), capture_output=True, text=True).stdout.strip())  # Leer y convertir el conteo de bloques directamente a int

    # Suponemos 64 halvings, aunque técnicamente podrían ser más
    max_halvings = 64
    blocks_per_halving = 210000
    halving_interval = timedelta(days=365 * 4)  # 4 años entre cada halving
    next_halving_date = datetime(2024, 4, 20)  # Fecha del próximo halving conocido

    halving_blocks = [(blocks_per_halving * i, next_halving_date + halving_interval * (i - (block_count // blocks_per_halving + 1))) for i in range(1, max_halvings + 1)]
    block_messages = []

    for index, (halving_point, halving_date) in enumerate(halving_blocks, start=1):
        blocks_to_halving = halving_point - block_count
        if block_count >= halving_point:
            status = f"\033[1;32;40mCOMPLETE {halving_date.year}\033[0;37;40m"
            blocks_to_halving = 0
        else:
            status = f"\033[1;35;40mPENDING {halving_date.year}\033[0;37;40m"

        block_messages.append(f"{index}th Halving: in {blocks_to_halving} Blocks {status}, Est. Date: {halving_date.strftime('%Y-%m-%d')}")

    halving_info = "\n            ".join(block_messages)

    q = f"""
    \033[0;37;40m------------------- HALVING CLOCK -------------------

            {halving_info}

    -------------------------------------------------------
    """
    print(q)
    input("\nContinue...")



def epoch():
    while True:
        try:
            clear()
            blogo()
            output = render("BITCOIN EPOCH CLOCK", colors=['yellow'], align='left', font='tiny')
            print(output)
            bitcoinclient = f'{path["bitcoincli"]} getblockcount'
            block = subprocess.run(str(bitcoinclient).split(), capture_output=True, text=True).stdout # 'getblockcount' convert to string
            b = block
            c = b
            oneh = 0 + int(c) / 2016

            q = """
            \033[0;37;40m------------------- EPOCH CLOCK -------------------

                    Epoch {} Status {}

            ---------------------------------------------------
            """.format("0" if int(c) == 6930000 else oneh,"\033[1;32;40mON\033[0;37;40m")
            print(q)
            t.sleep(2)
        except Exception as e:
            logger.debug("Loop interrupted: %s", e)
            break

#--------------------------------- End Hex Block Decoder Functions -------------------------------------

def pdfconvert():
    path = {"ip_port":"", "rpcuser":"", "rpcpass":"", "bitcoincli":""}
    pathv = json.load(open("config/bclock.conf", "r")) # Load the file 'bclock.conf'
    path = pathv # Copy the variable pathv to 'path'
    if not os.path.isfile("config/bitcoin.pdf"):
        clear()
        blogo()
        close()
        print("""
        -----------------------------------------

                The Bitcoin Whitepaper
                    is not in this
                       directory

        -----------------------------------------

        """)
        a = input("Do you want to download it from the Blockchain? Y/n: ")
        if a in ["y", "Y"]:
            clear()
            blogo()
            close()
            print("""
            ---------------------------------

                    You are going to
                      download the
                    Whitepaper  from
                     the Blockchain

                     This file will
                     be save in the
                      main PyBLOCK
                       folder  as
                       bitcoin.pdf

            ---------------------------------
            """)
            input("Continue...")
            bitcoincli = """seq 0 947 | (while read -r n; do bitcoin-cli gettxout 54e48e5f5c656b26c3bca14a8c95aa583d07ebe84dde3b7dd4a78f4e4186e713 $n | jq -r '.scriptPubKey.asm' | awk '{ print $2 $3 $4 }'; done) | tr -d '\n' | cut -c 17-368600 | xxd -r -p > bitcoin.pdf """
            subprocess.run(bitcoincli, shell=True)
            clear()
            blogo()
            close()
            subprocess.run(["pdf2txt.py", "bitcoin.pdf"])
            input("Continue...")
    else:
        clear()
        blogo()
        close()
        subprocess.run(["pdf2txt.py", "bitcoin.pdf"])
        input("Continue...")

def bip39convert():
    try:
        clear()
        blogo()
        output = render(
            "TinySeed", colors=['yellow'], align='left', font='tiny'
        )
        if os.path.isdir ('TinySeed'):
            print("...pass...")
        else: # Check if the file 'bclock.conf' is in the same folder
            os.makedirs("TinySeed", exist_ok=True)
            subprocess.run(["wget", "https://gist.githubusercontent.com/odudex/a29de0c91c4010a6b4c565d6f29fa0c6/raw/0349754c1b3f218ff61302acd1f346e0027ba215/TinySeed.py"], cwd="TinySeed")
        clear()
        blogo()
        print(output)
        responseC = input("Words to Tiny Seed: ")
        subprocess.run(["python3", "TinySeed.py", responseC], cwd="TinySeed")
        input("\a\nContinue...")
    except Exception as e:
        logger.debug("Menu error: %s", e)
        menuSelection()

#--------------------------------- NYMs -----------------------------------

def robotNym():
    try:
        if path['bitcoincli']:
            lncli = " getinfo"
            lsd = subprocess.run([lndconnectload['ln']] + lncli.split(), capture_output=True, text=True).stdout
            lsd0 = str(lsd)
            alias = json.loads(lsd0)
        else:
            cert_path = lndconnectload["tls"]
            macaroon = codecs.encode(open(lndconnectload["macaroon"], 'rb').read(), 'hex')
            headers = {'Grpc-Metadata-macaroon': macaroon}
            url = f'https://{lndconnectload["ip_port"]}/v1/getinfo'
            r = requests.get(url, headers=headers, verify=cert_path)
            alias = r.json()

        hash = alias['identity_pubkey']
        rh = Robohash(hash)
        rh.assemble(roboset='set1')
        with open("file.png", "wb") as f:
        	rh.img.save(f, format="png")

        img_path = open("file.png", "rb")
        img = Image.open(img_path)

        h = 40
        w = int((img.width / img.height) * 90)

        img = img.resize((w,h), Image.ANTIALIAS)
        img_arr = np.asarray(img)
        h,w,c = img_arr.shape

        for x in range(h):
            for y in range(w):
                pix = img_arr[x][y]
                print(get_color(pix[0], pix[1], pix[2]), sep='', end='')
            print()
        image = "\n\t\t\t\t\t    \u001b[31;1mNode\u001b[38;5;93mNym\033[0;37;40m\n"+ "\n\t         \u001b[33;1m" + alias['identity_pubkey'] + "\033[0;37;40m"
        print(image)
        input("\n\nContinue...")
    except Exception as e:
        logger.debug("Menu error: %s", e)
        menuSelection()


#---------------------------------Sat Sale----------------------------------
def callGitSatSale():
    if not os.path.isdir('SatSale'):
        subprocess.run(["git", "clone", "https://github.com/nickfarrow/SatSale.git"])
    subprocess.run(["python3", "satsale.py"], cwd="SatSale")

#---------------------------------Cashu----------------------------------
def callGitCashu():
    if not os.path.isdir('Cashu'):
        subprocess.run(["pip3", "install", "cashu"])
        os.makedirs("Cashu", exist_ok=True)
    subprocess.run(["cashu"], cwd="Cashu")

#-----------------------------Block Templates--------------------------------

def blockTmpConn():
    try:
        conn = """curl -s https://miningpool.observer/template-and-block | html2text | grep "Template and Block for" -A 13 """
        a = subprocess.run(conn.split(), capture_output=True, text=True).stdout
        clear()
        blogo()
        closed()
        output = render("Templates and Blocks", colors=['yellow'], align='left', font='tiny')
        print(output)
        print(a)
        input("\a\nContinue...")
    except Exception as e:
        show_error(str(e))
        logger.debug("Suppressed error: %s", e)

#-----------------------------END Block Templates--------------------------------
#---------------------------------ocean pool----------------------------------

def oceanH(): # show srings
    try:
        clear()
        blogo()
        output = render(
            "Ocean Hashrate", colors=['yellow'], align='left', font='tiny'
        )

        print(output)
        responseC = input("Your Bitcoin Address: ")
        cmd = f"""curl -s 'https://ocean.xyz/data/csv/hashrates/worker/{responseC}' | html2text """
        a = subprocess.run(cmd.split(), capture_output=True, text=True).stdout
        print("\nAddress: " + responseC)
        print("\nHashrate:\n" + a)
        input("\a\nContinue...")
    except Exception as e:
        show_error(str(e))
        logger.debug("Suppressed error: %s", e)

def oceanB(): # show srings
    try:
        clear()
        blogo()
        output = render(
            "Ocean Blocks", colors=['yellow'], align='left', font='tiny'
        )

        print(output)
        cmd = f"""curl -s 'https://ocean.xyz/data/json/blocksfound' | jq -C .[] """
        a = subprocess.run(cmd.split(), capture_output=True, text=True).stdout
        print("\nBlocks:\n" + a)
        input("\a\nContinue...")
    except Exception as e:
        show_error(str(e))
        logger.debug("Suppressed error: %s", e)

def oceanE(): # show srings
    try:
        clear()
        blogo()
        output = render(
            "Ocean Earnings", colors=['yellow'], align='left', font='tiny'
        )

        print(output)
        responseC = input("Your Bitcoin Address: ")
        cmd = f"""curl -s 'https://ocean.xyz/template/workers/earningscards?user={responseC}' | html2text """
        a = subprocess.run(cmd.split(), capture_output=True, text=True).stdout
        print("\nAddress: " + responseC)
        print("\nEarnings:\n" + a)
        input("\a\nContinue...")
    except Exception as e:
        show_error(str(e))
        logger.debug("Suppressed error: %s", e)

#---------------------------------ocean pool end----------------------------------

#---------------------------------Warden Terminal----------------------------------

def callGitWardenTerminal():
    if not os.path.isdir('warden_terminal'):
        subprocess.run(["git", "clone", "https://github.com/pxsocs/warden_terminal.git"])
    subprocess.run(["python3", "node_warden.py"], cwd="warden_terminal")

#---------------------------------Nostr Terminal----------------------------------

def callGitNostrLinTerminal():
    try:
        clear()
        blogo()
        output = render(
            "Nostr Console Linux", colors=['yellow'], align='left', font='tiny'
        )
        if os.path.isdir ('nostr_console_pyblock'):
            subprocess.run(["rm", "-rf", "nostr_console_linux_amd64"], cwd="nostr_console_pyblock")
            subprocess.run(["wget", "https://raw.githubusercontent.com/curly60e/pyblock/master/pybitblock/nostr_console_pyblock/nostr_console_linux_amd64"], cwd="nostr_console_pyblock")
            subprocess.run(["chmod", "+x", "nostr_console_linux_amd64"], cwd="nostr_console_pyblock")
        else: # Check if the file 'bclock.conf' is in the same folder
            os.makedirs("nostr_console_pyblock", exist_ok=True)
            subprocess.run(["wget", "https://raw.githubusercontent.com/curly60e/pyblock/master/pybitblock/nostr_console_pyblock/nostr_console_linux_amd64"], cwd="nostr_console_pyblock")
            subprocess.run(["chmod", "+x", "nostr_console_linux_amd64"], cwd="nostr_console_pyblock")
        clear()
        blogo()
        print(output)
        responseC = input("Paste your PrivateKey: ")
        subprocess.run(["./nostr_console_linux_amd64", "-k", responseC, "-l"], cwd="nostr_console_pyblock")
    except Exception as e:
        logger.debug("Menu error: %s", e)
        menuSelection()

def callGitNostrLinarmTerminal():
    try:
        clear()
        blogo()
        output = render(
            "Nostr Console Linux", colors=['yellow'], align='left', font='tiny'
        )
        if os.path.isdir ('nostr_console_pyblock'):
            subprocess.run(["rm", "-rf", "nostr_console_linux_arm64"], cwd="nostr_console_pyblock")
            subprocess.run(["wget", "https://raw.githubusercontent.com/curly60e/pyblock/master/pybitblock/nostr_console_pyblock/nostr_console_linux_arm64"], cwd="nostr_console_pyblock")
            subprocess.run(["chmod", "+x", "nostr_console_linux_arm64"], cwd="nostr_console_pyblock")
        else: # Check if the file 'bclock.conf' is in the same folder
            os.makedirs("nostr_console_pyblock", exist_ok=True)
            subprocess.run(["wget", "https://raw.githubusercontent.com/curly60e/pyblock/master/pybitblock/nostr_console_pyblock/nostr_console_linux_arm64"], cwd="nostr_console_pyblock")
            subprocess.run(["chmod", "+x", "nostr_console_linux_arm64"], cwd="nostr_console_pyblock")
        clear()
        blogo()
        print(output)
        responseC = input("Paste your PrivateKey: ")
        subprocess.run(["./nostr_console_linux_arm64", "-k", responseC, "-l"], cwd="nostr_console_pyblock")
    except Exception as e:
        logger.debug("Menu error: %s", e)
        menuSelection()

def callGitNostrMacTerminal():
    try:
        clear()
        blogo()
        output = render(
            "Nostr Console macOS", colors=['yellow'], align='left', font='tiny'
        )
        if os.path.isdir ('nostr_console_pyblock'):
            subprocess.run(["rm", "-rf", "nostr_console_macos_amd64"], cwd="nostr_console_pyblock")
            subprocess.run(["wget", "https://raw.githubusercontent.com/curly60e/pyblock/master/pybitblock/nostr_console_pyblock/nostr_console_macos_amd64"], cwd="nostr_console_pyblock")
        else: # Check if the file 'bclock.conf' is in the same folder
            os.makedirs("nostr_console_pyblock", exist_ok=True)
            subprocess.run(["wget", "https://raw.githubusercontent.com/curly60e/pyblock/master/pybitblock/nostr_console_pyblock/nostr_console_macos_amd64"], cwd="nostr_console_pyblock")
        clear()
        blogo()

        print(output)
        responseC = input("Paste your PrivateKey: ")
        subprocess.run(["./nostr_console_macos_amd64", "-k", responseC, "-l"], cwd="nostr_console_pyblock")
    except Exception as e:
        logger.debug("Menu error: %s", e)
        menuSelection()

def callGitNostrMacarmTerminal():
    try:
        clear()
        blogo()
        output = render(
            "Nostr Console macOS", colors=['yellow'], align='left', font='tiny'
        )
        if os.path.isdir ('nostr_console_pyblock'):
            subprocess.run(["rm", "-rf", "nostr_console_elf64"], cwd="nostr_console_pyblock")
            subprocess.run(["wget", "https://raw.githubusercontent.com/curly60e/pyblock/master/pybitblock/nostr_console_pyblock/nostr_console_elf64"], cwd="nostr_console_pyblock")
            subprocess.run(["chmod", "+x", "nostr_console_elf64"], cwd="nostr_console_pyblock")
        else: # Check if the file 'bclock.conf' is in the same folder
            os.makedirs("nostr_console_pyblock", exist_ok=True)
            subprocess.run(["wget", "https://raw.githubusercontent.com/curly60e/pyblock/master/pybitblock/nostr_console_pyblock/nostr_console_elf64"], cwd="nostr_console_pyblock")
            subprocess.run(["chmod", "+x", "nostr_console_elf64"], cwd="nostr_console_pyblock")
        clear()
        blogo()
        print(output)
        responseC = input("Paste your PrivateKey: ")
        subprocess.run(["./nostr_console_elf64", "-k", responseC, "-l"], cwd="nostr_console_pyblock")
    except Exception as e:
        logger.debug("Menu error: %s", e)
        menuSelection()

def callGitNostrWinTerminal():
    try:
        clear()
        blogo()
        output = render(
            "Nostr Console Windows", colors=['yellow'], align='left', font='tiny'
        )
        if os.path.isdir ('nostr_console_pyblock'):
            subprocess.run(["rm", "-rf", "nostr_console_windows_amd64.exe"], cwd="nostr_console_pyblock")
            subprocess.run(["wget", "https://raw.githubusercontent.com/curly60e/pyblock/master/pybitblock/nostr_console_pyblock/nostr_console_windows_amd64.exe"], cwd="nostr_console_pyblock")
        else: # Check if the file 'bclock.conf' is in the same folder
            os.makedirs("nostr_console_pyblock", exist_ok=True)
            subprocess.run(["wget", "https://raw.githubusercontent.com/curly60e/pyblock/master/pybitblock/nostr_console_pyblock/nostr_console_windows_amd64.exe"], cwd="nostr_console_pyblock")
        clear()
        blogo()
        print(output)
        responseC = input("Paste your PrivateKey: ")
        subprocess.run(["./nostr_console_windows_amd64.exe", "-k", responseC, "-l"], cwd="nostr_console_pyblock")
    except Exception as e:
        logger.debug("Menu error: %s", e)
        menuSelection()

def callGitNostrSeedTerminal():
    try:
        clear()
        blogo()
        output = render(
            "Nostr BIP39", colors=['yellow'], align='left', font='tiny'
        )
        if os.path.isdir ('nostr_seed'):
            print("...pass...")
        else: # Check if the file 'bclock.conf' is in the same folder
            os.makedirs("nostr_seed", exist_ok=True)
            subprocess.run(["wget", "https://gist.githubusercontent.com/odudex/93cfb5628b22f8675ab1939fd43133f4/raw/b48f047c0358a9ae50c2027106bdf5e37ee1fe5c/nostr_seed.py"], cwd="nostr_seed")
        clear()
        blogo()
        print(output)
        responseC = input("Hex to BIP39 & BIP39 to Hex: ")
        subprocess.run(["python3", "nostr_seed.py", responseC], cwd="nostr_seed")
        input("\a\nContinue...")
    except Exception as e:
        logger.debug("Menu error: %s", e)
        menuSelection()

def callGitNostrQRSeedTerminal():
    try:
        clear()
        blogo()
        output = render(
            "QR", colors=['yellow'], align='left', font='tiny'
        )
        if os.path.isdir ('nostr_QRseed'):
            print("...pass...")
        else: # Check if the file 'bclock.conf' is in the same folder
            os.makedirs("nostr_QRseed", exist_ok=True)
            subprocess.run(["wget", "https://gist.githubusercontent.com/odudex/9e848a91d23e967309bd1719910021e6/raw/dbe04893f4ee2e0aa020735528f7f19bb2d13a7e/nostr_c_seed_qr.py"], cwd="nostr_QRseed")
        clear()
        blogo()
        print(output)
        responseC = input("Hex to BIP39 QR & BIP39 to Hex QR: ")
        subprocess.run(["python3", "nostr_c_seed_qr.py", responseC], cwd="nostr_QRseed")
        input("\a\nContinue...")
    except Exception as e:
        logger.debug("Menu error: %s", e)
        menuSelection()

def callGitBija():
    if not os.path.isdir('bija'):
        subprocess.run(["git", "clone", "--recurse-submodules", "https://github.com/BrightonBTC/bija"])
    subprocess.run(["docker-compose", "up"], cwd="bija")
    input("\a\nYou can now access Bija at http://localhost:5000")

#---------------------------------Bpytop----------------------------------
def callGitBpytop():
    if not os.path.isdir('bpytop'):
        subprocess.run(["pip3", "install", "bpytop"])
        subprocess.run(["git", "clone", "https://github.com/aristocratos/bpytop.git"])
    subprocess.run(["sudo", "make", "install"], cwd="bpytop")
    subprocess.run(["bpytop"])

#----------------------------------------------------------------------PhoenixSta
def callPhoenixLin():
    try:
        clear()
        blogo()
        output = render(
            "Phoenix Linux", colors=['yellow'], align='left', font='tiny'
        )
        if os.path.isdir ('phoenixwallet'):
            subprocess.run(["rm", "-rf", "phoenix-0.3.0-linux-x64.zip"], cwd="phoenixwallet")
            subprocess.run(["wget", "https://github.com/ACINQ/phoenixd/releases/download/v0.3.0/phoenix-0.3.0-linux-x64.zip"], cwd="phoenixwallet")
        else: # Check if the file 'bclock.conf' is in the same folder
            os.makedirs("phoenixwallet", exist_ok=True)
            subprocess.run(["wget", "https://github.com/ACINQ/phoenixd/releases/download/v0.3.0/phoenix-0.3.0-linux-x64.zip"], cwd="phoenixwallet")
            subprocess.run(["unzip", "-j", "phoenix-0.3.0-linux-x64.zip"], cwd="phoenixwallet")
        clear()
        blogo()
        input("\a\nYou are going to launch your own Phoenix. Press Enter to Continue.")
        input("\a\nDon't close this window to stay Online. Press Enter to Continue.")
        input("\a\nOpen another Terminal and Select Manage in the Phoenix Menu. Press Enter to Continue.")
        clear()
        blogo()
        print(output)
        subprocess.run(["./phoenixd"], cwd="phoenixwallet")
    except Exception as e:
        logger.debug("Menu error: %s", e)
        menuSelection()

def callPhoenixWin():
    try:
        clear()
        blogo()
        output = render(
            "Phoenix Windows", colors=['yellow'], align='left', font='tiny'
        )
        if os.path.isdir ('phoenixwallet'):
            subprocess.run(["rm", "-rf", "v0.3.0.zip"], cwd="phoenixwallet")
            subprocess.run(["wget", "https://github.com/ACINQ/phoenixd/archive/refs/tags/v0.3.0.zip"], cwd="phoenixwallet")
        else: # Check if the file 'bclock.conf' is in the same folder
            os.makedirs("phoenixwallet", exist_ok=True)
            subprocess.run(["wget", "https://github.com/ACINQ/phoenixd/archive/refs/tags/v0.3.0.zip"], cwd="phoenixwallet")
            subprocess.run(["unzip", "-j", "v0.3.0.zip"], cwd="phoenixwallet")
        clear()
        blogo()
        input("\a\nYou are going to launch your own Phoenix. Press Enter to Continue.")
        input("\a\nDon't close this window to stay Online. Press Enter to Continue.")
        input("\a\nOpen another Terminal and Select Manage in the Phoenix Menu. Press Enter to Continue.")
        clear()
        blogo()
        print(output)
        subprocess.run(["./phoenixd"], cwd="phoenixwallet")
    except Exception as e:
        logger.debug("Menu error: %s", e)
        menuSelection()

def callPhoenixMacX64():
    try:
        clear()
        blogo()
        output = render(
            "Phoenix MacOSX64", colors=['yellow'], align='left', font='tiny'
        )
        if os.path.isdir ('phoenixwallet'):
            subprocess.run(["rm", "-rf", "phoenix-0.3.0-macos-x64.zip"], cwd="phoenixwallet")
            subprocess.run(["wget", "https://github.com/ACINQ/phoenixd/releases/download/v0.3.0/phoenix-0.3.0-macos-x64.zip"], cwd="phoenixwallet")
        else: # Check if the file 'bclock.conf' is in the same folder
            os.makedirs("phoenixwallet", exist_ok=True)
            subprocess.run(["wget", "https://github.com/ACINQ/phoenixd/releases/download/v0.3.0/phoenix-0.3.0-macos-x64.zip"], cwd="phoenixwallet")
            subprocess.run(["unzip", "-j", "phoenix-0.3.0-macos-x64.zip"], cwd="phoenixwallet")
        clear()
        blogo()
        input("\a\nYou are going to launch your own Phoenix. Press Enter to Continue.")
        input("\a\nDon't close this window to stay Online. Press Enter to Continue.")
        input("\a\nOpen another Terminal and Select Manage in the Phoenix Menu. Press Enter to Continue.")
        clear()
        blogo()
        print(output)
        subprocess.run(["./phoenixd"], cwd="phoenixwallet")
    except Exception as e:
        logger.debug("Menu error: %s", e)
        menuSelection()

def callPhoenixMacARM():
    try:
        clear()
        blogo()
        output = render(
            "Phoenix MacOSARM", colors=['yellow'], align='left', font='tiny'
        )
        if os.path.isdir ('phoenixwallet'):
            subprocess.run(["rm", "-rf", "phoenix-0.3.0-macos-arm64.zip"], cwd="phoenixwallet")
            subprocess.run(["wget", "https://github.com/ACINQ/phoenixd/releases/download/v0.3.0/phoenix-0.3.0-macos-arm64.zip"], cwd="phoenixwallet")
        else: # Check if the file 'bclock.conf' is in the same folder
            os.makedirs("phoenixwallet", exist_ok=True)
            subprocess.run(["wget", "https://github.com/ACINQ/phoenixd/releases/download/v0.3.0/phoenix-0.3.0-macos-arm64.zip"], cwd="phoenixwallet")
            subprocess.run(["unzip", "-j", "phoenix-0.3.0-macos-arm64.zip"], cwd="phoenixwallet")
        clear()
        blogo()
        input("\a\nYou are going to launch your own Phoenix. Press Enter to Continue.")
        input("\a\nDon't close this window to stay Online. Press Enter to Continue.")
        input("\a\nOpen another Terminal and Select Manage in the Phoenix Menu. Press Enter to Continue.")
        clear()
        blogo()
        print(output)
        subprocess.run(["./phoenixd"], cwd="phoenixwallet")
    except Exception as e:
        logger.debug("Menu error: %s", e)
        menuSelection()

def callPhoenix():
    try:
        clear()
        blogo()
        output = render(
            "Manage your Phoenix", colors=['yellow'], align='left', font='tiny'
        )
        clear()
        blogo()
        print(output)
        subprocess.run(["./phoenix-cli", "--help"], cwd="phoenixwallet")
        responseC = input("\a\nType a command of the list: ")
        subprocess.run(["./phoenix-cli", responseC], cwd="phoenixwallet")
        responseC = input("\a\nType a command of the list: ")
        subprocess.run(["./phoenix-cli", responseC], cwd="phoenixwallet")
        responseC = input("\a\nType a command of the list: ")
        subprocess.run(["./phoenix-cli", responseC], cwd="phoenixwallet")
        responseC = input("\a\nType a command of the list: ")
        subprocess.run(["./phoenix-cli", responseC], cwd="phoenixwallet")
        responseC = input("\a\nType a command of the list: ")
        subprocess.run(["./phoenix-cli", responseC], cwd="phoenixwallet")
        responseC = input("\a\nType a command of the list: ")
        subprocess.run(["./phoenix-cli", responseC], cwd="phoenixwallet")
        responseC = input("\a\nType a command of the list: ")
        subprocess.run(["./phoenix-cli", responseC], cwd="phoenixwallet")
        responseC = input("\a\nType a command of the list: ")
        subprocess.run(["./phoenix-cli", responseC], cwd="phoenixwallet")
        responseC = input("\a\nType a command of the list: ")
        subprocess.run(["./phoenix-cli", responseC], cwd="phoenixwallet")
        responseC = input("\a\nCType a command of the list: ")
        subprocess.run(["./phoenix-cli", responseC], cwd="phoenixwallet")
        input("\a\nContinue...")
    except Exception as e:
        logger.debug("Menu error: %s", e)
        menuSelection()

def wallPhoenix():
    try:
        clear()
        blogo()
        output = render(
        "PhoenixD Invoice Maker", colors=['yellow'], align='left', font='tiny'
        )
        responseC = input("Your PhoenixD Password: ")
        responseD = input("Your Description: ")
        responseE = input("Amount in Sats: ")
        r = requests.post('http://localhost:9740/createinvoice', auth=('', responseC), data={'description': responseD, 'amountSat': responseE})
        print(r.text)
        input("\a\nContinue...")
    except Exception as e:
        logger.debug("Menu error: %s", e)
        menuSelection()

def wallPhoenixBOLT12():
    try:
        clear()
        blogo()
        output = render(
        "PhoenixD BOLT12 Maker", colors=['yellow'], align='left', font='tiny'
        )
        responseC = input("Your PhoenixD Password: ")
        r = requests.get('http://localhost:9740/getoffer', auth=('', responseC))
        print(r.text)
        input("\a\nContinue...")
    except Exception as e:
        logger.debug("Menu error: %s", e)
        menuSelection()

#----------------------------------------------------------------------PhoenixEnd
#-----------------------------STARTBLOCKS--------------------------------

def allblocksConn():
    try:
        conn = """curl -s https://raw.githubusercontent.com/jlopp/bitcoin-blocks-by-mining-pool/master/blocks.csv """
        a = subprocess.run(conn.split(), capture_output=True, text=True).stdout
        clear()
        blogo()
        closed()
        output = render("All Blocks", colors=['yellow'], align='left', font='tiny')
        print(output)
        print(a)
        input("\a\nContinue...")
    except Exception as e:
        show_error(str(e))
        logger.debug("Suppressed error: %s", e)

#-----------------------------ENDBLOCKS--------------------------------
#-----------------------------STRLuxor--------------------------------

def luxorstats():
    try:
        clear()
        blogo()
        output = render(
            "Luxor Pool", colors=['yellow'], align='left', font='tiny'
        )
        if os.path.isdir ('luxor'):
            subprocess.run(["python3", "luxor.py", "--help"], cwd=os.path.join("luxor", "graphql-python-client"))
        else: # Check if the file 'bclock.conf' is in the same folder
            os.makedirs("luxor", exist_ok=True)
            subprocess.run(["git", "clone", "https://github.com/LuxorLabs/graphql-python-client.git"], cwd="luxor")
            subprocess.run(["pip3", "install", "-r", "requirements3.txt"], cwd=os.path.join("luxor", "graphql-python-client"))
            subprocess.run(["python3", "luxor.py", "--install-completion"], cwd=os.path.join("luxor", "graphql-python-client"))
        clear()
        blogo()
        input("\a\nYou need to COPY the lines inside the file .env.example and create a NEW file .env with your Luxor API Key. Press Enter to Continue.")
        input("\a\nOther way is this 2 commands: 1 - mv .env.example .env 2 - nano .env and paste your Luxor Api Key. Press Enter to Continue.")
        clear()
        blogo()
        print(output)
        subprocess.run(["python3", "luxor.py", "--help"], cwd="luxor/graphql-python-client")
        responseC = input("\a\nType a command of the list: ")
        subprocess.run(["python3", "luxor.py", responseC], cwd="luxor/graphql-python-client")
        responseC = input("\a\nType a command of the list: ")
        subprocess.run(["python3", "luxor.py", responseC], cwd="luxor/graphql-python-client")
        responseC = input("\a\nType a command of the list: ")
        subprocess.run(["python3", "luxor.py", responseC], cwd="luxor/graphql-python-client")
        responseC = input("\a\nType a command of the list: ")
        subprocess.run(["python3", "luxor.py", responseC], cwd="luxor/graphql-python-client")
        responseC = input("\a\nType a command of the list: ")
        subprocess.run(["python3", "luxor.py", responseC], cwd="luxor/graphql-python-client")
        responseC = input("\a\nType a command of the list: ")
        subprocess.run(["python3", "luxor.py", responseC], cwd="luxor/graphql-python-client")
        responseC = input("\a\nType a command of the list: ")
        subprocess.run(["python3", "luxor.py", responseC], cwd="luxor/graphql-python-client")
        responseC = input("\a\nType a command of the list: ")
        subprocess.run(["python3", "luxor.py", responseC], cwd="luxor/graphql-python-client")
        responseC = input("\a\nType a command of the list: ")
        subprocess.run(["python3", "luxor.py", responseC], cwd="luxor/graphql-python-client")
        responseC = input("\a\nCType a command of the list: ")
        subprocess.run(["python3", "luxor.py", responseC], cwd="luxor/graphql-python-client")
        input("\a\nContinue...")
    except Exception as e:
        logger.debug("Menu error: %s", e)
        menuSelection()

#-----------------------------ENDLuxor--------------------------------
#---------------------------------UTXOracle----------------------------------
def callGitUTXOracle():
    try:
        clear()
        blogo()
        output = render(
            "UTXORACLE", colors=['yellow'], align='left', font='tiny'
        )
        if os.path.isdir ('utxoracle'):
            print("...Reading UTXOSet...")
        else: # Check if the file 'bclock.conf' is in the same folder
            os.makedirs("utxoracle", exist_ok=True)
            subprocess.run(["wget", "https://raw.githubusercontent.com/Unbesteveable/UTXOracle/main/UTXOracle.py"], cwd="utxoracle")
        clear()
        blogo()
        print(output)
        subprocess.run(["python3", "UTXOracle.py"], cwd="utxoracle")
        input("\a\nContinue...")
    except Exception as e:
        logger.debug("Menu error: %s", e)
        menuSelection()
#---------------------------------ColdCore-----------------------------------------
def callColdCore():
    clear()
    blogo()
    close()
    try:
        if not os.path.isfile('$HOME/.pyblock/public.txt'):
            msg = """
            \033[0;37;40m-------------------------\a\u001b[31;1mFILE NOT FOUND\033[0;37;40m----------------------------
                    To ColdCore works it needs to import your wallet's
                        public information on your coldcard, go to
                        -----------------------------------------
                        |                                       |
                        |    \033[1;37;40mAdvanced > MicroSD > Dump Summary\033[0;37;40m  |
                        |                                       |
                        -----------------------------------------
                             Copy the file \033[1;37;40mpublic.txt\033[0;37;40m inside
                                the main \u001b[31;1mpyblock\033[0;37;40m folder
              (see: https://coldcardwallet.com/docs/microsd#dump-summary-file)
            -------------------------------------------------------------------"""
            print(msg)
            input("\nContinue...")
        else:
            if not os.path.isdir('$HOME/.pyblock/coldcore'):
                subprocess.run(["git", "clone", "https://github.com/jamesob/coldcore.git"])
                subprocess.run(["chmod", "+x", "coldcore"], cwd="coldcore")
                subprocess.run(["cp", "coldcore", os.path.expanduser("~/.local/bin/coldcore")], cwd="coldcore")
            subprocess.run(["coldcore"])
    except Exception as e:
        logger.debug("Menu error: %s", e)
        menuSelection()

#--------------------------------- Menu section -----------------------------------

def MainMenu(mode): #Unified Main Menu - mode: "local", "onchain_only", or "remote"
    clear()
    blogo()
    sysinfo()
    pathexec()

    # Validate bitcoincli path before attempting to use it
    if mode in ("local", "onchain_only") and not path.get('bitcoincli'):
        show_error("Bitcoin CLI path not configured. Redirecting to Lite Mode.")
        t.sleep(2)
        from SPV.spvblock import MainMenuCROPPED as _lite_menu
        _lite_menu()
        return
    if mode == "remote" and not lndconnectload.get('tls'):
        show_error("Remote node not configured. Redirecting to Lite Mode.")
        t.sleep(2)
        from SPV.spvblock import MainMenuCROPPED as _lite_menu
        _lite_menu()
        return

    # Fetch BTC price for status bar
    try:
        _price_r = requests.get("https://mempool.space/api/v1/prices", timeout=3)
        _btc_price = f"{_price_r.json().get('USD', ''):,}"
    except Exception:
        _btc_price = ""

    if mode == "remote":
        lndconnectexec()
        path_remote = {"ip_port":"", "rpcuser":"", "rpcpass":"", "bitcoincli":""}
        with open("config/bclock.conf", "r") as f:
            pathv = json.load(f)
        path_remote = pathv
        n = "Local" if path_remote['bitcoincli'] else "Remote"
        blk = rpc('getblockchaininfo')
        d = blk

        cert_path = lndconnectload["tls"]
        macaroon = codecs.encode(open(lndconnectload["macaroon"], 'rb').read(), 'hex')
        headers = {'Grpc-Metadata-macaroon': macaroon}
        url = f'https://{lndconnectload["ip_port"]}/v1/getinfo'
        r = requests.get(url, headers=headers, verify=cert_path)
        alias = r.json()
    elif mode == "local":
        lndconnectexec()
        n = "Local" if path['bitcoincli'] else "Remote"
        bitcoincli = " getblockchaininfo"
        a = subprocess.run([path['bitcoincli']] + bitcoincli.split(), capture_output=True, text=True).stdout
        b = json.loads(a)
        d = b

        lncli = " getinfo"
        lsd = subprocess.run([lndconnectload['ln']] + lncli.split(), capture_output=True, text=True).stdout
        lsd0 = str(lsd)
        alias = json.loads(lsd0)
    else:  # onchain_only
        n = "Local" if path['bitcoincli'] else "Remote"
        bitcoincli = " getblockchaininfo"
        a = subprocess.run([path['bitcoincli']] + bitcoincli.split(), capture_output=True, text=True).stdout
        b = json.loads(a)
        d = b
        alias = None

    # Rich status bar and header
    rich_status_bar(mode=mode, block_height=str(d.get('blocks', '')), btc_price=_btc_price)
    alias_name = alias.get('alias', '') if alias else None
    rich_header(n, str(d.get('blocks', '')), version, alias=alias_name)

    # Rich menu
    items = [
        ("A", "PyBLOCK", "red"),
        ("B", "Bitcoin", "rgb(255,102,0)"),
    ]
    if mode != "onchain_only":
        items.append(("L", "Lightning", "yellow"))
    items.extend([
        ("P", "Platforms", "rgb(0,200,0)"),
        ("S", "Settings", "blue"),
        ("X", "Donate", "white"),
        ("Q", "Exit", "rgb(128,0,255)"),
    ])
    rich_menu("Main Menu", items)

    print("\x1b[?25h")
    mainmenuControl(rich_prompt("Select option"), mode)

def MainMenuLOCAL(): #Main Menu
    MainMenu("local")

def MainMenuLOCALChainONLY(): #Main Menu
    MainMenu("onchain_only")

def MainMenuREMOTE(): #Main Menu
    MainMenu("remote")

def bitcoincoremenuLocal(mode): #Unified Bitcoin Core menu for local/onchain_only modes
    clear()
    blogo()
    sysinfo()
    pathexec()

    n = "Local" if path['bitcoincli'] else "Remote"
    bitcoincli = " getblockchaininfo"
    a = subprocess.run([path['bitcoincli']] + bitcoincli.split(), capture_output=True, text=True).stdout
    b = json.loads(a)
    d = b

    if mode == "local":
        lndconnectexec()
        lncli = " getinfo"
        lsd = subprocess.run([lndconnectload['ln']] + lncli.split(), capture_output=True, text=True).stdout
        lsd0 = str(lsd)
        alias = json.loads(lsd0)
    else:
        alias = None

    # Build header
    if alias is not None:
        header = """\t\t
    \033[1;37;40m{}\033[0;37;40m: \033[1;31;40mPyBLOCK\033[0;37;40m
    \033[1;37;40mNode\033[0;37;40m: \033[1;33;40m{}\033[0;37;40m
    \033[1;37;40mBlock\033[0;37;40m: \033[1;32;40m{}\033[0;37;40m
    \033[1;37;40mVersion\033[0;37;40m: {}""".format(n, alias['alias'], d['blocks'], version)
    else:
        header = """\t\t
    \033[1;37;40m{}\033[0;37;40m: \033[1;31;40mPyBLOCK\033[0;37;40m
    \033[1;37;40mBlock\033[0;37;40m: \033[1;32;40m{}\033[0;37;40m
    \033[1;37;40mVersion\033[0;37;40m: {}""".format(n, d['blocks'], version)

    # Build menu items
    menu_items = """

    \u001b[38;5;202mA.\033[0;37;40m Bitcoin-cli Console
    \u001b[38;5;202mB.\033[0;37;40m Show Genesis Block
    \u001b[38;5;202mC.\033[0;37;40m Show Blockchain Information
    \u001b[38;5;202mD.\033[0;37;40m Run the Numbers
    \u001b[38;5;202mE.\033[0;37;40m Decode in HEX
    \u001b[38;5;202mF.\033[0;37;40m Show QR from a Bitcoin Address
    \u001b[38;5;202mG.\033[0;37;40m Show confirmations from a transaction
    \u001b[38;5;202mH.\033[0;37;40m Miscellaneous
    \u001b[38;5;202mI.\033[0;37;40m ColdCore
    \u001b[38;5;202mJ.\033[0;37;40m Whitepaper
    \u001b[38;5;202mK.\033[0;37;40m Peers Monitor
    \u001b[38;5;202mL.\033[0;37;40m Latest Block
    \u001b[38;5;202mM.\033[0;37;40m Moscow Time
    \u001b[38;5;202mN.\033[0;37;40m Mempool Search
    \u001b[38;5;202mO.\033[0;37;40m OP_RETURN
    \u001b[38;5;202mP.\033[0;37;40m Block Monitor"""

    if mode == "onchain_only":
        menu_items += """
    \u001b[38;5;202mW.\033[0;37;40m Wallet"""

    menu_items += """
    \u001b[38;5;202mZ.\033[0;37;40m Stats
    \u001b[38;5;202mQ.\033[0;37;40m Hashrate
    \u001b[38;5;202mS.\033[0;37;40m Mempool
    \u001b[38;5;202mU.\033[0;37;40m Unconfirmed Txs
    \u001b[38;5;202mV.\033[0;37;40m Block Visualizer
    \u001b[38;5;202mX.\033[0;37;40m Node Monitor
    \u001b[38;5;202mY.\033[0;37;40m Mempool Monitor
    \u001b[38;5;202mCM.\033[0;37;40m CLI Miner
    \u001b[38;5;202mONM.\033[0;37;40m Own Node Miner
    \u001b[38;5;202mVG.\033[0;37;40m Vanity Generator
    \u001b[33;1mEnter.\033[0;37;40m Return
    \n\n\x1b[?25h"""

    print(header + menu_items)
    bitcoincoremenuLocalControl(input("\033[1;32;40mSelect option: \033[0;37;40m"), mode)

def bitcoincoremenuLOCAL():
    bitcoincoremenuLocal("local")

def bitcoincoremenuLOCALOnchainONLY():
    bitcoincoremenuLocal("onchain_only")

def OwnNodeMiner(menuMin):
    clear()
    blogo()
    sysinfo()
    pathexec()
    lndconnectexec()
    if path['bitcoincli']:
        n = "Local" if path['bitcoincli'] else "Remote"
        bitcoincli = " getblockchaininfo"
        a = subprocess.run([path['bitcoincli']] + bitcoincli.split(), capture_output=True, text=True).stdout
        b = json.loads(a)
        d = b

        lncli = " getinfo"
        lsd = subprocess.run([lndconnectload['ln']] + lncli.split(), capture_output=True, text=True).stdout
        lsd0 = str(lsd)
        alias = json.loads(lsd0)
    else:
        a = "Local" if path['bitcoincli'] else "Remote"
        blk = rpc('getblockchaininfo')
        d = blk

        cert_path = lndconnectload["tls"]
        macaroon = codecs.encode(open(lndconnectload["macaroon"], 'rb').read(), 'hex')
        headers = {'Grpc-Metadata-macaroon': macaroon}
        url = f'https://{lndconnectload["ip_port"]}/v1/getinfo'
        r = requests.get(url, headers=headers, verify=cert_path)
        alias = r.json()
    print("""\t\t
    \033[1;37;40m{}\033[0;37;40m: \033[1;31;40mPyBLOCK\033[0;37;40m
    \033[1;37;40mNode\033[0;37;40m: \033[1;33;40m{}\033[0;37;40m
    \033[1;37;40mBlock\033[0;37;40m: \033[1;32;40m{}\033[0;37;40m
    \033[1;37;40mVersion\033[0;37;40m: {}

    \033[1;32;40mA.\033[0;37;40m Computer Miner
    \033[1;32;40mB.\033[0;37;40m Raspberry Miner
    \u001b[33;1mEnter.\033[0;37;40m Return
    \n\n\x1b[?25h""".format(n, alias['alias'], d['blocks'], version ))
    OwnNodeMinerControl(input("\033[1;32;40mSelect option: \033[0;37;40m"))

def OwnNodeMinerONCHAIN():
    clear()
    blogo()
    sysinfo()
    pathexec()
    #lndconnectexec()
    n = "Local" if path['bitcoincli'] else "Remote"
    bitcoincli = " getblockchaininfo"
    a = subprocess.run([path['bitcoincli']] + bitcoincli.split(), capture_output=True, text=True).stdout
    b = json.loads(a)
    d = b

    print("""\t\t
    \033[1;37;40m{}\033[0;37;40m: \033[1;31;40mPyBLOCK\033[0;37;40m
    \033[1;37;40mBlock\033[0;37;40m: \033[1;32;40m{}\033[0;37;40m
    \033[1;37;40mVersion\033[0;37;40m: {}

    \033[1;32;40mA.\033[0;37;40m Computer Miner
    \033[1;32;40mB.\033[0;37;40m Raspberry Miner
    \u001b[33;1mEnter.\033[0;37;40m Return
    \n\n\x1b[?25h""".format(n,d['blocks'], version))
    OwnNodeMinerControlONCHAIN(input("\033[1;32;40mSelect option: \033[0;37;40m"))

def walletmenuLOCALOnchainONLY():
    clear()
    blogo()
    sysinfo()
    pathexec()
    #lndconnectexec()
    n = "Local" if path['bitcoincli'] else "Remote"
    bitcoincli = " getblockchaininfo"
    a = subprocess.run([path['bitcoincli']] + bitcoincli.split(), capture_output=True, text=True).stdout
    b = json.loads(a)
    d = b

    print("""\t\t
    \033[1;37;40m{}\033[0;37;40m: \033[1;31;40mPyBLOCK\033[0;37;40m
    \033[1;37;40mBlock\033[0;37;40m: \033[1;32;40m{}\033[0;37;40m
    \033[1;37;40mVersion\033[0;37;40m: {}

    \u001b[38;5;202mA.\033[0;37;40m Deposit
    \u001b[38;5;202mB.\033[0;37;40m Show transactions
    \u001b[38;5;202mC.\033[0;37;40m Dump Private Key
    \u001b[38;5;202mD.\033[0;37;40m Wallet Info
    \u001b[38;5;202mE.\033[0;37;40m Address Info
    \u001b[38;5;202mF.\033[0;37;40m Mining Info
    \u001b[33;1mEnter.\033[0;37;40m Return
    \n\n\x1b[?25h""".format(n,d['blocks'], version))
    walletmenuLOCALcontrolAOnchainONLY(input("\033[1;32;40mSelect option: \033[0;37;40m"))

def bitcoincoremenuLOCALOPRETURN():
    clear()
    blogo()
    sysinfo()
    pathexec()
    lndconnectexec()
    n = "Local" if path['bitcoincli'] else "Remote"
    bitcoincli = " getblockchaininfo"
    a = subprocess.run([path['bitcoincli']] + bitcoincli.split(), capture_output=True, text=True).stdout
    b = json.loads(a)
    d = b

    lncli = " getinfo"
    lsd = subprocess.run([lndconnectload['ln']] + lncli.split(), capture_output=True, text=True).stdout
    lsd0 = str(lsd)
    alias = json.loads(lsd0)

    print("""\t\t
    \033[1;37;40m{}\033[0;37;40m: \033[1;31;40mPyBLOCK\033[0;37;40m
    \033[1;37;40mNode\033[0;37;40m: \033[1;33;40m{}\033[0;37;40m
    \033[1;37;40mBlock\033[0;37;40m: \033[1;32;40m{}\033[0;37;40m
    \033[1;37;40mVersion\033[0;37;40m: {}

    \u001b[38;5;202mA.\033[0;37;40m Send OP_RETURN
    \u001b[38;5;202mB.\033[0;37;40m View OP_RETURN
    \u001b[38;5;202mC.\033[0;37;40m View Decoded Coinbase
    \u001b[33;1mEnter.\033[0;37;40m Return
    \n\n\x1b[?25h""".format(n, alias['alias'], d['blocks'], version ))
    bitcoincoremenuLOCALcontrolO(input("\033[1;32;40mSelect option: \033[0;37;40m"))

def bitcoincoremenuLOCALOPRETURNOnchainONLY():
    clear()
    blogo()
    sysinfo()
    pathexec()
    #lndconnectexec()
    n = "Local" if path['bitcoincli'] else "Remote"
    bitcoincli = " getblockchaininfo"
    a = subprocess.run([path['bitcoincli']] + bitcoincli.split(), capture_output=True, text=True).stdout
    b = json.loads(a)
    d = b

    print("""\t\t
    \033[1;37;40m{}\033[0;37;40m: \033[1;31;40mPyBLOCK\033[0;37;40m
    \033[1;37;40mBlock\033[0;37;40m: \033[1;32;40m{}\033[0;37;40m
    \033[1;37;40mVersion\033[0;37;40m: {}

    \u001b[38;5;202mA.\033[0;37;40m Send OP_RETURN
    \u001b[38;5;202mB.\033[0;37;40m View OP_RETURN
    \u001b[38;5;202mC.\033[0;37;40m View Decoded Coinbase
    \u001b[33;1mEnter.\033[0;37;40m Return
    \n\n\x1b[?25h""".format(n,d['blocks'], version ))
    bitcoincoremenuLOCALcontrolOOnchainONLY(input("\033[1;32;40mSelect option: \033[0;37;40m"))

def bitcoincoremenuREMOTE():
    clear()
    blogo()
    sysinfo()
    pathexec()
    lndconnectexec()
    a = "Local" if path['bitcoincli'] else "Remote"
    blk = rpc('getblockchaininfo')
    d = blk

    cert_path = lndconnectload["tls"]
    macaroon = codecs.encode(open(lndconnectload["macaroon"], 'rb').read(), 'hex')
    headers = {'Grpc-Metadata-macaroon': macaroon}
    url = f'https://{lndconnectload["ip_port"]}/v1/getinfo'
    r = requests.get(url, headers=headers, verify=cert_path)
    alias = r.json()

    print("""\t\t
    \033[1;37;40m{}\033[0;37;40m: \033[1;31;40mPyBLOCK\033[0;37;40m
    \033[1;37;40mNode\033[0;37;40m: \033[1;33;40m{}\033[0;37;40m
    \033[1;37;40mBlock\033[0;37;40m: \033[1;32;40m{}\033[0;37;40m
    \033[1;37;40mVersion\033[0;37;40m: {}

    \u001b[38;5;202mA.\033[0;37;40m Bitcoin-cli Console
    \u001b[38;5;202mB.\033[0;37;40m Show Blockchain Information
    \u001b[38;5;202mC.\033[0;37;40m Run the Numbers
    \u001b[38;5;202mD.\033[0;37;40m Show QR from a Bitcoin Address
    \u001b[38;5;202mE.\033[0;37;40m Miscellaneous
    \u001b[38;5;202mM.\033[0;37;40m Moscow Time
    \u001b[38;5;202mO.\033[0;37;40m OP_RETURN
    \u001b[38;5;202mR.\033[0;37;40m Hashrate
    \u001b[33;1mEnter.\033[0;37;40m Return
    \n\n\x1b[?25h""".format(a, alias['alias'], d['blocks'], version ))
    bitcoincoremenuREMOTEcontrol(input("\033[1;32;40mSelect option: \033[0;37;40m"))

def bitcoincoremenuREMOTEOPRETURN():
    clear()
    blogo()
    sysinfo()
    pathexec()
    lndconnectexec()
    a = "Local" if path['bitcoincli'] else "Remote"
    blk = rpc('getblockchaininfo')
    d = blk

    cert_path = lndconnectload["tls"]
    macaroon = codecs.encode(open(lndconnectload["macaroon"], 'rb').read(), 'hex')
    headers = {'Grpc-Metadata-macaroon': macaroon}
    url = f'https://{lndconnectload["ip_port"]}/v1/getinfo'
    r = requests.get(url, headers=headers, verify=cert_path)
    alias = r.json()

    print("""\t\t
    \033[1;37;40m{}\033[0;37;40m: \033[1;31;40mPyBLOCK\033[0;37;40m
    \033[1;37;40mNode\033[0;37;40m: \033[1;33;40m{}\033[0;37;40m
    \033[1;37;40mBlock\033[0;37;40m: \033[1;32;40m{}\033[0;37;40m
    \033[1;37;40mVersion\033[0;37;40m: {}

    \u001b[38;5;202mA.\033[0;37;40m Send OP_RETURN
    \u001b[38;5;202mB.\033[0;37;40m View OP_RETURN
    \u001b[38;5;202mC.\033[0;37;40m View Decoded Coinbase
    \u001b[33;1mEnter.\033[0;37;40m Return
    \n\n\x1b[?25h""".format(a, alias['alias'], d['blocks'], version ))
    bitcoincoremenuREMOTEcontrolO(input("\033[1;32;40mSelect option: \033[0;37;40m"))

def lightningnetworkLOCAL():
    clear()
    blogo()
    sysinfo()
    pathexec()
    lndconnectexec()
    n = "Local" if path['bitcoincli'] else "Remote"
    bitcoincli = " getblockchaininfo"
    a = subprocess.run([path['bitcoincli']] + bitcoincli.split(), capture_output=True, text=True).stdout
    b = json.loads(a)
    d = b

    lncli = " getinfo"
    lsd = subprocess.run([lndconnectload['ln']] + lncli.split(), capture_output=True, text=True).stdout
    lsd0 = str(lsd)
    alias = json.loads(lsd0)

    print("""\t\t
    \033[1;37;40m{}\033[0;37;40m: \033[1;31;40mPyBLOCK\033[0;37;40m
    \033[1;37;40mNode\033[0;37;40m: \033[1;33;40m{}\033[0;37;40m
    \033[1;37;40mBlock\033[0;37;40m: \033[1;32;40m{}\033[0;37;40m
    \033[1;37;40mVersion\033[0;37;40m: {}

    \u001b[33;1mA.\033[0;37;40m Lncli Console
    \u001b[33;1mB.\033[0;37;40m New Invoice
    \u001b[33;1mC.\033[0;37;40m Pay Invoice
    \u001b[33;1mD.\033[0;37;40m Make a KeySend Payment
    \u001b[33;1mE.\033[0;37;40m New Bitcoin Address
    \u001b[33;1mF.\033[0;37;40m List Invoices
    \u001b[33;1mG.\033[0;37;40m Channel Balance
    \u001b[33;1mH.\033[0;37;40m Show Channels
    \u001b[33;1mI.\033[0;37;40m Rebalance Channel
    \u001b[33;1mJ.\033[0;37;40m Show Peers
    \u001b[33;1mK.\033[0;37;40m Connect Peers
    \u001b[33;1mL.\033[0;37;40m Onchain Balance
    \u001b[33;1mM.\033[0;37;40m List Onchain Transactions
    \u001b[33;1mN.\033[0;37;40m Get Node Info
    \u001b[33;1mO.\033[0;37;40m Get Network Information
    \u001b[33;1mP.\033[0;37;40m PyChat
    \u001b[33;1mZ.\033[0;37;40m Stats
    \u001b[33;1mT.\033[0;37;40m Ranking
    \u001b[33;1mQ.\033[0;37;40m LNBits List LNURL     \033[3;35;40m{lnbitspaid}\033[0;37;40m
    \u001b[33;1mS.\033[0;37;40m LNBits Create LNURL   \033[3;35;40m{lnbitspaid}\033[0;37;40m
    \u001b[33;1mEnter.\033[0;37;40m Return
    \n\n\x1b[?25h""".format(n, alias['alias'], d['blocks'], version, lnbitspaid = "UNLOCKED" if os.path.isfile("lnbitSN.conf") else "LOCKED"))
    lightningnetworkLOCALcontrol(input("\033[1;32;40mSelect option: \033[0;37;40m"))

def chatConn():
    clear()
    blogo()
    sysinfo()
    pathexec()
    lndconnectexec()
    n = "Local" if path['bitcoincli'] else "Remote"
    bitcoincli = " getblockchaininfo"
    a = subprocess.run([path['bitcoincli']] + bitcoincli.split(), capture_output=True, text=True).stdout
    b = json.loads(a)
    d = b

    lncli = " getinfo"
    lsd = subprocess.run([lndconnectload['ln']] + lncli.split(), capture_output=True, text=True).stdout
    lsd0 = str(lsd)
    alias = json.loads(lsd0)

    print("""\t\t
    \033[1;37;40m{}\033[0;37;40m: \033[1;31;40mPyBLOCK\033[0;37;40m
    \033[1;37;40mBlock\033[0;37;40m: \033[1;32;40m{}\033[0;37;40m
    \033[1;37;40mVersion\033[0;37;40m: {}

    \u001b[38;5;202mA.\033[0;37;40m Open
    \u001b[38;5;202mB.\033[0;37;40m Close
    \u001b[38;5;202mC.\033[0;37;40m Hidden
    \u001b[33;1mEnter.\033[0;37;40m Return
    \n\n\x1b[?25h""".format(n, d['blocks'], version ))
    chatConnA(input("\033[1;32;40mSelect option: \033[0;37;40m"))

def pyCHATA():
    clear()
    blogo()
    sysinfo()
    pathexec()
    lndconnectexec()
    n = "Local" if path['bitcoincli'] else "Remote"
    bitcoincli = " getblockchaininfo"
    a = subprocess.run([path['bitcoincli']] + bitcoincli.split(), capture_output=True, text=True).stdout
    b = json.loads(a)
    d = b

    lncli = " getinfo"
    lsd = subprocess.run([lndconnectload['ln']] + lncli.split(), capture_output=True, text=True).stdout
    lsd0 = str(lsd)
    alias = json.loads(lsd0)

    print("""\t\t
    \033[1;37;40m{}\033[0;37;40m: \033[1;31;40mPyBLOCK\033[0;37;40m
    \033[1;37;40mBlock\033[0;37;40m: \033[1;32;40m{}\033[0;37;40m
    \033[1;37;40mVersion\033[0;37;40m: {}

    \u001b[38;5;202mA.\033[0;37;40m Write
    \u001b[38;5;202mB.\033[0;37;40m Read
    \u001b[38;5;202mC.\033[0;37;40m List
    \u001b[33;1mEnter.\033[0;37;40m Return
    \n\n\x1b[?25h""".format(n, d['blocks'], version ))
    chatConnB(input("\033[1;32;40mSelect option: \033[0;37;40m"))

def pyCHATB():
    clear()
    blogo()
    sysinfo()
    pathexec()
    lndconnectexec()
    n = "Local" if path['bitcoincli'] else "Remote"
    bitcoincli = " getblockchaininfo"
    a = subprocess.run([path['bitcoincli']] + bitcoincli.split(), capture_output=True, text=True).stdout
    b = json.loads(a)
    d = b

    lncli = " getinfo"
    lsd = subprocess.run([lndconnectload['ln']] + lncli.split(), capture_output=True, text=True).stdout
    lsd0 = str(lsd)
    alias = json.loads(lsd0)

    print("""\t\t
    \033[1;37;40m{}\033[0;37;40m: \033[1;31;40mPyBLOCK\033[0;37;40m
    \033[1;37;40mBlock\033[0;37;40m: \033[1;32;40m{}\033[0;37;40m
    \033[1;37;40mVersion\033[0;37;40m: {}

    \u001b[38;5;202mA.\033[0;37;40m Write
    \u001b[38;5;202mB.\033[0;37;40m Read
    \u001b[38;5;202mC.\033[0;37;40m List
    \u001b[33;1mEnter.\033[0;37;40m Return
    \n\n\x1b[?25h""".format(n, d['blocks'], version, ))
    chatConnC(input("\033[1;32;40mSelect option: \033[0;37;40m"))

def pyCHATC():
    clear()
    blogo()
    sysinfo()
    pathexec()
    lndconnectexec()
    n = "Local" if path['bitcoincli'] else "Remote"
    bitcoincli = " getblockchaininfo"
    a = subprocess.run([path['bitcoincli']] + bitcoincli.split(), capture_output=True, text=True).stdout
    b = json.loads(a)
    d = b

    lncli = " getinfo"
    lsd = subprocess.run([lndconnectload['ln']] + lncli.split(), capture_output=True, text=True).stdout
    lsd0 = str(lsd)
    alias = json.loads(lsd0)

    print("""\t\t
    \033[1;37;40m{}\033[0;37;40m: \033[1;31;40mPyBLOCK\033[0;37;40m
    \033[1;37;40mBlock\033[0;37;40m: \033[1;32;40m{}\033[0;37;40m
    \033[1;37;40mVersion\033[0;37;40m: {}

    \u001b[38;5;202mA.\033[0;37;40m Write
    \u001b[38;5;202mB.\033[0;37;40m Read
    \u001b[38;5;202mC.\033[0;37;40m List
    \u001b[33;1mEnter.\033[0;37;40m Return
    \n\n\x1b[?25h""".format(n, d['blocks'], version ))
    chatConnD(input("\033[1;32;40mSelect option: \033[0;37;40m"))

def lightningnetworkREMOTE():
    clear()
    blogo()
    sysinfo()
    pathexec()
    lndconnectexec()
    a = "Local" if path['bitcoincli'] else "Remote"
    blk = rpc('getblockchaininfo')
    d = blk

    cert_path = lndconnectload["tls"]
    macaroon = codecs.encode(open(lndconnectload["macaroon"], 'rb').read(), 'hex')
    headers = {'Grpc-Metadata-macaroon': macaroon}
    url = f'https://{lndconnectload["ip_port"]}/v1/getinfo'
    r = requests.get(url, headers=headers, verify=cert_path)
    alias = r.json()

    print("""\t\t
    \033[1;37;40m{}\033[0;37;40m: \033[1;31;40mPyBLOCK\033[0;37;40m
    \033[1;37;40mNode\033[0;37;40m: \033[1;33;40m{}\033[0;37;40m
    \033[1;37;40mBlock\033[0;37;40m: \033[1;32;40m{}\033[0;37;40m
    \033[1;37;40mVersion\033[0;37;40m: {}

    \u001b[33;1mA.\033[0;37;40m New Invoice
    \u001b[33;1mB.\033[0;37;40m Pay Invoice
    \u001b[33;1mC.\033[0;37;40m New Bitcoin Address
    \u001b[33;1mD.\033[0;37;40m List Invoices
    \u001b[33;1mE.\033[0;37;40m Channel Balance
    \u001b[33;1mF.\033[0;37;40m Show Channels
    \u001b[33;1mG.\033[0;37;40m Onchain Balance
    \u001b[33;1mH.\033[0;37;40m List Onchain Transactions
    \u001b[33;1mI.\033[0;37;40m Get Node Info
    \u001b[33;1mZ.\033[0;37;40m Stats
    \u001b[33;1mT.\033[0;37;40m Ranking
    \u001b[33;1mQ.\033[0;37;40m LNBits List LNURL     \033[3;35;40m{lnbitspaid}\033[0;37;40m
    \u001b[33;1mS.\033[0;37;40m LNBits Create LNURL   \033[3;35;40m{lnbitspaid}\033[0;37;40m
    \u001b[33;1mEnter.\033[0;37;40m Return
    \n\n\x1b[?25h""".format(a, alias['alias'], d['blocks'], version , lnbitspaid = "UNLOCKED" if os.path.isfile("lnbitSN.conf") else "LOCKED"))
    lightningnetworkREMOTEcontrol(input("\033[1;32;40mSelect option: \033[0;37;40m"))

def APIMenuLOCAL():
    clear()
    blogo()
    sysinfo()
    pathexec()
    lndconnectexec()
    if path['bitcoincli']:
        n = "Local" if path['bitcoincli'] else "Remote"
        bitcoincli = " getblockchaininfo"
        a = subprocess.run([path['bitcoincli']] + bitcoincli.split(), capture_output=True, text=True).stdout
        b = json.loads(a)
        d = b

        lncli = " getinfo"
        lsd = subprocess.run([lndconnectload['ln']] + lncli.split(), capture_output=True, text=True).stdout
        lsd0 = str(lsd)
        alias = json.loads(lsd0)
    else:
        a = "Local" if path['bitcoincli'] else "Remote"
        blk = rpc('getblockchaininfo')
        d = blk

        cert_path = lndconnectload["tls"]
        macaroon = codecs.encode(open(lndconnectload["macaroon"], 'rb').read(), 'hex')
        headers = {'Grpc-Metadata-macaroon': macaroon}
        url = f'https://{lndconnectload["ip_port"]}/v1/getinfo'
        r = requests.get(url, headers=headers, verify=cert_path)
        alias = r.json()
    print("""\t\t
    \033[1;37;40m{}\033[0;37;40m: \033[1;31;40mPyBLOCK\033[0;37;40m
    \033[1;37;40mNode\033[0;37;40m: \033[1;33;40m{}\033[0;37;40m
    \033[1;37;40mBlock\033[0;37;40m: \033[1;32;40m{}\033[0;37;40m
    \033[1;37;40mVersion\033[0;37;40m: {}

    \033[1;32;40mA.\033[0;37;40m TippinMe     FREE
    \033[1;32;40mB.\033[0;37;40m Tallycoin    FREE
    \033[1;32;40mC.\033[0;37;40m Mempool      FREE
    \033[1;32;40mD.\033[0;37;40m CoinGecko    FREE
    \033[1;32;40mE.\033[0;37;40m Rate.sx      FREE
    \033[1;32;40mF.\033[0;37;40m BWT          FREE
    \033[1;32;40mG.\033[0;37;40m LNBits       \033[3;35;40m{lnbitspaid}\033[0;37;40m
    \033[1;32;40mH.\033[0;37;40m LNPay        \033[3;35;40m{lnpaypaid}\033[0;37;40m
    \033[1;32;40mI.\033[0;37;40m OpenNode     \033[3;35;40m{opennodepaid}\033[0;37;40m
    \033[1;32;40mJ.\033[0;37;40m SatNode      FREE
    \033[1;32;40mK.\033[0;37;40m Weather      FREE
    \033[1;32;40mL.\033[0;37;40m Arcade       FREE
    \033[1;32;40mM.\033[0;37;40m Whale Alert  FREE
    \033[1;32;40mN.\033[0;37;40m Nostr        FREE
    \033[1;32;40mQ.\033[0;37;40m Ocean        FREE
    \033[1;32;40mS.\033[0;37;40m Braiins Pool FREE
    \033[1;32;40mT.\033[0;37;40m TinySeed     FREE
    \033[1;32;40mU.\033[0;37;40m UTXOracle    FREE
    \033[1;32;40mW.\033[0;37;40m CK Pool      FREE
    \033[1;32;40mZ.\033[0;37;40m PyBLOCK Pool FREE
    \u001b[33;1mEnter.\033[0;37;40m Return
    \n\n\x1b[?25h""".format(n if path['bitcoincli'] else a , alias['alias'], d['blocks'], version ,lnbitspaid = "PAID" if os.path.isfile("lnbitSN.conf") else "PREMIUM", lnpaypaid = "PAID" if os.path.isfile("lnpaySN.conf") else "PREMIUM", opennodepaid = "PAID" if os.path.isfile("opennodeSN.conf") else "PREMIUM"))
    platfformsLOCALcontrol(input("\033[1;32;40mSelect option: \033[0;37;40m"))

def APIMenuLOCALOnchainONLY():
    clear()
    blogo()
    sysinfo()
    pathexec()
    #lndconnectexec()
    if path['bitcoincli']:
        n = "Local" if path['bitcoincli'] else "Remote"
        bitcoincli = " getblockchaininfo"
        a = subprocess.run([path['bitcoincli']] + bitcoincli.split(), capture_output=True, text=True).stdout
        b = json.loads(a)
        d = b
    else:
        a = "Local" if path['bitcoincli'] else "Remote"
        blk = rpc('getblockchaininfo')
        d = blk

        cert_path = lndconnectload["tls"]
        macaroon = codecs.encode(open(lndconnectload["macaroon"], 'rb').read(), 'hex')
        headers = {'Grpc-Metadata-macaroon': macaroon}
        url = f'https://{lndconnectload["ip_port"]}/v1/getinfo'
        r = requests.get(url, headers=headers, verify=cert_path)
        alias = r.json()
    print("""\t\t
    \033[1;37;40m{}\033[0;37;40m: \033[1;31;40mPyBLOCK\033[0;37;40m
    \033[1;37;40mBlock\033[0;37;40m: \033[1;32;40m{}\033[0;37;40m
    \033[1;37;40mVersion\033[0;37;40m: {}

    \033[1;32;40mA.\033[0;37;40m TippinMe      FREE
    \033[1;32;40mB.\033[0;37;40m Tallycoin     FREE
    \033[1;32;40mC.\033[0;37;40m Mempool       FREE
    \033[1;32;40mD.\033[0;37;40m CoinGecko     FREE
    \033[1;32;40mE.\033[0;37;40m Rate.sx       FREE
    \033[1;32;40mF.\033[0;37;40m BWT           FREE
    \033[1;32;40mG.\033[0;37;40m LNBits        \033[3;35;40m{lnbitspaid}\033[0;37;40m
    \033[1;32;40mH.\033[0;37;40m LNPay         \033[3;35;40m{lnpaypaid}\033[0;37;40m
    \033[1;32;40mI.\033[0;37;40m OpenNode      \033[3;35;40m{opennodepaid}\033[0;37;40m
    \033[1;32;40mJ.\033[0;37;40m SatNode       FREE
    \033[1;32;40mK.\033[0;37;40m Weather       FREE
    \033[1;32;40mL.\033[0;37;40m Arcade        FREE
    \033[1;32;40mM.\033[0;37;40m Whale Alert   FREE
    \033[1;32;40mN.\033[0;37;40m Nostr         FREE
    \033[1;32;40mP.\033[0;37;40m PhoenixD      FREE
    \033[1;32;40mQ.\033[0;37;40m Ocean Pool    FREE
    \033[1;32;40mR.\033[0;37;40m Luxor Pool    FREE
    \033[1;32;40mS.\033[0;37;40m Braiins Pool  FREE
    \033[1;32;40mT.\033[0;37;40m TinySeed      FREE
    \033[1;32;40mU.\033[0;37;40m UTXOracle     FREE
    \033[1;32;40mW.\033[0;37;40m CK Pool       FREE
    \033[1;32;40mZ.\033[0;37;40m PyBLOCK Pool  FREE
    \u001b[33;1mEnter.\033[0;37;40m Return
    \n\n\x1b[?25h""".format(n if path['bitcoincli'] else a, d['blocks'], version ,lnbitspaid = "PAID" if os.path.isfile("lnbitSN.conf") else "PREMIUM", lnpaypaid = "PAID" if os.path.isfile("lnpaySN.conf") else "PREMIUM", opennodepaid = "PAID" if os.path.isfile("opennodeSN.conf") else "PREMIUM"))
    platfformsLOCALcontrolOnchainONLY(input("\033[1;32;40mSelect option: \033[0;37;40m"))

def decodeHex():
    clear()
    blogo()
    sysinfo()
    pathexec()
    lndconnectexec()
    n = "Local" if path['bitcoincli'] else "Remote"
    bitcoincli = " getblockchaininfo"
    a = subprocess.run([path['bitcoincli']] + bitcoincli.split(), capture_output=True, text=True).stdout
    b = json.loads(a)
    d = b

    lncli = " getinfo"
    lsd = subprocess.run([lndconnectload['ln']] + lncli.split(), capture_output=True, text=True).stdout
    lsd0 = str(lsd)
    alias = json.loads(lsd0)

    print("""\t\t
    \033[1;37;40m{}\033[0;37;40m: \033[1;31;40mPyBLOCK\033[0;37;40m
    \033[1;37;40mNode\033[0;37;40m: \033[1;33;40m{}\033[0;37;40m
    \033[1;37;40mBlock\033[0;37;40m: \033[1;32;40m{}\033[0;37;40m
    \033[1;37;40mVersion\033[0;37;40m: {}

    \u001b[38;5;202mA.\033[0;37;40m Decode Blocks in HEX
    \u001b[38;5;202mB.\033[0;37;40m Decode Transactions in HEX
    \u001b[33;1mEnter.\033[0;37;40m Return
    \n\n\x1b[?25h""".format(n, alias['alias'], d['blocks'], version ))
    decodeHexLOCAL(input("\033[1;32;40mSelect option: \033[0;37;40m"))

def decodeHexOnchainONLY():
    clear()
    blogo()
    sysinfo()
    pathexec()
    #lndconnectexec()
    n = "Local" if path['bitcoincli'] else "Remote"
    bitcoincli = " getblockchaininfo"
    a = subprocess.run([path['bitcoincli']] + bitcoincli.split(), capture_output=True, text=True).stdout
    b = json.loads(a)
    d = b

    print("""\t\t
    \033[1;37;40m{}\033[0;37;40m: \033[1;31;40mPyBLOCK\033[0;37;40m
    \033[1;37;40mBlock\033[0;37;40m: \033[1;32;40m{}\033[0;37;40m
    \033[1;37;40mVersion\033[0;37;40m: {}

    \u001b[38;5;202mA.\033[0;37;40m Decode Blocks in HEX
    \u001b[38;5;202mB.\033[0;37;40m Decode Transactions in HEX
    \u001b[33;1mEnter.\033[0;37;40m Return
    \n\n\x1b[?25h""".format(n, d['blocks'], version ))
    decodeHexLOCALOnchainONLY(input("\033[1;32;40mSelect option: \033[0;37;40m"))

def miscellaneousLOCAL():
    clear()
    blogo()
    sysinfo()
    pathexec()
    lndconnectexec()
    if path['bitcoincli']:
        n = "Local" if path['bitcoincli'] else "Remote"
        bitcoincli = " getblockchaininfo"
        a = subprocess.run([path['bitcoincli']] + bitcoincli.split(), capture_output=True, text=True).stdout
        b = json.loads(a)
        d = b

        lncli = " getinfo"
        lsd = subprocess.run([lndconnectload['ln']] + lncli.split(), capture_output=True, text=True).stdout
        lsd0 = str(lsd)
        alias = json.loads(lsd0)
    else:
        a = "Local" if path['bitcoincli'] else "Remote"
        blk = rpc('getblockchaininfo')
        d = blk

        cert_path = lndconnectload["tls"]
        macaroon = codecs.encode(open(lndconnectload["macaroon"], 'rb').read(), 'hex')
        headers = {'Grpc-Metadata-macaroon': macaroon}
        url = f'https://{lndconnectload["ip_port"]}/v1/getinfo'
        r = requests.get(url, headers=headers, verify=cert_path)
        alias = r.json()
    print("""\t\t
    \033[1;37;40m{}\033[0;37;40m: \033[1;31;40mPyBLOCK\033[0;37;40m
    \033[1;37;40mNode\033[0;37;40m: \033[1;33;40m{}\033[0;37;40m
    \033[1;37;40mBlock\033[0;37;40m: \033[1;32;40m{}\033[0;37;40m
    \033[1;37;40mVersion\033[0;37;40m: {}

    \u001b[38;5;202mA.\033[0;37;40m Ascii ₿
    \u001b[38;5;202mB.\033[0;37;40m System
    \u001b[38;5;202mC.\033[0;37;40m Dates
    \u001b[38;5;202mD.\033[0;37;40m Quotes
    \u001b[38;5;202mH.\033[0;37;40m SHA256
    \u001b[38;5;202mM.\033[0;37;40m Block Bitaxe
    \u001b[38;5;202mP.\033[0;37;40m PGP
    \u001b[38;5;202mS.\033[0;37;40m Satoshi Nakamoto
    \u001b[38;5;202mX.\033[0;37;40m All Blocks
    \u001b[38;5;202mSHS.\033[0;37;40m SHS
    \u001b[33;1mEnter.\033[0;37;40m Return
    \n\n\x1b[?25h""".format(n if path['bitcoincli'] else a , alias['alias'], d['blocks'], version ))
    miscellaneousLOCALmenu(input("\033[1;32;40mSelect option: \033[0;37;40m"))

def miscellaneousLOCALOnchainONLY():
    clear()
    blogo()
    sysinfo()
    pathexec()
    #lndconnectexec()
    if path['bitcoincli']:
        n = "Local" if path['bitcoincli'] else "Remote"
        bitcoincli = " getblockchaininfo"
        a = subprocess.run([path['bitcoincli']] + bitcoincli.split(), capture_output=True, text=True).stdout
        b = json.loads(a)
        d = b
    else:
        a = "Local" if path['bitcoincli'] else "Remote"
        blk = rpc('getblockchaininfo')
        d = blk

        cert_path = lndconnectload["tls"]
        macaroon = codecs.encode(open(lndconnectload["macaroon"], 'rb').read(), 'hex')
        headers = {'Grpc-Metadata-macaroon': macaroon}
        url = f'https://{lndconnectload["ip_port"]}/v1/getinfo'
        r = requests.get(url, headers=headers, verify=cert_path)
        alias = r.json()
    print("""\t\t
    \033[1;37;40m{}\033[0;37;40m: \033[1;31;40mPyBLOCK\033[0;37;40m
    \033[1;37;40mBlock\033[0;37;40m: \033[1;32;40m{}\033[0;37;40m
    \033[1;37;40mVersion\033[0;37;40m: {}

    \u001b[38;5;202mA.\033[0;37;40m Ascii ₿
    \u001b[38;5;202mB.\033[0;37;40m System
    \u001b[38;5;202mC.\033[0;37;40m Dates
    \u001b[38;5;202mD.\033[0;37;40m Quotes
    \u001b[38;5;202mH.\033[0;37;40m SHA256
    \u001b[38;5;202mM.\033[0;37;40m Block Bitaxe
    \u001b[38;5;202mP.\033[0;37;40m PGP
    \u001b[38;5;202mS.\033[0;37;40m Satoshi Nakamoto
    \u001b[38;5;202mX.\033[0;37;40m All Blocks
    \u001b[38;5;202mSHS.\033[0;37;40m SHS
    \u001b[33;1mEnter.\033[0;37;40m Return
    \n\n\x1b[?25h""".format(n if path['bitcoincli'] else a, d['blocks'], version ))
    miscellaneousLOCALmenuOnchainONLY(input("\033[1;32;40mSelect option: \033[0;37;40m"))

def PhoenixConn():
    clear()
    blogo()
    sysinfo()
    pathexec()
    #lndconnectexec()
    if path['bitcoincli']:
        n = "Local" if path['bitcoincli'] else "Remote"
        bitcoincli = " getblockchaininfo"
        a = subprocess.run([path['bitcoincli']] + bitcoincli.split(), capture_output=True, text=True).stdout
        b = json.loads(a)
        d = b
    else:
        a = "Local" if path['bitcoincli'] else "Remote"
        blk = rpc('getblockchaininfo')
        d = blk

        cert_path = lndconnectload["tls"]
        macaroon = codecs.encode(open(lndconnectload["macaroon"], 'rb').read(), 'hex')
        headers = {'Grpc-Metadata-macaroon': macaroon}
        url = f'https://{lndconnectload["ip_port"]}/v1/getinfo'
        r = requests.get(url, headers=headers, verify=cert_path)
        alias = r.json()
    print("""\t\t
    \033[1;37;40m{}\033[0;37;40m: \033[1;31;40mPyBLOCK\033[0;37;40m
    \033[1;37;40mBlock\033[0;37;40m: \033[1;32;40m{}\033[0;37;40m
    \033[1;37;40mVersion\033[0;37;40m: {}

    \u001b[38;5;202mA.\033[0;37;40m Linux
    \u001b[38;5;202mB.\033[0;37;40m Mac  arm64
    \u001b[38;5;202mC.\033[0;37;40m Mac    x64
    \u001b[38;5;202mD.\033[0;37;40m Windows
    \u001b[38;5;202mE.\033[0;37;40m Manage
    \u001b[38;5;202mF.\033[0;37;40m Invoice Maker
    \u001b[38;5;202mG.\033[0;37;40m BOLT12
    \u001b[33;1mEnter.\033[0;37;40m Return
    \n\n\x1b[?25h""".format(n if path['bitcoincli'] else a, d['blocks'], version ))
    phoenixmenu(input("\033[1;32;40mSelect option: \033[0;37;40m"))

def OceanConn():
    clear()
    blogo()
    sysinfo()
    pathexec()
    #lndconnectexec()
    if path['bitcoincli']:
        n = "Local" if path['bitcoincli'] else "Remote"
        bitcoincli = " getblockchaininfo"
        a = subprocess.run([path['bitcoincli']] + bitcoincli.split(), capture_output=True, text=True).stdout
        b = json.loads(a)
        d = b
    else:
        a = "Local" if path['bitcoincli'] else "Remote"
        blk = rpc('getblockchaininfo')
        d = blk

        cert_path = lndconnectload["tls"]
        macaroon = codecs.encode(open(lndconnectload["macaroon"], 'rb').read(), 'hex')
        headers = {'Grpc-Metadata-macaroon': macaroon}
        url = f'https://{lndconnectload["ip_port"]}/v1/getinfo'
        r = requests.get(url, headers=headers, verify=cert_path)
        alias = r.json()
    print("""\t\t
    \033[1;37;40m{}\033[0;37;40m: \033[1;31;40mPyBLOCK\033[0;37;40m
    \033[1;37;40mBlock\033[0;37;40m: \033[1;32;40m{}\033[0;37;40m
    \033[1;37;40mVersion\033[0;37;40m: {}

    \033[1;32;40mA.\033[0;37;40m Earnings
    \033[1;32;40mB.\033[0;37;40m Hashrate
    \033[1;32;40mC.\033[0;37;40m Blocks
    \u001b[33;1mEnter.\033[0;37;40m Return
    \n\n\x1b[?25h""".format(n if path['bitcoincli'] else a, d['blocks'], version ))
    oceanMstats(input("\033[1;32;40mSelect option: \033[0;37;40m"))

def slushpoolREMOTEOnchainONLY():
    clear()
    blogo()
    sysinfo()
    pathexec()
    #lndconnectexec()
    if path['bitcoincli']:
        n = "Local" if path['bitcoincli'] else "Remote"
        bitcoincli = " getblockchaininfo"
        a = subprocess.run([path['bitcoincli']] + bitcoincli.split(), capture_output=True, text=True).stdout
        b = json.loads(a)
        d = b
    else:
        a = "Local" if path['bitcoincli'] else "Remote"
        blk = rpc('getblockchaininfo')
        d = blk

        cert_path = lndconnectload["tls"]
        macaroon = codecs.encode(open(lndconnectload["macaroon"], 'rb').read(), 'hex')
        headers = {'Grpc-Metadata-macaroon': macaroon}
        url = f'https://{lndconnectload["ip_port"]}/v1/getinfo'
        r = requests.get(url, headers=headers, verify=cert_path)
        alias = r.json()
    print("""\t\t
    \033[1;37;40m{}\033[0;37;40m: \033[1;31;40mPyBLOCK\033[0;37;40m
    \033[1;37;40mBlock\033[0;37;40m: \033[1;32;40m{}\033[0;37;40m
    \033[1;37;40mVersion\033[0;37;40m: {}

    \u001b[38;5;202mA.\033[0;37;40m Difficulty
    \u001b[38;5;202mC.\033[0;37;40m Pool
    \u001b[38;5;202mE.\033[0;37;40m Miner
    \u001b[33;1mEnter.\033[0;37;40m Return
    \n\n\x1b[?25h""".format(n if path['bitcoincli'] else a, d['blocks'], version ))
    slushpoolLOCALOnchainONLYMenu(input("\033[1;32;40mSelect option: \033[0;37;40m"))

def slushpoolLOCALOnchainONLY():
    clear()
    blogo()
    sysinfo()
    pathexec()
    #lndconnectexec()
    if path['bitcoincli']:
        n = "Local" if path['bitcoincli'] else "Remote"
        bitcoincli = " getblockchaininfo"
        a = subprocess.run([path['bitcoincli']] + bitcoincli.split(), capture_output=True, text=True).stdout
        b = json.loads(a)
        d = b
    else:
        a = "Local" if path['bitcoincli'] else "Remote"
        blk = rpc('getblockchaininfo')
        d = blk

        cert_path = lndconnectload["tls"]
        macaroon = codecs.encode(open(lndconnectload["macaroon"], 'rb').read(), 'hex')
        headers = {'Grpc-Metadata-macaroon': macaroon}
        url = f'https://{lndconnectload["ip_port"]}/v1/getinfo'
        r = requests.get(url, headers=headers, verify=cert_path)
        alias = r.json()
    print("""\t\t
    \033[1;37;40m{}\033[0;37;40m: \033[1;31;40mPyBLOCK\033[0;37;40m
    \033[1;37;40mBlock\033[0;37;40m: \033[1;32;40m{}\033[0;37;40m
    \033[1;37;40mVersion\033[0;37;40m: {}

    \u001b[38;5;202mA.\033[0;37;40m Difficulty
    \u001b[38;5;202mC.\033[0;37;40m Pool
    \u001b[38;5;202mE.\033[0;37;40m Miner
    \u001b[33;1mEnter.\033[0;37;40m Return
    \n\n\x1b[?25h""".format(n if path['bitcoincli'] else a, d['blocks'], version ))
    slushpoolLOCALOnchainONLYMenu(input("\033[1;32;40mSelect option: \033[0;37;40m"))

def runTheNumbersMenu():
    clear()
    blogo()
    sysinfo()
    pathexec()
    lndconnectexec()
    if path['bitcoincli']:
        n = "Local" if path['bitcoincli'] else "Remote"
        bitcoincli = " getblockchaininfo"
        a = subprocess.run([path['bitcoincli']] + bitcoincli.split(), capture_output=True, text=True).stdout
        b = json.loads(a)
        d = b

        lncli = " getinfo"
        lsd = subprocess.run([lndconnectload['ln']] + lncli.split(), capture_output=True, text=True).stdout
        lsd0 = str(lsd)
        alias = json.loads(lsd0)
    else:
        a = "Local" if path['bitcoincli'] else "Remote"
        blk = rpc('getblockchaininfo')
        d = blk

        cert_path = lndconnectload["tls"]
        macaroon = codecs.encode(open(lndconnectload["macaroon"], 'rb').read(), 'hex')
        headers = {'Grpc-Metadata-macaroon': macaroon}
        url = f'https://{lndconnectload["ip_port"]}/v1/getinfo'
        r = requests.get(url, headers=headers, verify=cert_path)
        alias = r.json()
    print("""\t\t
    \033[1;37;40m{}\033[0;37;40m: \033[1;31;40mPyBLOCK\033[0;37;40m
    \033[1;37;40mNode\033[0;37;40m: \033[1;33;40m{}\033[0;37;40m
    \033[1;37;40mBlock\033[0;37;40m: \033[1;32;40m{}\033[0;37;40m
    \033[1;37;40mVersion\033[0;37;40m: {}

    \033[1;32;40mA.\033[0;37;40m Countdown Block
    \033[1;32;40mB.\033[0;37;40m Countdown Halving
    \033[1;32;40mC.\033[0;37;40m Audit
    \033[1;32;40mD.\033[0;37;40m Templates & Blocks
    \033[1;32;40mE.\033[0;37;40m Epoch
    \u001b[33;1mEnter.\033[0;37;40m Return
    \n\n\x1b[?25h""".format(n if path['bitcoincli'] else a , alias['alias'], d['blocks'], version ))
    runTheNumbersControl(input("\033[1;32;40mSelect option: \033[0;37;40m"))

def runTheNumbersMenuOnchainONLY():
    clear()
    blogo()
    sysinfo()
    pathexec()
    #lndconnectexec()
    if path['bitcoincli']:
        n = "Local" if path['bitcoincli'] else "Remote"
        bitcoincli = " getblockchaininfo"
        a = subprocess.run([path['bitcoincli']] + bitcoincli.split(), capture_output=True, text=True).stdout
        b = json.loads(a)
        d = b
    else:
        a = "Local" if path['bitcoincli'] else "Remote"
        blk = rpc('getblockchaininfo')
        d = blk

        cert_path = lndconnectload["tls"]
        macaroon = codecs.encode(open(lndconnectload["macaroon"], 'rb').read(), 'hex')
        headers = {'Grpc-Metadata-macaroon': macaroon}
        url = f'https://{lndconnectload["ip_port"]}/v1/getinfo'
        r = requests.get(url, headers=headers, verify=cert_path)
        alias = r.json()
    print("""\t\t
    \033[1;37;40m{}\033[0;37;40m: \033[1;31;40mPyBLOCK\033[0;37;40m
    \033[1;37;40mBlock\033[0;37;40m: \033[1;32;40m{}\033[0;37;40m
    \033[1;37;40mVersion\033[0;37;40m: {}

    \033[1;32;40mA.\033[0;37;40m Countdown Block
    \033[1;32;40mB.\033[0;37;40m Countdown Halving
    \033[1;32;40mC.\033[0;37;40m Audit
    \033[1;32;40mD.\033[0;37;40m Templates & Blocks
    \033[1;32;40mE.\033[0;37;40m Epoch
    \u001b[33;1mEnter.\033[0;37;40m Return
    \n\n\x1b[?25h""".format(n if path['bitcoincli'] else a, d['blocks'], version ))
    runTheNumbersControlOnchainONLY(input("\033[1;32;40mSelect option: \033[0;37;40m"))

def runTheNumbersMenuConn():
    clear()
    blogo()
    sysinfo()
    pathexec()
    lndconnectexec()
    if path['bitcoincli']:
        n = "Local" if path['bitcoincli'] else "Remote"
        bitcoincli = " getblockchaininfo"
        a = subprocess.run([path['bitcoincli']] + bitcoincli.split(), capture_output=True, text=True).stdout
        b = json.loads(a)
        d = b

        lncli = " getinfo"
        lsd = subprocess.run([lndconnectload['ln']] + lncli.split(), capture_output=True, text=True).stdout
        lsd0 = str(lsd)
        alias = json.loads(lsd0)
    else:
        a = "Local" if path['bitcoincli'] else "Remote"
        blk = rpc('getblockchaininfo')
        d = blk

        cert_path = lndconnectload["tls"]
        macaroon = codecs.encode(open(lndconnectload["macaroon"], 'rb').read(), 'hex')
        headers = {'Grpc-Metadata-macaroon': macaroon}
        url = f'https://{lndconnectload["ip_port"]}/v1/getinfo'
        r = requests.get(url, headers=headers, verify=cert_path)
        alias = r.json()
    print("""\t\t
    \033[1;37;40m{}\033[0;37;40m: \033[1;31;40mPyBLOCK\033[0;37;40m
    \033[1;37;40mNode\033[0;37;40m: \033[1;33;40m{}\033[0;37;40m
    \033[1;37;40mBlock\033[0;37;40m: \033[1;32;40m{}\033[0;37;40m
    \033[1;37;40mVersion\033[0;37;40m: {}

    \033[1;32;40mA.\033[0;37;40m Countdown Block
    \033[1;32;40mB.\033[0;37;40m Countdown Halving
    \033[1;32;40mC.\033[0;37;40m Audit
    \033[1;32;40mD.\033[0;37;40m Templates & Blocks
    \033[1;32;40mE.\033[0;37;40m Epoch
    \u001b[33;1mEnter.\033[0;37;40m Return
    \n\n\x1b[?25h""".format(n if path['bitcoincli'] else a , alias['alias'], d['blocks'], version ))
    runTheNumbersControlConn(input("\033[1;32;40mSelect option: \033[0;37;40m"))

def weatherMenuOnchainONLY():
    clear()
    blogo()
    sysinfo()
    pathexec()
    #lndconnectexec()
    if path['bitcoincli']:
        n = "Local" if path['bitcoincli'] else "Remote"
        bitcoincli = " getblockchaininfo"
        a = subprocess.run([path['bitcoincli']] + bitcoincli.split(), capture_output=True, text=True).stdout
        b = json.loads(a)
        d = b
    else:
        a = "Local" if path['bitcoincli'] else "Remote"
        blk = rpc('getblockchaininfo')
        d = blk

        cert_path = lndconnectload["tls"]
        macaroon = codecs.encode(open(lndconnectload["macaroon"], 'rb').read(), 'hex')
        headers = {'Grpc-Metadata-macaroon': macaroon}
        url = f'https://{lndconnectload["ip_port"]}/v1/getinfo'
        r = requests.get(url, headers=headers, verify=cert_path)
        alias = r.json()
    print("""\t\t
    \033[1;37;40m{}\033[0;37;40m: \033[1;31;40mPyBLOCK\033[0;37;40m
    \033[1;37;40mBlock\033[0;37;40m: \033[1;32;40m{}\033[0;37;40m
    \033[1;37;40mVersion\033[0;37;40m: {}

    \033[1;32;40mA.\033[0;37;40m Version 1
    \033[1;32;40mB.\033[0;37;40m Version 2
    \u001b[33;1mEnter.\033[0;37;40m Return
    \n\n\x1b[?25h""".format(n if path['bitcoincli'] else a, d['blocks'], version ))
    menuWeatherOnchainONLY(input("\033[1;32;40mSelect option: \033[0;37;40m"))

def weatherMenu():
    clear()
    blogo()
    sysinfo()
    pathexec()
    lndconnectexec()
    if path['bitcoincli']:
        n = "Local" if path['bitcoincli'] else "Remote"
        bitcoincli = " getblockchaininfo"
        a = subprocess.run([path['bitcoincli']] + bitcoincli.split(), capture_output=True, text=True).stdout
        b = json.loads(a)
        d = b

        lncli = " getinfo"
        lsd = subprocess.run([lndconnectload['ln']] + lncli.split(), capture_output=True, text=True).stdout
        lsd0 = str(lsd)
        alias = json.loads(lsd0)
    else:
        a = "Local" if path['bitcoincli'] else "Remote"
        blk = rpc('getblockchaininfo')
        d = blk

        cert_path = lndconnectload["tls"]
        macaroon = codecs.encode(open(lndconnectload["macaroon"], 'rb').read(), 'hex')
        headers = {'Grpc-Metadata-macaroon': macaroon}
        url = f'https://{lndconnectload["ip_port"]}/v1/getinfo'
        r = requests.get(url, headers=headers, verify=cert_path)
        alias = r.json()
    print("""\t\t
    \033[1;37;40m{}\033[0;37;40m: \033[1;31;40mPyBLOCK\033[0;37;40m
    \033[1;37;40mNode\033[0;37;40m: \033[1;33;40m{}\033[0;37;40m
    \033[1;37;40mBlock\033[0;37;40m: \033[1;32;40m{}\033[0;37;40m
    \033[1;37;40mVersion\033[0;37;40m: {}

    \033[1;32;40mA.\033[0;37;40m Version 1
    \033[1;32;40mB.\033[0;37;40m Version 2
    \u001b[33;1mEnter.\033[0;37;40m Return
    \n\n\x1b[?25h""".format(n if path['bitcoincli'] else a , alias['alias'], d['blocks'], version ))
    menuWeather(input("\033[1;32;40mSelect option: \033[0;37;40m"))

def dnt(): # Donation selection menu
    clear()
    blogo()
    sysinfo()
    pathexec()
    lndconnectexec()
    if path['bitcoincli']:
        n = "Local" if path['bitcoincli'] else "Remote"
        bitcoincli = " getblockchaininfo"
        a = subprocess.run([path['bitcoincli']] + bitcoincli.split(), capture_output=True, text=True).stdout
        b = json.loads(a)
        d = b

        lncli = " getinfo"
        lsd = subprocess.run([lndconnectload['ln']] + lncli.split(), capture_output=True, text=True).stdout
        lsd0 = str(lsd)
        alias = json.loads(lsd0)
    else:
        a = "Local" if path['bitcoincli'] else "Remote"
        blk = rpc('getblockchaininfo')
        d = blk

        cert_path = lndconnectload["tls"]
        macaroon = codecs.encode(open(lndconnectload["macaroon"], 'rb').read(), 'hex')
        headers = {'Grpc-Metadata-macaroon': macaroon}
        url = f'https://{lndconnectload["ip_port"]}/v1/getinfo'
        r = requests.get(url, headers=headers, verify=cert_path)
        alias = r.json()
    print("""\t\t
    \033[1;37;40m{}\033[0;37;40m: \033[1;31;40mPyBLOCK\033[0;37;40m
    \033[1;37;40mNode\033[0;37;40m: \033[1;33;40m{}\033[0;37;40m
    \033[1;37;40mBlock\033[0;37;40m: \033[1;32;40m{}\033[0;37;40m
    \033[1;37;40mVersion\033[0;37;40m: {}

    \u001b[38;5;15mA.\033[0;37;40m Developers Donation
    \u001b[38;5;15mB.\033[0;37;40m Testers Donation
    \u001b[33;1mEnter.\033[0;37;40m Return
    \n\n\x1b[?25h""".format(n if path['bitcoincli'] else a , alias['alias'], d['blocks'], version ))
    menuC(input("\033[1;32;40mSelect option: \033[0;37;40m"))

def dntOnchainONLY(): # Donation selection menu
    clear()
    blogo()
    sysinfo()
    pathexec()
    #lndconnectexec()
    if path['bitcoincli']:
        n = "Local" if path['bitcoincli'] else "Remote"
        bitcoincli = " getblockchaininfo"
        a = subprocess.run([path['bitcoincli']] + bitcoincli.split(), capture_output=True, text=True).stdout
        b = json.loads(a)
        d = b
    else:
        a = "Local" if path['bitcoincli'] else "Remote"
        blk = rpc('getblockchaininfo')
        d = blk

        cert_path = lndconnectload["tls"]
        macaroon = codecs.encode(open(lndconnectload["macaroon"], 'rb').read(), 'hex')
        headers = {'Grpc-Metadata-macaroon': macaroon}
        url = f'https://{lndconnectload["ip_port"]}/v1/getinfo'
        r = requests.get(url, headers=headers, verify=cert_path)
        alias = r.json()
    print("""\t\t
    \033[1;37;40m{}\033[0;37;40m: \033[1;31;40mPyBLOCK\033[0;37;40m
    \033[1;37;40mBlock\033[0;37;40m: \033[1;32;40m{}\033[0;37;40m
    \033[1;37;40mVersion\033[0;37;40m: {}

    \u001b[38;5;15mA.\033[0;37;40m Developers Donation
    \u001b[38;5;15mB.\033[0;37;40m Testers Donation
    \u001b[33;1mEnter.\033[0;37;40m Return
    \n\n\x1b[?25h""".format(n if path['bitcoincli'] else a, d['blocks'], version ))
    menuCOnchainONLY(input("\033[1;32;40mSelect option: \033[0;37;40m"))


def dntDev(): # Dev Donation Menu
    clear()
    blogo()
    sysinfo()
    pathexec()
    lndconnectexec()
    if path['bitcoincli']:
        n = "Local" if path['bitcoincli'] else "Remote"
        bitcoincli = " getblockchaininfo"
        a = subprocess.run([path['bitcoincli']] + bitcoincli.split(), capture_output=True, text=True).stdout
        b = json.loads(a)
        d = b

        lncli = " getinfo"
        lsd = subprocess.run([lndconnectload['ln']] + lncli.split(), capture_output=True, text=True).stdout
        lsd0 = str(lsd)
        alias = json.loads(lsd0)
    else:
        a = "Local" if path['bitcoincli'] else "Remote"
        blk = rpc('getblockchaininfo')
        d = blk

        cert_path = lndconnectload["tls"]
        macaroon = codecs.encode(open(lndconnectload["macaroon"], 'rb').read(), 'hex')
        headers = {'Grpc-Metadata-macaroon': macaroon}
        url = f'https://{lndconnectload["ip_port"]}/v1/getinfo'
        r = requests.get(url, headers=headers, verify=cert_path)
        alias = r.json()
    print("""\t\t
    \033[1;37;40m{}\033[0;37;40m: \033[1;31;40mPyBLOCK\033[0;37;40m
    \033[1;37;40mNode\033[0;37;40m: \033[1;33;40m{}\033[0;37;40m
    \033[1;37;40mBlock\033[0;37;40m: \033[1;32;40m{}\033[0;37;40m
    \033[1;37;40mVersion\033[0;37;40m: {}

    \u001b[38;5;202mA.\033[0;37;40m Samourai PayNym
    \u001b[38;5;202mB.\033[0;37;40m Bitcoin Address
    \u001b[33;1mC.\033[0;37;40m Lightning Network
    \u001b[33;1mEnter.\033[0;37;40m Return
    \n\n\x1b[?25h""".format(n if path['bitcoincli'] else a , alias['alias'], d['blocks'], version ))
    menuE(input("\033[1;32;40mSelect option: \033[0;37;40m"))

def dntDevOnchainONLY(): # Dev Donation Menu
    clear()
    blogo()
    sysinfo()
    pathexec()
    #lndconnectexec()
    if path['bitcoincli']:
        n = "Local" if path['bitcoincli'] else "Remote"
        bitcoincli = " getblockchaininfo"
        a = subprocess.run([path['bitcoincli']] + bitcoincli.split(), capture_output=True, text=True).stdout
        b = json.loads(a)
        d = b
    else:
        a = "Local" if path['bitcoincli'] else "Remote"
        blk = rpc('getblockchaininfo')
        d = blk

        cert_path = lndconnectload["tls"]
        macaroon = codecs.encode(open(lndconnectload["macaroon"], 'rb').read(), 'hex')
        headers = {'Grpc-Metadata-macaroon': macaroon}
        url = f'https://{lndconnectload["ip_port"]}/v1/getinfo'
        r = requests.get(url, headers=headers, verify=cert_path)
        alias = r.json()
    print("""\t\t
    \033[1;37;40m{}\033[0;37;40m: \033[1;31;40mPyBLOCK\033[0;37;40m
    \033[1;37;40mBlock\033[0;37;40m: \033[1;32;40m{}\033[0;37;40m
    \033[1;37;40mVersion\033[0;37;40m: {}

    \u001b[38;5;202mA.\033[0;37;40m Samourai PayNym
    \u001b[38;5;202mB.\033[0;37;40m Bitcoin Address
    \u001b[33;1mC.\033[0;37;40m Lightning Network
    \u001b[33;1mEnter.\033[0;37;40m Return
    \n\n\x1b[?25h""".format(n if path['bitcoincli'] else a, d['blocks'], version ))
    menuEOnchainONLY(input("\033[1;32;40mSelect option: \033[0;37;40m"))

def dntTst(): # Tester Donation Menu
    clear()
    blogo()
    sysinfo()
    pathexec()
    lndconnectexec()
    if path['bitcoincli']:
        n = "Local" if path['bitcoincli'] else "Remote"
        bitcoincli = " getblockchaininfo"
        a = subprocess.run([path['bitcoincli']] + bitcoincli.split(), capture_output=True, text=True).stdout
        b = json.loads(a)
        d = b

        lncli = " getinfo"
        lsd = subprocess.run([lndconnectload['ln']] + lncli.split(), capture_output=True, text=True).stdout
        lsd0 = str(lsd)
        alias = json.loads(lsd0)
    else:
        a = "Local" if path['bitcoincli'] else "Remote"
        blk = rpc('getblockchaininfo')
        d = blk

        cert_path = lndconnectload["tls"]
        macaroon = codecs.encode(open(lndconnectload["macaroon"], 'rb').read(), 'hex')
        headers = {'Grpc-Metadata-macaroon': macaroon}
        url = f'https://{lndconnectload["ip_port"]}/v1/getinfo'
        r = requests.get(url, headers=headers, verify=cert_path)
        alias = r.json()
    print("""\t\t
    \033[1;37;40m{}\033[0;37;40m: \033[1;31;40mPyBLOCK\033[0;37;40m
    \033[1;37;40mNode\033[0;37;40m: \033[1;33;40m{}\033[0;37;40m
    \033[1;37;40mBlock\033[0;37;40m: \033[1;32;40m{}\033[0;37;40m
    \033[1;37;40mVersion\033[0;37;40m: {}

    \u001b[38;5;202mA.\033[0;37;40m Bitcoin Address
    \u001b[33;1mB.\033[0;37;40m Lightning Network
    \u001b[33;1mEnter.\033[0;37;40m Return
    \n\n\x1b[?25h""".format(n if path['bitcoincli'] else a , alias['alias'], d['blocks'], version ))
    menuF(input("\033[1;32;40mSelect option: \033[0;37;40m"))

def dntTstOnchainONLY(): # Tester Donation Menu
    clear()
    blogo()
    sysinfo()
    pathexec()
    #lndconnectexec()
    if path['bitcoincli']:
        n = "Local" if path['bitcoincli'] else "Remote"
        bitcoincli = " getblockchaininfo"
        a = subprocess.run([path['bitcoincli']] + bitcoincli.split(), capture_output=True, text=True).stdout
        b = json.loads(a)
        d = b
    else:
        a = "Local" if path['bitcoincli'] else "Remote"
        blk = rpc('getblockchaininfo')
        d = blk

        cert_path = lndconnectload["tls"]
        macaroon = codecs.encode(open(lndconnectload["macaroon"], 'rb').read(), 'hex')
        headers = {'Grpc-Metadata-macaroon': macaroon}
        url = f'https://{lndconnectload["ip_port"]}/v1/getinfo'
        r = requests.get(url, headers=headers, verify=cert_path)
        alias = r.json()
    print("""\t\t
    \033[1;37;40m{}\033[0;37;40m: \033[1;31;40mPyBLOCK\033[0;37;40m
    \033[1;37;40mBlock\033[0;37;40m: \033[1;32;40m{}\033[0;37;40m
    \033[1;37;40mVersion\033[0;37;40m: {}

    \u001b[38;5;202mA.\033[0;37;40m Bitcoin Address
    \u001b[33;1mB.\033[0;37;40m Lightning Network
    \u001b[33;1mEnter.\033[0;37;40m Return
    \n\n\x1b[?25h""".format(n if path['bitcoincli'] else a, d['blocks'], version ))
    menuFOnchainONLY(input("\033[1;32;40mSelect option: \033[0;37;40m"))


def satnodeMenu(): # Satnode Menu
    clear()
    blogo()
    sysinfo()
    pathexec()
    lndconnectexec()
    if path['bitcoincli']:
        n = "Local" if path['bitcoincli'] else "Remote"
        bitcoincli = " getblockchaininfo"
        a = subprocess.run([path['bitcoincli']] + bitcoincli.split(), capture_output=True, text=True).stdout
        b = json.loads(a)
        d = b

        lncli = " getinfo"
        lsd = subprocess.run([lndconnectload['ln']] + lncli.split(), capture_output=True, text=True).stdout
        lsd0 = str(lsd)
        alias = json.loads(lsd0)
    else:
        a = "Local" if path['bitcoincli'] else "Remote"
        blk = rpc('getblockchaininfo')
        d = blk

        cert_path = lndconnectload["tls"]
        macaroon = codecs.encode(open(lndconnectload["macaroon"], 'rb').read(), 'hex')
        headers = {'Grpc-Metadata-macaroon': macaroon}
        url = f'https://{lndconnectload["ip_port"]}/v1/getinfo'
        r = requests.get(url, headers=headers, verify=cert_path)
        alias = r.json()
    print("""\t\t
    \033[1;37;40m{}\033[0;37;40m: \033[1;31;40mPyBLOCK\033[0;37;40m
    \033[1;37;40mNode\033[0;37;40m: \033[1;33;40m{}\033[0;37;40m
    \033[1;37;40mBlock\033[0;37;40m: \033[1;32;40m{}\033[0;37;40m
    \033[1;37;40mVersion\033[0;37;40m: {}

    \033[1;32;40mA.\033[0;37;40m Start SatNode
    \033[1;32;40mB.\033[0;37;40m Feed
    \033[1;32;40mC.\033[0;37;40m Setup
    \033[1;34;40mS.\033[0;37;40m Send a Message to Space
    \u001b[33;1mEnter.\033[0;37;40m Return
    \n\n\x1b[?25h""".format(n if path['bitcoincli'] else a , alias['alias'], d['blocks'], version ))
    menuD(input("\033[1;32;40mSelect option: \033[0;37;40m"))

def satnodeMenuOnchainONLY(): # Satnode Menu
    clear()
    blogo()
    sysinfo()
    pathexec()
    #lndconnectexec()
    if path['bitcoincli']:
        n = "Local" if path['bitcoincli'] else "Remote"
        bitcoincli = " getblockchaininfo"
        a = subprocess.run([path['bitcoincli']] + bitcoincli.split(), capture_output=True, text=True).stdout
        b = json.loads(a)
        d = b
    else:
        a = "Local" if path['bitcoincli'] else "Remote"
        blk = rpc('getblockchaininfo')
        d = blk

        cert_path = lndconnectload["tls"]
        macaroon = codecs.encode(open(lndconnectload["macaroon"], 'rb').read(), 'hex')
        headers = {'Grpc-Metadata-macaroon': macaroon}
        url = f'https://{lndconnectload["ip_port"]}/v1/getinfo'
        r = requests.get(url, headers=headers, verify=cert_path)
        alias = r.json()
    print("""\t\t
    \033[1;37;40m{}\033[0;37;40m: \033[1;31;40mPyBLOCK\033[0;37;40m
    \033[1;37;40mBlock\033[0;37;40m: \033[1;32;40m{}\033[0;37;40m
    \033[1;37;40mVersion\033[0;37;40m: {}

    \033[1;32;40mA.\033[0;37;40m Start SatNode
    \033[1;32;40mB.\033[0;37;40m Feed
    \033[1;32;40mC.\033[0;37;40m Setup
    \033[1;34;40mS.\033[0;37;40m Send a Message to Space
    \u001b[33;1mEnter.\033[0;37;40m Return
    \n\n\x1b[?25h""".format(n if path['bitcoincli'] else a, d['blocks'], version ))
    menuD(input("\033[1;32;40mSelect option: \033[0;37;40m"))

def rateSX():
    clear()
    blogo()
    sysinfo()
    pathexec()
    lndconnectexec()
    if path['bitcoincli']:
        n = "Local" if path['bitcoincli'] else "Remote"
        bitcoincli = " getblockchaininfo"
        a = subprocess.run([path['bitcoincli']] + bitcoincli.split(), capture_output=True, text=True).stdout
        b = json.loads(a)
        d = b

        lncli = " getinfo"
        lsd = subprocess.run([lndconnectload['ln']] + lncli.split(), capture_output=True, text=True).stdout
        lsd0 = str(lsd)
        alias = json.loads(lsd0)
    else:
        a = "Local" if path['bitcoincli'] else "Remote"
        blk = rpc('getblockchaininfo')
        d = blk

        cert_path = lndconnectload["tls"]
        macaroon = codecs.encode(open(lndconnectload["macaroon"], 'rb').read(), 'hex')
        headers = {'Grpc-Metadata-macaroon': macaroon}
        url = f'https://{lndconnectload["ip_port"]}/v1/getinfo'
        r = requests.get(url, headers=headers, verify=cert_path)
        alias = r.json()
    print("""\t\t
    \033[1;37;40m{}\033[0;37;40m: \033[1;31;40mPyBLOCK\033[0;37;40m
    \033[1;37;40mNode\033[0;37;40m: \033[1;33;40m{}\033[0;37;40m
    \033[1;37;40mBlock\033[0;37;40m: \033[1;32;40m{}\033[0;37;40m
    \033[1;37;40mVersion\033[0;37;40m: {}

    \033[1;32;40mA.\033[0;37;40m Rate
    \033[1;32;40mB.\033[0;37;40m Chart
    \u001b[33;1mEnter.\033[0;37;40m Return
    \n\n\x1b[?25h""".format(n if path['bitcoincli'] else a , alias['alias'], d['blocks'], version ))
    rateSXMenu(input("\033[1;32;40mSelect option: \033[0;37;40m"))

def rateSXOncainONLY():
    clear()
    blogo()
    sysinfo()
    pathexec()
    #lndconnectexec()
    if path['bitcoincli']:
        n = "Local" if path['bitcoincli'] else "Remote"
        bitcoincli = " getblockchaininfo"
        a = subprocess.run([path['bitcoincli']] + bitcoincli.split(), capture_output=True, text=True).stdout
        b = json.loads(a)
        d = b
    else:
        a = "Local" if path['bitcoincli'] else "Remote"
        blk = rpc('getblockchaininfo')
        d = blk

        cert_path = lndconnectload["tls"]
        macaroon = codecs.encode(open(lndconnectload["macaroon"], 'rb').read(), 'hex')
        headers = {'Grpc-Metadata-macaroon': macaroon}
        url = f'https://{lndconnectload["ip_port"]}/v1/getinfo'
        r = requests.get(url, headers=headers, verify=cert_path)
        alias = r.json()
    print("""\t\t
    \033[1;37;40m{}\033[0;37;40m: \033[1;31;40mPyBLOCK\033[0;37;40m
    \033[1;37;40mBlock\033[0;37;40m: \033[1;32;40m{}\033[0;37;40m
    \033[1;37;40mVersion\033[0;37;40m: {}

    \033[1;32;40mA.\033[0;37;40m Rate
    \033[1;32;40mB.\033[0;37;40m Chart
    \u001b[33;1mEnter.\033[0;37;40m Return
    \n\n\x1b[?25h""".format(n if path['bitcoincli'] else a, d['blocks'], version ))
    rateSXMenuOnchainONLY(input("\033[1;32;40mSelect option: \033[0;37;40m"))

def mempoolmenu():
    clear()
    blogo()
    sysinfo()
    pathexec()
    lndconnectexec()
    if path['bitcoincli']:
        n = "Local" if path['bitcoincli'] else "Remote"
        bitcoincli = " getblockchaininfo"
        a = subprocess.run([path['bitcoincli']] + bitcoincli.split(), capture_output=True, text=True).stdout
        b = json.loads(a)
        d = b

        lncli = " getinfo"
        lsd = subprocess.run([lndconnectload['ln']] + lncli.split(), capture_output=True, text=True).stdout
        lsd0 = str(lsd)
        alias = json.loads(lsd0)
    else:
        a = "Local" if path['bitcoincli'] else "Remote"
        blk = rpc('getblockchaininfo')
        d = blk

        cert_path = lndconnectload["tls"]
        macaroon = codecs.encode(open(lndconnectload["macaroon"], 'rb').read(), 'hex')
        headers = {'Grpc-Metadata-macaroon': macaroon}
        url = f'https://{lndconnectload["ip_port"]}/v1/getinfo'
        r = requests.get(url, headers=headers, verify=cert_path)
        alias = r.json()
    print("""\t\t
    \033[1;37;40m{}\033[0;37;40m: \033[1;31;40mPyBLOCK\033[0;37;40m
    \033[1;37;40mNode\033[0;37;40m: \033[1;33;40m{}\033[0;37;40m
    \033[1;37;40mBlock\033[0;37;40m: \033[1;32;40m{}\033[0;37;40m
    \033[1;37;40mVersion\033[0;37;40m: {}

    \033[1;32;40mA.\033[0;37;40m Blocks
    \033[1;32;40mB.\033[0;37;40m Recommended Fee
    \033[1;32;40mC.\033[0;37;40m Mempool Shell
    \u001b[33;1mEnter.\033[0;37;40m Return
    \n\n\x1b[?25h""".format(n if path['bitcoincli'] else a , alias['alias'], d['blocks'], version ))
    mempoolmenuS(input("\033[1;32;40mSelect option: \033[0;37;40m"))

def mempoolmenuOnchainONLY():
    clear()
    blogo()
    sysinfo()
    pathexec()
    #lndconnectexec()
    if path['bitcoincli']:
        n = "Local" if path['bitcoincli'] else "Remote"
        bitcoincli = " getblockchaininfo"
        a = subprocess.run([path['bitcoincli']] + bitcoincli.split(), capture_output=True, text=True).stdout
        b = json.loads(a)
        d = b
    else:
        a = "Local" if path['bitcoincli'] else "Remote"
        blk = rpc('getblockchaininfo')
        d = blk

        cert_path = lndconnectload["tls"]
        macaroon = codecs.encode(open(lndconnectload["macaroon"], 'rb').read(), 'hex')
        headers = {'Grpc-Metadata-macaroon': macaroon}
        url = f'https://{lndconnectload["ip_port"]}/v1/getinfo'
        r = requests.get(url, headers=headers, verify=cert_path)
        alias = r.json()
    print("""\t\t
    \033[1;37;40m{}\033[0;37;40m: \033[1;31;40mPyBLOCK\033[0;37;40m
    \033[1;37;40mBlock\033[0;37;40m: \033[1;32;40m{}\033[0;37;40m
    \033[1;37;40mVersion\033[0;37;40m: {}

    \033[1;32;40mA.\033[0;37;40m Blocks
    \033[1;32;40mB.\033[0;37;40m Recommended Fee
    \033[1;32;40mC.\033[0;37;40m Mempool Shell
    \u001b[33;1mEnter.\033[0;37;40m Return
    \n\n\x1b[?25h""".format(n if path['bitcoincli'] else a, d['blocks'], version ))
    mempoolmenuSOnchainONLY(input("\033[1;32;40mSelect option: \033[0;37;40m"))


def APILnbit():
    bitLN = {"NN":"","pd":""}
    if os.path.isfile('lnbitSN.conf'): # Check if the file 'bclock.conf' is in the same folder
        bitData= json.load(open("lnbitSN.conf", "r")) # Load the file 'bclock.conf'
        bitLN = bitData # Copy the variable pathv to 'path'
    clear()
    blogo()
    sysinfo()
    pathexec()
    lndconnectexec()
    if path['bitcoincli']:
        n = "Local" if path['bitcoincli'] else "Remote"
        bitcoincli = " getblockchaininfo"
        a = subprocess.run([path['bitcoincli']] + bitcoincli.split(), capture_output=True, text=True).stdout
        b = json.loads(a)
        d = b

        lncli = " getinfo"
        lsd = subprocess.run([lndconnectload['ln']] + lncli.split(), capture_output=True, text=True).stdout
        lsd0 = str(lsd)
        alias = json.loads(lsd0)
    else:
        a = "Local" if path['bitcoincli'] else "Remote"
        blk = rpc('getblockchaininfo')
        d = blk

        cert_path = lndconnectload["tls"]
        macaroon = codecs.encode(open(lndconnectload["macaroon"], 'rb').read(), 'hex')
        headers = {'Grpc-Metadata-macaroon': macaroon}
        url = f'https://{lndconnectload["ip_port"]}/v1/getinfo'
        r = requests.get(url, headers=headers, verify=cert_path)
        alias = r.json()
    print("""\t\t
    \033[1;37;40m{}\033[0;37;40m: \033[1;31;40mPyBLOCK\033[0;37;40m
    \033[1;37;40mNode\033[0;37;40m: \033[1;33;40m{}\033[0;37;40m
    \033[1;37;40mBlock\033[0;37;40m: \033[1;32;40m{}\033[0;37;40m
    \033[1;37;40mVersion\033[0;37;40m: {}

    \033[0;37;40mLNBits SN:{} \033[1;34;40mPremium\033[0;37;40m

    \033[1;32;40mA.\033[0;37;40m New Invoice
    \033[1;32;40mB.\033[0;37;40m Pay Invoice
    \033[1;32;40mC.\033[0;37;40m New PayWall
    \033[1;32;40mD.\033[0;37;40m Delete PayWall
    \033[1;32;40mE.\033[0;37;40m List PayWalls
    \033[1;32;40mF.\033[0;37;40m Create LNURL
    \033[1;32;40mG.\033[0;37;40m List LNURL
    \u001b[33;1mEnter.\033[0;37;40m Return
    \n\n\x1b[?25h""".format(n if path['bitcoincli'] else a , alias['alias'], d['blocks'], version, bitLN['NN'], ))
    menuLNBPI(input("\033[1;32;40mSelect option: \033[0;37;40m"))

def APILnbitOnchainONLY():
    path = {"ip_port":"", "rpcuser":"", "rpcpass":"", "bitcoincli":""}
    pathv = json.load(open("config/bclock.conf", "r")) # Load the file 'bclock.conf'
    path = pathv # Copy the variable pathv to 'path'
    lndconnectData = json.load(open("config/blndconnect.conf", "r")) # Load the file 'bclock.conf'
    lndconnectload = lndconnectData # Copy the variable pathv to 'path'
    bitLN = {"NN":"","pd":""}
    if os.path.isfile('lnbitSN.conf'): # Check if the file 'bclock.conf' is in the same folder
        bitData= json.load(open("lnbitSN.conf", "r")) # Load the file 'bclock.conf'
        bitLN = bitData # Copy the variable pathv to 'path'
    clear()
    blogo()
    sysinfo()
    pathexec()
    #lndconnectexec()
    if path['bitcoincli']:
        n = "Local" if path['bitcoincli'] else "Remote"
        bitcoincli = " getblockchaininfo"
        a = subprocess.run([path['bitcoincli']] + bitcoincli.split(), capture_output=True, text=True).stdout
        b = json.loads(a)
        d = b
    else:
        a = "Local" if path['bitcoincli'] else "Remote"
        blk = rpc('getblockchaininfo')
        d = blk

        cert_path = lndconnectload["tls"]
        macaroon = codecs.encode(open(lndconnectload["macaroon"], 'rb').read(), 'hex')
        headers = {'Grpc-Metadata-macaroon': macaroon}
        url = f'https://{lndconnectload["ip_port"]}/v1/getinfo'
        r = requests.get(url, headers=headers, verify=cert_path)
        alias = r.json()
    print("""\t\t
    \033[1;37;40m{}\033[0;37;40m: \033[1;31;40mPyBLOCK\033[0;37;40m
    \033[1;37;40mBlock\033[0;37;40m: \033[1;32;40m{}\033[0;37;40m
    \033[1;37;40mVersion\033[0;37;40m: {}

    \033[0;37;40mLNBits SN:{} \033[1;34;40mPremium\033[0;37;40m

    \033[1;32;40mA.\033[0;37;40m New Invoice
    \033[1;32;40mB.\033[0;37;40m Pay Invoice
    \033[1;32;40mC.\033[0;37;40m New PayWall
    \033[1;32;40mD.\033[0;37;40m Delete PayWall
    \033[1;32;40mE.\033[0;37;40m List PayWalls
    \033[1;32;40mF.\033[0;37;40m Create LNURL
    \033[1;32;40mG.\033[0;37;40m List LNURL
    \u001b[33;1mEnter.\033[0;37;40m Return
    \n\n\x1b[?25h""".format(n if path['bitcoincli'] else a, d['blocks'], version, bitLN['NN'], ))
    menuLNBPIOnchainONLY(input("\033[1;32;40mSelect option: \033[0;37;40m"))

def APILnPay():
    bitLN = {"NN":"","pd":""}
    if os.path.isfile('lnpaySN.conf'): # Check if the file 'bclock.conf' is in the same folder
        bitData= json.load(open("lnpaySN.conf", "r")) # Load the file 'bclock.conf'
        bitLN = bitData # Copy the variable pathv to 'path'
    clear()
    blogo()
    sysinfo()
    pathexec()
    lndconnectexec()
    if path['bitcoincli']:
        n = "Local" if path['bitcoincli'] else "Remote"
        bitcoincli = " getblockchaininfo"
        a = subprocess.run([path['bitcoincli']] + bitcoincli.split(), capture_output=True, text=True).stdout
        b = json.loads(a)
        d = b

        lncli = " getinfo"
        lsd = subprocess.run([lndconnectload['ln']] + lncli.split(), capture_output=True, text=True).stdout
        lsd0 = str(lsd)
        alias = json.loads(lsd0)
    else:
        a = "Local" if path['bitcoincli'] else "Remote"
        blk = rpc('getblockchaininfo')
        d = blk

        cert_path = lndconnectload["tls"]
        macaroon = codecs.encode(open(lndconnectload["macaroon"], 'rb').read(), 'hex')
        headers = {'Grpc-Metadata-macaroon': macaroon}
        url = f'https://{lndconnectload["ip_port"]}/v1/getinfo'
        r = requests.get(url, headers=headers, verify=cert_path)
        alias = r.json()
    print("""\t\t
    \033[1;37;40m{}\033[0;37;40m: \033[1;31;40mPyBLOCK\033[0;37;40m
    \033[1;37;40mNode\033[0;37;40m: \033[1;33;40m{}\033[0;37;40m
    \033[1;37;40mBlock\033[0;37;40m: \033[1;32;40m{}\033[0;37;40m
    \033[1;37;40mVersion\033[0;37;40m: {}

    \033[0;37;40mLNPay SN:{} \033[1;34;40mPremium\033[0;37;40m

    \033[1;32;40mA.\033[0;37;40m New Invoice
    \033[1;32;40mB.\033[0;37;40m Pay Invoice
    \033[1;32;40mC.\033[0;37;40m Wallet Balance
    \033[1;32;40mD.\033[0;37;40m List Invoices
    \033[1;32;40mE.\033[0;37;40m Transfer Between Wallets
    \u001b[33;1mEnter.\033[0;37;40m Return
    \n\n\x1b[?25h""".format(n if path['bitcoincli'] else a , alias['alias'], d['blocks'], version, bitLN['NN'], ))
    menuLNPAY(input("\033[1;32;40mSelect option: \033[0;37;40m"))

def APILnPayOnchainONLY():
    bitLN = {"NN":"","pd":""}
    if os.path.isfile('lnpaySN.conf'): # Check if the file 'bclock.conf' is in the same folder
        bitData= json.load(open("lnpaySN.conf", "r")) # Load the file 'bclock.conf'
        bitLN = bitData # Copy the variable pathv to 'path'
    clear()
    blogo()
    sysinfo()
    pathexec()
    #lndconnectexec()
    if path['bitcoincli']:
        n = "Local" if path['bitcoincli'] else "Remote"
        bitcoincli = " getblockchaininfo"
        a = subprocess.run([path['bitcoincli']] + bitcoincli.split(), capture_output=True, text=True).stdout
        b = json.loads(a)
        d = b
    else:
        a = "Local" if path['bitcoincli'] else "Remote"
        blk = rpc('getblockchaininfo')
        d = blk

        cert_path = lndconnectload["tls"]
        macaroon = codecs.encode(open(lndconnectload["macaroon"], 'rb').read(), 'hex')
        headers = {'Grpc-Metadata-macaroon': macaroon}
        url = f'https://{lndconnectload["ip_port"]}/v1/getinfo'
        r = requests.get(url, headers=headers, verify=cert_path)
        alias = r.json()
    print("""\t\t
    \033[1;37;40m{}\033[0;37;40m: \033[1;31;40mPyBLOCK\033[0;37;40m
    \033[1;37;40mBlock\033[0;37;40m: \033[1;32;40m{}\033[0;37;40m
    \033[1;37;40mVersion\033[0;37;40m: {}

    \033[0;37;40mLNPay SN:{} \033[1;34;40mPremium\033[0;37;40m

    \033[1;32;40mA.\033[0;37;40m New Invoice
    \033[1;32;40mB.\033[0;37;40m Pay Invoice
    \033[1;32;40mC.\033[0;37;40m Wallet Balance
    \033[1;32;40mD.\033[0;37;40m List Invoices
    \033[1;32;40mE.\033[0;37;40m Transfer Between Wallets
    \u001b[33;1mEnter.\033[0;37;40m Return
    \n\n\x1b[?25h""".format(n if path['bitcoincli'] else a, d['blocks'], version, bitLN['NN'], ))
    menuLNPAYOnchainONLY(input("\033[1;32;40mSelect option: \033[0;37;40m"))

def APIOpenNode():
    bitLN = {"NN":"","pd":""}
    if os.path.isfile('opennodeSN.conf'): # Check if the file 'bclock.conf' is in the same folder
        bitData= json.load(open("opennodeSN.conf", "r")) # Load the file 'bclock.conf'
        bitLN = bitData # Copy the variable pathv to 'path'
    clear()
    blogo()
    sysinfo()
    pathexec()
    lndconnectexec()
    if path['bitcoincli']:
        n = "Local" if path['bitcoincli'] else "Remote"
        bitcoincli = " getblockchaininfo"
        a = subprocess.run([path['bitcoincli']] + bitcoincli.split(), capture_output=True, text=True).stdout
        b = json.loads(a)
        d = b

        lncli = " getinfo"
        lsd = subprocess.run([lndconnectload['ln']] + lncli.split(), capture_output=True, text=True).stdout
        lsd0 = str(lsd)
        alias = json.loads(lsd0)
    else:
        a = "Local" if path['bitcoincli'] else "Remote"
        blk = rpc('getblockchaininfo')
        d = blk

        cert_path = lndconnectload["tls"]
        macaroon = codecs.encode(open(lndconnectload["macaroon"], 'rb').read(), 'hex')
        headers = {'Grpc-Metadata-macaroon': macaroon}
        url = f'https://{lndconnectload["ip_port"]}/v1/getinfo'
        r = requests.get(url, headers=headers, verify=cert_path)
        alias = r.json()
    print("""\t\t
    \033[1;37;40m{}\033[0;37;40m: \033[1;31;40mPyBLOCK\033[0;37;40m
    \033[1;37;40mNode\033[0;37;40m: \033[1;33;40m{}\033[0;37;40m
    \033[1;37;40mBlock\033[0;37;40m: \033[1;32;40m{}\033[0;37;40m
    \033[1;37;40mVersion\033[0;37;40m: {}

    \033[0;37;40mOpenNode SN:{} \033[1;34;40mPremium\033[0;37;40m

    \033[1;32;40mA.\033[0;37;40m New Invoice
    \033[1;32;40mB.\033[0;37;40m Pay Invoice
    \033[1;32;40mC.\033[0;37;40m Wallet Balance
    \033[1;32;40mD.\033[0;37;40m List Payments
    \033[1;32;40mS.\033[0;37;40m Status
    \u001b[33;1mEnter.\033[0;37;40m Return
    \n\n\x1b[?25h""".format(n if path['bitcoincli'] else a , alias['alias'], d['blocks'], version, bitLN['NN'], ))
    menuOpenNode(input("\033[1;32;40mSelect option: \033[0;37;40m"))

def APIOpenNodeOnchainONLY():
    bitLN = {"NN":"","pd":""}
    if os.path.isfile('opennodeSN.conf'): # Check if the file 'bclock.conf' is in the same folder
        bitData= json.load(open("opennodeSN.conf", "r")) # Load the file 'bclock.conf'
        bitLN = bitData # Copy the variable pathv to 'path'
    clear()
    blogo()
    sysinfo()
    pathexec()
    lndconnectexec()
    if path['bitcoincli']:
        n = "Local" if path['bitcoincli'] else "Remote"
        bitcoincli = " getblockchaininfo"
        a = subprocess.run([path['bitcoincli']] + bitcoincli.split(), capture_output=True, text=True).stdout
        b = json.loads(a)
        d = b
    else:
        a = "Local" if path['bitcoincli'] else "Remote"
        blk = rpc('getblockchaininfo')
        d = blk

        cert_path = lndconnectload["tls"]
        macaroon = codecs.encode(open(lndconnectload["macaroon"], 'rb').read(), 'hex')
        headers = {'Grpc-Metadata-macaroon': macaroon}
        url = f'https://{lndconnectload["ip_port"]}/v1/getinfo'
        r = requests.get(url, headers=headers, verify=cert_path)
        alias = r.json()
    print("""\t\t
    \033[1;37;40m{}\033[0;37;40m: \033[1;31;40mPyBLOCK\033[0;37;40m
    \033[1;37;40mBlock\033[0;37;40m: \033[1;32;40m{}\033[0;37;40m
    \033[1;37;40mVersion\033[0;37;40m: {}

    \033[0;37;40mOpenNode SN:{} \033[1;34;40mPremium\033[0;37;40m

    \033[1;32;40mA.\033[0;37;40m New Invoice
    \033[1;32;40mB.\033[0;37;40m Pay Invoice
    \033[1;32;40mC.\033[0;37;40m Wallet Balance
    \033[1;32;40mD.\033[0;37;40m List Payments
    \033[1;32;40mS.\033[0;37;40m Status
    \u001b[33;1mEnter.\033[0;37;40m Return
    \n\n\x1b[?25h""".format(n if path['bitcoincli'] else a , d['blocks'], version, bitLN['NN'], ()))
    menuOpenNodeOnchainONLY(input("\033[1;32;40mSelect option: \033[0;37;40m"))

def APITippinMe():
    clear()
    blogo()
    sysinfo()
    pathexec()
    lndconnectexec()
    if path['bitcoincli']:
        n = "Local" if path['bitcoincli'] else "Remote"
        bitcoincli = " getblockchaininfo"
        a = subprocess.run([path['bitcoincli']] + bitcoincli.split(), capture_output=True, text=True).stdout
        b = json.loads(a)
        d = b

        lncli = " getinfo"
        lsd = subprocess.run([lndconnectload['ln']] + lncli.split(), capture_output=True, text=True).stdout
        lsd0 = str(lsd)
        alias = json.loads(lsd0)
    else:
        a = "Local" if path['bitcoincli'] else "Remote"
        blk = rpc('getblockchaininfo')
        d = blk

        cert_path = lndconnectload["tls"]
        macaroon = codecs.encode(open(lndconnectload["macaroon"], 'rb').read(), 'hex')
        headers = {'Grpc-Metadata-macaroon': macaroon}
        url = f'https://{lndconnectload["ip_port"]}/v1/getinfo'
        r = requests.get(url, headers=headers, verify=cert_path)
        alias = r.json()
    print("""\t\t
    \033[1;37;40m{}\033[0;37;40m: \033[1;31;40mPyBLOCK\033[0;37;40m
    \033[1;37;40mNode\033[0;37;40m: \033[1;33;40m{}\033[0;37;40m
    \033[1;37;40mBlock\033[0;37;40m: \033[1;32;40m{}\033[0;37;40m
    \033[1;37;40mVersion\033[0;37;40m: {}

    \033[0;37;40mTippinMe

    \033[1;32;40mA.\033[0;37;40m New Invoice
    \u001b[33;1mEnter.\033[0;37;40m Return
    \n\n\x1b[?25h""".format(n if path['bitcoincli'] else a , alias['alias'], d['blocks'], version, ()))
    menuTippinMe(input("\033[1;32;40mSelect option: \033[0;37;40m"))

def APITippinMeOnchainONLY():
    clear()
    blogo()
    sysinfo()
    pathexec()
    #lndconnectexec()
    if path['bitcoincli']:
        n = "Local" if path['bitcoincli'] else "Remote"
        bitcoincli = " getblockchaininfo"
        a = subprocess.run([path['bitcoincli']] + bitcoincli.split(), capture_output=True, text=True).stdout
        b = json.loads(a)
        d = b
    else:
        a = "Local" if path['bitcoincli'] else "Remote"
        blk = rpc('getblockchaininfo')
        d = blk

        cert_path = lndconnectload["tls"]
        macaroon = codecs.encode(open(lndconnectload["macaroon"], 'rb').read(), 'hex')
        headers = {'Grpc-Metadata-macaroon': macaroon}
        url = f'https://{lndconnectload["ip_port"]}/v1/getinfo'
        r = requests.get(url, headers=headers, verify=cert_path)
        alias = r.json()
    print("""\t\t
    \033[1;37;40m{}\033[0;37;40m: \033[1;31;40mPyBLOCK\033[0;37;40m
    \033[1;37;40mBlock\033[0;37;40m: \033[1;32;40m{}\033[0;37;40m
    \033[1;37;40mVersion\033[0;37;40m: {}

    \033[0;37;40mTippinMe

    \033[1;32;40mA.\033[0;37;40m New Invoice
    \u001b[33;1mEnter.\033[0;37;40m Return
    \n\n\x1b[?25h""".format(n if path['bitcoincli'] else a, d['blocks'], version, ()))
    menuTippinMeOnchainONLY(input("\033[1;32;40mSelect option: \033[0;37;40m"))

def APITallyCo():
    clear()
    blogo()
    sysinfo()
    pathexec()
    lndconnectexec()
    if path['bitcoincli']:
        n = "Local" if path['bitcoincli'] else "Remote"
        bitcoincli = " getblockchaininfo"
        a = subprocess.run([path['bitcoincli']] + bitcoincli.split(), capture_output=True, text=True).stdout
        b = json.loads(a)
        d = b

        lncli = " getinfo"
        lsd = subprocess.run([lndconnectload['ln']] + lncli.split(), capture_output=True, text=True).stdout
        lsd0 = str(lsd)
        alias = json.loads(lsd0)
    else:
        a = "Local" if path['bitcoincli'] else "Remote"
        blk = rpc('getblockchaininfo')
        d = blk

        cert_path = lndconnectload["tls"]
        macaroon = codecs.encode(open(lndconnectload["macaroon"], 'rb').read(), 'hex')
        headers = {'Grpc-Metadata-macaroon': macaroon}
        url = f'https://{lndconnectload["ip_port"]}/v1/getinfo'
        r = requests.get(url, headers=headers, verify=cert_path)
        alias = r.json()
    print("""\t\t
    \033[1;37;40m{}\033[0;37;40m: \033[1;31;40mPyBLOCK\033[0;37;40m
    \033[1;37;40mNode\033[0;37;40m: \033[1;33;40m{}\033[0;37;40m
    \033[1;37;40mBlock\033[0;37;40m: \033[1;32;40m{}\033[0;37;40m
    \033[1;37;40mVersion\033[0;37;40m: {}

    \033[0;37;40mTallyCoin

    \033[1;32;40mA.\033[0;37;40m Get Payment
    \033[1;32;40mB.\033[0;37;40m Tip User
    \u001b[33;1mEnter.\033[0;37;40m Return
    \n\n\x1b[?25h""".format(n if path['bitcoincli'] else a , alias['alias'], d['blocks'], version, ()))
    menuTallyCo(input("\033[1;32;40mSelect option: \033[0;37;40m"))

def APITallyCoOnchainONLY():
    clear()
    blogo()
    sysinfo()
    pathexec()
    #lndconnectexec()
    if path['bitcoincli']:
        n = "Local" if path['bitcoincli'] else "Remote"
        bitcoincli = " getblockchaininfo"
        a = subprocess.run([path['bitcoincli']] + bitcoincli.split(), capture_output=True, text=True).stdout
        b = json.loads(a)
        d = b
    else:
        a = "Local" if path['bitcoincli'] else "Remote"
        blk = rpc('getblockchaininfo')
        d = blk

        cert_path = lndconnectload["tls"]
        macaroon = codecs.encode(open(lndconnectload["macaroon"], 'rb').read(), 'hex')
        headers = {'Grpc-Metadata-macaroon': macaroon}
        url = f'https://{lndconnectload["ip_port"]}/v1/getinfo'
        r = requests.get(url, headers=headers, verify=cert_path)
        alias = r.json()
    print("""\t\t
    \033[1;37;40m{}\033[0;37;40m: \033[1;31;40mPyBLOCK\033[0;37;40m
    \033[1;37;40mBlock\033[0;37;40m: \033[1;32;40m{}\033[0;37;40m
    \033[1;37;40mVersion\033[0;37;40m: {}

    \033[0;37;40mTallyCoin

    \033[1;32;40mA.\033[0;37;40m Get Payment
    \033[1;32;40mB.\033[0;37;40m Tip User
    \u001b[33;1mEnter.\033[0;37;40m Return
    \n\n\x1b[?25h""".format(n if path['bitcoincli'] else a , d['blocks'], version, ()))
    menuTallyCoOnchainONLY(input("\033[1;32;40mSelect option: \033[0;37;40m"))
#-------------------------------- SETTINGS -----------------------------------------------


def settings4Local():
    clear()
    blogo()
    sysinfo()
    pathexec()
    lndconnectexec()
    n = "Local" if path['bitcoincli'] else "Remote"
    bitcoincli = " getblockchaininfo"
    a = subprocess.run([path['bitcoincli']] + bitcoincli.split(), capture_output=True, text=True).stdout
    b = json.loads(a)
    d = b

    lncli = " getinfo"
    lsd = subprocess.run([lndconnectload['ln']] + lncli.split(), capture_output=True, text=True).stdout
    lsd0 = str(lsd)
    alias = json.loads(lsd0)

    print("""\t\t
    \033[1;37;40m{}\033[0;37;40m: \033[1;31;40mPyBLOCK\033[0;37;40m
    \033[1;37;40mNode\033[0;37;40m: \033[1;33;40m{}\033[0;37;40m
    \033[1;37;40mBlock\033[0;37;40m: \033[1;32;40m{}\033[0;37;40m
    \033[1;37;40mVersion\033[0;37;40m: {}

    \u001b[38;5;27mA.\033[0;37;40m Change Logo Design
    \u001b[38;5;27mB.\033[0;37;40m Change Logo Colors
    \u001b[38;5;27mC.\033[0;37;40m Change Clock Colors
    \u001b[38;5;27mD.\033[0;37;40m Clock Display Settings
    \u001b[33;1mEnter.\033[0;37;40m Return
    \n\n\x1b[?25h""".format(n, alias['alias'], d['blocks'], version, ()))
    menuSettingsLocal(input("\033[1;32;40mSelect option: \033[0;37;40m"))

def settings4LocalOnchainONLY():
    clear()
    blogo()
    sysinfo()
    pathexec()
    #lndconnectexec()
    n = "Local" if path['bitcoincli'] else "Remote"
    bitcoincli = " getblockchaininfo"
    a = subprocess.run([path['bitcoincli']] + bitcoincli.split(), capture_output=True, text=True).stdout
    b = json.loads(a)
    d = b

    print("""\t\t
    \033[1;37;40m{}\033[0;37;40m: \033[1;31;40mPyBLOCK\033[0;37;40m
    \033[1;37;40mBlock\033[0;37;40m: \033[1;32;40m{}\033[0;37;40m
    \033[1;37;40mVersion\033[0;37;40m: {}

    \u001b[38;5;27mA.\033[0;37;40m Change Logo Design
    \u001b[38;5;27mB.\033[0;37;40m Change Logo Colors
    \u001b[38;5;27mC.\033[0;37;40m Change Clock Colors
    \u001b[38;5;27mD.\033[0;37;40m Clock Display Settings
    \u001b[33;1mEnter.\033[0;37;40m Return
    \n\n\x1b[?25h""".format(n, d['blocks'], version, ()))
    menuSettingsLocalOnchainONLY(input("\033[1;32;40mSelect option: \033[0;37;40m"))

def settings4Remote():
    clear()
    blogo()
    sysinfo()
    pathexec()
    lndconnectexec()
    a = "Local" if path['bitcoincli'] else "Remote"
    blk = rpc('getblockchaininfo')
    d = blk

    cert_path = lndconnectload["tls"]
    macaroon = codecs.encode(open(lndconnectload["macaroon"], 'rb').read(), 'hex')
    headers = {'Grpc-Metadata-macaroon': macaroon}
    url = f'https://{lndconnectload["ip_port"]}/v1/getinfo'
    r = requests.get(url, headers=headers, verify=cert_path)
    alias = r.json()

    print("""\t\t
    \033[1;37;40m{}\033[0;37;40m: \033[1;31;40mPyBLOCK\033[0;37;40m
    \033[1;37;40mNode\033[0;37;40m: \033[1;33;40m{}\033[0;37;40m
    \033[1;37;40mBlock\033[0;37;40m: \033[1;32;40m{}\033[0;37;40m
    \033[1;37;40mVersion\033[0;37;40m: {}

    \u001b[38;5;27mA.\033[0;37;40m Change Logo Design
    \u001b[38;5;27mB.\033[0;37;40m Change Logo Colors
    \u001b[38;5;27mC.\033[0;37;40m Change Clock Colors
    \u001b[38;5;27mD.\033[0;37;40m Clock Display Settings
    \u001b[33;1mEnter.\033[0;37;40m Return
    \n\n\x1b[?25h""".format(a, alias['alias'], d['blocks'], version, ()))
    menuSettingsRemote(input("\033[1;32;40mSelect option: \033[0;37;40m"))

def designQ():
    clear()
    blogo()
    sysinfo()
    pathexec()
    lndconnectexec()
    if path['bitcoincli']:
        n = "Local" if path['bitcoincli'] else "Remote"
        bitcoincli = " getblockchaininfo"
        a = subprocess.run([path['bitcoincli']] + bitcoincli.split(), capture_output=True, text=True).stdout
        b = json.loads(a)
        d = b

        lncli = " getinfo"
        lsd = subprocess.run([lndconnectload['ln']] + lncli.split(), capture_output=True, text=True).stdout
        lsd0 = str(lsd)
        alias = json.loads(lsd0)
    else:
        a = "Local" if path['bitcoincli'] else "Remote"
        blk = rpc('getblockchaininfo')
        d = blk

        cert_path = lndconnectload["tls"]
        macaroon = codecs.encode(open(lndconnectload["macaroon"], 'rb').read(), 'hex')
        headers = {'Grpc-Metadata-macaroon': macaroon}
        url = f'https://{lndconnectload["ip_port"]}/v1/getinfo'
        r = requests.get(url, headers=headers, verify=cert_path)
        alias = r.json()
    print("""\t\t
    \033[1;37;40m{}\033[0;37;40m: \033[1;31;40mPyBLOCK\033[0;37;40m
    \033[1;37;40mNode\033[0;37;40m: \033[1;33;40m{}\033[0;37;40m
    \033[1;37;40mBlock\033[0;37;40m: \033[1;32;40m{}\033[0;37;40m
    \033[1;37;40mVersion\033[0;37;40m: {}

    \033[1;32;40mA.\033[0;37;40m Block
    \033[1;31;40mB.\033[0;37;40m Slick
    \033[1;31;40mC.\033[0;37;40m Tiny
    \033[1;31;40mD.\033[0;37;40m Grid
    \033[1;31;40mE.\033[0;37;40m Pallet
    \033[1;31;40mF.\033[0;37;40m Shade
    \033[1;31;40mG.\033[0;37;40m Chrome
    \033[1;31;40mH.\033[0;37;40m Simple
    \033[1;31;40mI.\033[0;37;40m Simple Block
    \033[1;31;40mJ.\033[0;37;40m 3D
    \033[1;31;40mK.\033[0;37;40m Simple 3D
    \033[1;31;40mL.\033[0;37;40m Huge
    \u001b[33;1mEnter.\033[0;37;40m Return
    \n\n\x1b[?25h""".format(n if path['bitcoincli'] else a , alias['alias'], d['blocks'], version, ()))
    menuDesign(input("\033[1;32;40mSelect option: \033[0;37;40m"))

def designQOnchainONLY():
    clear()
    blogo()
    sysinfo()
    pathexec()
    #lndconnectexec()
    if path['bitcoincli']:
        n = "Local" if path['bitcoincli'] else "Remote"
        bitcoincli = " getblockchaininfo"
        a = subprocess.run([path['bitcoincli']] + bitcoincli.split(), capture_output=True, text=True).stdout
        b = json.loads(a)
        d = b

    else:
        a = "Local" if path['bitcoincli'] else "Remote"
        blk = rpc('getblockchaininfo')
        d = blk

        cert_path = lndconnectload["tls"]
        macaroon = codecs.encode(open(lndconnectload["macaroon"], 'rb').read(), 'hex')
        headers = {'Grpc-Metadata-macaroon': macaroon}
        url = f'https://{lndconnectload["ip_port"]}/v1/getinfo'
        r = requests.get(url, headers=headers, verify=cert_path)
        alias = r.json()
    print("""\t\t
    \033[1;37;40m{}\033[0;37;40m: \033[1;31;40mPyBLOCK\033[0;37;40m
    \033[1;37;40mNode\033[0;37;40m: \033[1;33;40m{}\033[0;37;40m
    \033[1;37;40mBlock\033[0;37;40m: \033[1;32;40m{}\033[0;37;40m
    \033[1;37;40mVersion\033[0;37;40m: {}

    \033[1;32;40mA.\033[0;37;40m Block
    \033[1;31;40mB.\033[0;37;40m Slick
    \033[1;31;40mC.\033[0;37;40m Tiny
    \033[1;31;40mD.\033[0;37;40m Grid
    \033[1;31;40mE.\033[0;37;40m Pallet
    \033[1;31;40mF.\033[0;37;40m Shade
    \033[1;31;40mG.\033[0;37;40m Chrome
    \033[1;31;40mH.\033[0;37;40m Simple
    \033[1;31;40mI.\033[0;37;40m Simple Block
    \033[1;31;40mJ.\033[0;37;40m 3D
    \033[1;31;40mK.\033[0;37;40m Simple 3D
    \033[1;31;40mL.\033[0;37;40m Huge
    \u001b[33;1mEnter.\033[0;37;40m Return
    \n\n\x1b[?25h""".format(n if path['bitcoincli'] else a, d['blocks'], version ))
    menuDesignOnchainONLY(input("\033[1;32;40mSelect option: \033[0;37;40m"))

def designC():
    clear()
    blogo()
    sysinfo()
    pathexec()
    lndconnectexec()
    if path['bitcoincli']:
        n = "Local" if path['bitcoincli'] else "Remote"
        bitcoincli = " getblockchaininfo"
        a = subprocess.run([path['bitcoincli']] + bitcoincli.split(), capture_output=True, text=True).stdout
        b = json.loads(a)
        d = b

        lncli = " getinfo"
        lsd = subprocess.run([lndconnectload['ln']] + lncli.split(), capture_output=True, text=True).stdout
        lsd0 = str(lsd)
        alias = json.loads(lsd0)
    else:
        a = "Local" if path['bitcoincli'] else "Remote"
        blk = rpc('getblockchaininfo')
        d = blk

        cert_path = lndconnectload["tls"]
        macaroon = codecs.encode(open(lndconnectload["macaroon"], 'rb').read(), 'hex')
        headers = {'Grpc-Metadata-macaroon': macaroon}
        url = f'https://{lndconnectload["ip_port"]}/v1/getinfo'
        r = requests.get(url, headers=headers, verify=cert_path)
        alias = r.json()
    print("""\t\t
    \033[1;37;40m{}\033[0;37;40m: \033[1;31;40mPyBLOCK\033[0;37;40m
    \033[1;37;40mNode\033[0;37;40m: \033[1;33;40m{}\033[0;37;40m
    \033[1;37;40mBlock\033[0;37;40m: \033[1;32;40m{}\033[0;37;40m
    \033[1;37;40mVersion\033[0;37;40m: {}

    \033[1;32;40mA.\033[0;37;40m Block
    \033[1;31;40mB.\033[0;37;40m Slick
    \033[1;31;40mC.\033[0;37;40m Tiny
    \033[1;31;40mD.\033[0;37;40m Grid
    \033[1;31;40mE.\033[0;37;40m Pallet
    \033[1;31;40mF.\033[0;37;40m Shade
    \033[1;31;40mG.\033[0;37;40m Chrome
    \033[1;31;40mH.\033[0;37;40m Simple
    \033[1;31;40mI.\033[0;37;40m Simple Block
    \033[1;31;40mJ.\033[0;37;40m 3D
    \033[1;31;40mK.\033[0;37;40m Simple 3D
    \033[1;31;40mL.\033[0;37;40m Huge
    \u001b[33;1mEnter.\033[0;37;40m Return
    \n\n\x1b[?25h""".format(n if path['bitcoincli'] else a , alias['alias'], d['blocks'], version ()))
    menuDesignClock(input("\033[1;32;40mSelect option: \033[0;37;40m"))

def designCOnchainONLY():
    clear()
    blogo()
    sysinfo()
    pathexec()
    #lndconnectexec()
    if path['bitcoincli']:
        n = "Local" if path['bitcoincli'] else "Remote"
        bitcoincli = " getblockchaininfo"
        a = subprocess.run([path['bitcoincli']] + bitcoincli.split(), capture_output=True, text=True).stdout
        b = json.loads(a)
        d = b

    else:
        a = "Local" if path['bitcoincli'] else "Remote"
        blk = rpc('getblockchaininfo')
        d = blk

        cert_path = lndconnectload["tls"]
        macaroon = codecs.encode(open(lndconnectload["macaroon"], 'rb').read(), 'hex')
        headers = {'Grpc-Metadata-macaroon': macaroon}
        url = f'https://{lndconnectload["ip_port"]}/v1/getinfo'
        r = requests.get(url, headers=headers, verify=cert_path)
        alias = r.json()
    print("""\t\t
    \033[1;37;40m{}\033[0;37;40m: \033[1;31;40mPyBLOCK\033[0;37;40m
    \033[1;37;40mNode\033[0;37;40m: \033[1;33;40m{}\033[0;37;40m
    \033[1;37;40mBlock\033[0;37;40m: \033[1;32;40m{}\033[0;37;40m
    \033[1;37;40mVersion\033[0;37;40m: {}

    \033[1;32;40mA.\033[0;37;40m Block
    \033[1;31;40mB.\033[0;37;40m Slick
    \033[1;31;40mC.\033[0;37;40m Tiny
    \033[1;31;40mD.\033[0;37;40m Grid
    \033[1;31;40mE.\033[0;37;40m Pallet
    \033[1;31;40mF.\033[0;37;40m Shade
    \033[1;31;40mG.\033[0;37;40m Chrome
    \033[1;31;40mH.\033[0;37;40m Simple
    \033[1;31;40mI.\033[0;37;40m Simple Block
    \033[1;31;40mJ.\033[0;37;40m 3D
    \033[1;31;40mK.\033[0;37;40m Simple 3D
    \033[1;31;40mL.\033[0;37;40m Huge
    \u001b[33;1mEnter.\033[0;37;40m Return
    \n\n\x1b[?25h""".format(n if path['bitcoincli'] else a, d['blocks'], version ()))
    menuDesignClockOnchainONLY(input("\033[1;32;40mSelect option: \033[0;37;40m"))

def designCRemote():
    clear()
    blogo()
    sysinfo()
    pathexec()
    lndconnectexec()
    if path['bitcoincli']:
        n = "Local" if path['bitcoincli'] else "Remote"
        bitcoincli = " getblockchaininfo"
        a = subprocess.run([path['bitcoincli']] + bitcoincli.split(), capture_output=True, text=True).stdout
        b = json.loads(a)
        d = b

        lncli = " getinfo"
        lsd = subprocess.run([lndconnectload['ln']] + lncli.split(), capture_output=True, text=True).stdout
        lsd0 = str(lsd)
        alias = json.loads(lsd0)
    else:
        a = "Local" if path['bitcoincli'] else "Remote"
        blk = rpc('getblockchaininfo')
        d = blk

        cert_path = lndconnectload["tls"]
        macaroon = codecs.encode(open(lndconnectload["macaroon"], 'rb').read(), 'hex')
        headers = {'Grpc-Metadata-macaroon': macaroon}
        url = f'https://{lndconnectload["ip_port"]}/v1/getinfo'
        r = requests.get(url, headers=headers, verify=cert_path)
        alias = r.json()
    print("""\t\t
    \033[1;37;40m{}\033[0;37;40m: \033[1;31;40mPyBLOCK\033[0;37;40m
    \033[1;37;40mNode\033[0;37;40m: \033[1;33;40m{}\033[0;37;40m
    \033[1;37;40mBlock\033[0;37;40m: \033[1;32;40m{}\033[0;37;40m
    \033[1;37;40mVersion\033[0;37;40m: {}

    \033[1;32;40mA.\033[0;37;40m Block
    \033[1;31;40mB.\033[0;37;40m Slick
    \033[1;31;40mC.\033[0;37;40m Tiny
    \033[1;31;40mD.\033[0;37;40m Grid
    \033[1;31;40mE.\033[0;37;40m Pallet
    \033[1;31;40mF.\033[0;37;40m Shade
    \033[1;31;40mG.\033[0;37;40m Chrome
    \033[1;31;40mH.\033[0;37;40m Simple
    \033[1;31;40mI.\033[0;37;40m Simple Block
    \033[1;31;40mJ.\033[0;37;40m 3D
    \033[1;31;40mK.\033[0;37;40m Simple 3D
    \033[1;31;40mL.\033[0;37;40m Huge
    \u001b[33;1mEnter.\033[0;37;40m Return
    \n\n\x1b[?25h""".format(n if path['bitcoincli'] else a , alias['alias'], d['blocks'], version ()))
    menuDesignClockRemote(input("\033[1;32;40mSelect option: \033[0;37;40m"))

def colors():
    clear()
    blogo()
    sysinfo()
    pathexec()
    lndconnectexec()
    if path['bitcoincli']:
        n = "Local" if path['bitcoincli'] else "Remote"
        bitcoincli = " getblockchaininfo"
        a = subprocess.run([path['bitcoincli']] + bitcoincli.split(), capture_output=True, text=True).stdout
        b = json.loads(a)
        d = b

        lncli = " getinfo"
        lsd = subprocess.run([lndconnectload['ln']] + lncli.split(), capture_output=True, text=True).stdout
        lsd0 = str(lsd)
        alias = json.loads(lsd0)
    else:
        a = "Local" if path['bitcoincli'] else "Remote"
        blk = rpc('getblockchaininfo')
        d = blk

        cert_path = lndconnectload["tls"]
        macaroon = codecs.encode(open(lndconnectload["macaroon"], 'rb').read(), 'hex')
        headers = {'Grpc-Metadata-macaroon': macaroon}
        url = f'https://{lndconnectload["ip_port"]}/v1/getinfo'
        r = requests.get(url, headers=headers, verify=cert_path)
        alias = r.json()
    print("""\t\t
    \033[1;37;40m{}\033[0;37;40m: \033[1;31;40mPyBLOCK\033[0;37;40m
    \033[1;37;40mNode\033[0;37;40m: \033[1;33;40m{}\033[0;37;40m
    \033[1;37;40mBlock\033[0;37;40m: \033[1;32;40m{}\033[0;37;40m
    \033[1;37;40mVersion\033[0;37;40m: {}

    \033[1;32;40mA.\033[0;37;40m Front Color
    \033[1;31;40mB.\033[0;37;40m Back Color
    \033[1;31;40mC.\033[0;37;40m Rainbow
    \u001b[33;1mEnter.\033[0;37;40m Return
    \n\n\x1b[?25h""".format(n if path['bitcoincli'] else a , alias['alias'], d['blocks'], version ()))
    menuColors(input("\033[1;32;40mSelect option: \033[0;37;40m"))

def colorsOnchainONLY():
    clear()
    blogo()
    sysinfo()
    pathexec()
    #lndconnectexec()
    if path['bitcoincli']:
        n = "Local" if path['bitcoincli'] else "Remote"
        bitcoincli = " getblockchaininfo"
        a = subprocess.run([path['bitcoincli']] + bitcoincli.split(), capture_output=True, text=True).stdout
        b = json.loads(a)
        d = b

    else:
        a = "Local" if path['bitcoincli'] else "Remote"
        blk = rpc('getblockchaininfo')
        d = blk

        cert_path = lndconnectload["tls"]
        macaroon = codecs.encode(open(lndconnectload["macaroon"], 'rb').read(), 'hex')
        headers = {'Grpc-Metadata-macaroon': macaroon}
        url = f'https://{lndconnectload["ip_port"]}/v1/getinfo'
        r = requests.get(url, headers=headers, verify=cert_path)
        alias = r.json()
    print("""\t\t
    \033[1;37;40m{}\033[0;37;40m: \033[1;31;40mPyBLOCK\033[0;37;40m
    \033[1;37;40mNode\033[0;37;40m: \033[1;33;40m{}\033[0;37;40m
    \033[1;37;40mBlock\033[0;37;40m: \033[1;32;40m{}\033[0;37;40m
    \033[1;37;40mVersion\033[0;37;40m: {}

    \033[1;32;40mA.\033[0;37;40m Front Color
    \033[1;31;40mB.\033[0;37;40m Back Color
    \033[1;31;40mC.\033[0;37;40m Rainbow
    \u001b[33;1mEnter.\033[0;37;40m Return
    \n\n\x1b[?25h""".format(n if path['bitcoincli'] else a, d['blocks'], version ()))
    menuColorsOnchainONLY(input("\033[1;32;40mSelect option: \033[0;37;40m"))

def colorsC():
    clear()
    blogo()
    sysinfo()
    pathexec()
    lndconnectexec()
    if path['bitcoincli']:
        n = "Local" if path['bitcoincli'] else "Remote"
        bitcoincli = " getblockchaininfo"
        a = subprocess.run([path['bitcoincli']] + bitcoincli.split(), capture_output=True, text=True).stdout
        b = json.loads(a)
        d = b

        lncli = " getinfo"
        lsd = subprocess.run([lndconnectload['ln']] + lncli.split(), capture_output=True, text=True).stdout
        lsd0 = str(lsd)
        alias = json.loads(lsd0)
    else:
        a = "Local" if path['bitcoincli'] else "Remote"
        blk = rpc('getblockchaininfo')
        d = blk

        cert_path = lndconnectload["tls"]
        macaroon = codecs.encode(open(lndconnectload["macaroon"], 'rb').read(), 'hex')
        headers = {'Grpc-Metadata-macaroon': macaroon}
        url = f'https://{lndconnectload["ip_port"]}/v1/getinfo'
        r = requests.get(url, headers=headers, verify=cert_path)
        alias = r.json()
    print("""\t\t
    \033[1;37;40m{}\033[0;37;40m: \033[1;31;40mPyBLOCK\033[0;37;40m
    \033[1;37;40mNode\033[0;37;40m: \033[1;33;40m{}\033[0;37;40m
    \033[1;37;40mBlock\033[0;37;40m: \033[1;32;40m{}\033[0;37;40m
    \033[1;37;40mVersion\033[0;37;40m: {}

    \033[1;32;40mA.\033[0;37;40m Front Color
    \033[1;31;40mB.\033[0;37;40m Back Color
    \u001b[33;1mEnter.\033[0;37;40m Return
    \n\n\x1b[?25h""".format(n if path['bitcoincli'] else a , alias['alias'], d['blocks'], version ()))
    menuColorsClock(input("\033[1;32;40mSelect option: \033[0;37;40m"))

def colorsCOnchainONLY():
    clear()
    blogo()
    sysinfo()
    pathexec()
    #lndconnectexec()
    if path['bitcoincli']:
        n = "Local" if path['bitcoincli'] else "Remote"
        bitcoincli = " getblockchaininfo"
        a = subprocess.run([path['bitcoincli']] + bitcoincli.split(), capture_output=True, text=True).stdout
        b = json.loads(a)
        d = b
    else:
        a = "Local" if path['bitcoincli'] else "Remote"
        blk = rpc('getblockchaininfo')
        d = blk

        cert_path = lndconnectload["tls"]
        macaroon = codecs.encode(open(lndconnectload["macaroon"], 'rb').read(), 'hex')
        headers = {'Grpc-Metadata-macaroon': macaroon}
        url = f'https://{lndconnectload["ip_port"]}/v1/getinfo'
        r = requests.get(url, headers=headers, verify=cert_path)
        alias = r.json()
    print("""\t\t
    \033[1;37;40m{}\033[0;37;40m: \033[1;31;40mPyBLOCK\033[0;37;40m
    \033[1;37;40mNode\033[0;37;40m: \033[1;33;40m{}\033[0;37;40m
    \033[1;37;40mBlock\033[0;37;40m: \033[1;32;40m{}\033[0;37;40m
    \033[1;37;40mVersion\033[0;37;40m: {}

    \033[1;32;40mA.\033[0;37;40m Front Color
    \033[1;31;40mB.\033[0;37;40m Back Color
    \u001b[33;1mEnter.\033[0;37;40m Return
    \n\n\x1b[?25h""".format(n if path['bitcoincli'] else a, d['blocks'], version ()))
    menuColorsClockOnchainONLY(input("\033[1;32;40mSelect option: \033[0;37;40m"))

def colorsCRemote():
    clear()
    blogo()
    sysinfo()
    pathexec()
    lndconnectexec()
    if path['bitcoincli']:
        n = "Local" if path['bitcoincli'] else "Remote"
        bitcoincli = " getblockchaininfo"
        a = subprocess.run([path['bitcoincli']] + bitcoincli.split(), capture_output=True, text=True).stdout
        b = json.loads(a)
        d = b

        lncli = " getinfo"
        lsd = subprocess.run([lndconnectload['ln']] + lncli.split(), capture_output=True, text=True).stdout
        lsd0 = str(lsd)
        alias = json.loads(lsd0)
    else:
        a = "Local" if path['bitcoincli'] else "Remote"
        blk = rpc('getblockchaininfo')
        d = blk

        cert_path = lndconnectload["tls"]
        macaroon = codecs.encode(open(lndconnectload["macaroon"], 'rb').read(), 'hex')
        headers = {'Grpc-Metadata-macaroon': macaroon}
        url = f'https://{lndconnectload["ip_port"]}/v1/getinfo'
        r = requests.get(url, headers=headers, verify=cert_path)
        alias = r.json()
    print("""\t\t
    \033[1;37;40m{}\033[0;37;40m: \033[1;31;40mPyBLOCK\033[0;37;40m
    \033[1;37;40mNode\033[0;37;40m: \033[1;33;40m{}\033[0;37;40m
    \033[1;37;40mBlock\033[0;37;40m: \033[1;32;40m{}\033[0;37;40m
    \033[1;37;40mVersion\033[0;37;40m: {}

    \033[1;32;40mA.\033[0;37;40m Front Color
    \033[1;31;40mB.\033[0;37;40m Back Color
    \u001b[33;1mEnter.\033[0;37;40m Return
    \n\n\x1b[?25h""".format(n if path['bitcoincli'] else a , alias['alias'], d['blocks'], version ()))
    menuColorsClockRemote(input("\033[1;32;40mSelect option: \033[0;37;40m"))

def colorsSelectFront():
    clear()
    blogo()
    sysinfo()
    pathexec()
    lndconnectexec()
    if path['bitcoincli']:
        n = "Local" if path['bitcoincli'] else "Remote"
        bitcoincli = " getblockchaininfo"
        a = subprocess.run([path['bitcoincli']] + bitcoincli.split(), capture_output=True, text=True).stdout
        b = json.loads(a)
        d = b

        lncli = " getinfo"
        lsd = subprocess.run([lndconnectload['ln']] + lncli.split(), capture_output=True, text=True).stdout
        lsd0 = str(lsd)
        alias = json.loads(lsd0)
    else:
        a = "Local" if path['bitcoincli'] else "Remote"
        blk = rpc('getblockchaininfo')
        d = blk

        cert_path = lndconnectload["tls"]
        macaroon = codecs.encode(open(lndconnectload["macaroon"], 'rb').read(), 'hex')
        headers = {'Grpc-Metadata-macaroon': macaroon}
        url = f'https://{lndconnectload["ip_port"]}/v1/getinfo'
        r = requests.get(url, headers=headers, verify=cert_path)
        alias = r.json()
    print("""\t\t
    \033[1;37;40m{}\033[0;37;40m: \033[1;31;40mPyBLOCK\033[0;37;40m
    \033[1;37;40mNode\033[0;37;40m: \033[1;33;40m{}\033[0;37;40m
    \033[1;37;40mBlock\033[0;37;40m: \033[1;32;40m{}\033[0;37;40m
    \033[1;37;40mVersion\033[0;37;40m: {}

    \033[1;32;40mA.\033[0;37;40m Black
    \033[1;31;40mB.\033[0;37;40m Red
    \033[1;31;40mC.\033[0;37;40m Green
    \033[1;31;40mD.\033[0;37;40m Yellow
    \033[1;31;40mE.\033[0;37;40m Blue
    \033[1;31;40mF.\033[0;37;40m Magenta
    \033[1;31;40mG.\033[0;37;40m Cyan
    \033[1;31;40mH.\033[0;37;40m White
    \033[1;31;40mI.\033[0;37;40m Gray
    \u001b[33;1mEnter.\033[0;37;40m Return
    \n\n\x1b[?25h""".format(n if path['bitcoincli'] else a , alias['alias'], d['blocks'], version ()))
    menuColorsSelectFront(input("\033[1;32;40mSelect option: \033[0;37;40m"))

def colorsSelectFrontOnchainONLY():
    clear()
    blogo()
    sysinfo()
    pathexec()
    #lndconnectexec()
    if path['bitcoincli']:
        n = "Local" if path['bitcoincli'] else "Remote"
        bitcoincli = " getblockchaininfo"
        a = subprocess.run([path['bitcoincli']] + bitcoincli.split(), capture_output=True, text=True).stdout
        b = json.loads(a)
        d = b

    else:
        a = "Local" if path['bitcoincli'] else "Remote"
        blk = rpc('getblockchaininfo')
        d = blk

        cert_path = lndconnectload["tls"]
        macaroon = codecs.encode(open(lndconnectload["macaroon"], 'rb').read(), 'hex')
        headers = {'Grpc-Metadata-macaroon': macaroon}
        url = f'https://{lndconnectload["ip_port"]}/v1/getinfo'
        r = requests.get(url, headers=headers, verify=cert_path)
        alias = r.json()
    print("""\t\t
    \033[1;37;40m{}\033[0;37;40m: \033[1;31;40mPyBLOCK\033[0;37;40m
    \033[1;37;40mNode\033[0;37;40m: \033[1;33;40m{}\033[0;37;40m
    \033[1;37;40mBlock\033[0;37;40m: \033[1;32;40m{}\033[0;37;40m
    \033[1;37;40mVersion\033[0;37;40m: {}

    \033[1;32;40mA.\033[0;37;40m Black
    \033[1;31;40mB.\033[0;37;40m Red
    \033[1;31;40mC.\033[0;37;40m Green
    \033[1;31;40mD.\033[0;37;40m Yellow
    \033[1;31;40mE.\033[0;37;40m Blue
    \033[1;31;40mF.\033[0;37;40m Magenta
    \033[1;31;40mG.\033[0;37;40m Cyan
    \033[1;31;40mH.\033[0;37;40m White
    \033[1;31;40mI.\033[0;37;40m Gray
    \u001b[33;1mEnter.\033[0;37;40m Return
    \n\n\x1b[?25h""".format(n if path['bitcoincli'] else a ,d['blocks'], version ()))
    menuColorsSelectFrontOncainONLY(input("\033[1;32;40mSelect option: \033[0;37;40m"))

def colorsSelectFrontClock():
    clear()
    blogo()
    sysinfo()
    pathexec()
    lndconnectexec()
    if path['bitcoincli']:
        n = "Local" if path['bitcoincli'] else "Remote"
        bitcoincli = " getblockchaininfo"
        a = subprocess.run([path['bitcoincli']] + bitcoincli.split(), capture_output=True, text=True).stdout
        b = json.loads(a)
        d = b

        lncli = " getinfo"
        lsd = subprocess.run([lndconnectload['ln']] + lncli.split(), capture_output=True, text=True).stdout
        lsd0 = str(lsd)
        alias = json.loads(lsd0)
    else:
        a = "Local" if path['bitcoincli'] else "Remote"
        blk = rpc('getblockchaininfo')
        d = blk

        cert_path = lndconnectload["tls"]
        macaroon = codecs.encode(open(lndconnectload["macaroon"], 'rb').read(), 'hex')
        headers = {'Grpc-Metadata-macaroon': macaroon}
        url = f'https://{lndconnectload["ip_port"]}/v1/getinfo'
        r = requests.get(url, headers=headers, verify=cert_path)
        alias = r.json()
    print("""\t\t
    \033[1;37;40m{}\033[0;37;40m: \033[1;31;40mPyBLOCK\033[0;37;40m
    \033[1;37;40mNode\033[0;37;40m: \033[1;33;40m{}\033[0;37;40m
    \033[1;37;40mBlock\033[0;37;40m: \033[1;32;40m{}\033[0;37;40m
    \033[1;37;40mVersion\033[0;37;40m: {}

    \033[1;32;40mA.\033[0;37;40m Black
    \033[1;31;40mB.\033[0;37;40m Red
    \033[1;31;40mC.\033[0;37;40m Green
    \033[1;31;40mD.\033[0;37;40m Yellow
    \033[1;31;40mE.\033[0;37;40m Blue
    \033[1;31;40mF.\033[0;37;40m Magenta
    \033[1;31;40mG.\033[0;37;40m Cyan
    \033[1;31;40mH.\033[0;37;40m White
    \033[1;31;40mI.\033[0;37;40m Gray
    \u001b[33;1mEnter.\033[0;37;40m Return
    \n\n\x1b[?25h""".format(n if path['bitcoincli'] else a , alias['alias'], d['blocks'], version ()))
    menuColorsSelectFrontClock(input("\033[1;32;40mSelect option: \033[0;37;40m"))

def colorsSelectFrontClockOnchainONLY():
    clear()
    blogo()
    sysinfo()
    pathexec()
    #lndconnectexec()
    if path['bitcoincli']:
        n = "Local" if path['bitcoincli'] else "Remote"
        bitcoincli = " getblockchaininfo"
        a = subprocess.run([path['bitcoincli']] + bitcoincli.split(), capture_output=True, text=True).stdout
        b = json.loads(a)
        d = b

    else:
        a = "Local" if path['bitcoincli'] else "Remote"
        blk = rpc('getblockchaininfo')
        d = blk

        cert_path = lndconnectload["tls"]
        macaroon = codecs.encode(open(lndconnectload["macaroon"], 'rb').read(), 'hex')
        headers = {'Grpc-Metadata-macaroon': macaroon}
        url = f'https://{lndconnectload["ip_port"]}/v1/getinfo'
        r = requests.get(url, headers=headers, verify=cert_path)
        alias = r.json()
    print("""\t\t
    \033[1;37;40m{}\033[0;37;40m: \033[1;31;40mPyBLOCK\033[0;37;40m
    \033[1;37;40mNode\033[0;37;40m: \033[1;33;40m{}\033[0;37;40m
    \033[1;37;40mBlock\033[0;37;40m: \033[1;32;40m{}\033[0;37;40m
    \033[1;37;40mVersion\033[0;37;40m: {}

    \033[1;32;40mA.\033[0;37;40m Black
    \033[1;31;40mB.\033[0;37;40m Red
    \033[1;31;40mC.\033[0;37;40m Green
    \033[1;31;40mD.\033[0;37;40m Yellow
    \033[1;31;40mE.\033[0;37;40m Blue
    \033[1;31;40mF.\033[0;37;40m Magenta
    \033[1;31;40mG.\033[0;37;40m Cyan
    \033[1;31;40mH.\033[0;37;40m White
    \033[1;31;40mI.\033[0;37;40m Gray
    \u001b[33;1mEnter.\033[0;37;40m Return
    \n\n\x1b[?25h""".format(n if path['bitcoincli'] else a , d['blocks'], version ()))
    menuColorsSelectFrontClockOnchainONLY(input("\033[1;32;40mSelect option: \033[0;37;40m"))

def colorsSelectFrontClockRemote():
    clear()
    blogo()
    sysinfo()
    pathexec()
    lndconnectexec()
    if path['bitcoincli']:
        n = "Local" if path['bitcoincli'] else "Remote"
        bitcoincli = " getblockchaininfo"
        a = subprocess.run([path['bitcoincli']] + bitcoincli.split(), capture_output=True, text=True).stdout
        b = json.loads(a)
        d = b

        lncli = " getinfo"
        lsd = subprocess.run([lndconnectload['ln']] + lncli.split(), capture_output=True, text=True).stdout
        lsd0 = str(lsd)
        alias = json.loads(lsd0)
    else:
        a = "Local" if path['bitcoincli'] else "Remote"
        blk = rpc('getblockchaininfo')
        d = blk

        cert_path = lndconnectload["tls"]
        macaroon = codecs.encode(open(lndconnectload["macaroon"], 'rb').read(), 'hex')
        headers = {'Grpc-Metadata-macaroon': macaroon}
        url = f'https://{lndconnectload["ip_port"]}/v1/getinfo'
        r = requests.get(url, headers=headers, verify=cert_path)
        alias = r.json()
    print("""\t\t
    \033[1;37;40m{}\033[0;37;40m: \033[1;31;40mPyBLOCK\033[0;37;40m
    \033[1;37;40mNode\033[0;37;40m: \033[1;33;40m{}\033[0;37;40m
    \033[1;37;40mBlock\033[0;37;40m: \033[1;32;40m{}\033[0;37;40m
    \033[1;37;40mVersion\033[0;37;40m: {}

    \033[1;32;40mA.\033[0;37;40m Black
    \033[1;31;40mB.\033[0;37;40m Red
    \033[1;31;40mC.\033[0;37;40m Green
    \033[1;31;40mD.\033[0;37;40m Yellow
    \033[1;31;40mE.\033[0;37;40m Blue
    \033[1;31;40mF.\033[0;37;40m Magenta
    \033[1;31;40mG.\033[0;37;40m Cyan
    \033[1;31;40mH.\033[0;37;40m White
    \033[1;31;40mI.\033[0;37;40m Gray
    \u001b[33;1mEnter.\033[0;37;40m Return
    \n\n\x1b[?25h""".format(n if path['bitcoincli'] else a , alias['alias'], d['blocks'], version ()))
    menuColorsSelectFrontClockRemote(input("\033[1;32;40mSelect option: \033[0;37;40m"))

def colorsSelectBack():
    clear()
    blogo()
    sysinfo()
    pathexec()
    lndconnectexec()
    if path['bitcoincli']:
        n = "Local" if path['bitcoincli'] else "Remote"
        bitcoincli = " getblockchaininfo"
        a = subprocess.run([path['bitcoincli']] + bitcoincli.split(), capture_output=True, text=True).stdout
        b = json.loads(a)
        d = b

        lncli = " getinfo"
        lsd = subprocess.run([lndconnectload['ln']] + lncli.split(), capture_output=True, text=True).stdout
        lsd0 = str(lsd)
        alias = json.loads(lsd0)
    else:
        a = "Local" if path['bitcoincli'] else "Remote"
        blk = rpc('getblockchaininfo')
        d = blk

        cert_path = lndconnectload["tls"]
        macaroon = codecs.encode(open(lndconnectload["macaroon"], 'rb').read(), 'hex')
        headers = {'Grpc-Metadata-macaroon': macaroon}
        url = f'https://{lndconnectload["ip_port"]}/v1/getinfo'
        r = requests.get(url, headers=headers, verify=cert_path)
        alias = r.json()
    print("""\t\t
    \033[1;37;40m{}\033[0;37;40m: \033[1;31;40mPyBLOCK\033[0;37;40m
    \033[1;37;40mNode\033[0;37;40m: \033[1;33;40m{}\033[0;37;40m
    \033[1;37;40mBlock\033[0;37;40m: \033[1;32;40m{}\033[0;37;40m
    \033[1;37;40mVersion\033[0;37;40m: {}

    \033[1;32;40mA.\033[0;37;40m Black
    \033[1;31;40mB.\033[0;37;40m Red
    \033[1;31;40mC.\033[0;37;40m Green
    \033[1;31;40mD.\033[0;37;40m Yellow
    \033[1;31;40mE.\033[0;37;40m Blue
    \033[1;31;40mF.\033[0;37;40m Magenta
    \033[1;31;40mG.\033[0;37;40m Cyan
    \033[1;31;40mH.\033[0;37;40m White
    \033[1;31;40mI.\033[0;37;40m Gray
    \u001b[33;1mEnter.\033[0;37;40m Return
    \n\n\x1b[?25h""".format(n if path['bitcoincli'] else a , alias['alias'], d['blocks'], version ()))
    menuColorsSelectBack(input("\033[1;32;40mSelect option: \033[0;37;40m"))

def colorsSelectBackOnchainONLY():
    clear()
    blogo()
    sysinfo()
    pathexec()
    #lndconnectexec()
    if path['bitcoincli']:
        n = "Local" if path['bitcoincli'] else "RemotcolorsCe"
        bitcoincli = " getblockchaininfo"
        a = subprocess.run([path['bitcoincli']] + bitcoincli.split(), capture_output=True, text=True).stdout
        b = json.loads(a)
        d = b

    else:
        a = "Local" if path['bitcoincli'] else "Remote"
        blk = rpc('getblockchaininfo')
        d = blk

        cert_path = lndconnectload["tls"]
        macaroon = codecs.encode(open(lndconnectload["macaroon"], 'rb').read(), 'hex')
        headers = {'Grpc-Metadata-macaroon': macaroon}
        url = f'https://{lndconnectload["ip_port"]}/v1/getinfo'
        r = requests.get(url, headers=headers, verify=cert_path)
        alias = r.json()
    print("""\t\t
    \033[1;37;40m{}\033[0;37;40m: \033[1;31;40mPyBLOCK\033[0;37;40m
    \033[1;37;40mNode\033[0;37;40m: \033[1;33;40m{}\033[0;37;40m
    \033[1;37;40mBlock\033[0;37;40m: \033[1;32;40m{}\033[0;37;40m
    \033[1;37;40mVersion\033[0;37;40m: {}

    \033[1;32;40mA.\033[0;37;40m Black
    \033[1;31;40mB.\033[0;37;40m Red
    \033[1;31;40mC.\033[0;37;40m Green
    \033[1;31;40mD.\033[0;37;40m Yellow
    \033[1;31;40mE.\033[0;37;40m Blue
    \033[1;31;40mF.\033[0;37;40m Magenta
    \033[1;31;40mG.\033[0;37;40m Cyan
    \033[1;31;40mH.\033[0;37;40m White
    \033[1;31;40mI.\033[0;37;40m Gray
    \u001b[33;1mEnter.\033[0;37;40m Return
    \n\n\x1b[?25h""".format(n if path['bitcoincli'] else a, d['blocks'], version ()))
    menuColorsSelectBackOnchainONLY(input("\033[1;32;40mSelect option: \033[0;37;40m"))

def colorsSelectBackClock():
    clear()
    blogo()
    sysinfo()
    pathexec()
    lndconnectexec()
    if path['bitcoincli']:
        n = "Local" if path['bitcoincli'] else "Remote"
        bitcoincli = " getblockchaininfo"
        a = subprocess.run([path['bitcoincli']] + bitcoincli.split(), capture_output=True, text=True).stdout
        b = json.loads(a)
        d = b
        lncli = " getinfo"
        lsd = subprocess.run([lndconnectload['ln']] + lncli.split(), capture_output=True, text=True).stdout
        lsd0 = str(lsd)
        alias = json.loads(lsd0)

        lncli = " getinfo"
        lsd = subprocess.run([lndconnectload['ln']] + lncli.split(), capture_output=True, text=True).stdout
        lsd0 = str(lsd)
        alias = json.loads(lsd0)
    else:
        a = "Local" if path['bitcoincli'] else "Remote"
        blk = rpc('getblockchaininfo')
        d = blk

        cert_path = lndconnectload["tls"]
        macaroon = codecs.encode(open(lndconnectload["macaroon"], 'rb').read(), 'hex')
        headers = {'Grpc-Metadata-macaroon': macaroon}
        url = f'https://{lndconnectload["ip_port"]}/v1/getinfo'
        r = requests.get(url, headers=headers, verify=cert_path)
        alias = r.json()
    print("""\t\t
    \033[1;37;40m{}\033[0;37;40m: \033[1;31;40mPyBLOCK\033[0;37;40m
    \033[1;37;40mNode\033[0;37;40m: \033[1;33;40m{}\033[0;37;40m
    \033[1;37;40mBlock\033[0;37;40m: \033[1;32;40m{}\033[0;37;40m
    \033[1;37;40mVersion\033[0;37;40m: {}

    \033[1;32;40mA.\033[0;37;40m Black
    \033[1;31;40mB.\033[0;37;40m Red
    \033[1;31;40mC.\033[0;37;40m Green
    \033[1;31;40mD.\033[0;37;40m Yellow
    \033[1;31;40mE.\033[0;37;40m Blue
    \033[1;31;40mF.\033[0;37;40m Magenta
    \033[1;31;40mG.\033[0;37;40m Cyan
    \033[1;31;40mH.\033[0;37;40m White
    \033[1;31;40mI.\033[0;37;40m Gray
    \u001b[33;1mEnter.\033[0;37;40m Return
    \n\n\x1b[?25h""".format(n if path['bitcoincli'] else a , alias['alias'], d['blocks'], version ()))
    menuColorsSelectBackClock(input("\033[1;32;40mSelect option: \033[0;37;40m"))

def colorsSelectBackClockOnchainONLY():
    clear()
    blogo()
    sysinfo()
    pathexec()
    #lndconnectexec()
    if path['bitcoincli']:
        n = "Local" if path['bitcoincli'] else "Remote"
        bitcoincli = " getblockchaininfo"
        a = subprocess.run([path['bitcoincli']] + bitcoincli.split(), capture_output=True, text=True).stdout
        b = json.loads(a)
        d = b

    else:
        a = "Local" if path['bitcoincli'] else "Remote"
        blk = rpc('getblockchaininfo')
        d = blk

        cert_path = lndconnectload["tls"]
        macaroon = codecs.encode(open(lndconnectload["macaroon"], 'rb').read(), 'hex')
        headers = {'Grpc-Metadata-macaroon': macaroon}
        url = f'https://{lndconnectload["ip_port"]}/v1/getinfo'
        r = requests.get(url, headers=headers, verify=cert_path)
        alias = r.json()
    print("""\t\t
    \033[1;37;40m{}\033[0;37;40m: \033[1;31;40mPyBLOCK\033[0;37;40m
    \033[1;37;40mNode\033[0;37;40m: \033[1;33;40m{}\033[0;37;40m
    \033[1;37;40mBlock\033[0;37;40m: \033[1;32;40m{}\033[0;37;40m
    \033[1;37;40mVersion\033[0;37;40m: {}

    \033[1;32;40mA.\033[0;37;40m Black
    \033[1;31;40mB.\033[0;37;40m Red
    \033[1;31;40mC.\033[0;37;40m Green
    \033[1;31;40mD.\033[0;37;40m Yellow
    \033[1;31;40mE.\033[0;37;40m Blue
    \033[1;31;40mF.\033[0;37;40m Magenta
    \033[1;31;40mG.\033[0;37;40m Cyan
    \033[1;31;40mH.\033[0;37;40m White
    \033[1;31;40mI.\033[0;37;40m Gray
    \u001b[33;1mEnter.\033[0;37;40m Return
    \n\n\x1b[?25h""".format(n if path['bitcoincli'] else a , d['blocks'], version ()))
    menuColorsSelectBackClockOnchainONLY(input("\033[1;32;40mSelect option: \033[0;37;40m"))

def colorsSelectBackClockRemote():
    clear()
    blogo()
    sysinfo()
    pathexec()
    lndconnectexec()
    if path['bitcoincli']:
        n = "Local" if path['bitcoincli'] else "Remote"
        bitcoincli = " getblockchaininfo"
        a = subprocess.run([path['bitcoincli']] + bitcoincli.split(), capture_output=True, text=True).stdout
        b = json.loads(a)
        d = b

        lncli = " getinfo"
        lsd = subprocess.run([lndconnectload['ln']] + lncli.split(), capture_output=True, text=True).stdout
        lsd0 = str(lsd)
        alias = json.loads(lsd0)
    else:
        a = "Local" if path['bitcoincli'] else "Remote"
        blk = rpc('getblockchaininfo')
        d = blk

        cert_path = lndconnectload["tls"]
        macaroon = codecs.encode(open(lndconnectload["macaroon"], 'rb').read(), 'hex')
        headers = {'Grpc-Metadata-macaroon': macaroon}
        url = f'https://{lndconnectload["ip_port"]}/v1/getinfo'
        r = requests.get(url, headers=headers, verify=cert_path)
        alias = r.json()
    print("""\t\t
    \033[1;37;40m{}\033[0;37;40m: \033[1;31;40mPyBLOCK\033[0;37;40m
    \033[1;37;40mNode\033[0;37;40m: \033[1;33;40m{}\033[0;37;40m
    \033[1;37;40mBlock\033[0;37;40m: \033[1;32;40m{}\033[0;37;40m
    \033[1;37;40mVersion\033[0;37;40m: {}

    \033[1;32;40mA.\033[0;37;40m Black
    \033[1;31;40mB.\033[0;37;40m Red
    \033[1;31;40mC.\033[0;37;40m Green
    \033[1;31;40mD.\033[0;37;40m Yellow
    \033[1;31;40mE.\033[0;37;40m Blue
    \033[1;31;40mF.\033[0;37;40m Magenta
    \033[1;31;40mG.\033[0;37;40m Cyan
    \033[1;31;40mH.\033[0;37;40m White
    \033[1;31;40mI.\033[0;37;40m Gray
    \u001b[33;1mEnter.\033[0;37;40m Return
    \n\n\x1b[?25h""".format(n if path['bitcoincli'] else a , alias['alias'], d['blocks'], version ()))
    menuColorsSelectBackClockRemote(input("\033[1;32;40mSelect option: \033[0;37;40m"))

def colorsSelectRainbow():
    clear()
    blogo()
    sysinfo()
    pathexec()
    lndconnectexec()
    if path['bitcoincli']:
        n = "Local" if path['bitcoincli'] else "Remote"
        bitcoincli = " getblockchaininfo"
        a = subprocess.run([path['bitcoincli']] + bitcoincli.split(), capture_output=True, text=True).stdout
        b = json.loads(a)
        d = b

        lncli = " getinfo"
        lsd = subprocess.run([lndconnectload['ln']] + lncli.split(), capture_output=True, text=True).stdout
        lsd0 = str(lsd)
        alias = json.loads(lsd0)
    else:
        a = "Local" if path['bitcoincli'] else "Remote"
        blk = rpc('getblockchaininfo')
        d = blk

        cert_path = lndconnectload["tls"]
        macaroon = codecs.encode(open(lndconnectload["macaroon"], 'rb').read(), 'hex')
        headers = {'Grpc-Metadata-macaroon': macaroon}
        url = f'https://{lndconnectload["ip_port"]}/v1/getinfo'
        r = requests.get(url, headers=headers, verify=cert_path)
        alias = r.json()
    print("""\t\t
    \033[1;37;40m{}\033[0;37;40m: \033[1;31;40mPyBLOCK\033[0;37;40m
    \033[1;37;40mNode\033[0;37;40m: \033[1;33;40m{}\033[0;37;40m
    \033[1;37;40mBlock\033[0;37;40m: \033[1;32;40m{}\033[0;37;40m
    \033[1;37;40mVersion\033[0;37;40m: {}

    \033[1;32;40mA.\033[0;37;40m Start Color
    \033[1;31;40mB.\033[0;37;40m End Color
    \u001b[33;1mEnter.\033[0;37;40m Return
    \n\n\x1b[?25h""".format(n if path['bitcoincli'] else a , alias['alias'], d['blocks'], version ()))
    menuColorsSelectRainbow(input("\033[1;32;40mSelect option: \033[0;37;40m"))

def colorsSelectRainbowOnchainONLY():
    clear()
    blogo()
    sysinfo()
    pathexec()
    #lndconnectexec()
    if path['bitcoincli']:
        n = "Local" if path['bitcoincli'] else "Remote"
        bitcoincli = " getblockchaininfo"
        a = subprocess.run([path['bitcoincli']] + bitcoincli.split(), capture_output=True, text=True).stdout
        b = json.loads(a)
        d = b

    else:
        a = "Local" if path['bitcoincli'] else "Remote"
        blk = rpc('getblockchaininfo')
        d = blk

        cert_path = lndconnectload["tls"]
        macaroon = codecs.encode(open(lndconnectload["macaroon"], 'rb').read(), 'hex')
        headers = {'Grpc-Metadata-macaroon': macaroon}
        url = f'https://{lndconnectload["ip_port"]}/v1/getinfo'
        r = requests.get(url, headers=headers, verify=cert_path)
        alias = r.json()
    print("""\t\t
    \033[1;37;40m{}\033[0;37;40m: \033[1;31;40mPyBLOCK\033[0;37;40m
    \033[1;37;40mNode\033[0;37;40m: \033[1;33;40m{}\033[0;37;40m
    \033[1;37;40mBlock\033[0;37;40m: \033[1;32;40m{}\033[0;37;40m
    \033[1;37;40mVersion\033[0;37;40m: {}

    \033[1;32;40mA.\033[0;37;40m Start Color
    \033[1;31;40mB.\033[0;37;40m End Color
    \u001b[33;1mEnter.\033[0;37;40m Return
    \n\n\x1b[?25h""".format(n if path['bitcoincli'] else a , d['blocks'], version ()))
    menuColorsSelectRainbowOnchainONLY(input("\033[1;32;40mSelect option: \033[0;37;40m"))

def colorsSelectRainbowStart():
    clear()
    blogo()
    sysinfo()
    pathexec()
    lndconnectexec()
    if path['bitcoincli']:
        n = "Local" if path['bitcoincli'] else "Remote"
        bitcoincli = " getblockchaininfo"
        a = subprocess.run([path['bitcoincli']] + bitcoincli.split(), capture_output=True, text=True).stdout
        b = json.loads(a)
        d = b

        lncli = " getinfo"
        lsd = subprocess.run([lndconnectload['ln']] + lncli.split(), capture_output=True, text=True).stdout
        lsd0 = str(lsd)
        alias = json.loads(lsd0)
    else:
        a = "Local" if path['bitcoincli'] else "Remote"
        blk = rpc('getblockchaininfo')
        d = blk

        cert_path = lndconnectload["tls"]
        macaroon = codecs.encode(open(lndconnectload["macaroon"], 'rb').read(), 'hex')
        headers = {'Grpc-Metadata-macaroon': macaroon}
        url = f'https://{lndconnectload["ip_port"]}/v1/getinfo'
        r = requests.get(url, headers=headers, verify=cert_path)
        alias = r.json()
    print("""\t\t
    \033[1;37;40m{}\033[0;37;40m: \033[1;31;40mPyBLOCK\033[0;37;40m
    \033[1;37;40mNode\033[0;37;40m: \033[1;33;40m{}\033[0;37;40m
    \033[1;37;40mBlock\033[0;37;40m: \033[1;32;40m{}\033[0;37;40m
    \033[1;37;40mVersion\033[0;37;40m: {}

    \033[1;32;40mA.\033[0;37;40m Black
    \033[1;31;40mB.\033[0;37;40m Red
    \033[1;31;40mC.\033[0;37;40m Green
    \033[1;31;40mD.\033[0;37;40m Yellow
    \033[1;31;40mE.\033[0;37;40m Blue
    \033[1;31;40mF.\033[0;37;40m Magenta
    \033[1;31;40mG.\033[0;37;40m Cyan
    \033[1;31;40mH.\033[0;37;40m White
    \033[1;31;40mI.\033[0;37;40m Gray
    \u001b[33;1mEnter.\033[0;37;40m Return
    \n\n\x1b[?25h""".format(n if path['bitcoincli'] else a , alias['alias'], d['blocks'], version ()))
    menuColorsSelectRainbowStart(input("\033[1;32;40mSelect option: \033[0;37;40m"))

def colorsSelectRainbowStartOnchaiONLY():
    clear()
    blogo()
    sysinfo()
    pathexec()
    #lndconnectexec()
    if path['bitcoincli']:
        n = "Local" if path['bitcoincli'] else "Remote"
        bitcoincli = " getblockchaininfo"
        a = subprocess.run([path['bitcoincli']] + bitcoincli.split(), capture_output=True, text=True).stdout
        b = json.loads(a)
        d = b

    else:
        a = "Local" if path['bitcoincli'] else "Remote"
        blk = rpc('getblockchaininfo')
        d = blk

        cert_path = lndconnectload["tls"]
        macaroon = codecs.encode(open(lndconnectload["macaroon"], 'rb').read(), 'hex')
        headers = {'Grpc-Metadata-macaroon': macaroon}
        url = f'https://{lndconnectload["ip_port"]}/v1/getinfo'
        r = requests.get(url, headers=headers, verify=cert_path)
        alias = r.json()
    print("""\t\t
    \033[1;37;40m{}\033[0;37;40m: \033[1;31;40mPyBLOCK\033[0;37;40m
    \033[1;37;40mNode\033[0;37;40m: \033[1;33;40m{}\033[0;37;40m
    \033[1;37;40mBlock\033[0;37;40m: \033[1;32;40m{}\033[0;37;40m
    \033[1;37;40mVersion\033[0;37;40m: {}

    \033[1;32;40mA.\033[0;37;40m Black
    \033[1;31;40mB.\033[0;37;40m Red
    \033[1;31;40mC.\033[0;37;40m Green
    \033[1;31;40mD.\033[0;37;40m Yellow
    \033[1;31;40mE.\033[0;37;40m Blue
    \033[1;31;40mF.\033[0;37;40m Magenta
    \033[1;31;40mG.\033[0;37;40m Cyan
    \033[1;31;40mH.\033[0;37;40m White
    \033[1;31;40mI.\033[0;37;40m Gray
    \u001b[33;1mEnter.\033[0;37;40m Return
    \n\n\x1b[?25h""".format(n if path['bitcoincli'] else a ,  d['blocks'], version ()))
    menuColorsSelectRainbowStartOnchainONLY(input("\033[1;32;40mSelect option: \033[0;37;40m"))

def colorsSelectRainbowEnd():
    clear()
    blogo()
    sysinfo()
    pathexec()
    lndconnectexec()
    if path['bitcoincli']:
        n = "Local" if path['bitcoincli'] else "Remote"
        bitcoincli = " getblockchaininfo"
        a = subprocess.run([path['bitcoincli']] + bitcoincli.split(), capture_output=True, text=True).stdout
        b = json.loads(a)
        d = b

        lncli = " getinfo"
        lsd = subprocess.run([lndconnectload['ln']] + lncli.split(), capture_output=True, text=True).stdout
        lsd0 = str(lsd)
        alias = json.loads(lsd0)
    else:
        a = "Local" if path['bitcoincli'] else "Remote"
        blk = rpc('getblockchaininfo')
        d = blk

        cert_path = lndconnectload["tls"]
        macaroon = codecs.encode(open(lndconnectload["macaroon"], 'rb').read(), 'hex')
        headers = {'Grpc-Metadata-macaroon': macaroon}
        url = 'https://{}/v1/getinfo'.format(lndconnectload["ip_port"])
        r = requests.get(url, headers=headers, verify=cert_path)
        alias = r.json()
    print("""\t\t
    \033[1;37;40m{}\033[0;37;40m: \033[1;31;40mPyBLOCK\033[0;37;40m
    \033[1;37;40mNode\033[0;37;40m: \033[1;33;40m{}\033[0;37;40m
    \033[1;37;40mBlock\033[0;37;40m: \033[1;32;40m{}\033[0;37;40m
    \033[1;37;40mVersion\033[0;37;40m: {}

    \033[1;32;40mA.\033[0;37;40m Black
    \033[1;31;40mB.\033[0;37;40m Red
    \033[1;31;40mC.\033[0;37;40m Green
    \033[1;31;40mD.\033[0;37;40m Yellow
    \033[1;31;40mE.\033[0;37;40m Blue
    \033[1;31;40mF.\033[0;37;40m Magenta
    \033[1;31;40mG.\033[0;37;40m Cyan
    \033[1;31;40mH.\033[0;37;40m White
    \033[1;31;40mI.\033[0;37;40m Gray
    \u001b[33;1mEnter.\033[0;37;40m Return
    \n\n\x1b[?25h""".format(n if path['bitcoincli'] else a , alias['alias'], d['blocks'], version ()))
    menuColorsSelectRainbowEnd(input("\033[1;32;40mSelect option: \033[0;37;40m"))

def colorsSelectRainbowEndOnchainONLY():
    clear()
    blogo()
    sysinfo()
    pathexec()
    lndconnectexec()
    if path['bitcoincli']:
        n = "Local" if path['bitcoincli'] else "Remote"
        bitcoincli = " getblockchaininfo"
        a = subprocess.run([path['bitcoincli']] + bitcoincli.split(), capture_output=True, text=True).stdout
        b = json.loads(a)
        d = b

        lncli = " getinfo"
        lsd = subprocess.run([lndconnectload['ln']] + lncli.split(), capture_output=True, text=True).stdout
        lsd0 = str(lsd)
        alias = json.loads(lsd0)
    else:
        a = "Local" if path['bitcoincli'] else "Remote"
        blk = rpc('getblockchaininfo')
        d = blk

        cert_path = lndconnectload["tls"]
        macaroon = codecs.encode(open(lndconnectload["macaroon"], 'rb').read(), 'hex')
        headers = {'Grpc-Metadata-macaroon': macaroon}
        url = 'https://{}/v1/getinfo'.format(lndconnectload["ip_port"])
        r = requests.get(url, headers=headers, verify=cert_path)
        alias = r.json()
    print("""\t\t
    \033[1;37;40m{}\033[0;37;40m: \033[1;31;40mPyBLOCK\033[0;37;40m
    \033[1;37;40mNode\033[0;37;40m: \033[1;33;40m{}\033[0;37;40m
    \033[1;37;40mBlock\033[0;37;40m: \033[1;32;40m{}\033[0;37;40m
    \033[1;37;40mVersion\033[0;37;40m: {}

    \033[1;32;40mA.\033[0;37;40m Black
    \033[1;31;40mB.\033[0;37;40m Red
    \033[1;31;40mC.\033[0;37;40m Green
    \033[1;31;40mD.\033[0;37;40m Yellow
    \033[1;31;40mE.\033[0;37;40m Blue
    \033[1;31;40mF.\033[0;37;40m Magenta
    \033[1;31;40mG.\033[0;37;40m Cyan
    \033[1;31;40mH.\033[0;37;40m White
    \033[1;31;40mI.\033[0;37;40m Gray
    \u001b[33;1mEnter.\033[0;37;40m Return
    \n\n\x1b[?25h""".format(n if path['bitcoincli'] else a , d['blocks'], version ()))
    menuColorsSelectRainbowEndOnchainONLY(input("\033[1;32;40mSelect option: \033[0;37;40m"))

def menuSelection():
    chln = {"fullbtclnd":"","fullbtc":"","cropped":""}
    if cfg.has_config('intro.conf'):
        chln = cfg.intro_mode
        print(chln + "\n")
        if chln == "B":
            path = cfg.path
            MainMenuLOCALChainONLY()
        elif chln == "A":
            path = cfg.path
            MainMenuLOCAL()
        elif chln == "C":
            from SPV.spvblock import MainMenuCROPPED as _lite_menu
            _lite_menu()
    else:
        if cfg.has_config('blndconnect.conf'):
            chln['offchain'] = "offchain"
        else:
            chln['onchain'] = "onchain"

        cfg.save("selection.conf", chln)


def menuSelectionLN():
    lndconnectload = cfg.lndconnectload
    if lndconnectload['ln']:
        menuLNDLOCAL()
    else:
        menuLND()

def aaccPPiLNBits():
    try:
        bitLN = {"NN":"","pd":""}
        if os.path.isfile('config/lnbitSN.conf'):
            bitData= json.load(open("config/lnbitSN.conf", "r"))
            bitLN = bitData
            APILnbit()
        else:
            qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
            )
            bitLN['NN'] = randrange(10000000)
            curl = 'curl -X POST https://legend.lnbits.com/api/v1/payments -d ' + "'{" + """"out": false, "amount": 1000, "memo": "LNBits on PyBLOCK {}" """.format(bitLN['NN']) + "}'" + """ -H "X-Api-Key: 1d646820055e4e2da218e801eaacfc94 " -H "Content-type: application/json" """
            sh = subprocess.run(curl.split(), capture_output=True, text=True).stdout
            clear()
            blogo()
            n = str(sh)
            d = json.loads(n)
            q = d['payment_request']
            c = q.lower()
            while True:
                print("\033[1;30;47m")
                qr.add_data(c)
                qr.print_ascii()
                print("\033[0;37;40m")
                qr.clear()
                print("Lightning Invoice: " + c)
                dn = str(d['checking_id'])
                t.sleep(10)
                checkcurl = 'curl -X GET https://legend.lnbits.com/api/v1/payments/' + dn + """ -H "X-Api-Key: 1d646820055e4e2da218e801eaacfc94" -H "Content-type: application/json" """
                rsh = subprocess.run(checkcurl.split(), capture_output=True, text=True).stdout
                clear()
                blogo()
                nn = str(rsh)
                dd = json.loads(nn)
                db = dd['paid']
                if db is not True:
                    continue

                clear()
                blogo()
                tick()
                bitLN['pd'] = "PAID"
                with open("config/lnbitSN.conf", "w") as f: json.dump(bitLN, f, indent=2)
                createFileConnLNBits()
                break
    except Exception as e:
        logger.debug("Display error: %s", e)
        clear()
        blogo()
        print("\n\tSERIAL NUMBER NOT FOUND\n")
        input("Continue...")

def aaccPPiLNPay():
    try:
        bitLN = {"NN":"","pd":""}
        if os.path.isfile('config/lnpaySN.conf'): # Check if the file 'bclock.conf' is in the same folder
            bitData= json.load(open("config/lnpaySN.conf", "r")) # Load the file 'bclock.conf'
            bitLN = bitData # Copy the variable pathv to 'path'
            APILnPay()
        else:
            qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
            )
            bitLN['NN'] = randrange(10000000)
            curl = 'curl -X POST https://legend.lnbits.com/api/v1/payments -d ' + "'{" + """"out": false, "amount": 1000, "memo": "LNPay on PyBLOCK {}" """.format(bitLN['NN']) + "}'" + """ -H "X-Api-Key: 1d646820055e4e2da218e801eaacfc94 " -H "Content-type: application/json" """
            sh = subprocess.run(curl.split(), capture_output=True, text=True).stdout
            clear()
            blogo()
            n = str(sh)
            d = json.loads(n)
            q = d['payment_request']
            c = q.lower()
            while True:
                print("\033[1;30;47m")
                qr.add_data(c)
                qr.print_ascii()
                print("\033[0;37;40m")
                qr.clear()
                print("Lightning Invoice: " + c)
                dn = str(d['checking_id'])
                t.sleep(10)
                checkcurl = 'curl -X GET https://legend.lnbits.com/api/v1/payments/' + dn + """ -H "X-Api-Key: 1d646820055e4e2da218e801eaacfc94" -H "Content-type: application/json" """
                rsh = subprocess.run(checkcurl.split(), capture_output=True, text=True).stdout
                clear()
                blogo()
                nn = str(rsh)
                dd = json.loads(nn)
                db = dd['paid']
                if db is not True:
                    continue

                clear()
                blogo()
                tick()
                bitLN['pd'] = "PAID"
                with open("config/lnpaySN.conf", "w") as f: json.dump(bitLN, f, indent=2)
                createFileConnLNPay()
                break

    except Exception as e:
        logger.debug("Display error: %s", e)
        clear()
        blogo()
        print("\n\tSERIAL NUMBER NOT FOUND\n")
        input("Continue...")

def aaccPPiOpenNode():
    try:
        bitLN = {"NN":"","pd":""}
        if os.path.isfile('config/opennodeSN.conf'): # Check if the file 'bclock.conf' is in the same folder
            bitData= json.load(open("config/opennodeSN.conf", "r")) # Load the file 'bclock.conf'
            bitLN = bitData # Copy the variable pathv to 'path'
            APIOpenNode()
        else:
            qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
            )
            bitLN['NN'] = randrange(10000000)
            curl = 'curl -X POST https://legend.lnbits.com/api/v1/payments -d ' + "'{" + """"out": false, "amount": 1000, "memo": "OpenNode on PyBLOCK {}" """.format(bitLN['NN']) + "}'" + """ -H "X-Api-Key: 1d646820055e4e2da218e801eaacfc94 " -H "Content-type: application/json" """
            sh = subprocess.run(curl.split(), capture_output=True, text=True).stdout
            clear()
            blogo()
            n = str(sh)
            d = json.loads(n)
            q = d['payment_request']
            c = q.lower()
            while True:
                print("\033[1;30;47m")
                qr.add_data(c)
                qr.print_ascii()
                print("\033[0;37;40m")
                qr.clear()
                print("Lightning Invoice: " + c)
                dn = str(d['checking_id'])
                t.sleep(10)
                checkcurl = 'curl -X GET https://legend.lnbits.com/api/v1/payments/' + dn + """ -H "X-Api-Key: 1d646820055e4e2da218e801eaacfc94" -H "Content-type: application/json" """
                rsh = subprocess.run(checkcurl.split(), capture_output=True, text=True).stdout
                clear()
                blogo()
                nn = str(rsh)
                dd = json.loads(nn)
                db = dd['paid']
                if db is not True:
                    continue

                clear()
                blogo()
                tick()
                bitLN['pd'] = "PAID"
                with open("config/opennodeSN.conf", "w") as f: json.dump(bitLN, f, indent=2)
                createFileConnOpenNode()
                break

    except Exception as e:
        logger.debug("Display error: %s", e)
        clear()
        blogo()
        print("\n\tSERIAL NUMBER NOT FOUND\n")
        input("Continue...")


def aaccPPiTippinMe():
    if os.path.isfile('config/tippinme.conf'): # Check if the file 'bclock.conf' is in the same folder
        APITippinMe()
    else:
        createFileTippinMe()

def aaccPPiTallyCo():
    if os.path.isfile('config/tallyco.conf'): # Check if the file 'bclock.conf' is in the same folder
        APITallyCo()
    else:
        createFileConnTallyCo()

"""def ():
    r = requests.get('https://raw.githubusercontent.com/curly60e/pyblock/master/ver.txt')
    r.headers['Content-Type']
    n = r.text
    di = json.loads(n)
    if di['version'] == version:
        q = print(" ")
    else:
        print("\n    ------------------------------------------")
        q = print("    \033[1;31;40mNew version available\033[0;37;40m > Exit and $pip3 install pybitblock -U ")
        print("    ------------------------------------------")"""

def testlogo():
    output = render('PyBLOCK', colors=[settings['colorA'], settings['colorB']], align='left', font=settings['design'])
    print(output)
    print("""

    -------------------------
        Design:      {}
        Front Color: {}
        Back Color:  {}
    -------------------------

    """.format(settings['design'], settings['colorA'], settings['colorB']))
    try:
        print("<<< Cancel Control + C")
        input("Enter To Apply...")
        settings["gradient"] = "color"
        with open("config/pyblocksettings.conf", "w") as f: json.dump(settings, f, indent=2)
    except Exception as e:
        show_error(str(e))
        logger.debug("Suppressed error: %s", e)

def testlogoRB():
    output = render('PyBLOCK', gradient=[settings['colorA'], settings['colorB']], align='left', font=settings['design'])
    print(output)
    print("""

    -------------------------
        Design:      {}
        Start Color: {}
        End Color:   {}
    -------------------------

    """.format(settings['design'], settings['colorA'], settings['colorB']))
    try:
        print("<<< Cancel Control + C")
        input("Enter To Apply...")
        settings["gradient"] = "grd"
        with open("config/pyblocksettings.conf", "w") as f: json.dump(settings, f, indent=2)
    except Exception as e:
        show_error(str(e))
        logger.debug("Suppressed error: %s", e)

def testClock():
    pathexec()
    #lndconnectexec()
    bitcoinclient = path['bitcoincli'] + " getblockcount"
    block = subprocess.run(str(bitcoinclient).split(), capture_output=True, text=True).stdout # 'getblockcount' convert to string
    b = block
    output = render(str(b), colors=[settingsClock['colorA'], settingsClock['colorB']], align='left')
    print(output)
    print("""

    -------------------------
        Front Color: {}
        Back Color:  {}
    -------------------------

    """.format(settingsClock['colorA'], settingsClock['colorB']))
    try:
        print("<<< Cancel Control + C")
        input("Enter To Apply...")
        settingsClock["gradient"] = "color"
        with open("config/pyblocksettingsClock.conf", "w") as f: json.dump(settingsClock, f, indent=2)
    except Exception as e:
        show_error(str(e))
        logger.debug("Suppressed error: %s", e)

#--------------------------------- End Menu section -----------------------------------
#--------------------------------- Main Menu execution --------------------------------

def menuSettingsLocal(menuSTT):
    if menuSTT in ["A", "a"]:
        clear()
        blogo()
        designQ()
    elif menuSTT in ["B", "b"]:
        clear()
        blogo()
        colors()
    elif menuSTT in ["C", "c"]:
        clear()
        blogo()
        colorsC()
    elif menuSTT in ["D", "d"]:
        clockDisplaySettings()

def menuSettingsLocalOnchainONLY(menuSTT):
    if menuSTT in ["A", "a"]:
        clear()
        blogo()
        designQOnchainONLY()
    elif menuSTT in ["B", "b"]:
        clear()
        blogo()
        colorsOnchainONLY()
    elif menuSTT in ["C", "c"]:
        clear()
        blogo()
        colorsCOnchainONLY()
    elif menuSTT in ["D", "d"]:
        clockDisplaySettings()

def menuSettingsRemote(menuSTT):
    if menuSTT in ["A", "a"]:
        clear()
        blogo()
        designQ()
    elif menuSTT in ["B", "b"]:
        clear()
        blogo()
        colors()
    elif menuSTT in ["C", "c"]:
        clear()
        blogo()
        colorsCRemote()
    elif menuSTT in ["D", "d"]:
        clockDisplaySettings()

def clockDisplaySettings():
    """Interactive settings menu for clock display features."""
    while True:
        try:
            clear()
            blogo()
            s = cfg.settings_clock

            def _on_off(val):
                return "\033[1;32;40mON\033[0;37;40m" if val else "\033[1;31;40mOFF\033[0;37;40m"

            print("""\t\t
    \033[1;37;40mClock Display Settings\033[0;37;40m

    \u001b[38;5;27m1.\033[0;37;40m Countdown Timer        {}
    \u001b[38;5;27m2.\033[0;37;40m Epoch Progress Bar     {}
    \u001b[38;5;27m3.\033[0;37;40m Fee Rate Indicator     {}
    \u001b[38;5;27m4.\033[0;37;40m Hashrate Sparkline     {}
    \u001b[38;5;27m5.\033[0;37;40m UTC Time Display       {}
    \u001b[38;5;27m6.\033[0;37;40m Zen Mode               {}
    \u001b[38;5;27m7.\033[0;37;40m Heartbeat Pulse        {}
    \u001b[38;5;27m8.\033[0;37;40m Generative Art         {}
    \u001b[38;5;27m9.\033[0;37;40m Fireworks on Milestones {}

    \033[1;37;40m--- Visual ---\033[0;37;40m
    \u001b[38;5;27mM.\033[0;37;40m Miner Pool Tag         {}
    \u001b[38;5;27mW.\033[0;37;40m Block Weight Meter     {}
    \u001b[38;5;27mT.\033[0;37;40m Block Time Histogram   {}
    \u001b[38;5;27mP.\033[0;37;40m Peer Count             {}
    \u001b[38;5;27mL.\033[0;37;40m Moon Phase             {}

    \u001b[38;5;27mA.\033[0;37;40m Animation: \033[1;33;40m{}\033[0;37;40m
    \u001b[38;5;27mS.\033[0;37;40m Sound:     \033[1;33;40m{}\033[0;37;40m
    \u001b[33;1mEnter.\033[0;37;40m Return
    \n\x1b[?25h""".format(
                _on_off(s.get('show_countdown', True)),
                _on_off(s.get('show_epoch_bar', True)),
                _on_off(s.get('show_fee_rates', True)),
                _on_off(s.get('show_sparkline', False)),
                _on_off(s.get('show_utc_time', False)),
                _on_off(s.get('zen_mode', False)),
                _on_off(s.get('heartbeat', True)),
                _on_off(s.get('generative_art', False)),
                _on_off(s.get('fireworks', True)),
                _on_off(s.get('show_miner_pool', True)),
                _on_off(s.get('show_block_weight', False)),
                _on_off(s.get('show_block_times', True)),
                _on_off(s.get('show_peers', False)),
                _on_off(s.get('show_moon', False)),
                s.get('animation', 'matrix'),
                s.get('sound', 'bell'),
            ))

            opt = input("\033[1;32;40mSelect option: \033[0;37;40m").strip()

            toggles = {
                '1': 'show_countdown', '2': 'show_epoch_bar',
                '3': 'show_fee_rates', '4': 'show_sparkline',
                '5': 'show_utc_time', '6': 'zen_mode',
                '7': 'heartbeat', '8': 'generative_art',
                '9': 'fireworks',
            }
            toggles_alpha = {
                'M': 'show_miner_pool', 'm': 'show_miner_pool',
                'W': 'show_block_weight', 'w': 'show_block_weight',
                'T': 'show_block_times', 't': 'show_block_times',
                'P': 'show_peers', 'p': 'show_peers',
                'L': 'show_moon', 'l': 'show_moon',
            }

            if opt in toggles:
                key = toggles[opt]
                s[key] = not s.get(key, False)
                cfg.save("pyblocksettingsClock.conf", s)
            elif opt in toggles_alpha:
                key = toggles_alpha[opt]
                s[key] = not s.get(key, False)
                cfg.save("pyblocksettingsClock.conf", s)
            elif opt in ['A', 'a']:
                modes = ['matrix', 'odometer', 'none']
                current = s.get('animation', 'matrix')
                idx = (modes.index(current) + 1) % len(modes) if current in modes else 0
                s['animation'] = modes[idx]
                cfg.save("pyblocksettingsClock.conf", s)
            elif opt in ['S', 's']:
                modes = ['bell', 'pattern', 'silent']
                current = s.get('sound', 'bell')
                idx = (modes.index(current) + 1) % len(modes) if current in modes else 0
                s['sound'] = modes[idx]
                cfg.save("pyblocksettingsClock.conf", s)
            else:
                break
        except KeyboardInterrupt:
            break


def menuColors(menuCLS):
    if menuCLS in ["A", "a"]:
        colorsSelectFront()
    elif menuCLS in ["B", "b"]:
        colorsSelectBack()
    elif menuCLS in ["C", "c"]:
        colorsSelectRainbow()
    elif menuCLS in ["F", "f"]:
        colors()

def menuColorsOnchainONLY(menuCLS):
    if menuCLS in ["A", "a"]:
        colorsSelectFrontOnchainONLY()
    elif menuCLS in ["B", "b"]:
        colorsSelectBackOnchainONLY()
    elif menuCLS in ["C", "c"]:
        colorsSelectRainbowOnchainONLY()
    elif menuCLS in ["F", "f"]:
        colorsOnchainONLY()

def menuColorsClock(menuCLS):
    if menuCLS in ["A", "a"]:
        colorsSelectFrontClock()
    elif menuCLS in ["B", "b"]:
        colorsSelectBackClock()
    elif menuCLS in ["F", "f"]:
        colors()

def menuColorsClockOnchainONLY(menuCLS):
    if menuCLS in ["A", "a"]:
        colorsSelectFrontClockOnchainONLY()
    elif menuCLS in ["B", "b"]:
        colorsSelectBackClockOnchainONLY()
    elif menuCLS in ["F", "f"]:
        colorsOnchainONLY()

def menuColorsClockRemote(menuCLS):
    if menuCLS in ["A", "a"]:
        colorsSelectFrontClockRemote()
    elif menuCLS in ["B", "b"]:
        colorsSelectBackClockRemote()
    elif menuCLS in ["F", "f"]:
        colors()

def menuColorsSelectRainbow(menuRF):
    if menuRF in ["A", "a"]:
        colorsSelectRainbowStart()
    elif menuRF in ["B", "b"]:
        colorsSelectRainbowEnd()
    elif menuRF in ["F", "f"]:
        colors()

def menuColorsSelectRainbowOnchainONLY(menuRF):
    if menuRF in ["A", "a"]:
        colorsSelectRainbowStartOnchaiONLY()
    elif menuRF in ["B", "b"]:
        colorsSelectRainbowEndOnchainONLY()
    elif menuRF in ["F", "f"]:
        colorsOnchainONLY()

def menuColorsSelectRainbowEnd(menuCF):
    select_color(settings, "colorB", testlogoRB, colors)

def menuColorsSelectRainbowEndOnchainONLY(menuCF):
    select_color(settings, "colorB", testlogoRB, colorsOnchainONLY)

def menuColorsSelectRainbowStart(menuCF):
    select_color(settings, "colorA", testlogoRB, colors)

def menuColorsSelectRainbowStartOnchainONLY(menuCF):
    select_color(settings, "colorA", testlogoRB, colorsOnchainONLY)

def menuColorsSelectBack(menuCF):
    select_color(settings, "colorB", testlogo, colors)

def menuColorsSelectBackOnchainONLY(menuCF):
    select_color(settings, "colorB", testlogo, colorsOnchainONLY)

def menuColorsSelectFront(menuCF):
    select_color(settings, "colorA", testlogo, colors)

def menuColorsSelectFrontOncainONLY(menuCF):
    select_color(settings, "colorA", testlogo, colorsOnchainONLY)

def menuColorsSelectFrontClock(menuCF):
    select_color(settingsClock, "colorA", testClock, colors)

def menuColorsSelectFrontClockOnchainONLY(menuCF):
    select_color(settingsClock, "colorA", testClock, colorsOnchainONLY)

def menuColorsSelectBackClock(menuCF):
    select_color(settingsClock, "colorB", testClock, colors)

def menuColorsSelectBackClockOnchainONLY(menuCF):
    select_color(settingsClock, "colorB", testClock, colorsOnchainONLY)

def menuColorsSelectFrontClockRemote(menuCF):
    select_color(settingsClock, "colorA", testClockRemote, colors)

def menuColorsSelectBackClockRemote(menuCF):
    select_color(settingsClock, "colorB", testClockRemote, colors)

def menuDesign(menuDSN):
    if menuDSN in ["A", "a"]:
        clear()
        blogo()
        settings["design"] = "block"
        testlogo()
    elif menuDSN in ["B", "b"]:
        clear()
        blogo()
        settings['design'] = "slick"
        testlogo()
    elif menuDSN in ["C", "c"]:
        clear()
        blogo()
        settings['design'] = "tiny"
        testlogo()
    elif menuDSN in ["D", "d"]:
        clear()
        blogo()
        settings['design'] = "grid"
        testlogo()
    elif menuDSN in ["E", "e"]:
        clear()
        blogo()
        settings['design'] = "pallet"
        testlogo()
    elif menuDSN in ["F", "f"]:
        clear()
        blogo()
        settings['design'] = "shade"
        testlogo()
    elif menuDSN in ["G", "g"]:
        clear()
        blogo()
        settings['design'] = "chrome"
        testlogo()
    elif menuDSN in ["H", "h"]:
        clear()
        blogo()
        settings['design'] = "simple"
        testlogo()
    elif menuDSN in ["I", "i"]:
        clear()
        blogo()
        settings['design'] = "simpleBlock"
        testlogo()
    elif menuDSN in ["J", "j"]:
        clear()
        blogo()
        settings['design'] = "3d"
        testlogo()
    elif menuDSN in ["K", "k"]:
        clear()
        blogo()
        settings['design'] = "simple3d"
        testlogo()
    elif menuDSN in ["L", "l"]:
        clear()
        blogo()
        settings['design'] = "huge"
        testlogo()

def menuDesignOnchainONLY(menuDSN):
    if menuDSN in ["A", "a"]:
        clear()
        blogo()
        settings["design"] = "block"
        testlogo()
    elif menuDSN in ["B", "b"]:
        clear()
        blogo()
        settings['design'] = "slick"
        testlogo()
    elif menuDSN in ["C", "c"]:
        clear()
        blogo()
        settings['design'] = "tiny"
        testlogo()
    elif menuDSN in ["D", "d"]:
        clear()
        blogo()
        settings['design'] = "grid"
        testlogo()
    elif menuDSN in ["E", "e"]:
        clear()
        blogo()
        settings['design'] = "pallet"
        testlogo()
    elif menuDSN in ["F", "f"]:
        clear()
        blogo()
        settings['design'] = "shade"
        testlogo()
    elif menuDSN in ["G", "g"]:
        clear()
        blogo()
        settings['design'] = "chrome"
        testlogo()
    elif menuDSN in ["H", "h"]:
        clear()
        blogo()
        settings['design'] = "simple"
        testlogo()
    elif menuDSN in ["I", "i"]:
        clear()
        blogo()
        settings['design'] = "simpleBlock"
        testlogo()
    elif menuDSN in ["J", "j"]:
        clear()
        blogo()
        settings['design'] = "3d"
        testlogo()
    elif menuDSN in ["K", "k"]:
        clear()
        blogo()
        settings['design'] = "simple3d"
        testlogo()
    elif menuDSN in ["L", "l"]:
        clear()
        blogo()
        settings['design'] = "huge"
        testlogo()

#------------API---------------------

def OwnNodeMinerControl(menuMin):
    if menuMin in ["A", "a"]:
        OwnNodeMinerComputer()
    elif menuMin in ["B", "b"]:
        OwnNodeMinerRaspberry()
    elif menuMin in ["R", "r"]:
        menuSelection()

def OwnNodeMinerControlONCHAIN(menuMino):
    if menuMino in ["A", "a"]:
        OwnNodeMinerComputer()
    elif menuMino in ["B", "b"]:
        OwnNodeMinerRaspberry()
    elif menuMino in ["R", "r"]:
        menuSelection()

def mempoolmenuS(menuMem):
    if menuMem in ["A", "a"]:
        blocks()
    elif menuMem in ["B", "b"]:
        fee()
    elif menuMem in ["C", "c"]:
        MemShell()
    elif menuMem in ["R", "r"]:
        menuSelection()

def mempoolmenuSOnchainONLY(menuMem):
    if menuMem in ["A", "a"]:
        blocks()
    elif menuMem in ["B", "b"]:
        fee()
    elif menuMem in ["C", "c"]:
        MemShell()
    elif menuMem in ["R", "r"]:
        menuSelection()

def menuTallyCo(menuTLC):
    if menuTLC in ["A", "a"]:
        tallycoGetPayment()
    elif menuTLC in ["B", "b"]:
        tallycoDonateid()
    elif menuTLC in ["R", "r"]:
        menuSelection()

def menuTallyCoOnchainONLY(menuTLC):
    if menuTLC in ["A", "a"]:
        tallycoGetPayment()
    elif menuTLC in ["B", "b"]:
        tallycoDonateid()
    elif menuTLC in ["R", "r"]:
        menuSelection()

def menuTippinMe(menuTM):
    if menuTM in ["A", "a"]:
        tippinmeGetInvoice()
    elif menuTM in ["R", "r"]:
        menuSelection()

def menuTippinMeOnchainONLY(menuTM):
    if menuTM in ["A", "a"]:
        tippinmeGetInvoice()
    elif menuTM in ["R", "r"]:
        menuSelection()

def menuOpenNode(menuOP):
    if menuOP in ["A", "a"]:
        clear()
        blogo()
        OpenNodecreatecharge()
    elif menuOP in ["B", "b"]:
        clear()
        blogo()
        OpenNodeiniciatewithdrawal()
    elif menuOP in ["C", "c"]:
        clear()
        blogo()
        OpenNodelistfunds()
    elif menuOP in ["D", "d"]:
        clear()
        blogo()
        OpenNodeListPayments()
    elif menuOP in ["S", "s"]:
        clear()
        blogo()
        OpenNodeCheckStatus()
    elif menuOP in ["R", "r"]:
        menuSelection()

def menuOpenNodeOnchainONLY(menuOP):
    if menuOP in ["A", "a"]:
        clear()
        blogo()
        OpenNodecreatecharge()
    elif menuOP in ["B", "b"]:
        clear()
        blogo()
        OpenNodeiniciatewithdrawal()
    elif menuOP in ["C", "c"]:
        clear()
        blogo()
        OpenNodelistfunds()
    elif menuOP in ["D", "d"]:
        clear()
        blogo()
        OpenNodeListPayments()
    elif menuOP in ["S", "s"]:
        clear()
        blogo()
        OpenNodeCheckStatus()
    elif menuOP in ["R", "r"]:
        menuSelection()

def menuLNPAY(menuNW):
    if menuNW in ["A", "a"]:
        clear()
        blogo()
        lnpayCreateInvoice()
    elif menuNW in ["B", "b"]:
        clear()
        blogo()
        lnpayPayInvoice()
    elif menuNW in ["C", "c"]:
        clear()
        blogo()
        lnpayGetBalance()
    elif menuNW in ["D", "d"]:
        clear()
        blogo()
        lnpayGetTransactions()
    elif menuNW in ["E", "e"]:
        clear()
        blogo()
        lnpayTransBWallets()
    elif menuNW in ["R", "r"]:
        menuSelection()

def menuLNPAYOnchainONLY(menuNW):
    if menuNW in ["A", "a"]:
        clear()
        blogo()
        lnpayCreateInvoice()
    elif menuNW in ["B", "b"]:
        clear()
        blogo()
        lnpayPayInvoice()
    elif menuNW in ["C", "c"]:
        clear()
        blogo()
        lnpayGetBalance()
    elif menuNW in ["D", "d"]:
        clear()
        blogo()
        lnpayGetTransactions()
    elif menuNW in ["E", "e"]:
        clear()
        blogo()
        lnpayTransBWallets()
    elif menuNW in ["R", "r"]:
        menuSelection()

def menuLNBPI(menuLNQ):
    if menuLNQ in ["A", "a"]:
        clear()
        blogo()
        lnbitCreateNewInvoice()
    elif menuLNQ in ["B", "b"]:
        clear()
        blogo()
        lnbitPayInvoice()
    elif menuLNQ in ["C", "c"]:
        clear()
        blogo()
        lnbitCreatePayWall()
    elif menuLNQ in ["D", "d"]:
        clear()
        blogo()
        lnbitDeletePayWall()
    elif menuLNQ in ["E", "e"]:
        clear()
        blogo()
        lnbitListPawWall()
    elif menuLNQ in ["F", "f"]:
        clear()
        blogo()
        lnbitsLNURLw()
    elif menuLNQ in ["G", "g"]:
        clear()
        blogo()
        lnbitsLNURLwList()
    elif menuLNQ in ["R", "r"]:
        menuSelection()

def menuLNBPIOnchainONLY(menuLNQ):
    if menuLNQ in ["A", "a"]:
        clear()
        blogo()
        lnbitCreateNewInvoice()
    elif menuLNQ in ["B", "b"]:
        clear()
        blogo()
        lnbitPayInvoice()
    elif menuLNQ in ["C", "c"]:
        clear()
        blogo()
        lnbitCreatePayWall()
    elif menuLNQ in ["D", "d"]:
        clear()
        blogo()
        lnbitDeletePayWall()
    elif menuLNQ in ["E", "e"]:
        clear()
        blogo()
        lnbitListPawWall()
    elif menuLNQ in ["F", "f"]:
        clear()
        blogo()
        lnbitsLNURLw()
    elif menuLNQ in ["G", "g"]:
        clear()
        blogo()
        lnbitsLNURLwList()
    elif menuLNQ in ["R", "r"]:
        menuSelection()

def rateSXMenu(menuSX):
    if menuSX in ["A", "a"]:
        clear()
        blogo()
        rateSXList()
    elif menuSX in ["B", "b"]:
        clear()
        blogo()
        rateSXGraph()
    elif menuSX in ["R", "r"]:
        menuSelection()

def rateSXMenuOnchainONLY(menuSX):
    if menuSX in ["A", "a"]:
        clear()
        blogo()
        rateSXList()
    elif menuSX in ["B", "b"]:
        clear()
        blogo()
        rateSXGraph()
    elif menuSX in ["R", "r"]:
        menuSelection()

#---------------END API-----------


def runTheNumbersControl(menuNumbers):
    if menuNumbers in ["A", "a"]:
        clear()
        blogo()
        countdownblock()
    elif menuNumbers in ["B", "b"]:
        clear()
        blogo()
        localHalving()
    elif menuNumbers in ["C", "c"]:
        clear()
        blogo()
        calc = """
                    ----------------------------
                             PROCESSING
                            THE  NUMBERS
                    ----------------------------
         """
        comeback = """
                    ----------------------------
                       MAKE YOURSELF A COFFEE
                         AND COME BACK IN A
                               MOMENT
                    ----------------------------
        """
        cprint(comeback, 'yellow')
        cprint(calc, 'red', attrs=['blink'])
        runthenumbers()
    elif menuNumbers in ["D", "d"]:
        clear()
        blogo()
        blockTmpConn()
    elif menuNumbers in ["E", "e"]:
        clear()
        blogo()
        epoch()

def runTheNumbersControlOnchainONLY(menuNumbers):
    if menuNumbers in ["A", "a"]:
        clear()
        blogo()
        countdownblock()
    elif menuNumbers in ["B", "b"]:
        clear()
        blogo()
        localHalving()
    elif menuNumbers in ["C", "c"]:
        clear()
        blogo()
        calc = """
                    ----------------------------
                             PROCESSING
                            THE  NUMBERS
                    ----------------------------
         """
        comeback = """
                    ----------------------------
                       MAKE YOURSELF A COFFEE
                         AND COME BACK IN A
                               MOMENT
                    ----------------------------
        """
        cprint(comeback, 'yellow')
        cprint(calc, 'red', attrs=['blink'])
        runthenumbers()
    elif menuNumbers in ["D", "d"]:
        clear()
        blogo()
        blockTmpConn()
    elif menuNumbers in ["E", "e"]:
        clear()
        blogo()
        epoch()

def runTheNumbersControlConn(menuNumbersconn):
    if menuNumbersconn in ["A", "a"]:
        clear()
        blogo()
        countdownblockConn()
    elif menuNumbersconn in ["B", "b"]:
        clear()
        blogo()
        remoteHalving()
    elif menuNumbersconn in ["C", "c"]:
        clear()
        blogo()
        calc = """
                    ----------------------------
                             PROCESSING
                            THE  NUMBERS
                    ----------------------------
         """
        comeback = """
                    ----------------------------
                       MAKE YOURSELF A COFFEE
                         AND COME BACK IN A
                               MOMENT
                    ----------------------------
        """
        cprint(comeback, 'yellow')
        cprint(calc, 'red', attrs=['blink'])
        runthenumbersConn()
    elif menuNumbers in ["D", "d"]:
        clear()
        blogo()
        blockTmpConn()
    elif menuNumbers in ["E", "e"]:
        clear()
        blogo()
        epoch()

def menuWeather(menuWD):
    if menuWD in ["A", "a"]:
        wttrDataV1()
    elif menuWD in ["B", "b"]:
        wttrDataV2()

def menuWeatherOnchainONLY(menuWD):
    if menuWD in ["A", "a"]:
        wttrDataV1()
    elif menuWD in ["B", "b"]:
        wttrDataV2()

def mainmenuControl(menuS, mode): #Unified execution of Main Menu options
    if menuS in ["A", "a"]:
        from clock import run_clock
        clock_mode = "remote" if mode == "remote" else "local"
        run_clock(clock_mode, path, cfg.settings_clock)
    elif menuS in ["B", "b"]:
        if mode == "remote":
            bitcoincoremenuREMOTE()
        elif mode == "onchain_only":
            bitcoincoremenuLOCALOnchainONLY()
        else:
            bitcoincoremenuLOCAL()
    elif menuS in ["L", "l"]:
        if mode != "onchain_only":
            if mode == "remote":
                lightningnetworkREMOTE()
            else:
                lightningnetworkLOCAL()
    elif menuS in ["S", "s"]:
        if mode == "remote":
            settings4Remote()
        elif mode == "onchain_only":
            settings4LocalOnchainONLY()
        else:
            settings4Local()
    elif menuS in ["P", "p"]:
        if mode == "onchain_only":
            APIMenuLOCALOnchainONLY()
        else:
            APIMenuLOCAL()
    elif menuS in ["X", "x"]:
        if mode == "onchain_only":
            dntOnchainONLY()
        else:
            dnt()
    elif menuS in ["Q", "q"]:
        os._exit(0)
        apisnd.close()
        donation.close()
        clone.close()
        logos.close()
        feed.close()
        sysinf.close()
        nodeconnection.close()
        exit()
    elif menuS in ["T", "t"]:
        clear()
        delay_print("\033[1;32;40mWake up, Neo...")
        t.sleep(2)
        clear()
        delay_print("The Matrix has you...")
        t.sleep(2)
        clear()
        delay_print("Follow the white rabbit.")
        t.sleep(3)
        clear()
        print("Knock, knock, Neo.\033[0;37;40m\n")
        t.sleep(2)
        clear()
        t.sleep(3)
        screensv()
    elif menuS in ["nym", "Nym", "NYM", "nYm", "nyM", "NYm", "NyM", "nYM"]:
        clear()
        blogo()
        robotNym()
    elif menuS in ["wt", "WT", "Wt", "wT"]:
        clear()
        blogo()
        callGitWardenTerminal()
    elif menuS in ["ss", "SS", "Ss", "sS"]:
        clear()
        blogo()
        callGitSatSale()
    elif menuS in ["tt", "TT", "Tt", "tT"]:
        clear()
        blogo()
        callGitBpytop()
    elif menuS in ["CA", "ca", "Ca", "cA"]:
        clear()
        blogo()
        callGitCashu()
    elif menuS in ["7"]:
        clear()
        blogo()
        output = render("7 Blocks - The Game", colors=['yellow'], align='left', font='tiny')
        print(output)
        subprocess.run(["python3", "7Blocks.py"], cwd="SPV")
        input("\a\nContinue...")
    elif menuS in ["SOLO", "solo", "SoLo", "sOlO"]:
        clear()
        blogo()
        output = render("Solo Mining", colors=['yellow'], align='left', font='tiny')
        print(output)
        subprocess.run(["python3", "PyBlockMiner.py"], cwd="SPV")
        input("\a\nContinue...")
    else:
        if menuS.strip():
            from shared.ui import YELLOW, RESET
            print(f"    {YELLOW}Invalid option '{menuS}'. Try again.{RESET}")
            t.sleep(1)

def mainmenuLOCALcontrol(menuS): #Execution of the Main Menu options
    mainmenuControl(menuS, "local")

def mainmenuLOCALcontrolOnchainONLY(menuS): #Execution of the Main Menu options
    mainmenuControl(menuS, "onchain_only")

def slushpoolLOCALOnchainONLYMenu(slush):
    if slush in ["A", "a"]:
        clear()
        blogo()
        slDIFFConn()
    elif slush in ["C", "c"]:
        clear()
        blogo()
        slPOOLConn()
    elif slush in ["E", "e"]:
        clear()
        blogo()
        getPoolSlushCheck()

def ckpoolLOCALOnchainONLYMenu(slush):
    if ckpool in ["A", "a"]:
        clear()
        blogo()
        getPoolCKCheck()

def ckpoolREMOTEOnchainONLYMenu(slush):
    if ckpool in ["A", "a"]:
        clear()
        blogo()
        getPoolCKCheck()

def pyblockpoolLOCALOnchainONLYMenu(slush):
    if pyblockpool in ["A", "a"]:
        clear()
        blogo()
        getPoolPYBLOCKCheck()

def pyblockpoolREMOTEOnchainONLYMenu(slush):
    if pyblockpool in ["A", "a"]:
        clear()
        blogo()
        getPoolPYBLOCKCheck()

def bitcoincoremenuLocalControl(bcore, mode=None): #Unified Bitcoin Core local control
    if bcore in ["A", "a"]:
        while True:
            try:
                clear()
                blogo()
                sysinfo()
                close()
                console()
                t.sleep(5)
            except Exception as e:
                logger.debug("Loop interrupted: %s", e)
                break
    elif bcore in ["B", "b"]:
        clear()
        blogo()
        getgenesis()
        input("Continue...")
        menuSelection()
    elif bcore in ["C", "c"]:
        getblock()
    elif bcore in ["D", "d"]:
        runTheNumbersMenuOnchainONLY()
    elif bcore in ["E", "e"]:
        decodeHexOnchainONLY()
    elif bcore in ["F", "f"]:
        try:
            clear()
            blogo()
            sysinfo()
            close()
            decodeQR()
            input("Continue...")
        except Exception as e:
            show_error(str(e))
            logger.debug("Suppressed error: %s", e)
    elif bcore in ["G", "g"]:
        getrawtx()
    elif bcore in ["H", "h"]:
        miscellaneousLOCALOnchainONLY()
    elif bcore in ["I", "i"]:
        callColdCore()
    elif bcore in ["J", "j"]:
        pdfconvert()
    elif bcore in ["M", "m"]:
        mtConn()
    elif bcore in ["O", "o"]:
        bitcoincoremenuLOCALOPRETURNOnchainONLY()
    elif bcore in ["W", "w"]:
        walletmenuLOCALOnchainONLY()
    elif bcore in ["Z", "z"]:
        statsConn()
    elif bcore in ["Q", "q"]:
        miningConn()
    elif bcore in ["U", "u"]:
        untxsConn()
    elif bcore in ["S", "s"]:
        counttxs()
    elif bcore in ["L", "l"]:
        try:
            lastblockdetail.run_urwid()
        except Exception as e:
            show_error(str(e))
            logger.debug("Suppressed error: %s", e)
    elif bcore in ["V", "v"]:
        try:
            clear()
            execute_visualizer()
        except Exception as e:
            show_error(str(e))
            logger.debug("Suppressed error: %s", e)
    elif bcore in ["Y", "y"]:
        try:
            asyncio.run(mempool_monitor.display_mempool_info())
        except Exception as e:
            show_error(str(e))
            logger.debug("Suppressed error: %s", e)
    elif bcore in ["X", "x"]:
        try:
            clear()
            some_other_function()
        except Exception as e:
            show_error(str(e))
            logger.debug("Suppressed error: %s", e)
    elif bcore in ["K", "k"]:
        try:
            peers_monitor.run_peers_monitor()()
        except Exception as e:
            show_error(str(e))
            logger.debug("Suppressed error: %s", e)
    elif bcore in ["N", "n"]:
        try:
            tx_search.search_tx()
        except Exception as e:
            show_error(str(e))
            logger.debug("Suppressed error: %s", e)
    elif bcore in ["P", "p"]:
        try:
            clear()
            call_blocks()
        except Exception as e:
            show_error(str(e))
            logger.debug("Suppressed error: %s", e)
    elif bcore in ["CM", "cm"]:
        CoreMiner()
    elif bcore in ["ONM", "onm"]:
        OwnNodeMinerONCHAIN()
    elif bcore in ["VG", "vg"]:
        clear()
        blogo()
        output = render("Vanity Generator", colors=['yellow'], align='left', font='tiny')
        print(output)
        subprocess.run(["python3", "PyVanityGenerator.py"], cwd="SPV")
        input("\a\nContinue...")
    else:
        if bcore.strip():
            from shared.ui import YELLOW, RESET
            print(f"    {YELLOW}Invalid option '{bcore}'. Try again.{RESET}")
            t.sleep(1)

def bitcoincoremenuLOCALcontrolA(bcore):
    bitcoincoremenuLocalControl(bcore, "local")

def bitcoincoremenuLOCALcontrolAOnchainONLY(bcore):
    bitcoincoremenuLocalControl(bcore, "onchain_only")

def walletmenuLOCALcontrolAOnchainONLY(walletmnu):
    if walletmnu in ["A", "a"]:
        getnewaddressOnchain()
    elif walletmnu in ["B", "b"]:
        gettransactionsOnchain()
    elif walletmnu in ["C", "c"]:
        dumppk()
    elif walletmnu in ["D", "d"]:
        wallmenu()
    elif walletmnu in ["E", "e"]:
        inffmenu()
    elif walletmnu in ["F", "f"]:
        miningmenu()

def bitcoincoremenuLOCALcontrolO(oreturn):
    if oreturn in ["A", "a"]:
        clear()
        blogo()
        opreturn()
    elif oreturn in ["B", "b"]:
        clear()
        blogo()
        opreturn_view()
    elif oreturn in ["C", "c"]:
        clear()
        blogo()
        opretminer()

def bitcoincoremenuLOCALcontrolOOnchainONLY(oreturn):
    if oreturn in ["A", "a"]:
        clear()
        blogo()
        opreturn()
    elif oreturn in ["B", "b"]:
        clear()
        blogo()
        opreturn_view()
    elif oreturn in ["C", "c"]:
        clear()
        blogo()
        opretminer()

def miscellaneousLOCALmenu(misce):
    if misce in ["A", "a"]:
        while True:
            try:
                clear()
                blogo()
                close()
                logoA()
                tmp()
                clear()
                blogo()
                close()
                logoB()
                tmp()
                clear()
                blogo()
                close()
                logoC()
                tmp()
            except Exception as e:
                logger.debug("Loop interrupted: %s", e)
                break
    elif misce in ["B", "b"]:
        clear()
        blogo()
        close()
        sysinfoDetail()
    elif misce in ["C", "c"]:
        clear()
        blogo()
        datesConn()
    elif misce in ["D", "d"]:
        clear()
        blogo()
        quotesConn()
    elif misce in ["H", "h"]:
        clear()
        blogo()
        ex()
    elif misce in ["M", "m"]:
        subprocess.run(["printf", "\033[49m"])
        clear()
        subprocess.run(["printf", "\033[49m"])
        blogo()
        output = render("1st 𝕭𝐢𝐭𝐚𝐱𝐞 Block 853742", colors=['white'], align='center', font='console')
        print(output)
        createimagebitaxe()
        input("Continue...")
    elif misce in ["P", "p"]:
        clear()
        blogo()
        pgpConn()
    elif misce in ["S", "s"]:
        clear()
        blogo()
        satoshiConn()
    elif misce in ["X", "x"]:
        clear()
        blogo()
        allblocksConn()
    elif misce in ["SHS", "shs"]:
        clear()
        blogo()
        SHS()
    elif misce in ["R", "r"]:
        menuSelection()


def miscellaneousLOCALmenuOnchainONLY(misce):
    if misce in ["A", "a"]:
        while True:
            try:
                clear()
                blogo()
                close()
                logoA()
                tmp()
                clear()
                blogo()
                close()
                logoB()
                tmp()
                clear()
                blogo()
                close()
                logoC()
                tmp()
            except Exception as e:
                logger.debug("Loop interrupted: %s", e)
                break
    elif misce in ["B", "b"]:
        clear()
        blogo()
        close()
        sysinfoDetail()
    elif misce in ["D", "d"]:
        clear()
        blogo()
        quotesConn()
    elif misce in ["C", "c"]:
        clear()
        blogo()
        datesConn()
    elif misce in ["H", "h"]:
        clear()
        blogo()
        ex()
    elif misce in ["M", "m"]:
        subprocess.run(["printf", "\033[49m"])
        clear()
        subprocess.run(["printf", "\033[49m"])
        blogo()
        output = render("1st 𝕭𝐢𝐭𝐚𝐱𝐞 Block 853742", colors=['white'], align='center', font='console')
        print(output)
        createimagebitaxe()
        input("Continue...")
    elif misce in ["P", "p"]:
        clear()
        blogo()
        pgpConn()
    elif misce in ["S", "s"]:
        clear()
        blogo()
        satoshiConn()
    elif misce in ["X", "x"]:
        clear()
        blogo()
        allblocksConn()
    elif misce in ["SHS", "shs"]:
        clear()
        blogo()
        SHS()
    elif misce in ["R", "r"]:
        menuSelection()

def decodeHexLOCAL(hexloc):
    if hexloc in ["A", "a"]:
        clear()
        blogo()
        close()
        try:
            readHexBlock()
            while True:
                r = input("Do you want to continue decoding? Y/n: ")
                if r in ["Y", "y"]:
                    clear()
                    blogo()
                    readHexBlock()
                else:
                    break
        except Exception as e:
            show_error(str(e))
            logger.debug("Suppressed error: %s", e)
    elif hexloc in ["B", "b"]:
        clear()
        blogo()
        close()
        try:
            readHexTx()
            while True:
                r = input("Do you want to continue decoding? Y/n: ")
                if r not in ["Y", "y"]:
                    break
                clear()
                blogo()
                sysinfo()
                readHexTx()
        except Exception as e:
            show_error(str(e))
            logger.debug("Suppressed error: %s", e)

def decodeHexLOCALOnchainONLY(hexloc):
    if hexloc in ["A", "a"]:
        clear()
        blogo()
        close()
        try:
            readHexBlock()
            while True:
                r = input("Do you want to continue decoding? Y/n: ")
                if r in ["Y", "y"]:
                    clear()
                    blogo()
                    readHexBlock()
                else:
                    break
        except Exception as e:
            show_error(str(e))
            logger.debug("Suppressed error: %s", e)
    elif hexloc in ["B", "b"]:
        clear()
        blogo()
        close()
        try:
            readHexTx()
            while True:
                r = input("Do you want to continue decoding? Y/n: ")
                if r not in ["Y", "y"]:
                    break
                clear()
                blogo()
                sysinfo()
                readHexTx()
        except Exception as e:
            show_error(str(e))
            logger.debug("Suppressed error: %s", e)

def lightningnetworkLOCALcontrol(lncore):
    if lncore in ["A", "a"]:
        while True:
            try:
                clear()
                blogo()
                sysinfo()
                close()
                consoleLN()
                t.sleep(5)
            except Exception as e:
                logger.debug("Loop interrupted: %s", e)
                break
    elif lncore in ["B", "b"]:
        clear()
        blogo()
        localaddinvoice()
    elif lncore in ["C", "c"]:
        clear()
        blogo()
        localpayinvoice()
    elif lncore in ["D", "d"]:
        clear()
        blogo()
        localkeysend()
    elif lncore in ["E", "e"]:
        clear()
        blogo()
        localnewaddress()
    elif lncore in ["F", "f"]:
        clear()
        blogo()
        locallistinvoices()
    elif lncore in ["G", "g"]:
        clear()
        blogo()
        localchannelbalance()
    elif lncore in ["H", "h"]:
        clear()
        blogo()
        locallistchannels()
    elif lncore in ["I", "i"]:
        clear()
        blogo()
        localrebalancelnd()
    elif lncore in ["J", "j"]:
        clear()
        blogo()
        locallistpeersQQ()
    elif lncore in ["K", "k"]:
        clear()
        blogo()
        localconnectpeer()
    elif lncore in ["L", "l"]:
        clear()
        blogo()
        localbalanceOC()
    elif lncore in ["M", "m"]:
        clear()
        blogo()
        locallistchaintxns()
    elif lncore in ["N", "n"]:
        clear()
        blogo()
        localgetinfo()
    elif lncore in ["O", "o"]:
        clear()
        blogo()
        localgetnetworkinfo()
    elif lncore in ["P", "p"]:
        clear()
        blogo()
        chatConn()
    elif lncore in ["Z", "z"]:
        clear()
        blogo()
        stalnConn()
    elif lncore in ["T", "t"]:
        clear()
        blogo()
        ranConn()
    elif lncore in ["Q", "q"]:
        if os.path.isfile("lnbitSN.conf"):
            lnbitsLNURLwList()
    elif lncore in ["S", "s"]:
        if os.path.isfile("lnbitSN.conf"):
            lnbitsLNURLw()
    elif lncore in ["R", "r"]:
        menuSelection()

def chatConnA(menuch):
    if menuch in ["A", "a"]:
        pyCHATA()
    elif menuch in ["B", "b"]:
        pyCHATB()
    elif menuch in ["C", "c"]:
        pyCHATC()

def chatConnB(pyCHATA):
    if pyCHATA in ["A", "a"]:
        clear()
        blogo()
        localchatsendA()
    elif pyCHATA in ["B", "b"]:
        clear()
        blogo()
        localchatnewA()
    elif pyCHATA in ["C", "c"]:
        clear()
        blogo()
        localchatlistA()

def chatConnC(pyCHATB):
    if pyCHATB in ["A", "a"]:
        clear()
        blogo()
        localchatsendB()
    elif pyCHATB in ["B", "b"]:
        clear()
        blogo()
        localchatnewB()
    elif pyCHATB in ["C", "c"]:
        clear()
        blogo()
        localchatlistB()

def chatConnD(pyCHATC):
    if pyCHATC in ["A", "a"]:
        clear()
        blogo()
        localchatsendC()
    elif pyCHATC in ["B", "b"]:
        clear()
        blogo()
        localchatnewC()
    elif pyCHATC in ["C", "c"]:
        clear()
        blogo()
        localchatlistC()

def platfformsLOCALcontrol(platf):
    if platf in ["A", "a"]:
        aaccPPiTippinMe()
    elif platf in ["B", "b"]:
        aaccPPiTallyCo()
    elif platf in ["C", "c"]:
        mempoolmenu()
    elif platf in ["D", "d"]:
        clear()
        blogo()
        CoingeckoPP()
    elif platf in ["E", "e"]:
        rateSX()
    elif platf in ["F", "f"]:
        bwtConn()
    elif platf in ["G", "g"]:
        aaccPPiLNBits()
    elif platf in ["H", "h"]:
        aaccPPiLNPay()
    elif platf in ["I", "i"]:
        aaccPPiOpenNode()
    elif platf in ["J", "j"]:
        satnodeMenu()
    elif platf in ["K", "k"]:
        weatherMenu()
    elif platf in ["L", "l"]:
        gameroom()
    elif platf in ["M", "m"]:
        whalalConn()
    elif platf in ["N", "n"]:
        nostrConn()
    elif platf in ["Q", "q"]:
        OceanConn()
    elif platf in ["S", "s"]:
        slushpoolLOCALOnchainONLY()
    elif platf in ["T", "t"]:
        bip39convert()
    elif platf in ["U", "u"]:
        callGitUTXOracle()
    elif platf in ["W", "w"]:
        ckpoolpoolLOCALOnchainONLY()
    elif platf in ["Z", "z"]:
        pyblockpoolpoolLOCALOnchainONLY()
    elif platf in ["R", "r"]:
        menuSelection()

def platfformsLOCALcontrolOnchainONLY(platf):
    if platf in ["A", "a"]:
        aaccPPiTippin()
    elif platf in ["B", "b"]:
        aaccPPiTallyCo()
    elif platf in ["C", "c"]:
        mempoolmenuOnchainONLY()
    elif platf in ["D", "d"]:
        clear()
        blogo()
        CoingeckoPP()
    elif platf in ["E", "e"]:
        rateSXOncainONLY()
    elif platf in ["F", "f"]:
        bwtConn()
    elif platf in ["G", "g"]:
        aaccPPiLNBits()
    elif platf in ["H", "h"]:
        aaccPPiLNPay()
    elif platf in ["I", "i"]:
        aaccPPiOpenNode()
    elif platf in ["J", "j"]:
        satnodeMenuOnchainONLY()
    elif platf in ["K", "k"]:
        weatherMenuOnchainONLY()
    elif platf in ["L", "l"]:
        gameroom()
    elif platf in ["M", "m"]:
        whalalConn()
    elif platf in ["N", "n"]:
        nostrConn()
    elif platf in ["P", "p"]:
        PhoenixConn()
    elif platf in ["Q", "q"]:
        OceanConn()
    elif platf in ["R", "r"]:
        luxorstats()
    elif platf in ["S", "s"]:
        slushpoolLOCALOnchainONLY()
    elif platf in ["T", "t"]:
        bip39convert()
    elif platf in ["U", "u"]:
        callGitUTXOracle()
    elif platf in ["W", "w"]:
        ckpoolpoolLOCALOnchainONLY()
    elif platf in ["Z", "z"]:
        pyblockpoolpoolLOCALOnchainONLY()
    elif platf in ["R", "r"]:
        menuSelection()

def phoenixmenu(menunos):
    if menunos in ["A", "a"]:
        callPhoenixLin()
    elif menunos in ["B", "b"]:
        callPhoenixMacARM()
    elif menunos in ["C", "c"]:
        callPhoenixMacX64()
    elif menunos in ["D", "d"]:
        callPhoenixWin()
    elif menunos in ["E", "e"]:
        callPhoenix()
    elif menunos in ["F", "f"]:
        wallPhoenix()
    elif menunos in ["G", "g"]:
        wallPhoenixBOLT12()
    elif platf in ["R", "r"]:
        menuSelection()

def oceanMstats(menuunos):
    if menuunos in ["A", "a"]:
        oceanE()
    elif menuunos in ["B", "b"]:
        oceanH()
    elif menuunos in ["C", "c"]:
        oceanB()
    elif platf in ["R", "r"]:
        menuSelection()

def ckpool(menuch):
    if menuch in ["A", "a"]:
        ckpool()

def pyblockpool(menuchh):
    if menuchh in ["A", "a"]:
        pyblockpool()


def nostrmenu(menunos):
    if menunos in ["A", "a"]:
        callGitNostrLinTerminal()
    elif menunos in ["B", "b"]:
        callGitNostrLinarmTerminal()
    elif menunos in ["C", "c"]:
        callGitNostrMacTerminal()
    elif menunos in ["D", "d"]:
        nostrConn()
    elif menunos in ["E", "e"]:
        callGitNostrWinTerminal()
    elif menunos in ["S", "s"]:
        callGitNostrSeedTerminal()
    elif menunos in ["W", "w"]:
        callGitNostrQRSeedTerminal()
    elif menunos in ["Z", "z"]:
        callGitBija()

#----------------------------REMOTE MENUS

def mainmenuREMOTEcontrol(menuS): #Execution of the Main Menu options
    mainmenuControl(menuS, "remote")

def bitcoincoremenuREMOTEcontrol(bcore):
    if bcore in ["A", "a"]:
        while True:
            try:
                clear()
                blogo()
                sysinfo()
                close()
                remoteconsole()
                t.sleep(5)
            except Exception as e:
                logger.debug("Loop interrupted: %s", e)
                break
    elif bcore in ["B", "b"]:
        remotegetblockcount()
    elif bcore in ["C", "c"]:
        runTheNumbersMenuConn()
    elif bcore in ["D", "d"]:
        try:
            clear()
            blogo()
            sysinfo()
            close()
            decodeQR()
            input("Continue...")
        except Exception as e:
            show_error(str(e))
            logger.debug("Suppressed error: %s", e)
    elif bcore in ["E", "e"]:
        miscellaneousLOCAL()
    elif bcore in ["M", "m"]:
        mtConn()
    elif bcore in ["O", "o"]:
        bitcoincoremenuREMOTEOPRETURN()
    elif bcore in ["Z", "z"]:
        statsConn()
    elif bcore in ["Q", "q"]:
        miningConn()
    elif bcore in ["U", "u"]:
        untxsConn()
    elif bcore in ["ONM", "onm"]:
        OwnNodeMinerONCHAIN()
    elif bcore in ["VG", "vg"]:
        clear()
        blogo()
        output = render("Vanity Generator", colors=['yellow'], align='left', font='tiny')
        print(output)
        subprocess.run(["python3", "PyVanityGenerator.py"], cwd="SPV")
        input("\a\nContinue...")

def bitcoincoremenuREMOTEcontrolO(oreturn):
    if oreturn in ["A", "a"]:
        clear()
        blogo()
        opreturn()
    elif oreturn in ["B", "b"]:
        clear()
        blogo()
        opreturn_view()
    elif oreturn in ["C", "c"]:
        clear()
        blogo()
        opretminer()

def lightningnetworkREMOTEcontrol(lncore):
    if lncore in ["A", "a"]:
        clear()
        blogo()
        getnewinvoice()
    elif lncore in ["B", "b"]:
        clear()
        blogo()
        payinvoice()
    elif lncore in ["C", "c"]:
        clear()
        blogo()
        getnewaddress()
    elif lncore in ["D", "d"]:
        clear()
        blogo()
        listinvoice()
    elif lncore in ["E", "e"]:
        clear()
        blogo()
        channelbalance()
    elif lncore in ["F", "f"]:
        clear()
        blogo()
        channels()
    elif lncore in ["G", "g"]:
        clear()
        blogo()
        balanceOC()
    elif lncore in ["H", "h"]:
        clear()
        blogo()
        listonchaintxs()
    elif lncore in ["I", "i"]:
        clear()
        blogo()
        getinfo()
    elif lncore in ["Z", "z"]:
        clear()
        blogo()
        stalnConn()
    elif lncore in ["T", "t"]:
        clear()
        blogo()
        ranConn()
    elif lncore in ["Q", "q"]:
        if os.path.isfile("lnbitSN.conf"):
            lnbitsLNURLwList()
    elif lncore in ["S", "s"]:
        if os.path.isfile("lnbitSN.conf"):
            lnbitsLNURLw()
    elif lncore in ["R", "r"]:
        menuSelection()

def menuC(menuO): # Donation access Menu
    if menuO in ["A", "a"]:
        dntDev()
    elif menuO in ["B", "b"]:
        dntTst()
    elif menuO in ["R", "r"]:
        menuSelection()

def menuCOnchainONLY(menuO): # Donation access Menu
    if menuO in ["A", "a"]:
        dntDevOnchainONLY()
    elif menuO in ["B", "b"]:
        dntTstOnchainONLY()
    elif menuO in ["R", "r"]:
        menuSelection()

def menuD(menuN): # Satnode access Menu
    if menuN in ["A", "a"]:
        satnode()
    elif menuN in ["B", "b"]:
        readFile()
    elif menuN in ["S", "s"]:
        try:
            clear()
            blogo()
            close()
            message = input("\n\033[0;37;40mYour message it's a \033[1;34;40mF\033[0;37;40mile or a plain \033[1;32;40mT\033[0;37;40mext? \033[1;34;40mF\033[0;37;40m/\033[1;32;40mT\033[0;37;40m: ")
            if message in ["F", "f"]:
                try:
                    clear()
                    blogo()
                    close()
                    apisenderFile()
                    t.sleep(30)
                    menuSelection()
                except Exception as e:
                    logger.debug("Menu error: %s", e)
                    menuSelection()
            elif message in ["T", "t"]:
                try:
                    clear()
                    blogo()
                    close()
                    apisender()
                    t.sleep(30)
                    menuSelection()
                except Exception as e:
                    logger.debug("Menu error: %s", e)
                    menuSelection()
        except Exception as e:
            logger.debug("Menu error: %s", e)
            menuSelection()
    elif menuN in ["C", "c"]:
        try:
            print("\n\t This only will work on Linux or Unix systems.\n")
            a = input("Do we continue? Y/n: ")
            if a in ["Y", "y"]:
                gitclone()
            else:
                menuSelection()
        except Exception as e:
            show_error(str(e))
            logger.debug("Suppressed error: %s", e)
    elif menuN in ["R", "r"]:
        menuSelection()

def menuE(menuQ): # Dev Donation access Menu
    if menuQ in ["A", "a"]:
        try:
            clear()
            blogo()
            close()
            donationPayNym()
            t.sleep(50)
            menuSelection()
        except Exception as e:
            logger.debug("Menu error: %s", e)
            menuSelection()
    elif menuQ in ["B", "b"]:
        try:
            clear()
            blogo()
            close()
            donationAddr()
            t.sleep(50)
            menuSelection()
        except Exception as e:
            logger.debug("Menu error: %s", e)
            menuSelection()
    elif menuQ in ["C", "c"]:
        try:
            clear()
            blogo()
            close()
            donationLN()
            t.sleep(50)
            menuSelection()
        except Exception as e:
            logger.debug("Menu error: %s", e)
            menuSelection()
    elif menuQ in ["R", "r"]:
        menuSelection()

def menuEOnchainONLY(menuQ): # Dev Donation access Menu
    if menuQ in ["A", "a"]:
        try:
            clear()
            blogo()
            close()
            donationPayNym()
            t.sleep(50)
            menuSelection()
        except Exception as e:
            logger.debug("Menu error: %s", e)
            menuSelection()
    elif menuQ in ["B", "b"]:
        try:
            clear()
            blogo()
            close()
            donationAddr()
            t.sleep(50)
            menuSelection()
        except Exception as e:
            logger.debug("Menu error: %s", e)
            menuSelection()
    elif menuQ in ["C", "c"]:
        try:
            clear()
            blogo()
            close()
            donationLN()
            t.sleep(50)
            menuSelection()
        except Exception as e:
            logger.debug("Menu error: %s", e)
            menuSelection()
    elif menuQ in ["R", "r"]:
        menuSelection()

def menuF(menuV): # Tester Donation access Menu
    if menuV in ["A", "a"]:
        try:
            clear()
            blogo()
            close()
            donationAddrTst()
            t.sleep(50)
            menuSelection()
        except Exception as e:
            logger.debug("Menu error: %s", e)
            menuSelection()
    elif menuV in ["B", "b"]:
        try:
            clear()
            blogo()
            close()
            donationLNTst()
            t.sleep(50)
            menuSelection()
        except Exception as e:
            logger.debug("Menu error: %s", e)
            menuSelection()
    elif menuV in ["R", "r"]:
        menuSelection()

def menuFOnchainONLY(menuV): # Tester Donation access Menu
    if menuV in ["A", "a"]:
        try:
            clear()
            blogo()
            close()
            donationAddrTst()
            t.sleep(50)
            menuSelection()
        except Exception as e:
            logger.debug("Menu error: %s", e)
            menuSelection()
    elif menuV in ["B", "b"]:
        try:
            clear()
            blogo()
            close()
            donationLNTst()
            t.sleep(50)
            menuSelection()
        except Exception as e:
            logger.debug("Menu error: %s", e)
            menuSelection()
    elif menuV in ["R", "r"]:
        menuSelection()
#---------------------------------------------------------------------------------

def nostrConn():
    clear()
    blogo()
    sysinfo()

    if path['bitcoincli']:
        n = "Local" if path['bitcoincli'] else "Remote"
        bitcoincli = " getblockchaininfo"
        a = subprocess.run([path['bitcoincli']] + bitcoincli.split(), capture_output=True, text=True).stdout
        b = json.loads(a)
        d = b
    else:
        a = "Local" if path['bitcoincli'] else "Remote"
        blk = rpc('getblockchaininfo')
        d = blk

    print("""\t\t
    \033[1;37;40m{}\033[0;37;40m: \033[1;31;40mPyBLOCK\033[0;37;40m
    \033[1;37;40mBlock\033[0;37;40m: \033[1;32;40m{}\033[0;37;40m
    \033[1;37;40mVersion\033[0;37;40m: {}

    \033[1;32;40mA.\033[0;37;40m Linux   x64
    \033[1;32;40mB.\033[0;37;40m Linux   arm64
    \033[1;32;40mC.\033[0;37;40m Mac     x64
    \033[1;32;40mD.\033[0;37;40m Mac     arm64 (SOON)
    \033[1;32;40mE.\033[0;37;40m Windows
    \033[1;32;40mS.\033[0;37;40m Bip39
    \033[1;32;40mW.\033[0;37;40m QR
    \033[1;32;40mZ.\033[0;37;40m Bija
    \u001b[31;1mR.\033[0;37;40m Return
    \n\n\x1b[?25h""".format(n if path['bitcoincli'] else a, d['blocks'], version ()))
    nostrmenu(input("\033[1;32;40mSelect option: \033[0;37;40m"))


def testClockRemote():
    b = rpc('getblockcount')
    c = str(b)
    a = c
    output = render(str(c), colors=[settingsClock['colorA'], settingsClock['colorB']], align='left')
    print(output)
    print("""

    -------------------------
        Front Color: {}
        Back Color:  {}
    -------------------------

    """.format(settingsClock['colorA'], settingsClock['colorB']))
    try:
        print("<<< Cancel Control + C")
        input("Enter To Apply...")
        settingsClock["gradient"] = "color"
        with open("pyblocksettingsClock.conf", "w") as f: json.dump(settingsClock, f, indent=2)
    except Exception as e:
        show_error(str(e))
        logger.debug("Suppressed error: %s", e)


def commandsINIT(initCONF):
    intCONF = {"fullbtclnd":"","fullbtc":"","cropped":""}

    if not os.path.isdir("config"):
        os.makedirs("config", exist_ok=True)

    if os.path.isfile('config/intro.conf'):
        intro = json.load(open("config/intro.conf", "r"))
        initCONF = intro
        if initCONF['fullbtclnd']:
            fullbtclnd()
        elif initCONF['fullbtc']:
            fullbtc()
        elif initCONF['cropped']:
            cropped()
    else:
        if initCONF in ["A", "a"]:
            initDATA = "A"
            intCONF['fullbtclnd'] = initDATA
            initPATH = intCONF['fullbtclnd']
            with open("config/intro.conf", "w") as f: json.dump(initPATH, f, indent=2)
            clear()
            fullbtclnd()
        elif initCONF in ["B", "b"]:
            initDATA = "B"
            intCONF['fullbtc'] = initDATA
            initPATH = intCONF['fullbtc']
            with open("config/intro.conf", "w") as f: json.dump(initPATH, f, indent=2)
            clear()
            fullbtc()
        elif initCONF in ["C", "c"]:
            initDATA = "C"
            intCONF['cropped'] = initDATA
            initPATH = intCONF['cropped']
            with open("config/intro.conf", "w") as f: json.dump(initPATH, f, indent=2)
            clear()
            menuSelection()

    restart_script()

def restart_script():
    clear()
    blogo()
    print("Restarting PyBlock...")
    os.execv(sys.executable, ['python'] + sys.argv)

def fullbtc():
    path = {"ip_port":"", "rpcuser":"", "rpcpass":"", "bitcoincli":""}
    if not os.path.isdir("config"):
        os.makedirs("config", exist_ok=True)

    if os.path.isfile('config/bclock.conf') or os.path.isfile('config/blnclock.conf'): # Check if the file 'bclock.conf' is in the same folder
        pathv = json.load(open("config/bclock.conf", "r")) # Load the file 'bclock.conf'
        path = pathv # Copy the variable pathv to 'path'
    else:
        blogo()
        print("Welcome to \033[1;31;40mPyBLOCK\033[0;37;40m\n\n")
        print("\n\tIf you are going to use your local node leave IP:PORT/USER/PASSWORD in 𝗕𝗟𝗔𝗡𝗞.\n")
        path['ip_port'] = "http://{}".format(input("Insert IP:PORT to access your remote Bitcoin-Cli node: "))
        path['rpcuser'] = input("RPC User: ")
        path['rpcpass'] = input("RPC Password: ")
        print("\n\tLocal Bitcoin Core Node connection.\n")
        path['bitcoincli']= input("Insert the Path to Bitcoin-Cli. Normally you just need to type 𝙗𝙞𝙩𝙘𝙤𝙞𝙣-𝙘𝙡𝙞: ")
        with open("config/bclock.conf", "w") as f: json.dump(path, f, indent=2)
    menuSelection()

def fullbtclnd():
    path = {"ip_port":"", "rpcuser":"", "rpcpass":"", "bitcoincli":""}
    lndconnectload = {"ip_port":"", "tls":"", "macaroon":"", "ln":""}
    if not os.path.isdir("config"):
        os.makedirs("config", exist_ok=True)

    if os.path.isfile('config/bclock.conf') or os.path.isfile('config/blnclock.conf'): # Check if the file 'bclock.conf' is in the same folder
        pathv = json.load(open("config/bclock.conf", "r")) # Load the file 'bclock.conf'
        path = pathv # Copy the variable pathv to 'path'
    else:
        blogo()
        print("Welcome to \033[1;31;40mPyBLOCK\033[0;37;40m\n\n")
        print("\n\tIf you are going to use your local node leave IP:PORT/USER/PASSWORD in 𝗕𝗟𝗔𝗡𝗞.\n")
        path['ip_port'] = "http://{}".format(input("Insert IP:PORT to access your remote Bitcoin-Cli node: "))
        path['rpcuser'] = input("RPC User: ")
        path['rpcpass'] = input("RPC Password: ")
        print("\n\tLocal Bitcoin Core Node connection.\n")
        path['bitcoincli']= input("Insert the Path to Bitcoin-Cli. Normally you just need to type 𝙗𝙞𝙩𝙘𝙤𝙞𝙣-𝙘𝙡𝙞: ")
        with open("config/bclock.conf", "w") as f: json.dump(path, f, indent=2)

    if os.path.isfile('config/blndconnect.conf'):
        lndconnectData= json.load(open("config/blndconnect.conf", "r"))
        lndconnectload = lndconnectData # Copy the variable pathv to 'path'
    else:
        clear()
        blogo()
        if os.path.isfile('config/init.conf'):
            pqr = json.load(open("config/init.conf", "r"))
            yesno = pqr
        else:
            yesno = input("You are going to 𝐜𝐨𝐧𝐧𝐞𝐜𝐭 your 𝐋𝐢𝐠𝐡𝐭𝐧𝐢𝐧𝐠 𝐍𝐨𝐝𝐞, type 𝐘𝐞𝐬 to continue: ")
            with open("config/init.conf", "w") as f: json.dump(yesno, f, indent=2)
            if yesno in ["YES", "yes", "yES", "yeS", "Yes", "YEs"]:
                print("\n\tIf you are going to use your local node leave IP:PORT/CERT/MACAROONS in 𝗕𝗟𝗔𝗡𝗞.\n")
                lndconnectload["ip_port"] = input("Insert IP:PORT to your node: ")
                lndconnectload["tls"] = input("Insert the path to tls.cert file: ")
                lndconnectload["macaroon"] = input("Insert the path to admin.macaroon: ")
                print("\n\tLocal Lightning Node connection.\n")
                lndconnectload["ln"] = input("Insert the Path to Lncli. Normally you just need to type 𝙡𝙣𝙘𝙡𝙞: ")
                with open("config/blndconnect.conf", "w") as f: json.dump(lndconnectload, f, indent=2)
    menuSelection()


def introINIT():
    if not os.path.isdir("config"):
        os.makedirs("config", exist_ok=True)
    clear()
    blogo()
    #sysinfo()
    print("""\t\t
    Welcome 𝓒𝔂𝓹𝓱𝓮𝓻𝓹𝓾𝓷𝓴.

    Connect 𝗣𝘆𝗕𝗟Ø𝗖𝗞 to your Nodes or Run Lite Mode (no node required).


    \u001b[31;1mA.\033[0;37;40m 𝗣𝘆𝗕𝗟Ø𝗖𝗞 (Bitcoin & Lightning)
    \u001b[38;5;202mB.\033[0;37;40m 𝗣𝘆𝗕𝗟Ø𝗖𝗞 (Bitcoin)
    \u001b[33;1mC.\033[0;37;40m 𝗣𝘆𝗕𝗟Ø𝗖𝗞 (Lite Mode)
    \n\n\x1b[?25h""")
    commandsINIT(input("\033[1;32;40mSelect option: \033[0;37;40m"))

#--------------------------------- End Main Menu execution --------------------------------

def main():
    global settings, settingsClock, path, lndconnectload
    cfg.load()
    settings = cfg.settings
    settingsClock = cfg.settings_clock
    while True:
        try:
            path = cfg.path
            lndconnectload = cfg.lndconnectload
            clear()
            if not cfg.has_config('intro.conf'):
                set_terminal_background()
                introINIT()
            else:
                set_terminal_background()
                menuSelection()
        except KeyboardInterrupt:
            continue  # Ctrl+C returns to main menu
        except Exception as e:
            show_error(str(e))
            logger.error("Fatal error: %s", e)
            sys.exit(101)

if __name__ == "__main__":
    if "--tui" in sys.argv:
        from tui.app import run as run_tui
        mode = "lite"
        cfg.load()
        if cfg.has_config('intro.conf'):
            init_data = cfg.intro_mode
            if isinstance(init_data, str):
                if init_data == "A":
                    mode = "local"
                elif init_data == "B":
                    mode = "onchain_only"
            elif isinstance(init_data, dict):
                if init_data.get("fullbtclnd"):
                    mode = "local"
                elif init_data.get("fullbtc"):
                    mode = "onchain_only"
        run_tui(mode=mode)
    else:
        main()
