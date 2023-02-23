#Developer: Curly60e
#Tester: __B__T__C__
#ℙ𝕪𝔹𝕃𝕆ℂ𝕂 𝕚𝕥𝕤 𝕒 𝔹𝕚𝕥𝕔𝕠𝕚𝕟 𝔻𝕒𝕤𝕙𝕓𝕠𝕒𝕣𝕕 𝕨𝕚𝕥𝕙 ℂ𝕪𝕡𝕙𝕖𝕣𝕡𝕦𝕟𝕜 𝕒𝕖𝕤𝕥𝕙𝕖𝕥𝕚𝕔.

import os
import os.path
import time as t
import pickle
import psutil
import html2text
import jq
import qrcode
import random
import xmltodict
import sys
import subprocess
import requests
import json
import simplejson as json
import numpy as np
from SPV.spvblock import *
from cfonts import render, say
from clone import *
from donation import *
from feed import *
from art import *
from logos import *
from sysinf import *
from pblogo import *
from apisnd import *
from ppi import *
from termcolor import colored, cprint
from nodeconnection import *
from terminal_matrix.matrix import *
from PIL import Image
from robohash import Robohash
from binascii import unhexlify
from embit import bip39
from embit.wordlists.bip39 import WORDLIST
from io import StringIO


version = "2.0.16"

def close():
    print("<<< Ctrl + C.\n\n")

def sysinfo():  #Cpu and memory usage
    print("    \033[0;37;40m----------------------")
    print("    \033[3;33;40mCPU Usage: \033[1;32;40m" + str(psutil.cpu_percent()) + "%\033[0;37;40m")
    print(
        f"    \033[3;33;40mMemory Usage: \033[1;32;40m{int(psutil.virtual_memory().percent)}% \033[0;37;40m"
    )

    print("    \033[0;37;40m----------------------")

def rectangle(n):
    x = n - 3
    y = n - x
    [
        print(''.join(i))
        for i in
        (
            ''*x
            if i in (0,y-1)
            else
            (
                f'{""*n}{"|"*n}{""*n}'
                if i >= (n+1)/2 and i <= (1*n)/2
                else
                f'\u001b[38;5;27m{"█"*(x-1)}'
            )
            for i in range(y)
        )
    ]

def rpc(method, params=[]):
    payload = json.dumps({
        "jsonrpc": "2.0",
        "id": "minebet",
        "method": method,
        "params": params
    })
    path = {"ip_port":"", "rpcuser":"", "rpcpass":"", "bitcoincli":""}
    if os.path.isfile('config/bclock.conf'): # Check if the file 'bclock.conf' is in the same folder
        pathv = pickle.load(open("config/bclock.conf", "rb")) # Load the file 'bclock.conf'
        path = pathv # Copy the variable pathv to 'path'
    return requests.post(path['ip_port'], auth=(path['rpcuser'], path['rpcpass']), data=payload).json()['result']

def pathexec():
    global path
    path = {"ip_port":"", "rpcuser":"", "rpcpass":"", "bitcoincli":""}
    pathv = pickle.load(open("config/bclock.conf", "rb")) # Load the file 'bclock.conf'
    path = pathv # Copy the variable pathv to 'path'

def lndconnectexec():
    global lndconnectload
    lndconnectData = pickle.load(open("config/blndconnect.conf", "rb")) # Load the file 'bclock.conf'
    lndconnectload = lndconnectData # Copy the variable pathv to 'path'
#-----------------------------Slush--------------------------------

def counttxs():
    try:
        bitcoinclient = f'{path["bitcoincli"]} getblockcount'
        block = os.popen(str(bitcoinclient)).read() # 'getblockcount' convert to string
        b = block
        a = b
        pathexec()
        clear()
        getrawmempool = " getrawmempool"
        gna = os.popen(path['bitcoincli'] + getrawmempool)
        gnaa = gna.read()
        gna1 = str(gnaa)
        d = json.loads(gna1)
        e = len(d)
        n = e / 10
        nn = n
        getrawmempool = " getrawmempool"
        while True:
            x = a
            bitcoinclient = f'{path["bitcoincli"]} getblockcount'
            block = os.popen(str(bitcoinclient)).read() # 'getblockcount' convert to string
            b = block
            pathexec()
            gna = os.popen(path['bitcoincli'] + getrawmempool)
            gnaa = gna.read()
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
                bb = os.popen(str(bitcoinclient)).read()
                ll = bb
                bitcoinclientgetblock = f'{path["bitcoincli"]} getblock {ll}'
                qq = os.popen(bitcoinclientgetblock).read()
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
                        p = subprocess.Popen(['curl', 'https://poptart.spinda.net'])
                        p.wait(5)
                    except subprocess.TimeoutExpired:
                        p.kill()
                print("\033[0;37;40m\x1b[?25l")
                clear()
                a = b
                nn = e
    except:
        pass

def slDIFFConn():
    try:
        conn = """curl -s https://insights.braiins.com/api/v1.0/difficulty-stats"""
        a = os.popen(conn).read()
        clear()
        blogo()
        closed()
        output = render("difficulty", colors=['yellow'], align='left', font='tiny')
        print(output)
        b = json.loads(a)
        print(f"""\n

            Block epoch: {b['blocks_epoch']}
            Difficulty: {b['difficulty']}
            Epoch block time: {b['epoch_block_time']}
            Estimated adjustment: {b['estimated_adjustment']}
            Estimated adjustemnt date: {b['estimated_adjustment_date']}
            Estimated next differece: {b['estimated_next_diff']}
            Previous adjustment: {b['previous_adjustment']}

        """)
        input("\a\nContinue...")
    except:
        pass

def slHASHConn():
    try:
        conn = """curl -s https://insights.braiins.com/api/v1.0/hash-rate-stats"""
        a = os.popen(conn).read()
        clear()
        blogo()
        closed()
        output = render("hash rate", colors=['yellow'], align='left', font='tiny')
        print(output)
        b = json.loads(a)
        print(f"""\n

            Averiage fees per block: {b['avg_fees_per_block']}
            Current hashrate: {b['current_hashrate']}
            Fees percent: {b['fees_percent']}
            Hash price: {b['hash_price']}
            Hash rate 30: {b['hash_rate_30']}
            Hash value: {b['hash_value']}
            Rev. USD: {b['rev_usd']}

        """)
        input("\a\nContinue...")
    except:
        pass

def slPOOLConn():
    try:
        conn = """curl -s https://insights.braiins.com/api/v1.0/pool-stats?json=1 | jq -C '.[]' | tr -d '{|}|]|,' | xargs -L 1 | grep -E " " """
        a = os.popen(conn).read()
        clear()
        blogo()
        closed()
        output = render("pool", colors=['yellow'], align='left', font='tiny')
        print(output)
        print(a)
        input("\a\nContinue...")
    except:
        pass

def slHISTConn():
    try:
        conn = """curl -s https://insights.braiins.com/api/v1.0/hashrate-and-difficulty-history?json=1 | jq -C '.[]' | tr -d '{|}|]|,' | xargs -L 1 | grep -E " " """
        a = os.popen(conn).read()
        clear()
        blogo()
        closed()
        output = render("history", colors=['yellow'], align='left', font='tiny')
        print(output)
        print(a)
        input("\a\nContinue...")
    except:
        pass

def getPoolSlushCheck():

    s = ""
    sq = s

    api = ""
    try:
        if os.path.isfile("config/slushAPI.conf"):
            apiv = pickle.load(open("config/slushAPI.conf", "rb"))
            api = apiv
        else:
            clear()
            blogo()
            api = input("Insert Slush API KEY: ")
            pickle.dump(api, open("config/slushAPI.conf", "wb"))
    except:
        pass

    while True:
        try:
            slushpoolbtc = f"curl https://slushpool.com/accounts/profile/json/btc/ -H 'SlushPool-Auth-Token: {api}' 2>/dev/null"

            slushpoolbtcblock = f"curl https://slushpool.com/stats/json/btc/ -H 'SlushPool-Auth-Token: {api}' 2>/dev/null"


            b = os.popen(slushpoolbtc)
            c = b.read()
            d = json.loads(c)
            f = d['btc']

            bblock = os.popen(slushpoolbtcblock)
            cblock = bblock.read()
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
                        Confirmed reward: \u001b[38;5;40m{}\033[0;37;40m BTC
                        Unconfirmed reward: \u001b[33;1m{}\033[0;37;40m BTC
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

            \033[A""".format(d['username'], f['confirmed_reward'], f['unconfirmed_reward'], f['estimated_reward'], f['all_time_reward'], f['hash_rate_5m'], f['hash_rate_60m'], f['hash_rate_24h'], f['hash_rate_scoring'], f['hash_rate_yesterday'], f['ok_workers'], f['off_workers'],newblock))

            t.sleep(10)

        except:
            break


#-----------------------------END Slush--------------------------------

def ckpoolpoolLOCALOnchainONLY():

    s = ""
    sq = s

    api = ""
    try:
        if os.path.isfile("config/CKPOOLAPI.conf"):
            apiv = pickle.load(open("config/CKPOOLAPI.conf", "rb"))
            api = apiv
        else:
            clear()
            blogo()
            api = input("Insert CKPool Wallet.Worker: ")
            pickle.dump(api, open("config/CKPOOLAPI.conf", "wb"))
    except:
        pass

    while True:
        try:
            ckpool = f"curl https://solo.ckpool.org/users/{api} 2>/dev/null"


            b = os.popen(ckpool)
            c = b.read()
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

        except:
            break

def getblock(): # get access to bitcoin-cli with the command getblockchaininfo
    while True:
        try:
            bitcoincli = " getblockchaininfo"
            a = os.popen(path['bitcoincli'] + bitcoincli).read()
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
        except:
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
            gnt = os.popen(path['bitcoincli'] + gettxout + tx + " 1")
            gnta = gnt.read()
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
    except:
        pass

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
            gna = os.popen(path['bitcoincli'] + getrawmempool)
            gnaa = gna.read()
            gna1 = str(gnaa)
            d = json.loads(gna1)
            getrawtrans = " getrawtransaction "
            for b in d:
                n = "".join(map(str, b))
                m = getrawtrans + n + " 1"
                gnb = os.popen(path['bitcoincli'] + m)
                gnba = gnb.read()
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
                        os.system(decodeTX)
                input("\n\033[?25l\033[0;37;40m\n\033[AContinue...\033[A")
    except:
        pass

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
        gna = os.popen(path['bitcoincli'] + getadd)
        gnaa = gna.read()
        gna1 = str(gnaa)
        gnb = os.popen(path['bitcoincli'] + getbal)
        gnbb= gnb.read()
        gnb1 = str(gnbb)
        gnu = os.popen(path['bitcoincli'] + getunconfirm)
        gnua= gnu.read()
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
            gnb = os.popen(path['bitcoincli'] + getbal)
            gnbb= gnb.read()
            gnb1 = str(gnbb)
            gnaq = os.popen(path['bitcoincli'] + getfeemempool)
            gnaaq = gnaq.read()
            gna1q = str(gnaaq)
            gnu = os.popen(path['bitcoincli'] + getunconfirm)
            gnua= gnu.read()
            gnub = str(gnua)
            d = json.loads(gna1q)
            if gnub > a or gnb1 > b:
                clear()
                blogo()
                close()
                getadd = " getnewaddress"
                gna = os.popen(path['bitcoincli'] + getadd)
                gnaa = gna.read()
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
                gnaq = os.popen(path['bitcoincli'] + getfeemempool)
                gnaaq = gnaq.read()
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
    except:
        walletmenuLOCALOnchainONLY()

def gettransactionsOnchain():
    try:
        listtxs = " listunspent"
        while True:
            clear()
            blogo()
            close()
            gna = os.popen(path['bitcoincli'] + listtxs)
            gnaa = gna.read()
            gna1 = str(gnaa)
            d = json.loads(gna1)
            gnb = os.popen(path['bitcoincli'] + " getbalance")
            gnbb= gnb.read()
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
    except:
        walletmenuLOCALOnchainONLY()

def dumppk(): #
    try:
        clear()
        blogo()
        output = render("Dumpprivkey", colors=['yellow'], align='left', font='tiny')
        print(output)
        responseC = input("Bitcoin Address: ")
        bitcoincli = " dumpprivkey"
        os.system(path['bitcoincli'] + bitcoincli + f"{responseC}")
        input("\a\nContinue...")
    except:
        walletmenuLOCALOnchainONLY()

def wallmenu(): #
    try:
        clear()
        blogo()
        output = render("Your Wallet info", colors=['yellow'], align='left', font='tiny')
        print(output)
        bitcoincli = " getwalletinfo"
        os.system(path['bitcoincli'] + bitcoincli)
        input("\a\nContinue...")
    except:
        walletmenuLOCALOnchainONLY()
        
def inffmenu(): #
    try:
        clear()
        blogo()
        output = render("Address info", colors=['yellow'], align='left', font='tiny')
        print(output)
        responseC = input("Bitcoin Address: ")
        bitcoincli = " getaddressinfo"
        os.system(path['bitcoincli'] + bitcoincli + f"{responseC}")
        input("\a\nContinue...")
    except:
        walletmenuLOCALOnchainONLY()

def miningmenu(): #
    try:
        clear()
        blogo()
        output = render("Minning info", colors=['yellow'], align='left', font='tiny')
        print(output)
        bitcoincli = " getmininginfo"
        os.system(path['bitcoincli'] + bitcoincli)
        input("\a\nContinue...")
    except:
        walletmenuLOCALOnchainONLY()

def getblockcount(): # get access to bitcoin-cli with the command getblockcount
    bitcoincli = " getblockcount"
    os.system(path['bitcoincli'] + bitcoincli)

def getbestblockhash(): # get access to bitcoin-cli with the command getblockcount
    bitcoincli = " getbestblockhash"
    os.system(path['bitcoincli'] + bitcoincli)

def clear(): # clear the screen
    os.system('cls' if os.name=='nt' else 'clear')

def getgenesis(): # get and decode Genesis block
    output = render("genesis", colors=['yellow'], align='left', font='tiny')
    print(output)
    bitcoincli = " getblock 000000000019d6689c085ae165831e934ff763ae46a2a6c172b3f1b60a8ce26f 0 | xxd -r -p | hexyl -n 256"
    os.system(path['bitcoincli'] + bitcoincli)

def readHexBlock(): # Hex Decoder using Hexyl on local node
    hexa = input("Add the Block Hash you want to decode: ")
    blocknumber = input("Add the Block number: ")
    decodeBlock = (
        path['bitcoincli']
        + f" getblock {hexa} {blocknumber}"
        + " | xxd -r -p | hexyl -n 256"
    )

    os.system(decodeBlock)

def readHexTx(): # Hex Decoder using Hexyl on an external node
    hexa = input("Add the Transaction ID. you want to decode: ")
    decodeTX = (
        path['bitcoincli']
        + f" getrawtransaction {hexa}"
        + " | xxd -r -p | hexyl -n 256"
    )

    os.system(decodeTX)

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
        lsd = os.popen(f'{path["bitcoincli"]} {cle}')
        lsd0 = lsd.read()
        lsd1 = str(lsd0)
        print(lsd1)
        lsd.close()

def screensv():
    try:
        doit()
    except (KeyboardInterrupt, SystemExit):
        matrix.close()
        clear()
        blogo()
        menu()

def delay_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.25)
#------------------------------------------------------

def artist(): # here we convert the result of the command 'getblockcount' on a random art design
    while True:
        try:
            clear()
            close()
            design()
        except:
            break

def design():
    if os.path.isfile('config/pyblocksettingsClock.conf') or os.path.isfile('config/pyblocksettingsClock.conf'): # Check if the file 'bclock.conf' is in the same folder
        settingsv = pickle.load(open("config/pyblocksettingsClock.conf", "rb")) # Load the file 'bclock.conf'
        settingsClock = settingsv # Copy the variable pathv to 'path'
    else:
        settingsClock = {"gradient":"", "design":"block", "colorA":"green", "colorB":"yellow"}
        pickle.dump(settingsClock, open("config/pyblocksettingsClock.conf", "wb"))
    bitcoinclient = f'{path["bitcoincli"]} getblockcount'
    block = os.popen(str(bitcoinclient)).read() # 'getblockcount' convert to string
    b = block
    a = b
    output = render(str(b), colors=[settingsClock['colorA'], settingsClock['colorB']], align='center')
    print("\033[0;37;40m\x1b[?25l" + output)
    while True:
        x = a
        bitcoinclient = f'{path["bitcoincli"]} getblockcount'
        block = os.popen(str(bitcoinclient)).read() # 'getblockcount' convert to string
        b = block
        if b > a:
            clear()
            close()
            output = render(str(b), colors=[settingsClock['colorA'], settingsClock['colorB']], align='center')
            print("\a\x1b[?25l" + output)
            bitcoinclient = f'{path["bitcoincli"]} getbestblockhash'
            bb = os.popen(str(bitcoinclient)).read()
            ll = bb
            bitcoinclientgetblock = f'{path["bitcoincli"]} getblock {ll}'
            qq = os.popen(bitcoinclientgetblock).read()
            yy = json.loads(qq)
            mm = yy
            outputsize = render(str(mm['size']) + " bytes", colors=[settingsClock['colorA'], settingsClock['colorB']], align='center', font='tiny')
            print("\x1b[?25l" + outputsize)
            outputtxs = render(str(mm['nTx']) + " txs", colors=[settingsClock['colorA'], settingsClock['colorB']], align='center', font='tiny')
            print("\x1b[?25l" + outputtxs)
            sh = int(mm['nTx']) / 4
            shq = int(sh)
            ss = str(rectangle(shq))
            print(ss.replace("None",""))
            t.sleep(10)
            txs = str(mm['nTx'])
            if txs == "1":
                try:
                    p = subprocess.Popen(['curl', 'https://poptart.spinda.net'])
                    p.wait(5)
                except subprocess.TimeoutExpired:
                    p.kill()
            print("\033[0;37;40m\x1b[?25l")
            clear()
            close()
            a = b
            output = render(str(b), colors=[settingsClock['colorA'], settingsClock['colorB']], align='center')
            print("\x1b[?25l" + output)


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
                lsd = os.popen(path['bitcoincli'] + bitcoincli + tx + " 1")
                lsd0 = lsd.read()
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
        except:
            break

def runthenumbers():
    bitcoincli = " gettxoutsetinfo"
    os.system(path['bitcoincli'] + bitcoincli)
    input("\nContinue...")

def countdownblock():
    bitcoinclient = f'{path["bitcoincli"]} getblockcount'
    block = os.popen(str(bitcoinclient)).read() # 'getblockcount' convert to string
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
                block = os.popen(str(bitcoinclient)).read() # 'getblockcount' convert to string
                b = block
                if a == b:
                    break
                elif n != int(b):
                    print("CountDown: ", b)
                    q = int(a) - int(b)
                    print(f'Remaining: {str(q)}' + " Blocks\n")
                    n = int(b)
            except:
                break
        print(f'#RunTheNumbers {str(a)} PyBLOCK')
        input("\nContinue...")
    except:
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
            except:
                break
        print(f'#RunTheNumbers {a} PyBLOCK')
        input("\nContinue...")
    except:
        menuSelection()


def localHalving():
    bitcoinclient = f'{path["bitcoincli"]} getblockcount'
    block = os.popen(str(bitcoinclient)).read() # 'getblockcount' convert to string
    b = block
    c = b
    oneh = 0 - int(c) + 210000
    twoh = 210000 - int(c) + 210000
    thrh = 420000 - int(c) + 210000
    forh = 630000 - int(c) + 210000
    fifh = 840000 - int(c) + 210000
    sixh = 1050000 - int(c) + 210000
    sevh = 1260000 - int(c) + 210000
    eith = 1470000 - int(c) + 210000
    ninh = 1680000 - int(c) + 210000
    tenh = 1890000 - int(c) + 210000

    q = """
    \033[0;37;40m------------------- HALVING CLOCK -------------------

            1st  Halving: in {} Blocks {}
            2nd  Halving: in {} Blocks {}
            3rd  Halving: in {} Blocks {}
            4th  Halving: in {} Blocks {}
            5th  Halving: in {} Blocks {}
            6th  Halving: in {} Blocks {}
            7th  Halving: in {} Blocks {}
            8th  Halving: in {} Blocks {}
            9th  Halving: in {} Blocks {}
            10th Halving: in {} Blocks {}

    -------------------------------------------------------
    """.format("0" if int(c) == 210000 else oneh,"\033[1;32;40mCOMPLETE\033[0;37;40m","0" if int(c) == 420000 else twoh,"\033[1;32;40mCOMPLETE\033[0;37;40m", "0" if int(c) == 630000 else thrh,"\033[1;32;40mCOMPLETE\033[0;37;40m","0" if int(c) == 840000 else forh,"\033[1;32;40mCOMPLETE\033[0;37;40m" if int(c) >= 840000 else "\033[1;35;40mPENDING\033[0;37;40m", "0" if int(c) >= 1050000 else fifh , "\033[1;32;40mCOMPLETE\033[0;37;40m" if int(c) >= 1050000 else "\033[1;35;40mPENDING\033[0;37;40m", sixh, "\033[1;32;40mCOMPLETE\033[0;37;40m" if int(c) >= 1260000 else "\033[1;35;40mPENDING\033[0;37;40m", sevh,"\033[1;32;40mCOMPLETE\033[0;37;40m" if int(c) >= 1470000 else "\033[1;35;40mPENDING\033[0;37;40m", eith,"\033[1;32;40mCOMPLETE\033[0;37;40m" if int(c) >= 1680000 else "\033[1;35;40mPENDING\033[0;37;40m", ninh, "\033[1;32;40mCOMPLETE\033[0;37;40m" if int(c) >= 1890000 else "\033[1;35;40mPENDING\033[0;37;40m", tenh, "\033[1;32;40mCOMPLETE\033[0;37;40m" if int(c) >= 1890000 else "\033[1;35;40mPENDING\033[0;37;40m")
    print(q)
    input("\nContinue...")


def epoch():
    bitcoinclient = f'{path["bitcoincli"]} getblockcount'
    block = os.popen(str(bitcoinclient)).read() # 'getblockcount' convert to string
    b = block
    c = b
    oneh = 0 + int(c) / 2016

    q = """
    \033[0;37;40m------------------- EPOCH CLOCK -------------------

            Epoch {} Status {}

    ---------------------------------------------------
    """.format("0" if int(c) == 6930000 else oneh,"\033[1;32;40mON\033[0;37;40m")
    print(q)
    input("\nContinue...")

#--------------------------------- End Hex Block Decoder Functions -------------------------------------

def pdfconvert():
    path = {"ip_port":"", "rpcuser":"", "rpcpass":"", "bitcoincli":""}
    pathv = pickle.load(open("config/bclock.conf", "rb")) # Load the file 'bclock.conf'
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
            os.system(bitcoincli)
            clear()
            blogo()
            close()
            os.system("pdf2txt.py bitcoin.pdf")
            input("Continue...")
    else:
        clear()
        blogo()
        close()
        os.system("pdf2txt.py bitcoin.pdf")
        input("Continue...")
        
def bip39convert():
    clear()
    blogo()
    close()
    print("""
    
    
    Bip39 Words List
    
1. abandon
2. ability
3. able
4. about
5. above
6. absent
7. absorb
8. abstract
9. absurd
10. abuse
11. access
12. accident
13. account
14. accuse
15. achieve
16. acid
17. acoustic
18. acquire
19. across
20. act
21. action
22. actor
23. actress
24. actual
25. adapt
26. add
27. addict
28. address
29. adjust
30. admit
31. adult
32. advance
33. advice
34. aerobic
35. affair
36. afford
37. afraid
38. again
39. age
40. agent
41. agree
42. ahead
43. aim
44. air
45. airport
46. aisle
47. alarm
48. album
49. alcohol
50. alert
51. alien
52. all
53. alley
54. allow
55. almost
56. alone
57. alpha
58. already
59. also
60. alter
61. always
62. amateur
63. amazing
64. among
65. amount
66. amused
67. analyst
68. anchor
69. ancient
70. anger
71. angle
72. angry
73. animal
74. ankle
75. announce
76. annual
77. another
78. answer
79. antenna
80. antique
81. anxiety
82. any
83. apart
84. apology
85. appear
86. apple
87. approve
88. april
89. arch
90. arctic
91. area
92. arena
93. argue
94. arm
95. armed
96. armor
97. army
98. around
99. arrange
100. arrest
101. arrive
102. arrow
103. art
104. artefact
105. artist
106. artwork
107. ask
108. aspect
109. assault
110. asset
111. assist
112. assume
113. asthma
114. athlete
115. atom
116. attack
117. attend
118. attitude
119. attract
120. auction
121. audit
122. august
123. aunt
124. author
125. auto
126. autumn
127. average
128. avocado
129. avoid
130. awake
131. aware
132. away
133. awesome
134. awful
135. awkward
136. axis
137. baby
138. bachelor
139. bacon
140. badge
141. bag
142. balance
143. balcony
144. ball
145. bamboo
146. banana
147. banner
148. bar
149. barely
150. bargain
151. barrel
152. base
153. basic
154. basket
155. battle
156. beach
157. bean
158. beauty
159. because
160. become
161. beef
162. before
163. begin
164. behave
165. behind
166. believe
167. below
168. belt
169. bench
170. benefit
171. best
172. betray
173. better
174. between
175. beyond
176. bicycle
177. bid
178. bike
179. bind
180. biology
181. bird
182. birth
183. bitter
184. black
185. blade
186. blame
187. blanket
188. blast
189. bleak
190. bless
191. blind
192. blood
193. blossom
194. blouse
195. blue
196. blur
197. blush
198. board
199. boat
200. body
201. boil
202. bomb
203. bone
204. bonus
205. book
206. boost
207. border
208. boring
209. borrow
210. boss
211. bottom
212. bounce
213. box
214. boy
215. bracket
216. brain
217. brand
218. brass
219. brave
220. bread
221. breeze
222. brick
223. bridge
224. brief
225. bright
226. bring
227. brisk
228. broccoli
229. broken
230. bronze
231. broom
232. brother
233. brown
234. brush
235. bubble
236. buddy
237. budget
238. buffalo
239. build
240. bulb
241. bulk
242. bullet
243. bundle
244. bunker
245. burden
246. burger
247. burst
248. bus
249. business
250. busy
251. butter
252. buyer
253. buzz
254. cabbage
255. cabin
256. cable
257. cactus
258. cage
259. cake
260. call
261. calm
262. camera
263. camp
264. can
265. canal
266. cancel
267. candy
268. cannon
269. canoe
270. canvas
271. canyon
272. capable
273. capital
274. captain
275. car
276. carbon
277. card
278. cargo
279. carpet
280. carry
281. cart
282. case
283. cash
284. casino
285. castle
286. casual
287. cat
288. catalog
289. catch
290. category
291. cattle
292. caught
293. cause
294. caution
295. cave
296. ceiling
297. celery
298. cement
299. census
300. century
301. cereal
302. certain
303. chair
304. chalk
305. champion
306. change
307. chaos
308. chapter
309. charge
310. chase
311. chat
312. cheap
313. check
314. cheese
315. chef
316. cherry
317. chest
318. chicken
319. chief
320. child
321. chimney
322. choice
323. choose
324. chronic
325. chuckle
326. chunk
327. churn
328. cigar
329. cinnamon
330. circle
331. citizen
332. city
333. civil
334. claim
335. clap
336. clarify
337. claw
338. clay
339. clean
340. clerk
341. clever
342. click
343. client
344. cliff
345. climb
346. clinic
347. clip
348. clock
349. clog
350. close
351. cloth
352. cloud
353. clown
354. club
355. clump
356. cluster
357. clutch
358. coach
359. coast
360. coconut
361. code
362. coffee
363. coil
364. coin
365. collect
366. color
367. column
368. combine
369. come
370. comfort
371. comic
372. common
373. company
374. concert
375. conduct
376. confirm
377. congress
378. connect
379. consider
380. control
381. convince
382. cook
383. cool
384. copper
385. copy
386. coral
387. core
388. corn
389. correct
390. cost
391. cotton
392. couch
393. country
394. couple
395. course
396. cousin
397. cover
398. coyote
399. crack
400. cradle
401. craft
402. cram
403. crane
404. crash
405. crater
406. crawl
407. crazy
408. cream
409. credit
410. creek
411. crew
412. cricket
413. crime
414. crisp
415. critic
416. crop
417. cross
418. crouch
419. crowd
420. crucial
421. cruel
422. cruise
423. crumble
424. crunch
425. crush
426. cry
427. crystal
428. cube
429. culture
430. cup
431. cupboard
432. curious
433. current
434. curtain
435. curve
436. cushion
437. custom
438. cute
439. cycle
440. dad
441. damage
442. damp
443. dance
444. danger
445. daring
446. dash
447. daughter
448. dawn
449. day
450. deal
451. debate
452. debris
453. decade
454. december
455. decide
456. decline
457. decorate
458. decrease
459. deer
460. defense
461. define
462. defy
463. degree
464. delay
465. deliver
466. demand
467. demise
468. denial
469. dentist
470. deny
471. depart
472. depend
473. deposit
474. depth
475. deputy
476. derive
477. describe
478. desert
479. design
480. desk
481. despair
482. destroy
483. detail
484. detect
485. develop
486. device
487. devote
488. diagram
489. dial
490. diamond
491. diary
492. dice
493. diesel
494. diet
495. differ
496. digital
497. dignity
498. dilemma
499. dinner
500. dinosaur
501. direct
502. dirt
503. disagree
504. discover
505. disease
506. dish
507. dismiss
508. disorder
509. display
510. distance
511. divert
512. divide
513. divorce
514. dizzy
515. doctor
516. document
517. dog
518. doll
519. dolphin
520. domain
521. donate
522. donkey
523. donor
524. door
525. dose
526. double
527. dove
528. draft
529. dragon
530. drama
531. drastic
532. draw
533. dream
534. dress
535. drift
536. drill
537. drink
538. drip
539. drive
540. drop
541. drum
542. dry
543. duck
544. dumb
545. dune
546. during
547. dust
548. dutch
549. duty
550. dwarf
551. dynamic
552. eager
553. eagle
554. early
555. earn
556. earth
557. easily
558. east
559. easy
560. echo
561. ecology
562. economy
563. edge
564. edit
565. educate
566. effort
567. egg
568. eight
569. either
570. elbow
571. elder
572. electric
573. elegant
574. element
575. elephant
576. elevator
577. elite
578. else
579. embark
580. embody
581. embrace
582. emerge
583. emotion
584. employ
585. empower
586. empty
587. enable
588. enact
589. end
590. endless
591. endorse
592. enemy
593. energy
594. enforce
595. engage
596. engine
597. enhance
598. enjoy
599. enlist
600. enough
601. enrich
602. enroll
603. ensure
604. enter
605. entire
606. entry
607. envelope
608. episode
609. equal
610. equip
611. era
612. erase
613. erode
614. erosion
615. error
616. erupt
617. escape
618. essay
619. essence
620. estate
621. eternal
622. ethics
623. evidence
624. evil
625. evoke
626. evolve
627. exact
628. example
629. excess
630. exchange
631. excite
632. exclude
633. excuse
634. execute
635. exercise
636. exhaust
637. exhibit
638. exile
639. exist
640. exit
641. exotic
642. expand
643. expect
644. expire
645. explain
646. expose
647. express
648. extend
649. extra
650. eye
651. eyebrow
652. fabric
653. face
654. faculty
655. fade
656. faint
657. faith
658. fall
659. false
660. fame
661. family
662. famous
663. fan
664. fancy
665. fantasy
666. farm
667. fashion
668. fat
669. fatal
670. father
671. fatigue
672. fault
673. favorite
674. feature
675. february
676. federal
677. fee
678. feed
679. feel
680. female
681. fence
682. festival
683. fetch
684. fever
685. few
686. fiber
687. fiction
688. field
689. figure
690. file
691. film
692. filter
693. final
694. find
695. fine
696. finger
697. finish
698. fire
699. firm
700. first
701. fiscal
702. fish
703. fit
704. fitness
705. fix
706. flag
707. flame
708. flash
709. flat
710. flavor
711. flee
712. flight
713. flip
714. float
715. flock
716. floor
717. flower
718. fluid
719. flush
720. fly
721. foam
722. focus
723. fog
724. foil
725. fold
726. follow
727. food
728. foot
729. force
730. forest
731. forget
732. fork
733. fortune
734. forum
735. forward
736. fossil
737. foster
738. found
739. fox
740. fragile
741. frame
742. frequent
743. fresh
744. friend
745. fringe
746. frog
747. front
748. frost
749. frown
750. frozen
751. fruit
752. fuel
753. fun
754. funny
755. furnace
756. fury
757. future
758. gadget
759. gain
760. galaxy
761. gallery
762. game
763. gap
764. garage
765. garbage
766. garden
767. garlic
768. garment
769. gas
770. gasp
771. gate
772. gather
773. gauge
774. gaze
775. general
776. genius
777. genre
778. gentle
779. genuine
780. gesture
781. ghost
782. giant
783. gift
784. giggle
785. ginger
786. giraffe
787. girl
788. give
789. glad
790. glance
791. glare
792. glass
793. glide
794. glimpse
795. globe
796. gloom
797. glory
798. glove
799. glow
800. glue
801. goat
802. goddess
803. gold
804. good
805. goose
806. gorilla
807. gospel
808. gossip
809. govern
810. gown
811. grab
812. grace
813. grain
814. grant
815. grape
816. grass
817. gravity
818. great
819. green
820. grid
821. grief
822. grit
823. grocery
824. group
825. grow
826. grunt
827. guard
828. guess
829. guide
830. guilt
831. guitar
832. gun
833. gym
834. habit
835. hair
836. half
837. hammer
838. hamster
839. hand
840. happy
841. harbor
842. hard
843. harsh
844. harvest
845. hat
846. have
847. hawk
848. hazard
849. head
850. health
851. heart
852. heavy
853. hedgehog
854. height
855. hello
856. helmet
857. help
858. hen
859. hero
860. hidden
861. high
862. hill
863. hint
864. hip
865. hire
866. history
867. hobby
868. hockey
869. hold
870. hole
871. holiday
872. hollow
873. home
874. honey
875. hood
876. hope
877. horn
878. horror
879. horse
880. hospital
881. host
882. hotel
883. hour
884. hover
885. hub
886. huge
887. human
888. humble
889. humor
890. hundred
891. hungry
892. hunt
893. hurdle
894. hurry
895. hurt
896. husband
897. hybrid
898. ice
899. icon
900. idea
901. identify
902. idle
903. ignore
904. ill
905. illegal
906. illness
907. image
908. imitate
909. immense
910. immune
911. impact
912. impose
913. improve
914. impulse
915. inch
916. include
917. income
918. increase
919. index
920. indicate
921. indoor
922. industry
923. infant
924. inflict
925. inform
926. inhale
927. inherit
928. initial
929. inject
930. injury
931. inmate
932. inner
933. innocent
934. input
935. inquiry
936. insane
937. insect
938. inside
939. inspire
940. install
941. intact
942. interest
943. into
944. invest
945. invite
946. involve
947. iron
948. island
949. isolate
950. issue
951. item
952. ivory
953. jacket
954. jaguar
955. jar
956. jazz
957. jealous
958. jeans
959. jelly
960. jewel
961. job
962. join
963. joke
964. journey
965. joy
966. judge
967. juice
968. jump
969. jungle
970. junior
971. junk
972. just
973. kangaroo
974. keen
975. keep
976. ketchup
977. key
978. kick
979. kid
980. kidney
981. kind
982. kingdom
983. kiss
984. kit
985. kitchen
986. kite
987. kitten
988. kiwi
989. knee
990. knife
991. knock
992. know
993. lab
994. label
995. labor
996. ladder
997. lady
998. lake
999. lamp
1000. language
1001. laptop
1002. large
1003. later
1004. latin
1005. laugh
1006. laundry
1007. lava
1008. law
1009. lawn
1010. lawsuit
1011. layer
1012. lazy
1013. leader
1014. leaf
1015. learn
1016. leave
1017. lecture
1018. left
1019. leg
1020. legal
1021. legend
1022. leisure
1023. lemon
1024. lend
1025. length
1026. lens
1027. leopard
1028. lesson
1029. letter
1030. level
1031. liar
1032. liberty
1033. library
1034. license
1035. life
1036. lift
1037. light
1038. like
1039. limb
1040. limit
1041. link
1042. lion
1043. liquid
1044. list
1045. little
1046. live
1047. lizard
1048. load
1049. loan
1050. lobster
1051. local
1052. lock
1053. logic
1054. lonely
1055. long
1056. loop
1057. lottery
1058. loud
1059. lounge
1060. love
1061. loyal
1062. lucky
1063. luggage
1064. lumber
1065. lunar
1066. lunch
1067. luxury
1068. lyrics
1069. machine
1070. mad
1071. magic
1072. magnet
1073. maid
1074. mail
1075. main
1076. major
1077. make
1078. mammal
1079. man
1080. manage
1081. mandate
1082. mango
1083. mansion
1084. manual
1085. maple
1086. marble
1087. march
1088. margin
1089. marine
1090. market
1091. marriage
1092. mask
1093. mass
1094. master
1095. match
1096. material
1097. math
1098. matrix
1099. matter
1100. maximum
1101. maze
1102. meadow
1103. mean
1104. measure
1105. meat
1106. mechanic
1107. medal
1108. media
1109. melody
1110. melt
1111. member
1112. memory
1113. mention
1114. menu
1115. mercy
1116. merge
1117. merit
1118. merry
1119. mesh
1120. message
1121. metal
1122. method
1123. middle
1124. midnight
1125. milk
1126. million
1127. mimic
1128. mind
1129. minimum
1130. minor
1131. minute
1132. miracle
1133. mirror
1134. misery
1135. miss
1136. mistake
1137. mix
1138. mixed
1139. mixture
1140. mobile
1141. model
1142. modify
1143. mom
1144. moment
1145. monitor
1146. monkey
1147. monster
1148. month
1149. moon
1150. moral
1151. more
1152. morning
1153. mosquito
1154. mother
1155. motion
1156. motor
1157. mountain
1158. mouse
1159. move
1160. movie
1161. much
1162. muffin
1163. mule
1164. multiply
1165. muscle
1166. museum
1167. mushroom
1168. music
1169. must
1170. mutual
1171. myself
1172. mystery
1173. myth
1174. naive
1175. name
1176. napkin
1177. narrow
1178. nasty
1179. nation
1180. nature
1181. near
1182. neck
1183. need
1184. negative
1185. neglect
1186. neither
1187. nephew
1188. nerve
1189. nest
1190. net
1191. network
1192. neutral
1193. never
1194. news
1195. next
1196. nice
1197. night
1198. noble
1199. noise
1200. nominee
1201. noodle
1202. normal
1203. north
1204. nose
1205. notable
1206. note
1207. nothing
1208. notice
1209. novel
1210. now
1211. nuclear
1212. number
1213. nurse
1214. nut
1215. oak
1216. obey
1217. object
1218. oblige
1219. obscure
1220. observe
1221. obtain
1222. obvious
1223. occur
1224. ocean
1225. october
1226. odor
1227. off
1228. offer
1229. office
1230. often
1231. oil
1232. okay
1233. old
1234. olive
1235. olympic
1236. omit
1237. once
1238. one
1239. onion
1240. online
1241. only
1242. open
1243. opera
1244. opinion
1245. oppose
1246. option
1247. orange
1248. orbit
1249. orchard
1250. order
1251. ordinary
1252. organ
1253. orient
1254. original
1255. orphan
1256. ostrich
1257. other
1258. outdoor
1259. outer
1260. output
1261. outside
1262. oval
1263. oven
1264. over
1265. own
1266. owner
1267. oxygen
1268. oyster
1269. ozone
1270. pact
1271. paddle
1272. page
1273. pair
1274. palace
1275. palm
1276. panda
1277. panel
1278. panic
1279. panther
1280. paper
1281. parade
1282. parent
1283. park
1284. parrot
1285. party
1286. pass
1287. patch
1288. path
1289. patient
1290. patrol
1291. pattern
1292. pause
1293. pave
1294. payment
1295. peace
1296. peanut
1297. pear
1298. peasant
1299. pelican
1300. pen
1301. penalty
1302. pencil
1303. people
1304. pepper
1305. perfect
1306. permit
1307. person
1308. pet
1309. phone
1310. photo
1311. phrase
1312. physical
1313. piano
1314. picnic
1315. picture
1316. piece
1317. pig
1318. pigeon
1319. pill
1320. pilot
1321. pink
1322. pioneer
1323. pipe
1324. pistol
1325. pitch
1326. pizza
1327. place
1328. planet
1329. plastic
1330. plate
1331. play
1332. please
1333. pledge
1334. pluck
1335. plug
1336. plunge
1337. poem
1338. poet
1339. point
1340. polar
1341. pole
1342. police
1343. pond
1344. pony
1345. pool
1346. popular
1347. portion
1348. position
1349. possible
1350. post
1351. potato
1352. pottery
1353. poverty
1354. powder
1355. power
1356. practice
1357. praise
1358. predict
1359. prefer
1360. prepare
1361. present
1362. pretty
1363. prevent
1364. price
1365. pride
1366. primary
1367. print
1368. priority
1369. prison
1370. private
1371. prize
1372. problem
1373. process
1374. produce
1375. profit
1376. program
1377. project
1378. promote
1379. proof
1380. property
1381. prosper
1382. protect
1383. proud
1384. provide
1385. public
1386. pudding
1387. pull
1388. pulp
1389. pulse
1390. pumpkin
1391. punch
1392. pupil
1393. puppy
1394. purchase
1395. purity
1396. purpose
1397. purse
1398. push
1399. put
1400. puzzle
1401. pyramid
1402. quality
1403. quantum
1404. quarter
1405. question
1406. quick
1407. quit
1408. quiz
1409. quote
1410. rabbit
1411. raccoon
1412. race
1413. rack
1414. radar
1415. radio
1416. rail
1417. rain
1418. raise
1419. rally
1420. ramp
1421. ranch
1422. random
1423. range
1424. rapid
1425. rare
1426. rate
1427. rather
1428. raven
1429. raw
1430. razor
1431. ready
1432. real
1433. reason
1434. rebel
1435. rebuild
1436. recall
1437. receive
1438. recipe
1439. record
1440. recycle
1441. reduce
1442. reflect
1443. reform
1444. refuse
1445. region
1446. regret
1447. regular
1448. reject
1449. relax
1450. release
1451. relief
1452. rely
1453. remain
1454. remember
1455. remind
1456. remove
1457. render
1458. renew
1459. rent
1460. reopen
1461. repair
1462. repeat
1463. replace
1464. report
1465. require
1466. rescue
1467. resemble
1468. resist
1469. resource
1470. response
1471. result
1472. retire
1473. retreat
1474. return
1475. reunion
1476. reveal
1477. review
1478. reward
1479. rhythm
1480. rib
1481. ribbon
1482. rice
1483. rich
1484. ride
1485. ridge
1486. rifle
1487. right
1488. rigid
1489. ring
1490. riot
1491. ripple
1492. risk
1493. ritual
1494. rival
1495. river
1496. road
1497. roast
1498. robot
1499. robust
1500. rocket
1501. romance
1502. roof
1503. rookie
1504. room
1505. rose
1506. rotate
1507. rough
1508. round
1509. route
1510. royal
1511. rubber
1512. rude
1513. rug
1514. rule
1515. run
1516. runway
1517. rural
1518. sad
1519. saddle
1520. sadness
1521. safe
1522. sail
1523. salad
1524. salmon
1525. salon
1526. salt
1527. salute
1528. same
1529. sample
1530. sand
1531. satisfy
1532. satoshi
1533. sauce
1534. sausage
1535. save
1536. say
1537. scale
1538. scan
1539. scare
1540. scatter
1541. scene
1542. scheme
1543. school
1544. science
1545. scissors
1546. scorpion
1547. scout
1548. scrap
1549. screen
1550. script
1551. scrub
1552. sea
1553. search
1554. season
1555. seat
1556. second
1557. secret
1558. section
1559. security
1560. seed
1561. seek
1562. segment
1563. select
1564. sell
1565. seminar
1566. senior
1567. sense
1568. sentence
1569. series
1570. service
1571. session
1572. settle
1573. setup
1574. seven
1575. shadow
1576. shaft
1577. shallow
1578. share
1579. shed
1580. shell
1581. sheriff
1582. shield
1583. shift
1584. shine
1585. ship
1586. shiver
1587. shock
1588. shoe
1589. shoot
1590. shop
1591. short
1592. shoulder
1593. shove
1594. shrimp
1595. shrug
1596. shuffle
1597. shy
1598. sibling
1599. sick
1600. side
1601. siege
1602. sight
1603. sign
1604. silent
1605. silk
1606. silly
1607. silver
1608. similar
1609. simple
1610. since
1611. sing
1612. siren
1613. sister
1614. situate
1615. six
1616. size
1617. skate
1618. sketch
1619. ski
1620. skill
1621. skin
1622. skirt
1623. skull
1624. slab
1625. slam
1626. sleep
1627. slender
1628. slice
1629. slide
1630. slight
1631. slim
1632. slogan
1633. slot
1634. slow
1635. slush
1636. small
1637. smart
1638. smile
1639. smoke
1640. smooth
1641. snack
1642. snake
1643. snap
1644. sniff
1645. snow
1646. soap
1647. soccer
1648. social
1649. sock
1650. soda
1651. soft
1652. solar
1653. soldier
1654. solid
1655. solution
1656. solve
1657. someone
1658. song
1659. soon
1660. sorry
1661. sort
1662. soul
1663. sound
1664. soup
1665. source
1666. south
1667. space
1668. spare
1669. spatial
1670. spawn
1671. speak
1672. special
1673. speed
1674. spell
1675. spend
1676. sphere
1677. spice
1678. spider
1679. spike
1680. spin
1681. spirit
1682. split
1683. spoil
1684. sponsor
1685. spoon
1686. sport
1687. spot
1688. spray
1689. spread
1690. spring
1691. spy
1692. square
1693. squeeze
1694. squirrel
1695. stable
1696. stadium
1697. staff
1698. stage
1699. stairs
1700. stamp
1701. stand
1702. start
1703. state
1704. stay
1705. steak
1706. steel
1707. stem
1708. step
1709. stereo
1710. stick
1711. still
1712. sting
1713. stock
1714. stomach
1715. stone
1716. stool
1717. story
1718. stove
1719. strategy
1720. street
1721. strike
1722. strong
1723. struggle
1724. student
1725. stuff
1726. stumble
1727. style
1728. subject
1729. submit
1730. subway
1731. success
1732. such
1733. sudden
1734. suffer
1735. sugar
1736. suggest
1737. suit
1738. summer
1739. sun
1740. sunny
1741. sunset
1742. super
1743. supply
1744. supreme
1745. sure
1746. surface
1747. surge
1748. surprise
1749. surround
1750. survey
1751. suspect
1752. sustain
1753. swallow
1754. swamp
1755. swap
1756. swarm
1757. swear
1758. sweet
1759. swift
1760. swim
1761. swing
1762. switch
1763. sword
1764. symbol
1765. symptom
1766. syrup
1767. system
1768. table
1769. tackle
1770. tag
1771. tail
1772. talent
1773. talk
1774. tank
1775. tape
1776. target
1777. task
1778. taste
1779. tattoo
1780. taxi
1781. teach
1782. team
1783. tell
1784. ten
1785. tenant
1786. tennis
1787. tent
1788. term
1789. test
1790. text
1791. thank
1792. that
1793. theme
1794. then
1795. theory
1796. there
1797. they
1798. thing
1799. this
1800. thought
1801. three
1802. thrive
1803. throw
1804. thumb
1805. thunder
1806. ticket
1807. tide
1808. tiger
1809. tilt
1810. timber
1811. time
1812. tiny
1813. tip
1814. tired
1815. tissue
1816. title
1817. toast
1818. tobacco
1819. today
1820. toddler
1821. toe
1822. together
1823. toilet
1824. token
1825. tomato
1826. tomorrow
1827. tone
1828. tongue
1829. tonight
1830. tool
1831. tooth
1832. top
1833. topic
1834. topple
1835. torch
1836. tornado
1837. tortoise
1838. toss
1839. total
1840. tourist
1841. toward
1842. tower
1843. town
1844. toy
1845. track
1846. trade
1847. traffic
1848. tragic
1849. train
1850. transfer
1851. trap
1852. trash
1853. travel
1854. tray
1855. treat
1856. tree
1857. trend
1858. trial
1859. tribe
1860. trick
1861. trigger
1862. trim
1863. trip
1864. trophy
1865. trouble
1866. truck
1867. true
1868. truly
1869. trumpet
1870. trust
1871. truth
1872. try
1873. tube
1874. tuition
1875. tumble
1876. tuna
1877. tunnel
1878. turkey
1879. turn
1880. turtle
1881. twelve
1882. twenty
1883. twice
1884. twin
1885. twist
1886. two
1887. type
1888. typical
1889. ugly
1890. umbrella
1891. unable
1892. unaware
1893. uncle
1894. uncover
1895. under
1896. undo
1897. unfair
1898. unfold
1899. unhappy
1900. uniform
1901. unique
1902. unit
1903. universe
1904. unknown
1905. unlock
1906. until
1907. unusual
1908. unveil
1909. update
1910. upgrade
1911. uphold
1912. upon
1913. upper
1914. upset
1915. urban
1916. urge
1917. usage
1918. use
1919. used
1920. useful
1921. useless
1922. usual
1923. utility
1924. vacant
1925. vacuum
1926. vague
1927. valid
1928. valley
1929. valve
1930. van
1931. vanish
1932. vapor
1933. various
1934. vast
1935. vault
1936. vehicle
1937. velvet
1938. vendor
1939. venture
1940. venue
1941. verb
1942. verify
1943. version
1944. very
1945. vessel
1946. veteran
1947. viable
1948. vibrant
1949. vicious
1950. victory
1951. video
1952. view
1953. village
1954. vintage
1955. violin
1956. virtual
1957. virus
1958. visa
1959. visit
1960. visual
1961. vital
1962. vivid
1963. vocal
1964. voice
1965. void
1966. volcano
1967. volume
1968. vote
1969. voyage
1970. wage
1971. wagon
1972. wait
1973. walk
1974. wall
1975. walnut
1976. want
1977. warfare
1978. warm
1979. warrior
1980. wash
1981. wasp
1982. waste
1983. water
1984. wave
1985. way
1986. wealth
1987. weapon
1988. wear
1989. weasel
1990. weather
1991. web
1992. wedding
1993. weekend
1994. weird
1995. welcome
1996. west
1997. wet
1998. whale
1999. what
2000. wheat
2001. wheel
2002. when
2003. where
2004. whip
2005. whisper
2006. wide
2007. width
2008. wife
2009. wild
2010. will
2011. win
2012. window
2013. wine
2014. wing
2015. wink
2016. winner
2017. winter
2018. wire
2019. wisdom
2020. wise
2021. wish
2022. witness
2023. wolf
2024. woman
2025. wonder
2026. wood
2027. wool
2028. word
2029. work
2030. world
2031. worry
2032. worth
2033. wrap
2034. wreck
2035. wrestle
2036. wrist
2037. write
2038. wrong
2039. yard
2040. year
2041. yellow
2042. you
2043. young
2044. youth
2045. zebra
2046. zero
2047. zone
2048. zoo



     Bip39 TinySeed Dots


	N.01TinySeed          ⚪️⚪️⚪️⚪️⚪️⚪️⚪️⚪️⚪️⚪️⚪️🔘
	N.02TinySeed          ⚪️⚪️⚪️⚪️⚪️⚪️⚪️⚪️⚪️⚪️🔘⚪️
	N.03TinySeed          ⚪️⚪️⚪️⚪️⚪️⚪️⚪️⚪️⚪️⚪️🔘🔘
	N.04TinySeed          ⚪️⚪️⚪️⚪️⚪️⚪️⚪️⚪️⚪️🔘⚪️⚪️
	N.05TinySeed          ⚪️⚪️⚪️⚪️⚪️⚪️⚪️⚪️⚪️🔘⚪️🔘
	N.06TinySeed          ⚪️⚪️⚪️⚪️⚪️⚪️⚪️⚪️⚪️🔘🔘⚪️
	N.07TinySeed          ⚪️⚪️⚪️⚪️⚪️⚪️⚪️⚪️⚪️🔘🔘🔘
	N.08TinySeed          ⚪️⚪️⚪️⚪️⚪️⚪️⚪️⚪️🔘⚪️⚪️⚪️
	N.09TinySeed          ⚪️⚪️⚪️⚪️⚪️⚪️⚪️⚪️🔘⚪️⚪️🔘
	N.10TinySeed          ⚪️⚪️⚪️⚪️⚪️⚪️⚪️⚪️🔘⚪️🔘⚪️
	N.11TinySeed          ⚪️⚪️⚪️⚪️⚪️⚪️⚪️⚪️🔘⚪️🔘🔘
	N.12TinySeed          ⚪️⚪️⚪️⚪️⚪️⚪️⚪️⚪️🔘🔘⚪️⚪️
	N.13TinySeed          ⚪️⚪️⚪️⚪️⚪️⚪️⚪️⚪️🔘🔘⚪️🔘
	N.14TinySeed          ⚪️⚪️⚪️⚪️⚪️⚪️⚪️⚪️🔘🔘🔘⚪️
	N.15TinySeed          ⚪️⚪️⚪️⚪️⚪️⚪️⚪️⚪️🔘🔘🔘🔘
	N.16TinySeed          ⚪️⚪️⚪️⚪️⚪️⚪️⚪️🔘⚪️⚪️⚪️⚪️
	N.17TinySeed          ⚪️⚪️⚪️⚪️⚪️⚪️⚪️🔘⚪️⚪️⚪️🔘
	N.18TinySeed          ⚪️⚪️⚪️⚪️⚪️⚪️⚪️🔘⚪️⚪️🔘⚪️
	N.19TinySeed          ⚪️⚪️⚪️⚪️⚪️⚪️⚪️🔘⚪️⚪️🔘🔘
	N.20TinySeed          ⚪️⚪️⚪️⚪️⚪️⚪️⚪️🔘⚪️🔘⚪️⚪️
	N.21TinySeed          ⚪️⚪️⚪️⚪️⚪️⚪️⚪️🔘⚪️🔘⚪️🔘
	N.22TinySeed          ⚪️⚪️⚪️⚪️⚪️⚪️⚪️🔘⚪️🔘🔘⚪️
	N.23TinySeed          ⚪️⚪️⚪️⚪️⚪️⚪️⚪️🔘⚪️🔘🔘🔘
	N.24TinySeed          ⚪️⚪️⚪️⚪️⚪️⚪️⚪️🔘🔘⚪️⚪️⚪️
	N.25TinySeed          ⚪️⚪️⚪️⚪️⚪️⚪️⚪️🔘🔘⚪️⚪️🔘
	N.26TinySeed          ⚪️⚪️⚪️⚪️⚪️⚪️⚪️🔘🔘⚪️🔘⚪️
	N.27TinySeed          ⚪️⚪️⚪️⚪️⚪️⚪️⚪️🔘🔘⚪️🔘🔘
	N.28TinySeed          ⚪️⚪️⚪️⚪️⚪️⚪️⚪️🔘🔘🔘⚪️⚪️
	N.29TinySeed          ⚪️⚪️⚪️⚪️⚪️⚪️⚪️🔘🔘🔘⚪️🔘
	N.30TinySeed          ⚪️⚪️⚪️⚪️⚪️⚪️⚪️🔘🔘🔘🔘⚪️
	N.31TinySeed          ⚪️⚪️⚪️⚪️⚪️⚪️⚪️🔘🔘🔘🔘🔘
	N.32TinySeed          ⚪️⚪️⚪️⚪️⚪️⚪️🔘⚪️⚪️⚪️⚪️⚪️
	N.33TinySeed          ⚪️⚪️⚪️⚪️⚪️⚪️🔘⚪️⚪️⚪️⚪️🔘
	N.34TinySeed          ⚪️⚪️⚪️⚪️⚪️⚪️🔘⚪️⚪️⚪️🔘⚪️
	N.35TinySeed          ⚪️⚪️⚪️⚪️⚪️⚪️🔘⚪️⚪️⚪️🔘🔘
	N.36TinySeed          ⚪️⚪️⚪️⚪️⚪️⚪️🔘⚪️⚪️🔘⚪️⚪️
	N.37TinySeed          ⚪️⚪️⚪️⚪️⚪️⚪️🔘⚪️⚪️🔘⚪️🔘
	N.38TinySeed          ⚪️⚪️⚪️⚪️⚪️⚪️🔘⚪️⚪️🔘🔘⚪️
	N.39TinySeed          ⚪️⚪️⚪️⚪️⚪️⚪️🔘⚪️⚪️🔘🔘🔘
	N.40TinySeed          ⚪️⚪️⚪️⚪️⚪️⚪️🔘⚪️🔘⚪️⚪️⚪️
	N.41TinySeed          ⚪️⚪️⚪️⚪️⚪️⚪️🔘⚪️🔘⚪️⚪️🔘
	N.42TinySeed          ⚪️⚪️⚪️⚪️⚪️⚪️🔘⚪️🔘⚪️🔘⚪️
	N.43TinySeed          ⚪️⚪️⚪️⚪️⚪️⚪️🔘⚪️🔘⚪️🔘🔘
	N.44TinySeed          ⚪️⚪️⚪️⚪️⚪️⚪️🔘⚪️🔘🔘⚪️⚪️
	N.45TinySeed          ⚪️⚪️⚪️⚪️⚪️⚪️🔘⚪️🔘🔘⚪️🔘
	N.46TinySeed          ⚪️⚪️⚪️⚪️⚪️⚪️🔘⚪️🔘🔘🔘⚪️
	N.47TinySeed          ⚪️⚪️⚪️⚪️⚪️⚪️🔘⚪️🔘🔘🔘🔘
	N.48TinySeed          ⚪️⚪️⚪️⚪️⚪️⚪️🔘🔘⚪️⚪️⚪️⚪️
	N.49TinySeed          ⚪️⚪️⚪️⚪️⚪️⚪️🔘🔘⚪️⚪️⚪️🔘
	N.50TinySeed          ⚪️⚪️⚪️⚪️⚪️⚪️🔘🔘⚪️⚪️🔘⚪️
	N.51TinySeed          ⚪️⚪️⚪️⚪️⚪️⚪️🔘🔘⚪️⚪️🔘🔘
	N.52TinySeed          ⚪️⚪️⚪️⚪️⚪️⚪️🔘🔘⚪️🔘⚪️⚪️
	N.53TinySeed          ⚪️⚪️⚪️⚪️⚪️⚪️🔘🔘⚪️🔘⚪️🔘
	N.54TinySeed          ⚪️⚪️⚪️⚪️⚪️⚪️🔘🔘⚪️🔘🔘⚪️
	N.55TinySeed          ⚪️⚪️⚪️⚪️⚪️⚪️🔘🔘⚪️🔘🔘🔘
	N.56TinySeed          ⚪️⚪️⚪️⚪️⚪️⚪️🔘🔘🔘⚪️⚪️⚪️
	N.57TinySeed          ⚪️⚪️⚪️⚪️⚪️⚪️🔘🔘🔘⚪️⚪️🔘
	N.58TinySeed          ⚪️⚪️⚪️⚪️⚪️⚪️🔘🔘🔘⚪️🔘⚪️
	N.59TinySeed          ⚪️⚪️⚪️⚪️⚪️⚪️🔘🔘🔘⚪️🔘🔘
	N.60TinySeed          ⚪️⚪️⚪️⚪️⚪️⚪️🔘🔘🔘🔘⚪️⚪️
	N.61TinySeed          ⚪️⚪️⚪️⚪️⚪️⚪️🔘🔘🔘🔘⚪️🔘
	N.62TinySeed          ⚪️⚪️⚪️⚪️⚪️⚪️🔘🔘🔘🔘🔘⚪️
	N.63TinySeed          ⚪️⚪️⚪️⚪️⚪️⚪️🔘🔘🔘🔘🔘🔘
	N.64TinySeed          ⚪️⚪️⚪️⚪️⚪️🔘⚪️⚪️⚪️⚪️⚪️⚪️
	N.65TinySeed          ⚪️⚪️⚪️⚪️⚪️🔘⚪️⚪️⚪️⚪️⚪️🔘
	N.66TinySeed          ⚪️⚪️⚪️⚪️⚪️🔘⚪️⚪️⚪️⚪️🔘⚪️
	N.67TinySeed          ⚪️⚪️⚪️⚪️⚪️🔘⚪️⚪️⚪️⚪️🔘🔘
	N.68TinySeed          ⚪️⚪️⚪️⚪️⚪️🔘⚪️⚪️⚪️🔘⚪️⚪️
	N.69TinySeed          ⚪️⚪️⚪️⚪️⚪️🔘⚪️⚪️⚪️🔘⚪️🔘
	N.70TinySeed          ⚪️⚪️⚪️⚪️⚪️🔘⚪️⚪️⚪️🔘🔘⚪️
	N.71TinySeed          ⚪️⚪️⚪️⚪️⚪️🔘⚪️⚪️⚪️🔘🔘🔘
	N.72TinySeed          ⚪️⚪️⚪️⚪️⚪️🔘⚪️⚪️🔘⚪️⚪️⚪️
	N.73TinySeed          ⚪️⚪️⚪️⚪️⚪️🔘⚪️⚪️🔘⚪️⚪️🔘
	N.74TinySeed          ⚪️⚪️⚪️⚪️⚪️🔘⚪️⚪️🔘⚪️🔘⚪️
	N.75TinySeed          ⚪️⚪️⚪️⚪️⚪️🔘⚪️⚪️🔘⚪️🔘🔘
	N.76TinySeed          ⚪️⚪️⚪️⚪️⚪️🔘⚪️⚪️🔘🔘⚪️⚪️
	N.77TinySeed          ⚪️⚪️⚪️⚪️⚪️🔘⚪️⚪️🔘🔘⚪️🔘
	N.78TinySeed          ⚪️⚪️⚪️⚪️⚪️🔘⚪️⚪️🔘🔘🔘⚪️
	N.79TinySeed          ⚪️⚪️⚪️⚪️⚪️🔘⚪️⚪️🔘🔘🔘🔘
	N.80TinySeed          ⚪️⚪️⚪️⚪️⚪️🔘⚪️🔘⚪️⚪️⚪️⚪️
	N.81TinySeed          ⚪️⚪️⚪️⚪️⚪️🔘⚪️🔘⚪️⚪️⚪️🔘
	N.82TinySeed          ⚪️⚪️⚪️⚪️⚪️🔘⚪️🔘⚪️⚪️🔘⚪️
	N.83TinySeed          ⚪️⚪️⚪️⚪️⚪️🔘⚪️🔘⚪️⚪️🔘🔘
	N.84TinySeed          ⚪️⚪️⚪️⚪️⚪️🔘⚪️🔘⚪️🔘⚪️⚪️
	N.85TinySeed          ⚪️⚪️⚪️⚪️⚪️🔘⚪️🔘⚪️🔘⚪️🔘
	N.86TinySeed          ⚪️⚪️⚪️⚪️⚪️🔘⚪️🔘⚪️🔘🔘⚪️
	N.87TinySeed          ⚪️⚪️⚪️⚪️⚪️🔘⚪️🔘⚪️🔘🔘🔘
	N.88TinySeed          ⚪️⚪️⚪️⚪️⚪️🔘⚪️🔘🔘⚪️⚪️⚪️
	N.89TinySeed          ⚪️⚪️⚪️⚪️⚪️🔘⚪️🔘🔘⚪️⚪️🔘
	N.90TinySeed          ⚪️⚪️⚪️⚪️⚪️🔘⚪️🔘🔘⚪️🔘⚪️
	N.91TinySeed          ⚪️⚪️⚪️⚪️⚪️🔘⚪️🔘🔘⚪️🔘🔘
	N.92TinySeed          ⚪️⚪️⚪️⚪️⚪️🔘⚪️🔘🔘🔘⚪️⚪️
	N.93TinySeed          ⚪️⚪️⚪️⚪️⚪️🔘⚪️🔘🔘🔘⚪️🔘
	N.94TinySeed          ⚪️⚪️⚪️⚪️⚪️🔘⚪️🔘🔘🔘🔘⚪️
	N.95TinySeed          ⚪️⚪️⚪️⚪️⚪️🔘⚪️🔘🔘🔘🔘🔘
	N.96TinySeed          ⚪️⚪️⚪️⚪️⚪️🔘🔘⚪️⚪️⚪️⚪️⚪️
	N.97TinySeed          ⚪️⚪️⚪️⚪️⚪️🔘🔘⚪️⚪️⚪️⚪️🔘
	N.98TinySeed          ⚪️⚪️⚪️⚪️⚪️🔘🔘⚪️⚪️⚪️🔘⚪️
	N.99TinySeed          ⚪️⚪️⚪️⚪️⚪️🔘🔘⚪️⚪️⚪️🔘🔘
	N.100TinySeed          ⚪️⚪️⚪️⚪️⚪️🔘🔘⚪️⚪️🔘⚪️⚪️
	N.101TinySeed          ⚪️⚪️⚪️⚪️⚪️🔘🔘⚪️⚪️🔘⚪️🔘
	N.102TinySeed          ⚪️⚪️⚪️⚪️⚪️🔘🔘⚪️⚪️🔘🔘⚪️
	N.103TinySeed          ⚪️⚪️⚪️⚪️⚪️🔘🔘⚪️⚪️🔘🔘🔘
	N.104TinySeed          ⚪️⚪️⚪️⚪️⚪️🔘🔘⚪️🔘⚪️⚪️⚪️
	N.105TinySeed          ⚪️⚪️⚪️⚪️⚪️🔘🔘⚪️🔘⚪️⚪️🔘
	N.106TinySeed          ⚪️⚪️⚪️⚪️⚪️🔘🔘⚪️🔘⚪️🔘⚪️
	N.107TinySeed          ⚪️⚪️⚪️⚪️⚪️🔘🔘⚪️🔘⚪️🔘🔘
	N.108TinySeed          ⚪️⚪️⚪️⚪️⚪️🔘🔘⚪️🔘🔘⚪️⚪️
	N.109TinySeed          ⚪️⚪️⚪️⚪️⚪️🔘🔘⚪️🔘🔘⚪️🔘
	N.110TinySeed          ⚪️⚪️⚪️⚪️⚪️🔘🔘⚪️🔘🔘🔘⚪️
	N.111TinySeed          ⚪️⚪️⚪️⚪️⚪️🔘🔘⚪️🔘🔘🔘🔘
	N.112TinySeed          ⚪️⚪️⚪️⚪️⚪️🔘🔘🔘⚪️⚪️⚪️⚪️
	N.113TinySeed          ⚪️⚪️⚪️⚪️⚪️🔘🔘🔘⚪️⚪️⚪️🔘
	N.114TinySeed          ⚪️⚪️⚪️⚪️⚪️🔘🔘🔘⚪️⚪️🔘⚪️
	N.115TinySeed          ⚪️⚪️⚪️⚪️⚪️🔘🔘🔘⚪️⚪️🔘🔘
	N.116TinySeed          ⚪️⚪️⚪️⚪️⚪️🔘🔘🔘⚪️🔘⚪️⚪️
	N.117TinySeed          ⚪️⚪️⚪️⚪️⚪️🔘🔘🔘⚪️🔘⚪️🔘
	N.118TinySeed          ⚪️⚪️⚪️⚪️⚪️🔘🔘🔘⚪️🔘🔘⚪️
	N.119TinySeed          ⚪️⚪️⚪️⚪️⚪️🔘🔘🔘⚪️🔘🔘🔘
	N.120TinySeed          ⚪️⚪️⚪️⚪️⚪️🔘🔘🔘🔘⚪️⚪️⚪️
	N.121TinySeed          ⚪️⚪️⚪️⚪️⚪️🔘🔘🔘🔘⚪️⚪️🔘
	N.122TinySeed          ⚪️⚪️⚪️⚪️⚪️🔘🔘🔘🔘⚪️🔘⚪️
	N.123TinySeed          ⚪️⚪️⚪️⚪️⚪️🔘🔘🔘🔘⚪️🔘🔘
	N.124TinySeed          ⚪️⚪️⚪️⚪️⚪️🔘🔘🔘🔘🔘⚪️⚪️
	N.125TinySeed          ⚪️⚪️⚪️⚪️⚪️🔘🔘🔘🔘🔘⚪️🔘
	N.126TinySeed          ⚪️⚪️⚪️⚪️⚪️🔘🔘🔘🔘🔘🔘⚪️
	N.127TinySeed          ⚪️⚪️⚪️⚪️⚪️🔘🔘🔘🔘🔘🔘🔘
	N.128TinySeed          ⚪️⚪️⚪️⚪️🔘⚪️⚪️⚪️⚪️⚪️⚪️⚪️
	N.129TinySeed          ⚪️⚪️⚪️⚪️🔘⚪️⚪️⚪️⚪️⚪️⚪️🔘
	N.130TinySeed          ⚪️⚪️⚪️⚪️🔘⚪️⚪️⚪️⚪️⚪️🔘⚪️
	N.131TinySeed          ⚪️⚪️⚪️⚪️🔘⚪️⚪️⚪️⚪️⚪️🔘🔘
	N.132TinySeed          ⚪️⚪️⚪️⚪️🔘⚪️⚪️⚪️⚪️🔘⚪️⚪️
	N.133TinySeed          ⚪️⚪️⚪️⚪️🔘⚪️⚪️⚪️⚪️🔘⚪️🔘
	N.134TinySeed          ⚪️⚪️⚪️⚪️🔘⚪️⚪️⚪️⚪️🔘🔘⚪️
	N.135TinySeed          ⚪️⚪️⚪️⚪️🔘⚪️⚪️⚪️⚪️🔘🔘🔘
	N.136TinySeed          ⚪️⚪️⚪️⚪️🔘⚪️⚪️⚪️🔘⚪️⚪️⚪️
	N.137TinySeed          ⚪️⚪️⚪️⚪️🔘⚪️⚪️⚪️🔘⚪️⚪️🔘
	N.138TinySeed          ⚪️⚪️⚪️⚪️🔘⚪️⚪️⚪️🔘⚪️🔘⚪️
	N.139TinySeed          ⚪️⚪️⚪️⚪️🔘⚪️⚪️⚪️🔘⚪️🔘🔘
	N.140TinySeed          ⚪️⚪️⚪️⚪️🔘⚪️⚪️⚪️🔘🔘⚪️⚪️
	N.141TinySeed          ⚪️⚪️⚪️⚪️🔘⚪️⚪️⚪️🔘🔘⚪️🔘
	N.142TinySeed          ⚪️⚪️⚪️⚪️🔘⚪️⚪️⚪️🔘🔘🔘⚪️
	N.143TinySeed          ⚪️⚪️⚪️⚪️🔘⚪️⚪️⚪️🔘🔘🔘🔘
	N.144TinySeed          ⚪️⚪️⚪️⚪️🔘⚪️⚪️🔘⚪️⚪️⚪️⚪️
	N.145TinySeed          ⚪️⚪️⚪️⚪️🔘⚪️⚪️🔘⚪️⚪️⚪️🔘
	N.146TinySeed          ⚪️⚪️⚪️⚪️🔘⚪️⚪️🔘⚪️⚪️🔘⚪️
	N.147TinySeed          ⚪️⚪️⚪️⚪️🔘⚪️⚪️🔘⚪️⚪️🔘🔘
	N.148TinySeed          ⚪️⚪️⚪️⚪️🔘⚪️⚪️🔘⚪️🔘⚪️⚪️
	N.149TinySeed          ⚪️⚪️⚪️⚪️🔘⚪️⚪️🔘⚪️🔘⚪️🔘
	N.150TinySeed          ⚪️⚪️⚪️⚪️🔘⚪️⚪️🔘⚪️🔘🔘⚪️
	N.151TinySeed          ⚪️⚪️⚪️⚪️🔘⚪️⚪️🔘⚪️🔘🔘🔘
	N.152TinySeed          ⚪️⚪️⚪️⚪️🔘⚪️⚪️🔘🔘⚪️⚪️⚪️
	N.153TinySeed          ⚪️⚪️⚪️⚪️🔘⚪️⚪️🔘🔘⚪️⚪️🔘
	N.154TinySeed          ⚪️⚪️⚪️⚪️🔘⚪️⚪️🔘🔘⚪️🔘⚪️
	N.155TinySeed          ⚪️⚪️⚪️⚪️🔘⚪️⚪️🔘🔘⚪️🔘🔘
	N.156TinySeed          ⚪️⚪️⚪️⚪️🔘⚪️⚪️🔘🔘🔘⚪️⚪️
	N.157TinySeed          ⚪️⚪️⚪️⚪️🔘⚪️⚪️🔘🔘🔘⚪️🔘
	N.158TinySeed          ⚪️⚪️⚪️⚪️🔘⚪️⚪️🔘🔘🔘🔘⚪️
	N.159TinySeed          ⚪️⚪️⚪️⚪️🔘⚪️⚪️🔘🔘🔘🔘🔘
	N.160TinySeed          ⚪️⚪️⚪️⚪️🔘⚪️🔘⚪️⚪️⚪️⚪️⚪️
	N.161TinySeed          ⚪️⚪️⚪️⚪️🔘⚪️🔘⚪️⚪️⚪️⚪️🔘
	N.162TinySeed          ⚪️⚪️⚪️⚪️🔘⚪️🔘⚪️⚪️⚪️🔘⚪️
	N.163TinySeed          ⚪️⚪️⚪️⚪️🔘⚪️🔘⚪️⚪️⚪️🔘🔘
	N.164TinySeed          ⚪️⚪️⚪️⚪️🔘⚪️🔘⚪️⚪️🔘⚪️⚪️
	N.165TinySeed          ⚪️⚪️⚪️⚪️🔘⚪️🔘⚪️⚪️🔘⚪️🔘
	N.166TinySeed          ⚪️⚪️⚪️⚪️🔘⚪️🔘⚪️⚪️🔘🔘⚪️
	N.167TinySeed          ⚪️⚪️⚪️⚪️🔘⚪️🔘⚪️⚪️🔘🔘🔘
	N.168TinySeed          ⚪️⚪️⚪️⚪️🔘⚪️🔘⚪️🔘⚪️⚪️⚪️
	N.169TinySeed          ⚪️⚪️⚪️⚪️🔘⚪️🔘⚪️🔘⚪️⚪️🔘
	N.170TinySeed          ⚪️⚪️⚪️⚪️🔘⚪️🔘⚪️🔘⚪️🔘⚪️
	N.171TinySeed          ⚪️⚪️⚪️⚪️🔘⚪️🔘⚪️🔘⚪️🔘🔘
	N.172TinySeed          ⚪️⚪️⚪️⚪️🔘⚪️🔘⚪️🔘🔘⚪️⚪️
	N.173TinySeed          ⚪️⚪️⚪️⚪️🔘⚪️🔘⚪️🔘🔘⚪️🔘
	N.174TinySeed          ⚪️⚪️⚪️⚪️🔘⚪️🔘⚪️🔘🔘🔘⚪️
	N.175TinySeed          ⚪️⚪️⚪️⚪️🔘⚪️🔘⚪️🔘🔘🔘🔘
	N.176TinySeed          ⚪️⚪️⚪️⚪️🔘⚪️🔘🔘⚪️⚪️⚪️⚪️
	N.177TinySeed          ⚪️⚪️⚪️⚪️🔘⚪️🔘🔘⚪️⚪️⚪️🔘
	N.178TinySeed          ⚪️⚪️⚪️⚪️🔘⚪️🔘🔘⚪️⚪️🔘⚪️
	N.179TinySeed          ⚪️⚪️⚪️⚪️🔘⚪️🔘🔘⚪️⚪️🔘🔘
	N.180TinySeed          ⚪️⚪️⚪️⚪️🔘⚪️🔘🔘⚪️🔘⚪️⚪️
	N.181TinySeed          ⚪️⚪️⚪️⚪️🔘⚪️🔘🔘⚪️🔘⚪️🔘
	N.182TinySeed          ⚪️⚪️⚪️⚪️🔘⚪️🔘🔘⚪️🔘🔘⚪️
	N.183TinySeed          ⚪️⚪️⚪️⚪️🔘⚪️🔘🔘⚪️🔘🔘🔘
	N.184TinySeed          ⚪️⚪️⚪️⚪️🔘⚪️🔘🔘🔘⚪️⚪️⚪️
	N.185TinySeed          ⚪️⚪️⚪️⚪️🔘⚪️🔘🔘🔘⚪️⚪️🔘
	N.186TinySeed          ⚪️⚪️⚪️⚪️🔘⚪️🔘🔘🔘⚪️🔘⚪️
	N.187TinySeed          ⚪️⚪️⚪️⚪️🔘⚪️🔘🔘🔘⚪️🔘🔘
	N.188TinySeed          ⚪️⚪️⚪️⚪️🔘⚪️🔘🔘🔘🔘⚪️⚪️
	N.189TinySeed          ⚪️⚪️⚪️⚪️🔘⚪️🔘🔘🔘🔘⚪️🔘
	N.190TinySeed          ⚪️⚪️⚪️⚪️🔘⚪️🔘🔘🔘🔘🔘⚪️
	N.191TinySeed          ⚪️⚪️⚪️⚪️🔘⚪️🔘🔘🔘🔘🔘🔘
	N.192TinySeed          ⚪️⚪️⚪️⚪️🔘🔘⚪️⚪️⚪️⚪️⚪️⚪️
	N.193TinySeed          ⚪️⚪️⚪️⚪️🔘🔘⚪️⚪️⚪️⚪️⚪️🔘
	N.194TinySeed          ⚪️⚪️⚪️⚪️🔘🔘⚪️⚪️⚪️⚪️🔘⚪️
	N.195TinySeed          ⚪️⚪️⚪️⚪️🔘🔘⚪️⚪️⚪️⚪️🔘🔘
	N.196TinySeed          ⚪️⚪️⚪️⚪️🔘🔘⚪️⚪️⚪️🔘⚪️⚪️
	N.197TinySeed          ⚪️⚪️⚪️⚪️🔘🔘⚪️⚪️⚪️🔘⚪️🔘
	N.198TinySeed          ⚪️⚪️⚪️⚪️🔘🔘⚪️⚪️⚪️🔘🔘⚪️
	N.199TinySeed          ⚪️⚪️⚪️⚪️🔘🔘⚪️⚪️⚪️🔘🔘🔘
	N.200TinySeed          ⚪️⚪️⚪️⚪️🔘🔘⚪️⚪️🔘⚪️⚪️⚪️
	N.201TinySeed          ⚪️⚪️⚪️⚪️🔘🔘⚪️⚪️🔘⚪️⚪️🔘
	N.202TinySeed          ⚪️⚪️⚪️⚪️🔘🔘⚪️⚪️🔘⚪️🔘⚪️
	N.203TinySeed          ⚪️⚪️⚪️⚪️🔘🔘⚪️⚪️🔘⚪️🔘🔘
	N.204TinySeed          ⚪️⚪️⚪️⚪️🔘🔘⚪️⚪️🔘🔘⚪️⚪️
	N.205TinySeed          ⚪️⚪️⚪️⚪️🔘🔘⚪️⚪️🔘🔘⚪️🔘
	N.206TinySeed          ⚪️⚪️⚪️⚪️🔘🔘⚪️⚪️🔘🔘🔘⚪️
	N.207TinySeed          ⚪️⚪️⚪️⚪️🔘🔘⚪️⚪️🔘🔘🔘🔘
	N.208TinySeed          ⚪️⚪️⚪️⚪️🔘🔘⚪️🔘⚪️⚪️⚪️⚪️
	N.209TinySeed          ⚪️⚪️⚪️⚪️🔘🔘⚪️🔘⚪️⚪️⚪️🔘
	N.210TinySeed          ⚪️⚪️⚪️⚪️🔘🔘⚪️🔘⚪️⚪️🔘⚪️
	N.211TinySeed          ⚪️⚪️⚪️⚪️🔘🔘⚪️🔘⚪️⚪️🔘🔘
	N.212TinySeed          ⚪️⚪️⚪️⚪️🔘🔘⚪️🔘⚪️🔘⚪️⚪️
	N.213TinySeed          ⚪️⚪️⚪️⚪️🔘🔘⚪️🔘⚪️🔘⚪️🔘
	N.214TinySeed          ⚪️⚪️⚪️⚪️🔘🔘⚪️🔘⚪️🔘🔘⚪️
	N.215TinySeed          ⚪️⚪️⚪️⚪️🔘🔘⚪️🔘⚪️🔘🔘🔘
	N.216TinySeed          ⚪️⚪️⚪️⚪️🔘🔘⚪️🔘🔘⚪️⚪️⚪️
	N.217TinySeed          ⚪️⚪️⚪️⚪️🔘🔘⚪️🔘🔘⚪️⚪️🔘
	N.218TinySeed          ⚪️⚪️⚪️⚪️🔘🔘⚪️🔘🔘⚪️🔘⚪️
	N.219TinySeed          ⚪️⚪️⚪️⚪️🔘🔘⚪️🔘🔘⚪️🔘🔘
	N.220TinySeed          ⚪️⚪️⚪️⚪️🔘🔘⚪️🔘🔘🔘⚪️⚪️
	N.221TinySeed          ⚪️⚪️⚪️⚪️🔘🔘⚪️🔘🔘🔘⚪️🔘
	N.222TinySeed          ⚪️⚪️⚪️⚪️🔘🔘⚪️🔘🔘🔘🔘⚪️
	N.223TinySeed          ⚪️⚪️⚪️⚪️🔘🔘⚪️🔘🔘🔘🔘🔘
	N.224TinySeed          ⚪️⚪️⚪️⚪️🔘🔘🔘⚪️⚪️⚪️⚪️⚪️
	N.225TinySeed          ⚪️⚪️⚪️⚪️🔘🔘🔘⚪️⚪️⚪️⚪️🔘
	N.226TinySeed          ⚪️⚪️⚪️⚪️🔘🔘🔘⚪️⚪️⚪️🔘⚪️
	N.227TinySeed          ⚪️⚪️⚪️⚪️🔘🔘🔘⚪️⚪️⚪️🔘🔘
	N.228TinySeed          ⚪️⚪️⚪️⚪️🔘🔘🔘⚪️⚪️🔘⚪️⚪️
	N.229TinySeed          ⚪️⚪️⚪️⚪️🔘🔘🔘⚪️⚪️🔘⚪️🔘
	N.230TinySeed          ⚪️⚪️⚪️⚪️🔘🔘🔘⚪️⚪️🔘🔘⚪️
	N.231TinySeed          ⚪️⚪️⚪️⚪️🔘🔘🔘⚪️⚪️🔘🔘🔘
	N.232TinySeed          ⚪️⚪️⚪️⚪️🔘🔘🔘⚪️🔘⚪️⚪️⚪️
	N.233TinySeed          ⚪️⚪️⚪️⚪️🔘🔘🔘⚪️🔘⚪️⚪️🔘
	N.234TinySeed          ⚪️⚪️⚪️⚪️🔘🔘🔘⚪️🔘⚪️🔘⚪️
	N.235TinySeed          ⚪️⚪️⚪️⚪️🔘🔘🔘⚪️🔘⚪️🔘🔘
	N.236TinySeed          ⚪️⚪️⚪️⚪️🔘🔘🔘⚪️🔘🔘⚪️⚪️
	N.237TinySeed          ⚪️⚪️⚪️⚪️🔘🔘🔘⚪️🔘🔘⚪️🔘
	N.238TinySeed          ⚪️⚪️⚪️⚪️🔘🔘🔘⚪️🔘🔘🔘⚪️
	N.239TinySeed          ⚪️⚪️⚪️⚪️🔘🔘🔘⚪️🔘🔘🔘🔘
	N.240TinySeed          ⚪️⚪️⚪️⚪️🔘🔘🔘🔘⚪️⚪️⚪️⚪️
	N.241TinySeed          ⚪️⚪️⚪️⚪️🔘🔘🔘🔘⚪️⚪️⚪️🔘
	N.242TinySeed          ⚪️⚪️⚪️⚪️🔘🔘🔘🔘⚪️⚪️🔘⚪️
	N.243TinySeed          ⚪️⚪️⚪️⚪️🔘🔘🔘🔘⚪️⚪️🔘🔘
	N.244TinySeed          ⚪️⚪️⚪️⚪️🔘🔘🔘🔘⚪️🔘⚪️⚪️
	N.245TinySeed          ⚪️⚪️⚪️⚪️🔘🔘🔘🔘⚪️🔘⚪️🔘
	N.246TinySeed          ⚪️⚪️⚪️⚪️🔘🔘🔘🔘⚪️🔘🔘⚪️
	N.247TinySeed          ⚪️⚪️⚪️⚪️🔘🔘🔘🔘⚪️🔘🔘🔘
	N.248TinySeed          ⚪️⚪️⚪️⚪️🔘🔘🔘🔘🔘⚪️⚪️⚪️
	N.249TinySeed          ⚪️⚪️⚪️⚪️🔘🔘🔘🔘🔘⚪️⚪️🔘
	N.250TinySeed          ⚪️⚪️⚪️⚪️🔘🔘🔘🔘🔘⚪️🔘⚪️
	N.251TinySeed          ⚪️⚪️⚪️⚪️🔘🔘🔘🔘🔘⚪️🔘🔘
	N.252TinySeed          ⚪️⚪️⚪️⚪️🔘🔘🔘🔘🔘🔘⚪️⚪️
	N.253TinySeed          ⚪️⚪️⚪️⚪️🔘🔘🔘🔘🔘🔘⚪️🔘
	N.254TinySeed          ⚪️⚪️⚪️⚪️🔘🔘🔘🔘🔘🔘🔘⚪️
	N.255TinySeed          ⚪️⚪️⚪️⚪️🔘🔘🔘🔘🔘🔘🔘🔘
	N.256TinySeed          ⚪️⚪️⚪️🔘⚪️⚪️⚪️⚪️⚪️⚪️⚪️⚪️
	N.257TinySeed          ⚪️⚪️⚪️🔘⚪️⚪️⚪️⚪️⚪️⚪️⚪️🔘
	N.258TinySeed          ⚪️⚪️⚪️🔘⚪️⚪️⚪️⚪️⚪️⚪️🔘⚪️
	N.259TinySeed          ⚪️⚪️⚪️🔘⚪️⚪️⚪️⚪️⚪️⚪️🔘🔘
	N.260TinySeed          ⚪️⚪️⚪️🔘⚪️⚪️⚪️⚪️⚪️🔘⚪️⚪️
	N.261TinySeed          ⚪️⚪️⚪️🔘⚪️⚪️⚪️⚪️⚪️🔘⚪️🔘
	N.262TinySeed          ⚪️⚪️⚪️🔘⚪️⚪️⚪️⚪️⚪️🔘🔘⚪️
	N.263TinySeed          ⚪️⚪️⚪️🔘⚪️⚪️⚪️⚪️⚪️🔘🔘🔘
	N.264TinySeed          ⚪️⚪️⚪️🔘⚪️⚪️⚪️⚪️🔘⚪️⚪️⚪️
	N.265TinySeed          ⚪️⚪️⚪️🔘⚪️⚪️⚪️⚪️🔘⚪️⚪️🔘
	N.266TinySeed          ⚪️⚪️⚪️🔘⚪️⚪️⚪️⚪️🔘⚪️🔘⚪️
	N.267TinySeed          ⚪️⚪️⚪️🔘⚪️⚪️⚪️⚪️🔘⚪️🔘🔘
	N.268TinySeed          ⚪️⚪️⚪️🔘⚪️⚪️⚪️⚪️🔘🔘⚪️⚪️
	N.269TinySeed          ⚪️⚪️⚪️🔘⚪️⚪️⚪️⚪️🔘🔘⚪️🔘
	N.270TinySeed          ⚪️⚪️⚪️🔘⚪️⚪️⚪️⚪️🔘🔘🔘⚪️
	N.271TinySeed          ⚪️⚪️⚪️🔘⚪️⚪️⚪️⚪️🔘🔘🔘🔘
	N.272TinySeed          ⚪️⚪️⚪️🔘⚪️⚪️⚪️🔘⚪️⚪️⚪️⚪️
	N.273TinySeed          ⚪️⚪️⚪️🔘⚪️⚪️⚪️🔘⚪️⚪️⚪️🔘
	N.274TinySeed          ⚪️⚪️⚪️🔘⚪️⚪️⚪️🔘⚪️⚪️🔘⚪️
	N.275TinySeed          ⚪️⚪️⚪️🔘⚪️⚪️⚪️🔘⚪️⚪️🔘🔘
	N.276TinySeed          ⚪️⚪️⚪️🔘⚪️⚪️⚪️🔘⚪️🔘⚪️⚪️
	N.277TinySeed          ⚪️⚪️⚪️🔘⚪️⚪️⚪️🔘⚪️🔘⚪️🔘
	N.278TinySeed          ⚪️⚪️⚪️🔘⚪️⚪️⚪️🔘⚪️🔘🔘⚪️
	N.279TinySeed          ⚪️⚪️⚪️🔘⚪️⚪️⚪️🔘⚪️🔘🔘🔘
	N.280TinySeed          ⚪️⚪️⚪️🔘⚪️⚪️⚪️🔘🔘⚪️⚪️⚪️
	N.281TinySeed          ⚪️⚪️⚪️🔘⚪️⚪️⚪️🔘🔘⚪️⚪️🔘
	N.282TinySeed          ⚪️⚪️⚪️🔘⚪️⚪️⚪️🔘🔘⚪️🔘⚪️
	N.283TinySeed          ⚪️⚪️⚪️🔘⚪️⚪️⚪️🔘🔘⚪️🔘🔘
	N.284TinySeed          ⚪️⚪️⚪️🔘⚪️⚪️⚪️🔘🔘🔘⚪️⚪️
	N.285TinySeed          ⚪️⚪️⚪️🔘⚪️⚪️⚪️🔘🔘🔘⚪️🔘
	N.286TinySeed          ⚪️⚪️⚪️🔘⚪️⚪️⚪️🔘🔘🔘🔘⚪️
	N.287TinySeed          ⚪️⚪️⚪️🔘⚪️⚪️⚪️🔘🔘🔘🔘🔘
	N.288TinySeed          ⚪️⚪️⚪️🔘⚪️⚪️🔘⚪️⚪️⚪️⚪️⚪️
	N.289TinySeed          ⚪️⚪️⚪️🔘⚪️⚪️🔘⚪️⚪️⚪️⚪️🔘
	N.290TinySeed          ⚪️⚪️⚪️🔘⚪️⚪️🔘⚪️⚪️⚪️🔘⚪️
	N.291TinySeed          ⚪️⚪️⚪️🔘⚪️⚪️🔘⚪️⚪️⚪️🔘🔘
	N.292TinySeed          ⚪️⚪️⚪️🔘⚪️⚪️🔘⚪️⚪️🔘⚪️⚪️
	N.293TinySeed          ⚪️⚪️⚪️🔘⚪️⚪️🔘⚪️⚪️🔘⚪️🔘
	N.294TinySeed          ⚪️⚪️⚪️🔘⚪️⚪️🔘⚪️⚪️🔘🔘⚪️
	N.295TinySeed          ⚪️⚪️⚪️🔘⚪️⚪️🔘⚪️⚪️🔘🔘🔘
	N.296TinySeed          ⚪️⚪️⚪️🔘⚪️⚪️🔘⚪️🔘⚪️⚪️⚪️
	N.297TinySeed          ⚪️⚪️⚪️🔘⚪️⚪️🔘⚪️🔘⚪️⚪️🔘
	N.298TinySeed          ⚪️⚪️⚪️🔘⚪️⚪️🔘⚪️🔘⚪️🔘⚪️
	N.299TinySeed          ⚪️⚪️⚪️🔘⚪️⚪️🔘⚪️🔘⚪️🔘🔘
	N.300TinySeed          ⚪️⚪️⚪️🔘⚪️⚪️🔘⚪️🔘🔘⚪️⚪️
	N.301TinySeed          ⚪️⚪️⚪️🔘⚪️⚪️🔘⚪️🔘🔘⚪️🔘
	N.302TinySeed          ⚪️⚪️⚪️🔘⚪️⚪️🔘⚪️🔘🔘🔘⚪️
	N.303TinySeed          ⚪️⚪️⚪️🔘⚪️⚪️🔘⚪️🔘🔘🔘🔘
	N.304TinySeed          ⚪️⚪️⚪️🔘⚪️⚪️🔘🔘⚪️⚪️⚪️⚪️
	N.305TinySeed          ⚪️⚪️⚪️🔘⚪️⚪️🔘🔘⚪️⚪️⚪️🔘
	N.306TinySeed          ⚪️⚪️⚪️🔘⚪️⚪️🔘🔘⚪️⚪️🔘⚪️
	N.307TinySeed          ⚪️⚪️⚪️🔘⚪️⚪️🔘🔘⚪️⚪️🔘🔘
	N.308TinySeed          ⚪️⚪️⚪️🔘⚪️⚪️🔘🔘⚪️🔘⚪️⚪️
	N.309TinySeed          ⚪️⚪️⚪️🔘⚪️⚪️🔘🔘⚪️🔘⚪️🔘
	N.310TinySeed          ⚪️⚪️⚪️🔘⚪️⚪️🔘🔘⚪️🔘🔘⚪️
	N.311TinySeed          ⚪️⚪️⚪️🔘⚪️⚪️🔘🔘⚪️🔘🔘🔘
	N.312TinySeed          ⚪️⚪️⚪️🔘⚪️⚪️🔘🔘🔘⚪️⚪️⚪️
	N.313TinySeed          ⚪️⚪️⚪️🔘⚪️⚪️🔘🔘🔘⚪️⚪️🔘
	N.314TinySeed          ⚪️⚪️⚪️🔘⚪️⚪️🔘🔘🔘⚪️🔘⚪️
	N.315TinySeed          ⚪️⚪️⚪️🔘⚪️⚪️🔘🔘🔘⚪️🔘🔘
	N.316TinySeed          ⚪️⚪️⚪️🔘⚪️⚪️🔘🔘🔘🔘⚪️⚪️
	N.317TinySeed          ⚪️⚪️⚪️🔘⚪️⚪️🔘🔘🔘🔘⚪️🔘
	N.318TinySeed          ⚪️⚪️⚪️🔘⚪️⚪️🔘🔘🔘🔘🔘⚪️
	N.319TinySeed          ⚪️⚪️⚪️🔘⚪️⚪️🔘🔘🔘🔘🔘🔘
	N.320TinySeed          ⚪️⚪️⚪️🔘⚪️🔘⚪️⚪️⚪️⚪️⚪️⚪️
	N.321TinySeed          ⚪️⚪️⚪️🔘⚪️🔘⚪️⚪️⚪️⚪️⚪️🔘
	N.322TinySeed          ⚪️⚪️⚪️🔘⚪️🔘⚪️⚪️⚪️⚪️🔘⚪️
	N.323TinySeed          ⚪️⚪️⚪️🔘⚪️🔘⚪️⚪️⚪️⚪️🔘🔘
	N.324TinySeed          ⚪️⚪️⚪️🔘⚪️🔘⚪️⚪️⚪️🔘⚪️⚪️
	N.325TinySeed          ⚪️⚪️⚪️🔘⚪️🔘⚪️⚪️⚪️🔘⚪️🔘
	N.326TinySeed          ⚪️⚪️⚪️🔘⚪️🔘⚪️⚪️⚪️🔘🔘⚪️
	N.327TinySeed          ⚪️⚪️⚪️🔘⚪️🔘⚪️⚪️⚪️🔘🔘🔘
	N.328TinySeed          ⚪️⚪️⚪️🔘⚪️🔘⚪️⚪️🔘⚪️⚪️⚪️
	N.329TinySeed          ⚪️⚪️⚪️🔘⚪️🔘⚪️⚪️🔘⚪️⚪️🔘
	N.330TinySeed          ⚪️⚪️⚪️🔘⚪️🔘⚪️⚪️🔘⚪️🔘⚪️
	N.331TinySeed          ⚪️⚪️⚪️🔘⚪️🔘⚪️⚪️🔘⚪️🔘🔘
	N.332TinySeed          ⚪️⚪️⚪️🔘⚪️🔘⚪️⚪️🔘🔘⚪️⚪️
	N.333TinySeed          ⚪️⚪️⚪️🔘⚪️🔘⚪️⚪️🔘🔘⚪️🔘
	N.334TinySeed          ⚪️⚪️⚪️🔘⚪️🔘⚪️⚪️🔘🔘🔘⚪️
	N.335TinySeed          ⚪️⚪️⚪️🔘⚪️🔘⚪️⚪️🔘🔘🔘🔘
	N.336TinySeed          ⚪️⚪️⚪️🔘⚪️🔘⚪️🔘⚪️⚪️⚪️⚪️
	N.337TinySeed          ⚪️⚪️⚪️🔘⚪️🔘⚪️🔘⚪️⚪️⚪️🔘
	N.338TinySeed          ⚪️⚪️⚪️🔘⚪️🔘⚪️🔘⚪️⚪️🔘⚪️
	N.339TinySeed          ⚪️⚪️⚪️🔘⚪️🔘⚪️🔘⚪️⚪️🔘🔘
	N.340TinySeed          ⚪️⚪️⚪️🔘⚪️🔘⚪️🔘⚪️🔘⚪️⚪️
	N.341TinySeed          ⚪️⚪️⚪️🔘⚪️🔘⚪️🔘⚪️🔘⚪️🔘
	N.342TinySeed          ⚪️⚪️⚪️🔘⚪️🔘⚪️🔘⚪️🔘🔘⚪️
	N.343TinySeed          ⚪️⚪️⚪️🔘⚪️🔘⚪️🔘⚪️🔘🔘🔘
	N.344TinySeed          ⚪️⚪️⚪️🔘⚪️🔘⚪️🔘🔘⚪️⚪️⚪️
	N.345TinySeed          ⚪️⚪️⚪️🔘⚪️🔘⚪️🔘🔘⚪️⚪️🔘
	N.346TinySeed          ⚪️⚪️⚪️🔘⚪️🔘⚪️🔘🔘⚪️🔘⚪️
	N.347TinySeed          ⚪️⚪️⚪️🔘⚪️🔘⚪️🔘🔘⚪️🔘🔘
	N.348TinySeed          ⚪️⚪️⚪️🔘⚪️🔘⚪️🔘🔘🔘⚪️⚪️
	N.349TinySeed          ⚪️⚪️⚪️🔘⚪️🔘⚪️🔘🔘🔘⚪️🔘
	N.350TinySeed          ⚪️⚪️⚪️🔘⚪️🔘⚪️🔘🔘🔘🔘⚪️
	N.351TinySeed          ⚪️⚪️⚪️🔘⚪️🔘⚪️🔘🔘🔘🔘🔘
	N.352TinySeed          ⚪️⚪️⚪️🔘⚪️🔘🔘⚪️⚪️⚪️⚪️⚪️
	N.353TinySeed          ⚪️⚪️⚪️🔘⚪️🔘🔘⚪️⚪️⚪️⚪️🔘
	N.354TinySeed          ⚪️⚪️⚪️🔘⚪️🔘🔘⚪️⚪️⚪️🔘⚪️
	N.355TinySeed          ⚪️⚪️⚪️🔘⚪️🔘🔘⚪️⚪️⚪️🔘🔘
	N.356TinySeed          ⚪️⚪️⚪️🔘⚪️🔘🔘⚪️⚪️🔘⚪️⚪️
	N.357TinySeed          ⚪️⚪️⚪️🔘⚪️🔘🔘⚪️⚪️🔘⚪️🔘
	N.358TinySeed          ⚪️⚪️⚪️🔘⚪️🔘🔘⚪️⚪️🔘🔘⚪️
	N.359TinySeed          ⚪️⚪️⚪️🔘⚪️🔘🔘⚪️⚪️🔘🔘🔘
	N.360TinySeed          ⚪️⚪️⚪️🔘⚪️🔘🔘⚪️🔘⚪️⚪️⚪️
	N.361TinySeed          ⚪️⚪️⚪️🔘⚪️🔘🔘⚪️🔘⚪️⚪️🔘
	N.362TinySeed          ⚪️⚪️⚪️🔘⚪️🔘🔘⚪️🔘⚪️🔘⚪️
	N.363TinySeed          ⚪️⚪️⚪️🔘⚪️🔘🔘⚪️🔘⚪️🔘🔘
	N.364TinySeed          ⚪️⚪️⚪️🔘⚪️🔘🔘⚪️🔘🔘⚪️⚪️
	N.365TinySeed          ⚪️⚪️⚪️🔘⚪️🔘🔘⚪️🔘🔘⚪️🔘
	N.366TinySeed          ⚪️⚪️⚪️🔘⚪️🔘🔘⚪️🔘🔘🔘⚪️
	N.367TinySeed          ⚪️⚪️⚪️🔘⚪️🔘🔘⚪️🔘🔘🔘🔘
	N.368TinySeed          ⚪️⚪️⚪️🔘⚪️🔘🔘🔘⚪️⚪️⚪️⚪️
	N.369TinySeed          ⚪️⚪️⚪️🔘⚪️🔘🔘🔘⚪️⚪️⚪️🔘
	N.370TinySeed          ⚪️⚪️⚪️🔘⚪️🔘🔘🔘⚪️⚪️🔘⚪️
	N.371TinySeed          ⚪️⚪️⚪️🔘⚪️🔘🔘🔘⚪️⚪️🔘🔘
	N.372TinySeed          ⚪️⚪️⚪️🔘⚪️🔘🔘🔘⚪️🔘⚪️⚪️
	N.373TinySeed          ⚪️⚪️⚪️🔘⚪️🔘🔘🔘⚪️🔘⚪️🔘
	N.374TinySeed          ⚪️⚪️⚪️🔘⚪️🔘🔘🔘⚪️🔘🔘⚪️
	N.375TinySeed          ⚪️⚪️⚪️🔘⚪️🔘🔘🔘⚪️🔘🔘🔘
	N.376TinySeed          ⚪️⚪️⚪️🔘⚪️🔘🔘🔘🔘⚪️⚪️⚪️
	N.377TinySeed          ⚪️⚪️⚪️🔘⚪️🔘🔘🔘🔘⚪️⚪️🔘
	N.378TinySeed          ⚪️⚪️⚪️🔘⚪️🔘🔘🔘🔘⚪️🔘⚪️
	N.379TinySeed          ⚪️⚪️⚪️🔘⚪️🔘🔘🔘🔘⚪️🔘🔘
	N.380TinySeed          ⚪️⚪️⚪️🔘⚪️🔘🔘🔘🔘🔘⚪️⚪️
	N.381TinySeed          ⚪️⚪️⚪️🔘⚪️🔘🔘🔘🔘🔘⚪️🔘
	N.382TinySeed          ⚪️⚪️⚪️🔘⚪️🔘🔘🔘🔘🔘🔘⚪️
	N.383TinySeed          ⚪️⚪️⚪️🔘⚪️🔘🔘🔘🔘🔘🔘🔘
	N.384TinySeed          ⚪️⚪️⚪️🔘🔘⚪️⚪️⚪️⚪️⚪️⚪️⚪️
	N.385TinySeed          ⚪️⚪️⚪️🔘🔘⚪️⚪️⚪️⚪️⚪️⚪️🔘
	N.386TinySeed          ⚪️⚪️⚪️🔘🔘⚪️⚪️⚪️⚪️⚪️🔘⚪️
	N.387TinySeed          ⚪️⚪️⚪️🔘🔘⚪️⚪️⚪️⚪️⚪️🔘🔘
	N.388TinySeed          ⚪️⚪️⚪️🔘🔘⚪️⚪️⚪️⚪️🔘⚪️⚪️
	N.389TinySeed          ⚪️⚪️⚪️🔘🔘⚪️⚪️⚪️⚪️🔘⚪️🔘
	N.390TinySeed          ⚪️⚪️⚪️🔘🔘⚪️⚪️⚪️⚪️🔘🔘⚪️
	N.391TinySeed          ⚪️⚪️⚪️🔘🔘⚪️⚪️⚪️⚪️🔘🔘🔘
	N.392TinySeed          ⚪️⚪️⚪️🔘🔘⚪️⚪️⚪️🔘⚪️⚪️⚪️
	N.393TinySeed          ⚪️⚪️⚪️🔘🔘⚪️⚪️⚪️🔘⚪️⚪️🔘
	N.394TinySeed          ⚪️⚪️⚪️🔘🔘⚪️⚪️⚪️🔘⚪️🔘⚪️
	N.395TinySeed          ⚪️⚪️⚪️🔘🔘⚪️⚪️⚪️🔘⚪️🔘🔘
	N.396TinySeed          ⚪️⚪️⚪️🔘🔘⚪️⚪️⚪️🔘🔘⚪️⚪️
	N.397TinySeed          ⚪️⚪️⚪️🔘🔘⚪️⚪️⚪️🔘🔘⚪️🔘
	N.398TinySeed          ⚪️⚪️⚪️🔘🔘⚪️⚪️⚪️🔘🔘🔘⚪️
	N.399TinySeed          ⚪️⚪️⚪️🔘🔘⚪️⚪️⚪️🔘🔘🔘🔘
	N.400TinySeed          ⚪️⚪️⚪️🔘🔘⚪️⚪️🔘⚪️⚪️⚪️⚪️
	N.401TinySeed          ⚪️⚪️⚪️🔘🔘⚪️⚪️🔘⚪️⚪️⚪️🔘
	N.402TinySeed          ⚪️⚪️⚪️🔘🔘⚪️⚪️🔘⚪️⚪️🔘⚪️
	N.403TinySeed          ⚪️⚪️⚪️🔘🔘⚪️⚪️🔘⚪️⚪️🔘🔘
	N.404TinySeed          ⚪️⚪️⚪️🔘🔘⚪️⚪️🔘⚪️🔘⚪️⚪️
	N.405TinySeed          ⚪️⚪️⚪️🔘🔘⚪️⚪️🔘⚪️🔘⚪️🔘
	N.406TinySeed          ⚪️⚪️⚪️🔘🔘⚪️⚪️🔘⚪️🔘🔘⚪️
	N.407TinySeed          ⚪️⚪️⚪️🔘🔘⚪️⚪️🔘⚪️🔘🔘🔘
	N.408TinySeed          ⚪️⚪️⚪️🔘🔘⚪️⚪️🔘🔘⚪️⚪️⚪️
	N.409TinySeed          ⚪️⚪️⚪️🔘🔘⚪️⚪️🔘🔘⚪️⚪️🔘
	N.410TinySeed          ⚪️⚪️⚪️🔘🔘⚪️⚪️🔘🔘⚪️🔘⚪️
	N.411TinySeed          ⚪️⚪️⚪️🔘🔘⚪️⚪️🔘🔘⚪️🔘🔘
	N.412TinySeed          ⚪️⚪️⚪️🔘🔘⚪️⚪️🔘🔘🔘⚪️⚪️
	N.413TinySeed          ⚪️⚪️⚪️🔘🔘⚪️⚪️🔘🔘🔘⚪️🔘
	N.414TinySeed          ⚪️⚪️⚪️🔘🔘⚪️⚪️🔘🔘🔘🔘⚪️
	N.415TinySeed          ⚪️⚪️⚪️🔘🔘⚪️⚪️🔘🔘🔘🔘🔘
	N.416TinySeed          ⚪️⚪️⚪️🔘🔘⚪️🔘⚪️⚪️⚪️⚪️⚪️
	N.417TinySeed          ⚪️⚪️⚪️🔘🔘⚪️🔘⚪️⚪️⚪️⚪️🔘
	N.418TinySeed          ⚪️⚪️⚪️🔘🔘⚪️🔘⚪️⚪️⚪️🔘⚪️
	N.419TinySeed          ⚪️⚪️⚪️🔘🔘⚪️🔘⚪️⚪️⚪️🔘🔘
	N.420TinySeed          ⚪️⚪️⚪️🔘🔘⚪️🔘⚪️⚪️🔘⚪️⚪️
	N.421TinySeed          ⚪️⚪️⚪️🔘🔘⚪️🔘⚪️⚪️🔘⚪️🔘
	N.422TinySeed          ⚪️⚪️⚪️🔘🔘⚪️🔘⚪️⚪️🔘🔘⚪️
	N.423TinySeed          ⚪️⚪️⚪️🔘🔘⚪️🔘⚪️⚪️🔘🔘🔘
	N.424TinySeed          ⚪️⚪️⚪️🔘🔘⚪️🔘⚪️🔘⚪️⚪️⚪️
	N.425TinySeed          ⚪️⚪️⚪️🔘🔘⚪️🔘⚪️🔘⚪️⚪️🔘
	N.426TinySeed          ⚪️⚪️⚪️🔘🔘⚪️🔘⚪️🔘⚪️🔘⚪️
	N.427TinySeed          ⚪️⚪️⚪️🔘🔘⚪️🔘⚪️🔘⚪️🔘🔘
	N.428TinySeed          ⚪️⚪️⚪️🔘🔘⚪️🔘⚪️🔘🔘⚪️⚪️
	N.429TinySeed          ⚪️⚪️⚪️🔘🔘⚪️🔘⚪️🔘🔘⚪️🔘
	N.430TinySeed          ⚪️⚪️⚪️🔘🔘⚪️🔘⚪️🔘🔘🔘⚪️
	N.431TinySeed          ⚪️⚪️⚪️🔘🔘⚪️🔘⚪️🔘🔘🔘🔘
	N.432TinySeed          ⚪️⚪️⚪️🔘🔘⚪️🔘🔘⚪️⚪️⚪️⚪️
	N.433TinySeed          ⚪️⚪️⚪️🔘🔘⚪️🔘🔘⚪️⚪️⚪️🔘
	N.434TinySeed          ⚪️⚪️⚪️🔘🔘⚪️🔘🔘⚪️⚪️🔘⚪️
	N.435TinySeed          ⚪️⚪️⚪️🔘🔘⚪️🔘🔘⚪️⚪️🔘🔘
	N.436TinySeed          ⚪️⚪️⚪️🔘🔘⚪️🔘🔘⚪️🔘⚪️⚪️
	N.437TinySeed          ⚪️⚪️⚪️🔘🔘⚪️🔘🔘⚪️🔘⚪️🔘
	N.438TinySeed          ⚪️⚪️⚪️🔘🔘⚪️🔘🔘⚪️🔘🔘⚪️
	N.439TinySeed          ⚪️⚪️⚪️🔘🔘⚪️🔘🔘⚪️🔘🔘🔘
	N.440TinySeed          ⚪️⚪️⚪️🔘🔘⚪️🔘🔘🔘⚪️⚪️⚪️
	N.441TinySeed          ⚪️⚪️⚪️🔘🔘⚪️🔘🔘🔘⚪️⚪️🔘
	N.442TinySeed          ⚪️⚪️⚪️🔘🔘⚪️🔘🔘🔘⚪️🔘⚪️
	N.443TinySeed          ⚪️⚪️⚪️🔘🔘⚪️🔘🔘🔘⚪️🔘🔘
	N.444TinySeed          ⚪️⚪️⚪️🔘🔘⚪️🔘🔘🔘🔘⚪️⚪️
	N.445TinySeed          ⚪️⚪️⚪️🔘🔘⚪️🔘🔘🔘🔘⚪️🔘
	N.446TinySeed          ⚪️⚪️⚪️🔘🔘⚪️🔘🔘🔘🔘🔘⚪️
	N.447TinySeed          ⚪️⚪️⚪️🔘🔘⚪️🔘🔘🔘🔘🔘🔘
	N.448TinySeed          ⚪️⚪️⚪️🔘🔘🔘⚪️⚪️⚪️⚪️⚪️⚪️
	N.449TinySeed          ⚪️⚪️⚪️🔘🔘🔘⚪️⚪️⚪️⚪️⚪️🔘
	N.450TinySeed          ⚪️⚪️⚪️🔘🔘🔘⚪️⚪️⚪️⚪️🔘⚪️
	N.451TinySeed          ⚪️⚪️⚪️🔘🔘🔘⚪️⚪️⚪️⚪️🔘🔘
	N.452TinySeed          ⚪️⚪️⚪️🔘🔘🔘⚪️⚪️⚪️🔘⚪️⚪️
	N.453TinySeed          ⚪️⚪️⚪️🔘🔘🔘⚪️⚪️⚪️🔘⚪️🔘
	N.454TinySeed          ⚪️⚪️⚪️🔘🔘🔘⚪️⚪️⚪️🔘🔘⚪️
	N.455TinySeed          ⚪️⚪️⚪️🔘🔘🔘⚪️⚪️⚪️🔘🔘🔘
	N.456TinySeed          ⚪️⚪️⚪️🔘🔘🔘⚪️⚪️🔘⚪️⚪️⚪️
	N.457TinySeed          ⚪️⚪️⚪️🔘🔘🔘⚪️⚪️🔘⚪️⚪️🔘
	N.458TinySeed          ⚪️⚪️⚪️🔘🔘🔘⚪️⚪️🔘⚪️🔘⚪️
	N.459TinySeed          ⚪️⚪️⚪️🔘🔘🔘⚪️⚪️🔘⚪️🔘🔘
	N.460TinySeed          ⚪️⚪️⚪️🔘🔘🔘⚪️⚪️🔘🔘⚪️⚪️
	N.461TinySeed          ⚪️⚪️⚪️🔘🔘🔘⚪️⚪️🔘🔘⚪️🔘
	N.462TinySeed          ⚪️⚪️⚪️🔘🔘🔘⚪️⚪️🔘🔘🔘⚪️
	N.463TinySeed          ⚪️⚪️⚪️🔘🔘🔘⚪️⚪️🔘🔘🔘🔘
	N.464TinySeed          ⚪️⚪️⚪️🔘🔘🔘⚪️🔘⚪️⚪️⚪️⚪️
	N.465TinySeed          ⚪️⚪️⚪️🔘🔘🔘⚪️🔘⚪️⚪️⚪️🔘
	N.466TinySeed          ⚪️⚪️⚪️🔘🔘🔘⚪️🔘⚪️⚪️🔘⚪️
	N.467TinySeed          ⚪️⚪️⚪️🔘🔘🔘⚪️🔘⚪️⚪️🔘🔘
	N.468TinySeed          ⚪️⚪️⚪️🔘🔘🔘⚪️🔘⚪️🔘⚪️⚪️
	N.469TinySeed          ⚪️⚪️⚪️🔘🔘🔘⚪️🔘⚪️🔘⚪️🔘
	N.470TinySeed          ⚪️⚪️⚪️🔘🔘🔘⚪️🔘⚪️🔘🔘⚪️
	N.471TinySeed          ⚪️⚪️⚪️🔘🔘🔘⚪️🔘⚪️🔘🔘🔘
	N.472TinySeed          ⚪️⚪️⚪️🔘🔘🔘⚪️🔘🔘⚪️⚪️⚪️
	N.473TinySeed          ⚪️⚪️⚪️🔘🔘🔘⚪️🔘🔘⚪️⚪️🔘
	N.474TinySeed          ⚪️⚪️⚪️🔘🔘🔘⚪️🔘🔘⚪️🔘⚪️
	N.475TinySeed          ⚪️⚪️⚪️🔘🔘🔘⚪️🔘🔘⚪️🔘🔘
	N.476TinySeed          ⚪️⚪️⚪️🔘🔘🔘⚪️🔘🔘🔘⚪️⚪️
	N.477TinySeed          ⚪️⚪️⚪️🔘🔘🔘⚪️🔘🔘🔘⚪️🔘
	N.478TinySeed          ⚪️⚪️⚪️🔘🔘🔘⚪️🔘🔘🔘🔘⚪️
	N.479TinySeed          ⚪️⚪️⚪️🔘🔘🔘⚪️🔘🔘🔘🔘🔘
	N.480TinySeed          ⚪️⚪️⚪️🔘🔘🔘🔘⚪️⚪️⚪️⚪️⚪️
	N.481TinySeed          ⚪️⚪️⚪️🔘🔘🔘🔘⚪️⚪️⚪️⚪️🔘
	N.482TinySeed          ⚪️⚪️⚪️🔘🔘🔘🔘⚪️⚪️⚪️🔘⚪️
	N.483TinySeed          ⚪️⚪️⚪️🔘🔘🔘🔘⚪️⚪️⚪️🔘🔘
	N.484TinySeed          ⚪️⚪️⚪️🔘🔘🔘🔘⚪️⚪️🔘⚪️⚪️
	N.485TinySeed          ⚪️⚪️⚪️🔘🔘🔘🔘⚪️⚪️🔘⚪️🔘
	N.486TinySeed          ⚪️⚪️⚪️🔘🔘🔘🔘⚪️⚪️🔘🔘⚪️
	N.487TinySeed          ⚪️⚪️⚪️🔘🔘🔘🔘⚪️⚪️🔘🔘🔘
	N.488TinySeed          ⚪️⚪️⚪️🔘🔘🔘🔘⚪️🔘⚪️⚪️⚪️
	N.489TinySeed          ⚪️⚪️⚪️🔘🔘🔘🔘⚪️🔘⚪️⚪️🔘
	N.490TinySeed          ⚪️⚪️⚪️🔘🔘🔘🔘⚪️🔘⚪️🔘⚪️
	N.491TinySeed          ⚪️⚪️⚪️🔘🔘🔘🔘⚪️🔘⚪️🔘🔘
	N.492TinySeed          ⚪️⚪️⚪️🔘🔘🔘🔘⚪️🔘🔘⚪️⚪️
	N.493TinySeed          ⚪️⚪️⚪️🔘🔘🔘🔘⚪️🔘🔘⚪️🔘
	N.494TinySeed          ⚪️⚪️⚪️🔘🔘🔘🔘⚪️🔘🔘🔘⚪️
	N.495TinySeed          ⚪️⚪️⚪️🔘🔘🔘🔘⚪️🔘🔘🔘🔘
	N.496TinySeed          ⚪️⚪️⚪️🔘🔘🔘🔘🔘⚪️⚪️⚪️⚪️
	N.497TinySeed          ⚪️⚪️⚪️🔘🔘🔘🔘🔘⚪️⚪️⚪️🔘
	N.498TinySeed          ⚪️⚪️⚪️🔘🔘🔘🔘🔘⚪️⚪️🔘⚪️
	N.499TinySeed          ⚪️⚪️⚪️🔘🔘🔘🔘🔘⚪️⚪️🔘🔘
	N.500TinySeed          ⚪️⚪️⚪️🔘🔘🔘🔘🔘⚪️🔘⚪️⚪️
	N.501TinySeed          ⚪️⚪️⚪️🔘🔘🔘🔘🔘⚪️🔘⚪️🔘
	N.502TinySeed          ⚪️⚪️⚪️🔘🔘🔘🔘🔘⚪️🔘🔘⚪️
	N.503TinySeed          ⚪️⚪️⚪️🔘🔘🔘🔘🔘⚪️🔘🔘🔘
	N.504TinySeed          ⚪️⚪️⚪️🔘🔘🔘🔘🔘🔘⚪️⚪️⚪️
	N.505TinySeed          ⚪️⚪️⚪️🔘🔘🔘🔘🔘🔘⚪️⚪️🔘
	N.506TinySeed          ⚪️⚪️⚪️🔘🔘🔘🔘🔘🔘⚪️🔘⚪️
	N.507TinySeed          ⚪️⚪️⚪️🔘🔘🔘🔘🔘🔘⚪️🔘🔘
	N.508TinySeed          ⚪️⚪️⚪️🔘🔘🔘🔘🔘🔘🔘⚪️⚪️
	N.509TinySeed          ⚪️⚪️⚪️🔘🔘🔘🔘🔘🔘🔘⚪️🔘
	N.510TinySeed          ⚪️⚪️⚪️🔘🔘🔘🔘🔘🔘🔘🔘⚪️
	N.511TinySeed          ⚪️⚪️⚪️🔘🔘🔘🔘🔘🔘🔘🔘🔘
	N.512TinySeed          ⚪️⚪️🔘⚪️⚪️⚪️⚪️⚪️⚪️⚪️⚪️⚪️
	N.513TinySeed          ⚪️⚪️🔘⚪️⚪️⚪️⚪️⚪️⚪️⚪️⚪️🔘
	N.514TinySeed          ⚪️⚪️🔘⚪️⚪️⚪️⚪️⚪️⚪️⚪️🔘⚪️
	N.515TinySeed          ⚪️⚪️🔘⚪️⚪️⚪️⚪️⚪️⚪️⚪️🔘🔘
	N.516TinySeed          ⚪️⚪️🔘⚪️⚪️⚪️⚪️⚪️⚪️🔘⚪️⚪️
	N.517TinySeed          ⚪️⚪️🔘⚪️⚪️⚪️⚪️⚪️⚪️🔘⚪️🔘
	N.518TinySeed          ⚪️⚪️🔘⚪️⚪️⚪️⚪️⚪️⚪️🔘🔘⚪️
	N.519TinySeed          ⚪️⚪️🔘⚪️⚪️⚪️⚪️⚪️⚪️🔘🔘🔘
	N.520TinySeed          ⚪️⚪️🔘⚪️⚪️⚪️⚪️⚪️🔘⚪️⚪️⚪️
	N.521TinySeed          ⚪️⚪️🔘⚪️⚪️⚪️⚪️⚪️🔘⚪️⚪️🔘
	N.522TinySeed          ⚪️⚪️🔘⚪️⚪️⚪️⚪️⚪️🔘⚪️🔘⚪️
	N.523TinySeed          ⚪️⚪️🔘⚪️⚪️⚪️⚪️⚪️🔘⚪️🔘🔘
	N.524TinySeed          ⚪️⚪️🔘⚪️⚪️⚪️⚪️⚪️🔘🔘⚪️⚪️
	N.525TinySeed          ⚪️⚪️🔘⚪️⚪️⚪️⚪️⚪️🔘🔘⚪️🔘
	N.526TinySeed          ⚪️⚪️🔘⚪️⚪️⚪️⚪️⚪️🔘🔘🔘⚪️
	N.527TinySeed          ⚪️⚪️🔘⚪️⚪️⚪️⚪️⚪️🔘🔘🔘🔘
	N.528TinySeed          ⚪️⚪️🔘⚪️⚪️⚪️⚪️🔘⚪️⚪️⚪️⚪️
	N.529TinySeed          ⚪️⚪️🔘⚪️⚪️⚪️⚪️🔘⚪️⚪️⚪️🔘
	N.530TinySeed          ⚪️⚪️🔘⚪️⚪️⚪️⚪️🔘⚪️⚪️🔘⚪️
	N.531TinySeed          ⚪️⚪️🔘⚪️⚪️⚪️⚪️🔘⚪️⚪️🔘🔘
	N.532TinySeed          ⚪️⚪️🔘⚪️⚪️⚪️⚪️🔘⚪️🔘⚪️⚪️
	N.533TinySeed          ⚪️⚪️🔘⚪️⚪️⚪️⚪️🔘⚪️🔘⚪️🔘
	N.534TinySeed          ⚪️⚪️🔘⚪️⚪️⚪️⚪️🔘⚪️🔘🔘⚪️
	N.535TinySeed          ⚪️⚪️🔘⚪️⚪️⚪️⚪️🔘⚪️🔘🔘🔘
	N.536TinySeed          ⚪️⚪️🔘⚪️⚪️⚪️⚪️🔘🔘⚪️⚪️⚪️
	N.537TinySeed          ⚪️⚪️🔘⚪️⚪️⚪️⚪️🔘🔘⚪️⚪️🔘
	N.538TinySeed          ⚪️⚪️🔘⚪️⚪️⚪️⚪️🔘🔘⚪️🔘⚪️
	N.539TinySeed          ⚪️⚪️🔘⚪️⚪️⚪️⚪️🔘🔘⚪️🔘🔘
	N.540TinySeed          ⚪️⚪️🔘⚪️⚪️⚪️⚪️🔘🔘🔘⚪️⚪️
	N.541TinySeed          ⚪️⚪️🔘⚪️⚪️⚪️⚪️🔘🔘🔘⚪️🔘
	N.542TinySeed          ⚪️⚪️🔘⚪️⚪️⚪️⚪️🔘🔘🔘🔘⚪️
	N.543TinySeed          ⚪️⚪️🔘⚪️⚪️⚪️⚪️🔘🔘🔘🔘🔘
	N.544TinySeed          ⚪️⚪️🔘⚪️⚪️⚪️🔘⚪️⚪️⚪️⚪️⚪️
	N.545TinySeed          ⚪️⚪️🔘⚪️⚪️⚪️🔘⚪️⚪️⚪️⚪️🔘
	N.546TinySeed          ⚪️⚪️🔘⚪️⚪️⚪️🔘⚪️⚪️⚪️🔘⚪️
	N.547TinySeed          ⚪️⚪️🔘⚪️⚪️⚪️🔘⚪️⚪️⚪️🔘🔘
	N.548TinySeed          ⚪️⚪️🔘⚪️⚪️⚪️🔘⚪️⚪️🔘⚪️⚪️
	N.549TinySeed          ⚪️⚪️🔘⚪️⚪️⚪️🔘⚪️⚪️🔘⚪️🔘
	N.550TinySeed          ⚪️⚪️🔘⚪️⚪️⚪️🔘⚪️⚪️🔘🔘⚪️
	N.551TinySeed          ⚪️⚪️🔘⚪️⚪️⚪️🔘⚪️⚪️🔘🔘🔘
	N.552TinySeed          ⚪️⚪️🔘⚪️⚪️⚪️🔘⚪️🔘⚪️⚪️⚪️
	N.553TinySeed          ⚪️⚪️🔘⚪️⚪️⚪️🔘⚪️🔘⚪️⚪️🔘
	N.554TinySeed          ⚪️⚪️🔘⚪️⚪️⚪️🔘⚪️🔘⚪️🔘⚪️
	N.555TinySeed          ⚪️⚪️🔘⚪️⚪️⚪️🔘⚪️🔘⚪️🔘🔘
	N.556TinySeed          ⚪️⚪️🔘⚪️⚪️⚪️🔘⚪️🔘🔘⚪️⚪️
	N.557TinySeed          ⚪️⚪️🔘⚪️⚪️⚪️🔘⚪️🔘🔘⚪️🔘
	N.558TinySeed          ⚪️⚪️🔘⚪️⚪️⚪️🔘⚪️🔘🔘🔘⚪️
	N.559TinySeed          ⚪️⚪️🔘⚪️⚪️⚪️🔘⚪️🔘🔘🔘🔘
	N.560TinySeed          ⚪️⚪️🔘⚪️⚪️⚪️🔘🔘⚪️⚪️⚪️⚪️
	N.561TinySeed          ⚪️⚪️🔘⚪️⚪️⚪️🔘🔘⚪️⚪️⚪️🔘
	N.562TinySeed          ⚪️⚪️🔘⚪️⚪️⚪️🔘🔘⚪️⚪️🔘⚪️
	N.563TinySeed          ⚪️⚪️🔘⚪️⚪️⚪️🔘🔘⚪️⚪️🔘🔘
	N.564TinySeed          ⚪️⚪️🔘⚪️⚪️⚪️🔘🔘⚪️🔘⚪️⚪️
	N.565TinySeed          ⚪️⚪️🔘⚪️⚪️⚪️🔘🔘⚪️🔘⚪️🔘
	N.566TinySeed          ⚪️⚪️🔘⚪️⚪️⚪️🔘🔘⚪️🔘🔘⚪️
	N.567TinySeed          ⚪️⚪️🔘⚪️⚪️⚪️🔘🔘⚪️🔘🔘🔘
	N.568TinySeed          ⚪️⚪️🔘⚪️⚪️⚪️🔘🔘🔘⚪️⚪️⚪️
	N.569TinySeed          ⚪️⚪️🔘⚪️⚪️⚪️🔘🔘🔘⚪️⚪️🔘
	N.570TinySeed          ⚪️⚪️🔘⚪️⚪️⚪️🔘🔘🔘⚪️🔘⚪️
	N.571TinySeed          ⚪️⚪️🔘⚪️⚪️⚪️🔘🔘🔘⚪️🔘🔘
	N.572TinySeed          ⚪️⚪️🔘⚪️⚪️⚪️🔘🔘🔘🔘⚪️⚪️
	N.573TinySeed          ⚪️⚪️🔘⚪️⚪️⚪️🔘🔘🔘🔘⚪️🔘
	N.574TinySeed          ⚪️⚪️🔘⚪️⚪️⚪️🔘🔘🔘🔘🔘⚪️
	N.575TinySeed          ⚪️⚪️🔘⚪️⚪️⚪️🔘🔘🔘🔘🔘🔘
	N.576TinySeed          ⚪️⚪️🔘⚪️⚪️🔘⚪️⚪️⚪️⚪️⚪️⚪️
	N.577TinySeed          ⚪️⚪️🔘⚪️⚪️🔘⚪️⚪️⚪️⚪️⚪️🔘
	N.578TinySeed          ⚪️⚪️🔘⚪️⚪️🔘⚪️⚪️⚪️⚪️🔘⚪️
	N.579TinySeed          ⚪️⚪️🔘⚪️⚪️🔘⚪️⚪️⚪️⚪️🔘🔘
	N.580TinySeed          ⚪️⚪️🔘⚪️⚪️🔘⚪️⚪️⚪️🔘⚪️⚪️
	N.581TinySeed          ⚪️⚪️🔘⚪️⚪️🔘⚪️⚪️⚪️🔘⚪️🔘
	N.582TinySeed          ⚪️⚪️🔘⚪️⚪️🔘⚪️⚪️⚪️🔘🔘⚪️
	N.583TinySeed          ⚪️⚪️🔘⚪️⚪️🔘⚪️⚪️⚪️🔘🔘🔘
	N.584TinySeed          ⚪️⚪️🔘⚪️⚪️🔘⚪️⚪️🔘⚪️⚪️⚪️
	N.585TinySeed          ⚪️⚪️🔘⚪️⚪️🔘⚪️⚪️🔘⚪️⚪️🔘
	N.586TinySeed          ⚪️⚪️🔘⚪️⚪️🔘⚪️⚪️🔘⚪️🔘⚪️
	N.587TinySeed          ⚪️⚪️🔘⚪️⚪️🔘⚪️⚪️🔘⚪️🔘🔘
	N.588TinySeed          ⚪️⚪️🔘⚪️⚪️🔘⚪️⚪️🔘🔘⚪️⚪️
	N.589TinySeed          ⚪️⚪️🔘⚪️⚪️🔘⚪️⚪️🔘🔘⚪️🔘
	N.590TinySeed          ⚪️⚪️🔘⚪️⚪️🔘⚪️⚪️🔘🔘🔘⚪️
	N.591TinySeed          ⚪️⚪️🔘⚪️⚪️🔘⚪️⚪️🔘🔘🔘🔘
	N.592TinySeed          ⚪️⚪️🔘⚪️⚪️🔘⚪️🔘⚪️⚪️⚪️⚪️
	N.593TinySeed          ⚪️⚪️🔘⚪️⚪️🔘⚪️🔘⚪️⚪️⚪️🔘
	N.594TinySeed          ⚪️⚪️🔘⚪️⚪️🔘⚪️🔘⚪️⚪️🔘⚪️
	N.595TinySeed          ⚪️⚪️🔘⚪️⚪️🔘⚪️🔘⚪️⚪️🔘🔘
	N.596TinySeed          ⚪️⚪️🔘⚪️⚪️🔘⚪️🔘⚪️🔘⚪️⚪️
	N.597TinySeed          ⚪️⚪️🔘⚪️⚪️🔘⚪️🔘⚪️🔘⚪️🔘
	N.598TinySeed          ⚪️⚪️🔘⚪️⚪️🔘⚪️🔘⚪️🔘🔘⚪️
	N.599TinySeed          ⚪️⚪️🔘⚪️⚪️🔘⚪️🔘⚪️🔘🔘🔘
	N.600TinySeed          ⚪️⚪️🔘⚪️⚪️🔘⚪️🔘🔘⚪️⚪️⚪️
	N.601TinySeed          ⚪️⚪️🔘⚪️⚪️🔘⚪️🔘🔘⚪️⚪️🔘
	N.602TinySeed          ⚪️⚪️🔘⚪️⚪️🔘⚪️🔘🔘⚪️🔘⚪️
	N.603TinySeed          ⚪️⚪️🔘⚪️⚪️🔘⚪️🔘🔘⚪️🔘🔘
	N.604TinySeed          ⚪️⚪️🔘⚪️⚪️🔘⚪️🔘🔘🔘⚪️⚪️
	N.605TinySeed          ⚪️⚪️🔘⚪️⚪️🔘⚪️🔘🔘🔘⚪️🔘
	N.606TinySeed          ⚪️⚪️🔘⚪️⚪️🔘⚪️🔘🔘🔘🔘⚪️
	N.607TinySeed          ⚪️⚪️🔘⚪️⚪️🔘⚪️🔘🔘🔘🔘🔘
	N.608TinySeed          ⚪️⚪️🔘⚪️⚪️🔘🔘⚪️⚪️⚪️⚪️⚪️
	N.609TinySeed          ⚪️⚪️🔘⚪️⚪️🔘🔘⚪️⚪️⚪️⚪️🔘
	N.610TinySeed          ⚪️⚪️🔘⚪️⚪️🔘🔘⚪️⚪️⚪️🔘⚪️
	N.611TinySeed          ⚪️⚪️🔘⚪️⚪️🔘🔘⚪️⚪️⚪️🔘🔘
	N.612TinySeed          ⚪️⚪️🔘⚪️⚪️🔘🔘⚪️⚪️🔘⚪️⚪️
	N.613TinySeed          ⚪️⚪️🔘⚪️⚪️🔘🔘⚪️⚪️🔘⚪️🔘
	N.614TinySeed          ⚪️⚪️🔘⚪️⚪️🔘🔘⚪️⚪️🔘🔘⚪️
	N.615TinySeed          ⚪️⚪️🔘⚪️⚪️🔘🔘⚪️⚪️🔘🔘🔘
	N.616TinySeed          ⚪️⚪️🔘⚪️⚪️🔘🔘⚪️🔘⚪️⚪️⚪️
	N.617TinySeed          ⚪️⚪️🔘⚪️⚪️🔘🔘⚪️🔘⚪️⚪️🔘
	N.618TinySeed          ⚪️⚪️🔘⚪️⚪️🔘🔘⚪️🔘⚪️🔘⚪️
	N.619TinySeed          ⚪️⚪️🔘⚪️⚪️🔘🔘⚪️🔘⚪️🔘🔘
	N.620TinySeed          ⚪️⚪️🔘⚪️⚪️🔘🔘⚪️🔘🔘⚪️⚪️
	N.621TinySeed          ⚪️⚪️🔘⚪️⚪️🔘🔘⚪️🔘🔘⚪️🔘
	N.622TinySeed          ⚪️⚪️🔘⚪️⚪️🔘🔘⚪️🔘🔘🔘⚪️
	N.623TinySeed          ⚪️⚪️🔘⚪️⚪️🔘🔘⚪️🔘🔘🔘🔘
	N.624TinySeed          ⚪️⚪️🔘⚪️⚪️🔘🔘🔘⚪️⚪️⚪️⚪️
	N.625TinySeed          ⚪️⚪️🔘⚪️⚪️🔘🔘🔘⚪️⚪️⚪️🔘
	N.626TinySeed          ⚪️⚪️🔘⚪️⚪️🔘🔘🔘⚪️⚪️🔘⚪️
	N.627TinySeed          ⚪️⚪️🔘⚪️⚪️🔘🔘🔘⚪️⚪️🔘🔘
	N.628TinySeed          ⚪️⚪️🔘⚪️⚪️🔘🔘🔘⚪️🔘⚪️⚪️
	N.629TinySeed          ⚪️⚪️🔘⚪️⚪️🔘🔘🔘⚪️🔘⚪️🔘
	N.630TinySeed          ⚪️⚪️🔘⚪️⚪️🔘🔘🔘⚪️🔘🔘⚪️
	N.631TinySeed          ⚪️⚪️🔘⚪️⚪️🔘🔘🔘⚪️🔘🔘🔘
	N.632TinySeed          ⚪️⚪️🔘⚪️⚪️🔘🔘🔘🔘⚪️⚪️⚪️
	N.633TinySeed          ⚪️⚪️🔘⚪️⚪️🔘🔘🔘🔘⚪️⚪️🔘
	N.634TinySeed          ⚪️⚪️🔘⚪️⚪️🔘🔘🔘🔘⚪️🔘⚪️
	N.635TinySeed          ⚪️⚪️🔘⚪️⚪️🔘🔘🔘🔘⚪️🔘🔘
	N.636TinySeed          ⚪️⚪️🔘⚪️⚪️🔘🔘🔘🔘🔘⚪️⚪️
	N.637TinySeed          ⚪️⚪️🔘⚪️⚪️🔘🔘🔘🔘🔘⚪️🔘
	N.638TinySeed          ⚪️⚪️🔘⚪️⚪️🔘🔘🔘🔘🔘🔘⚪️
	N.639TinySeed          ⚪️⚪️🔘⚪️⚪️🔘🔘🔘🔘🔘🔘🔘
	N.640TinySeed          ⚪️⚪️🔘⚪️🔘⚪️⚪️⚪️⚪️⚪️⚪️⚪️
	N.641TinySeed          ⚪️⚪️🔘⚪️🔘⚪️⚪️⚪️⚪️⚪️⚪️🔘
	N.642TinySeed          ⚪️⚪️🔘⚪️🔘⚪️⚪️⚪️⚪️⚪️🔘⚪️
	N.643TinySeed          ⚪️⚪️🔘⚪️🔘⚪️⚪️⚪️⚪️⚪️🔘🔘
	N.644TinySeed          ⚪️⚪️🔘⚪️🔘⚪️⚪️⚪️⚪️🔘⚪️⚪️
	N.645TinySeed          ⚪️⚪️🔘⚪️🔘⚪️⚪️⚪️⚪️🔘⚪️🔘
	N.646TinySeed          ⚪️⚪️🔘⚪️🔘⚪️⚪️⚪️⚪️🔘🔘⚪️
	N.647TinySeed          ⚪️⚪️🔘⚪️🔘⚪️⚪️⚪️⚪️🔘🔘🔘
	N.648TinySeed          ⚪️⚪️🔘⚪️🔘⚪️⚪️⚪️🔘⚪️⚪️⚪️
	N.649TinySeed          ⚪️⚪️🔘⚪️🔘⚪️⚪️⚪️🔘⚪️⚪️🔘
	N.650TinySeed          ⚪️⚪️🔘⚪️🔘⚪️⚪️⚪️🔘⚪️🔘⚪️
	N.651TinySeed          ⚪️⚪️🔘⚪️🔘⚪️⚪️⚪️🔘⚪️🔘🔘
	N.652TinySeed          ⚪️⚪️🔘⚪️🔘⚪️⚪️⚪️🔘🔘⚪️⚪️
	N.653TinySeed          ⚪️⚪️🔘⚪️🔘⚪️⚪️⚪️🔘🔘⚪️🔘
	N.654TinySeed          ⚪️⚪️🔘⚪️🔘⚪️⚪️⚪️🔘🔘🔘⚪️
	N.655TinySeed          ⚪️⚪️🔘⚪️🔘⚪️⚪️⚪️🔘🔘🔘🔘
	N.656TinySeed          ⚪️⚪️🔘⚪️🔘⚪️⚪️🔘⚪️⚪️⚪️⚪️
	N.657TinySeed          ⚪️⚪️🔘⚪️🔘⚪️⚪️🔘⚪️⚪️⚪️🔘
	N.658TinySeed          ⚪️⚪️🔘⚪️🔘⚪️⚪️🔘⚪️⚪️🔘⚪️
	N.659TinySeed          ⚪️⚪️🔘⚪️🔘⚪️⚪️🔘⚪️⚪️🔘🔘
	N.660TinySeed          ⚪️⚪️🔘⚪️🔘⚪️⚪️🔘⚪️🔘⚪️⚪️
	N.661TinySeed          ⚪️⚪️🔘⚪️🔘⚪️⚪️🔘⚪️🔘⚪️🔘
	N.662TinySeed          ⚪️⚪️🔘⚪️🔘⚪️⚪️🔘⚪️🔘🔘⚪️
	N.663TinySeed          ⚪️⚪️🔘⚪️🔘⚪️⚪️🔘⚪️🔘🔘🔘
	N.664TinySeed          ⚪️⚪️🔘⚪️🔘⚪️⚪️🔘🔘⚪️⚪️⚪️
	N.665TinySeed          ⚪️⚪️🔘⚪️🔘⚪️⚪️🔘🔘⚪️⚪️🔘
	N.666TinySeed          ⚪️⚪️🔘⚪️🔘⚪️⚪️🔘🔘⚪️🔘⚪️
	N.667TinySeed          ⚪️⚪️🔘⚪️🔘⚪️⚪️🔘🔘⚪️🔘🔘
	N.668TinySeed          ⚪️⚪️🔘⚪️🔘⚪️⚪️🔘🔘🔘⚪️⚪️
	N.669TinySeed          ⚪️⚪️🔘⚪️🔘⚪️⚪️🔘🔘🔘⚪️🔘
	N.670TinySeed          ⚪️⚪️🔘⚪️🔘⚪️⚪️🔘🔘🔘🔘⚪️
	N.671TinySeed          ⚪️⚪️🔘⚪️🔘⚪️⚪️🔘🔘🔘🔘🔘
	N.672TinySeed          ⚪️⚪️🔘⚪️🔘⚪️🔘⚪️⚪️⚪️⚪️⚪️
	N.673TinySeed          ⚪️⚪️🔘⚪️🔘⚪️🔘⚪️⚪️⚪️⚪️🔘
	N.674TinySeed          ⚪️⚪️🔘⚪️🔘⚪️🔘⚪️⚪️⚪️🔘⚪️
	N.675TinySeed          ⚪️⚪️🔘⚪️🔘⚪️🔘⚪️⚪️⚪️🔘🔘
	N.676TinySeed          ⚪️⚪️🔘⚪️🔘⚪️🔘⚪️⚪️🔘⚪️⚪️
	N.677TinySeed          ⚪️⚪️🔘⚪️🔘⚪️🔘⚪️⚪️🔘⚪️🔘
	N.678TinySeed          ⚪️⚪️🔘⚪️🔘⚪️🔘⚪️⚪️🔘🔘⚪️
	N.679TinySeed          ⚪️⚪️🔘⚪️🔘⚪️🔘⚪️⚪️🔘🔘🔘
	N.680TinySeed          ⚪️⚪️🔘⚪️🔘⚪️🔘⚪️🔘⚪️⚪️⚪️
	N.681TinySeed          ⚪️⚪️🔘⚪️🔘⚪️🔘⚪️🔘⚪️⚪️🔘
	N.682TinySeed          ⚪️⚪️🔘⚪️🔘⚪️🔘⚪️🔘⚪️🔘⚪️
	N.683TinySeed          ⚪️⚪️🔘⚪️🔘⚪️🔘⚪️🔘⚪️🔘🔘
	N.684TinySeed          ⚪️⚪️🔘⚪️🔘⚪️🔘⚪️🔘🔘⚪️⚪️
	N.685TinySeed          ⚪️⚪️🔘⚪️🔘⚪️🔘⚪️🔘🔘⚪️🔘
	N.686TinySeed          ⚪️⚪️🔘⚪️🔘⚪️🔘⚪️🔘🔘🔘⚪️
	N.687TinySeed          ⚪️⚪️🔘⚪️🔘⚪️🔘⚪️🔘🔘🔘🔘
	N.688TinySeed          ⚪️⚪️🔘⚪️🔘⚪️🔘🔘⚪️⚪️⚪️⚪️
	N.689TinySeed          ⚪️⚪️🔘⚪️🔘⚪️🔘🔘⚪️⚪️⚪️🔘
	N.690TinySeed          ⚪️⚪️🔘⚪️🔘⚪️🔘🔘⚪️⚪️🔘⚪️
	N.691TinySeed          ⚪️⚪️🔘⚪️🔘⚪️🔘🔘⚪️⚪️🔘🔘
	N.692TinySeed          ⚪️⚪️🔘⚪️🔘⚪️🔘🔘⚪️🔘⚪️⚪️
	N.693TinySeed          ⚪️⚪️🔘⚪️🔘⚪️🔘🔘⚪️🔘⚪️🔘
	N.694TinySeed          ⚪️⚪️🔘⚪️🔘⚪️🔘🔘⚪️🔘🔘⚪️
	N.695TinySeed          ⚪️⚪️🔘⚪️🔘⚪️🔘🔘⚪️🔘🔘🔘
	N.696TinySeed          ⚪️⚪️🔘⚪️🔘⚪️🔘🔘🔘⚪️⚪️⚪️
	N.697TinySeed          ⚪️⚪️🔘⚪️🔘⚪️🔘🔘🔘⚪️⚪️🔘
	N.698TinySeed          ⚪️⚪️🔘⚪️🔘⚪️🔘🔘🔘⚪️🔘⚪️
	N.699TinySeed          ⚪️⚪️🔘⚪️🔘⚪️🔘🔘🔘⚪️🔘🔘
	N.700TinySeed          ⚪️⚪️🔘⚪️🔘⚪️🔘🔘🔘🔘⚪️⚪️
	N.701TinySeed          ⚪️⚪️🔘⚪️🔘⚪️🔘🔘🔘🔘⚪️🔘
	N.702TinySeed          ⚪️⚪️🔘⚪️🔘⚪️🔘🔘🔘🔘🔘⚪️
	N.703TinySeed          ⚪️⚪️🔘⚪️🔘⚪️🔘🔘🔘🔘🔘🔘
	N.704TinySeed          ⚪️⚪️🔘⚪️🔘🔘⚪️⚪️⚪️⚪️⚪️⚪️
	N.705TinySeed          ⚪️⚪️🔘⚪️🔘🔘⚪️⚪️⚪️⚪️⚪️🔘
	N.706TinySeed          ⚪️⚪️🔘⚪️🔘🔘⚪️⚪️⚪️⚪️🔘⚪️
	N.707TinySeed          ⚪️⚪️🔘⚪️🔘🔘⚪️⚪️⚪️⚪️🔘🔘
	N.708TinySeed          ⚪️⚪️🔘⚪️🔘🔘⚪️⚪️⚪️🔘⚪️⚪️
	N.709TinySeed          ⚪️⚪️🔘⚪️🔘🔘⚪️⚪️⚪️🔘⚪️🔘
	N.710TinySeed          ⚪️⚪️🔘⚪️🔘🔘⚪️⚪️⚪️🔘🔘⚪️
	N.711TinySeed          ⚪️⚪️🔘⚪️🔘🔘⚪️⚪️⚪️🔘🔘🔘
	N.712TinySeed          ⚪️⚪️🔘⚪️🔘🔘⚪️⚪️🔘⚪️⚪️⚪️
	N.713TinySeed          ⚪️⚪️🔘⚪️🔘🔘⚪️⚪️🔘⚪️⚪️🔘
	N.714TinySeed          ⚪️⚪️🔘⚪️🔘🔘⚪️⚪️🔘⚪️🔘⚪️
	N.715TinySeed          ⚪️⚪️🔘⚪️🔘🔘⚪️⚪️🔘⚪️🔘🔘
	N.716TinySeed          ⚪️⚪️🔘⚪️🔘🔘⚪️⚪️🔘🔘⚪️⚪️
	N.717TinySeed          ⚪️⚪️🔘⚪️🔘🔘⚪️⚪️🔘🔘⚪️🔘
	N.718TinySeed          ⚪️⚪️🔘⚪️🔘🔘⚪️⚪️🔘🔘🔘⚪️
	N.719TinySeed          ⚪️⚪️🔘⚪️🔘🔘⚪️⚪️🔘🔘🔘🔘
	N.720TinySeed          ⚪️⚪️🔘⚪️🔘🔘⚪️🔘⚪️⚪️⚪️⚪️
	N.721TinySeed          ⚪️⚪️🔘⚪️🔘🔘⚪️🔘⚪️⚪️⚪️🔘
	N.722TinySeed          ⚪️⚪️🔘⚪️🔘🔘⚪️🔘⚪️⚪️🔘⚪️
	N.723TinySeed          ⚪️⚪️🔘⚪️🔘🔘⚪️🔘⚪️⚪️🔘🔘
	N.724TinySeed          ⚪️⚪️🔘⚪️🔘🔘⚪️🔘⚪️🔘⚪️⚪️
	N.725TinySeed          ⚪️⚪️🔘⚪️🔘🔘⚪️🔘⚪️🔘⚪️🔘
	N.726TinySeed          ⚪️⚪️🔘⚪️🔘🔘⚪️🔘⚪️🔘🔘⚪️
	N.727TinySeed          ⚪️⚪️🔘⚪️🔘🔘⚪️🔘⚪️🔘🔘🔘
	N.728TinySeed          ⚪️⚪️🔘⚪️🔘🔘⚪️🔘🔘⚪️⚪️⚪️
	N.729TinySeed          ⚪️⚪️🔘⚪️🔘🔘⚪️🔘🔘⚪️⚪️🔘
	N.730TinySeed          ⚪️⚪️🔘⚪️🔘🔘⚪️🔘🔘⚪️🔘⚪️
	N.731TinySeed          ⚪️⚪️🔘⚪️🔘🔘⚪️🔘🔘⚪️🔘🔘
	N.732TinySeed          ⚪️⚪️🔘⚪️🔘🔘⚪️🔘🔘🔘⚪️⚪️
	N.733TinySeed          ⚪️⚪️🔘⚪️🔘🔘⚪️🔘🔘🔘⚪️🔘
	N.734TinySeed          ⚪️⚪️🔘⚪️🔘🔘⚪️🔘🔘🔘🔘⚪️
	N.735TinySeed          ⚪️⚪️🔘⚪️🔘🔘⚪️🔘🔘🔘🔘🔘
	N.736TinySeed          ⚪️⚪️🔘⚪️🔘🔘🔘⚪️⚪️⚪️⚪️⚪️
	N.737TinySeed          ⚪️⚪️🔘⚪️🔘🔘🔘⚪️⚪️⚪️⚪️🔘
	N.738TinySeed          ⚪️⚪️🔘⚪️🔘🔘🔘⚪️⚪️⚪️🔘⚪️
	N.739TinySeed          ⚪️⚪️🔘⚪️🔘🔘🔘⚪️⚪️⚪️🔘🔘
	N.740TinySeed          ⚪️⚪️🔘⚪️🔘🔘🔘⚪️⚪️🔘⚪️⚪️
	N.741TinySeed          ⚪️⚪️🔘⚪️🔘🔘🔘⚪️⚪️🔘⚪️🔘
	N.742TinySeed          ⚪️⚪️🔘⚪️🔘🔘🔘⚪️⚪️🔘🔘⚪️
	N.743TinySeed          ⚪️⚪️🔘⚪️🔘🔘🔘⚪️⚪️🔘🔘🔘
	N.744TinySeed          ⚪️⚪️🔘⚪️🔘🔘🔘⚪️🔘⚪️⚪️⚪️
	N.745TinySeed          ⚪️⚪️🔘⚪️🔘🔘🔘⚪️🔘⚪️⚪️🔘
	N.746TinySeed          ⚪️⚪️🔘⚪️🔘🔘🔘⚪️🔘⚪️🔘⚪️
	N.747TinySeed          ⚪️⚪️🔘⚪️🔘🔘🔘⚪️🔘⚪️🔘🔘
	N.748TinySeed          ⚪️⚪️🔘⚪️🔘🔘🔘⚪️🔘🔘⚪️⚪️
	N.749TinySeed          ⚪️⚪️🔘⚪️🔘🔘🔘⚪️🔘🔘⚪️🔘
	N.750TinySeed          ⚪️⚪️🔘⚪️🔘🔘🔘⚪️🔘🔘🔘⚪️
	N.751TinySeed          ⚪️⚪️🔘⚪️🔘🔘🔘⚪️🔘🔘🔘🔘
	N.752TinySeed          ⚪️⚪️🔘⚪️🔘🔘🔘🔘⚪️⚪️⚪️⚪️
	N.753TinySeed          ⚪️⚪️🔘⚪️🔘🔘🔘🔘⚪️⚪️⚪️🔘
	N.754TinySeed          ⚪️⚪️🔘⚪️🔘🔘🔘🔘⚪️⚪️🔘⚪️
	N.755TinySeed          ⚪️⚪️🔘⚪️🔘🔘🔘🔘⚪️⚪️🔘🔘
	N.756TinySeed          ⚪️⚪️🔘⚪️🔘🔘🔘🔘⚪️🔘⚪️⚪️
	N.757TinySeed          ⚪️⚪️🔘⚪️🔘🔘🔘🔘⚪️🔘⚪️🔘
	N.758TinySeed          ⚪️⚪️🔘⚪️🔘🔘🔘🔘⚪️🔘🔘⚪️
	N.759TinySeed          ⚪️⚪️🔘⚪️🔘🔘🔘🔘⚪️🔘🔘🔘
	N.760TinySeed          ⚪️⚪️🔘⚪️🔘🔘🔘🔘🔘⚪️⚪️⚪️
	N.761TinySeed          ⚪️⚪️🔘⚪️🔘🔘🔘🔘🔘⚪️⚪️🔘
	N.762TinySeed          ⚪️⚪️🔘⚪️🔘🔘🔘🔘🔘⚪️🔘⚪️
	N.763TinySeed          ⚪️⚪️🔘⚪️🔘🔘🔘🔘🔘⚪️🔘🔘
	N.764TinySeed          ⚪️⚪️🔘⚪️🔘🔘🔘🔘🔘🔘⚪️⚪️
	N.765TinySeed          ⚪️⚪️🔘⚪️🔘🔘🔘🔘🔘🔘⚪️🔘
	N.766TinySeed          ⚪️⚪️🔘⚪️🔘🔘🔘🔘🔘🔘🔘⚪️
	N.767TinySeed          ⚪️⚪️🔘⚪️🔘🔘🔘🔘🔘🔘🔘🔘
	N.768TinySeed          ⚪️⚪️🔘🔘⚪️⚪️⚪️⚪️⚪️⚪️⚪️⚪️
	N.769TinySeed          ⚪️⚪️🔘🔘⚪️⚪️⚪️⚪️⚪️⚪️⚪️🔘
	N.770TinySeed          ⚪️⚪️🔘🔘⚪️⚪️⚪️⚪️⚪️⚪️🔘⚪️
	N.771TinySeed          ⚪️⚪️🔘🔘⚪️⚪️⚪️⚪️⚪️⚪️🔘🔘
	N.772TinySeed          ⚪️⚪️🔘🔘⚪️⚪️⚪️⚪️⚪️🔘⚪️⚪️
	N.773TinySeed          ⚪️⚪️🔘🔘⚪️⚪️⚪️⚪️⚪️🔘⚪️🔘
	N.774TinySeed          ⚪️⚪️🔘🔘⚪️⚪️⚪️⚪️⚪️🔘🔘⚪️
	N.775TinySeed          ⚪️⚪️🔘🔘⚪️⚪️⚪️⚪️⚪️🔘🔘🔘
	N.776TinySeed          ⚪️⚪️🔘🔘⚪️⚪️⚪️⚪️🔘⚪️⚪️⚪️
	N.777TinySeed          ⚪️⚪️🔘🔘⚪️⚪️⚪️⚪️🔘⚪️⚪️🔘
	N.778TinySeed          ⚪️⚪️🔘🔘⚪️⚪️⚪️⚪️🔘⚪️🔘⚪️
	N.779TinySeed          ⚪️⚪️🔘🔘⚪️⚪️⚪️⚪️🔘⚪️🔘🔘
	N.780TinySeed          ⚪️⚪️🔘🔘⚪️⚪️⚪️⚪️🔘🔘⚪️⚪️
	N.781TinySeed          ⚪️⚪️🔘🔘⚪️⚪️⚪️⚪️🔘🔘⚪️🔘
	N.782TinySeed          ⚪️⚪️🔘🔘⚪️⚪️⚪️⚪️🔘🔘🔘⚪️
	N.783TinySeed          ⚪️⚪️🔘🔘⚪️⚪️⚪️⚪️🔘🔘🔘🔘
	N.784TinySeed          ⚪️⚪️🔘🔘⚪️⚪️⚪️🔘⚪️⚪️⚪️⚪️
	N.785TinySeed          ⚪️⚪️🔘🔘⚪️⚪️⚪️🔘⚪️⚪️⚪️🔘
	N.786TinySeed          ⚪️⚪️🔘🔘⚪️⚪️⚪️🔘⚪️⚪️🔘⚪️
	N.787TinySeed          ⚪️⚪️🔘🔘⚪️⚪️⚪️🔘⚪️⚪️🔘🔘
	N.788TinySeed          ⚪️⚪️🔘🔘⚪️⚪️⚪️🔘⚪️🔘⚪️⚪️
	N.789TinySeed          ⚪️⚪️🔘🔘⚪️⚪️⚪️🔘⚪️🔘⚪️🔘
	N.790TinySeed          ⚪️⚪️🔘🔘⚪️⚪️⚪️🔘⚪️🔘🔘⚪️
	N.791TinySeed          ⚪️⚪️🔘🔘⚪️⚪️⚪️🔘⚪️🔘🔘🔘
	N.792TinySeed          ⚪️⚪️🔘🔘⚪️⚪️⚪️🔘🔘⚪️⚪️⚪️
	N.793TinySeed          ⚪️⚪️🔘🔘⚪️⚪️⚪️🔘🔘⚪️⚪️🔘
	N.794TinySeed          ⚪️⚪️🔘🔘⚪️⚪️⚪️🔘🔘⚪️🔘⚪️
	N.795TinySeed          ⚪️⚪️🔘🔘⚪️⚪️⚪️🔘🔘⚪️🔘🔘
	N.796TinySeed          ⚪️⚪️🔘🔘⚪️⚪️⚪️🔘🔘🔘⚪️⚪️
	N.797TinySeed          ⚪️⚪️🔘🔘⚪️⚪️⚪️🔘🔘🔘⚪️🔘
	N.798TinySeed          ⚪️⚪️🔘🔘⚪️⚪️⚪️🔘🔘🔘🔘⚪️
	N.799TinySeed          ⚪️⚪️🔘🔘⚪️⚪️⚪️🔘🔘🔘🔘🔘
	N.800TinySeed          ⚪️⚪️🔘🔘⚪️⚪️🔘⚪️⚪️⚪️⚪️⚪️
	N.801TinySeed          ⚪️⚪️🔘🔘⚪️⚪️🔘⚪️⚪️⚪️⚪️🔘
	N.802TinySeed          ⚪️⚪️🔘🔘⚪️⚪️🔘⚪️⚪️⚪️🔘⚪️
	N.803TinySeed          ⚪️⚪️🔘🔘⚪️⚪️🔘⚪️⚪️⚪️🔘🔘
	N.804TinySeed          ⚪️⚪️🔘🔘⚪️⚪️🔘⚪️⚪️🔘⚪️⚪️
	N.805TinySeed          ⚪️⚪️🔘🔘⚪️⚪️🔘⚪️⚪️🔘⚪️🔘
	N.806TinySeed          ⚪️⚪️🔘🔘⚪️⚪️🔘⚪️⚪️🔘🔘⚪️
	N.807TinySeed          ⚪️⚪️🔘🔘⚪️⚪️🔘⚪️⚪️🔘🔘🔘
	N.808TinySeed          ⚪️⚪️🔘🔘⚪️⚪️🔘⚪️🔘⚪️⚪️⚪️
	N.809TinySeed          ⚪️⚪️🔘🔘⚪️⚪️🔘⚪️🔘⚪️⚪️🔘
	N.810TinySeed          ⚪️⚪️🔘🔘⚪️⚪️🔘⚪️🔘⚪️🔘⚪️
	N.811TinySeed          ⚪️⚪️🔘🔘⚪️⚪️🔘⚪️🔘⚪️🔘🔘
	N.812TinySeed          ⚪️⚪️🔘🔘⚪️⚪️🔘⚪️🔘🔘⚪️⚪️
	N.813TinySeed          ⚪️⚪️🔘🔘⚪️⚪️🔘⚪️🔘🔘⚪️🔘
	N.814TinySeed          ⚪️⚪️🔘🔘⚪️⚪️🔘⚪️🔘🔘🔘⚪️
	N.815TinySeed          ⚪️⚪️🔘🔘⚪️⚪️🔘⚪️🔘🔘🔘🔘
	N.816TinySeed          ⚪️⚪️🔘🔘⚪️⚪️🔘🔘⚪️⚪️⚪️⚪️
	N.817TinySeed          ⚪️⚪️🔘🔘⚪️⚪️🔘🔘⚪️⚪️⚪️🔘
	N.818TinySeed          ⚪️⚪️🔘🔘⚪️⚪️🔘🔘⚪️⚪️🔘⚪️
	N.819TinySeed          ⚪️⚪️🔘🔘⚪️⚪️🔘🔘⚪️⚪️🔘🔘
	N.820TinySeed          ⚪️⚪️🔘🔘⚪️⚪️🔘🔘⚪️🔘⚪️⚪️
	N.821TinySeed          ⚪️⚪️🔘🔘⚪️⚪️🔘🔘⚪️🔘⚪️🔘
	N.822TinySeed          ⚪️⚪️🔘🔘⚪️⚪️🔘🔘⚪️🔘🔘⚪️
	N.823TinySeed          ⚪️⚪️🔘🔘⚪️⚪️🔘🔘⚪️🔘🔘🔘
	N.824TinySeed          ⚪️⚪️🔘🔘⚪️⚪️🔘🔘🔘⚪️⚪️⚪️
	N.825TinySeed          ⚪️⚪️🔘🔘⚪️⚪️🔘🔘🔘⚪️⚪️🔘
	N.826TinySeed          ⚪️⚪️🔘🔘⚪️⚪️🔘🔘🔘⚪️🔘⚪️
	N.827TinySeed          ⚪️⚪️🔘🔘⚪️⚪️🔘🔘🔘⚪️🔘🔘
	N.828TinySeed          ⚪️⚪️🔘🔘⚪️⚪️🔘🔘🔘🔘⚪️⚪️
	N.829TinySeed          ⚪️⚪️🔘🔘⚪️⚪️🔘🔘🔘🔘⚪️🔘
	N.830TinySeed          ⚪️⚪️🔘🔘⚪️⚪️🔘🔘🔘🔘🔘⚪️
	N.831TinySeed          ⚪️⚪️🔘🔘⚪️⚪️🔘🔘🔘🔘🔘🔘
	N.832TinySeed          ⚪️⚪️🔘🔘⚪️🔘⚪️⚪️⚪️⚪️⚪️⚪️
	N.833TinySeed          ⚪️⚪️🔘🔘⚪️🔘⚪️⚪️⚪️⚪️⚪️🔘
	N.834TinySeed          ⚪️⚪️🔘🔘⚪️🔘⚪️⚪️⚪️⚪️🔘⚪️
	N.835TinySeed          ⚪️⚪️🔘🔘⚪️🔘⚪️⚪️⚪️⚪️🔘🔘
	N.836TinySeed          ⚪️⚪️🔘🔘⚪️🔘⚪️⚪️⚪️🔘⚪️⚪️
	N.837TinySeed          ⚪️⚪️🔘🔘⚪️🔘⚪️⚪️⚪️🔘⚪️🔘
	N.838TinySeed          ⚪️⚪️🔘🔘⚪️🔘⚪️⚪️⚪️🔘🔘⚪️
	N.839TinySeed          ⚪️⚪️🔘🔘⚪️🔘⚪️⚪️⚪️🔘🔘🔘
	N.840TinySeed          ⚪️⚪️🔘🔘⚪️🔘⚪️⚪️🔘⚪️⚪️⚪️
	N.841TinySeed          ⚪️⚪️🔘🔘⚪️🔘⚪️⚪️🔘⚪️⚪️🔘
	N.842TinySeed          ⚪️⚪️🔘🔘⚪️🔘⚪️⚪️🔘⚪️🔘⚪️
	N.843TinySeed          ⚪️⚪️🔘🔘⚪️🔘⚪️⚪️🔘⚪️🔘🔘
	N.844TinySeed          ⚪️⚪️🔘🔘⚪️🔘⚪️⚪️🔘🔘⚪️⚪️
	N.845TinySeed          ⚪️⚪️🔘🔘⚪️🔘⚪️⚪️🔘🔘⚪️🔘
	N.846TinySeed          ⚪️⚪️🔘🔘⚪️🔘⚪️⚪️🔘🔘🔘⚪️
	N.847TinySeed          ⚪️⚪️🔘🔘⚪️🔘⚪️⚪️🔘🔘🔘🔘
	N.848TinySeed          ⚪️⚪️🔘🔘⚪️🔘⚪️🔘⚪️⚪️⚪️⚪️
	N.849TinySeed          ⚪️⚪️🔘🔘⚪️🔘⚪️🔘⚪️⚪️⚪️🔘
	N.850TinySeed          ⚪️⚪️🔘🔘⚪️🔘⚪️🔘⚪️⚪️🔘⚪️
	N.851TinySeed          ⚪️⚪️🔘🔘⚪️🔘⚪️🔘⚪️⚪️🔘🔘
	N.852TinySeed          ⚪️⚪️🔘🔘⚪️🔘⚪️🔘⚪️🔘⚪️⚪️
	N.853TinySeed          ⚪️⚪️🔘🔘⚪️🔘⚪️🔘⚪️🔘⚪️🔘
	N.854TinySeed          ⚪️⚪️🔘🔘⚪️🔘⚪️🔘⚪️🔘🔘⚪️
	N.855TinySeed          ⚪️⚪️🔘🔘⚪️🔘⚪️🔘⚪️🔘🔘🔘
	N.856TinySeed          ⚪️⚪️🔘🔘⚪️🔘⚪️🔘🔘⚪️⚪️⚪️
	N.857TinySeed          ⚪️⚪️🔘🔘⚪️🔘⚪️🔘🔘⚪️⚪️🔘
	N.858TinySeed          ⚪️⚪️🔘🔘⚪️🔘⚪️🔘🔘⚪️🔘⚪️
	N.859TinySeed          ⚪️⚪️🔘🔘⚪️🔘⚪️🔘🔘⚪️🔘🔘
	N.860TinySeed          ⚪️⚪️🔘🔘⚪️🔘⚪️🔘🔘🔘⚪️⚪️
	N.861TinySeed          ⚪️⚪️🔘🔘⚪️🔘⚪️🔘🔘🔘⚪️🔘
	N.862TinySeed          ⚪️⚪️🔘🔘⚪️🔘⚪️🔘🔘🔘🔘⚪️
	N.863TinySeed          ⚪️⚪️🔘🔘⚪️🔘⚪️🔘🔘🔘🔘🔘
	N.864TinySeed          ⚪️⚪️🔘🔘⚪️🔘🔘⚪️⚪️⚪️⚪️⚪️
	N.865TinySeed          ⚪️⚪️🔘🔘⚪️🔘🔘⚪️⚪️⚪️⚪️🔘
	N.866TinySeed          ⚪️⚪️🔘🔘⚪️🔘🔘⚪️⚪️⚪️🔘⚪️
	N.867TinySeed          ⚪️⚪️🔘🔘⚪️🔘🔘⚪️⚪️⚪️🔘🔘
	N.868TinySeed          ⚪️⚪️🔘🔘⚪️🔘🔘⚪️⚪️🔘⚪️⚪️
	N.869TinySeed          ⚪️⚪️🔘🔘⚪️🔘🔘⚪️⚪️🔘⚪️🔘
	N.870TinySeed          ⚪️⚪️🔘🔘⚪️🔘🔘⚪️⚪️🔘🔘⚪️
	N.871TinySeed          ⚪️⚪️🔘🔘⚪️🔘🔘⚪️⚪️🔘🔘🔘
	N.872TinySeed          ⚪️⚪️🔘🔘⚪️🔘🔘⚪️🔘⚪️⚪️⚪️
	N.873TinySeed          ⚪️⚪️🔘🔘⚪️🔘🔘⚪️🔘⚪️⚪️🔘
	N.874TinySeed          ⚪️⚪️🔘🔘⚪️🔘🔘⚪️🔘⚪️🔘⚪️
	N.875TinySeed          ⚪️⚪️🔘🔘⚪️🔘🔘⚪️🔘⚪️🔘🔘
	N.876TinySeed          ⚪️⚪️🔘🔘⚪️🔘🔘⚪️🔘🔘⚪️⚪️
	N.877TinySeed          ⚪️⚪️🔘🔘⚪️🔘🔘⚪️🔘🔘⚪️🔘
	N.878TinySeed          ⚪️⚪️🔘🔘⚪️🔘🔘⚪️🔘🔘🔘⚪️
	N.879TinySeed          ⚪️⚪️🔘🔘⚪️🔘🔘⚪️🔘🔘🔘🔘
	N.880TinySeed          ⚪️⚪️🔘🔘⚪️🔘🔘🔘⚪️⚪️⚪️⚪️
	N.881TinySeed          ⚪️⚪️🔘🔘⚪️🔘🔘🔘⚪️⚪️⚪️🔘
	N.882TinySeed          ⚪️⚪️🔘🔘⚪️🔘🔘🔘⚪️⚪️🔘⚪️
	N.883TinySeed          ⚪️⚪️🔘🔘⚪️🔘🔘🔘⚪️⚪️🔘🔘
	N.884TinySeed          ⚪️⚪️🔘🔘⚪️🔘🔘🔘⚪️🔘⚪️⚪️
	N.885TinySeed          ⚪️⚪️🔘🔘⚪️🔘🔘🔘⚪️🔘⚪️🔘
	N.886TinySeed          ⚪️⚪️🔘🔘⚪️🔘🔘🔘⚪️🔘🔘⚪️
	N.887TinySeed          ⚪️⚪️🔘🔘⚪️🔘🔘🔘⚪️🔘🔘🔘
	N.888TinySeed          ⚪️⚪️🔘🔘⚪️🔘🔘🔘🔘⚪️⚪️⚪️
	N.889TinySeed          ⚪️⚪️🔘🔘⚪️🔘🔘🔘🔘⚪️⚪️🔘
	N.890TinySeed          ⚪️⚪️🔘🔘⚪️🔘🔘🔘🔘⚪️🔘⚪️
	N.891TinySeed          ⚪️⚪️🔘🔘⚪️🔘🔘🔘🔘⚪️🔘🔘
	N.892TinySeed          ⚪️⚪️🔘🔘⚪️🔘🔘🔘🔘🔘⚪️⚪️
	N.893TinySeed          ⚪️⚪️🔘🔘⚪️🔘🔘🔘🔘🔘⚪️🔘
	N.894TinySeed          ⚪️⚪️🔘🔘⚪️🔘🔘🔘🔘🔘🔘⚪️
	N.895TinySeed          ⚪️⚪️🔘🔘⚪️🔘🔘🔘🔘🔘🔘🔘
	N.896TinySeed          ⚪️⚪️🔘🔘🔘⚪️⚪️⚪️⚪️⚪️⚪️⚪️
	N.897TinySeed          ⚪️⚪️🔘🔘🔘⚪️⚪️⚪️⚪️⚪️⚪️🔘
	N.898TinySeed          ⚪️⚪️🔘🔘🔘⚪️⚪️⚪️⚪️⚪️🔘⚪️
	N.899TinySeed          ⚪️⚪️🔘🔘🔘⚪️⚪️⚪️⚪️⚪️🔘🔘
	N.900TinySeed          ⚪️⚪️🔘🔘🔘⚪️⚪️⚪️⚪️🔘⚪️⚪️
	N.901TinySeed          ⚪️⚪️🔘🔘🔘⚪️⚪️⚪️⚪️🔘⚪️🔘
	N.902TinySeed          ⚪️⚪️🔘🔘🔘⚪️⚪️⚪️⚪️🔘🔘⚪️
	N.903TinySeed          ⚪️⚪️🔘🔘🔘⚪️⚪️⚪️⚪️🔘🔘🔘
	N.904TinySeed          ⚪️⚪️🔘🔘🔘⚪️⚪️⚪️🔘⚪️⚪️⚪️
	N.905TinySeed          ⚪️⚪️🔘🔘🔘⚪️⚪️⚪️🔘⚪️⚪️🔘
	N.906TinySeed          ⚪️⚪️🔘🔘🔘⚪️⚪️⚪️🔘⚪️🔘⚪️
	N.907TinySeed          ⚪️⚪️🔘🔘🔘⚪️⚪️⚪️🔘⚪️🔘🔘
	N.908TinySeed          ⚪️⚪️🔘🔘🔘⚪️⚪️⚪️🔘🔘⚪️⚪️
	N.909TinySeed          ⚪️⚪️🔘🔘🔘⚪️⚪️⚪️🔘🔘⚪️🔘
	N.910TinySeed          ⚪️⚪️🔘🔘🔘⚪️⚪️⚪️🔘🔘🔘⚪️
	N.911TinySeed          ⚪️⚪️🔘🔘🔘⚪️⚪️⚪️🔘🔘🔘🔘
	N.912TinySeed          ⚪️⚪️🔘🔘🔘⚪️⚪️🔘⚪️⚪️⚪️⚪️
	N.913TinySeed          ⚪️⚪️🔘🔘🔘⚪️⚪️🔘⚪️⚪️⚪️🔘
	N.914TinySeed          ⚪️⚪️🔘🔘🔘⚪️⚪️🔘⚪️⚪️🔘⚪️
	N.915TinySeed          ⚪️⚪️🔘🔘🔘⚪️⚪️🔘⚪️⚪️🔘🔘
	N.916TinySeed          ⚪️⚪️🔘🔘🔘⚪️⚪️🔘⚪️🔘⚪️⚪️
	N.917TinySeed          ⚪️⚪️🔘🔘🔘⚪️⚪️🔘⚪️🔘⚪️🔘
	N.918TinySeed          ⚪️⚪️🔘🔘🔘⚪️⚪️🔘⚪️🔘🔘⚪️
	N.919TinySeed          ⚪️⚪️🔘🔘🔘⚪️⚪️🔘⚪️🔘🔘🔘
	N.920TinySeed          ⚪️⚪️🔘🔘🔘⚪️⚪️🔘🔘⚪️⚪️⚪️
	N.921TinySeed          ⚪️⚪️🔘🔘🔘⚪️⚪️🔘🔘⚪️⚪️🔘
	N.922TinySeed          ⚪️⚪️🔘🔘🔘⚪️⚪️🔘🔘⚪️🔘⚪️
	N.923TinySeed          ⚪️⚪️🔘🔘🔘⚪️⚪️🔘🔘⚪️🔘🔘
	N.924TinySeed          ⚪️⚪️🔘🔘🔘⚪️⚪️🔘🔘🔘⚪️⚪️
	N.925TinySeed          ⚪️⚪️🔘🔘🔘⚪️⚪️🔘🔘🔘⚪️🔘
	N.926TinySeed          ⚪️⚪️🔘🔘🔘⚪️⚪️🔘🔘🔘🔘⚪️
	N.927TinySeed          ⚪️⚪️🔘🔘🔘⚪️⚪️🔘🔘🔘🔘🔘
	N.928TinySeed          ⚪️⚪️🔘🔘🔘⚪️🔘⚪️⚪️⚪️⚪️⚪️
	N.929TinySeed          ⚪️⚪️🔘🔘🔘⚪️🔘⚪️⚪️⚪️⚪️🔘
	N.930TinySeed          ⚪️⚪️🔘🔘🔘⚪️🔘⚪️⚪️⚪️🔘⚪️
	N.931TinySeed          ⚪️⚪️🔘🔘🔘⚪️🔘⚪️⚪️⚪️🔘🔘
	N.932TinySeed          ⚪️⚪️🔘🔘🔘⚪️🔘⚪️⚪️🔘⚪️⚪️
	N.933TinySeed          ⚪️⚪️🔘🔘🔘⚪️🔘⚪️⚪️🔘⚪️🔘
	N.934TinySeed          ⚪️⚪️🔘🔘🔘⚪️🔘⚪️⚪️🔘🔘⚪️
	N.935TinySeed          ⚪️⚪️🔘🔘🔘⚪️🔘⚪️⚪️🔘🔘🔘
	N.936TinySeed          ⚪️⚪️🔘🔘🔘⚪️🔘⚪️🔘⚪️⚪️⚪️
	N.937TinySeed          ⚪️⚪️🔘🔘🔘⚪️🔘⚪️🔘⚪️⚪️🔘
	N.938TinySeed          ⚪️⚪️🔘🔘🔘⚪️🔘⚪️🔘⚪️🔘⚪️
	N.939TinySeed          ⚪️⚪️🔘🔘🔘⚪️🔘⚪️🔘⚪️🔘🔘
	N.940TinySeed          ⚪️⚪️🔘🔘🔘⚪️🔘⚪️🔘🔘⚪️⚪️
	N.941TinySeed          ⚪️⚪️🔘🔘🔘⚪️🔘⚪️🔘🔘⚪️🔘
	N.942TinySeed          ⚪️⚪️🔘🔘🔘⚪️🔘⚪️🔘🔘🔘⚪️
	N.943TinySeed          ⚪️⚪️🔘🔘🔘⚪️🔘⚪️🔘🔘🔘🔘
	N.944TinySeed          ⚪️⚪️🔘🔘🔘⚪️🔘🔘⚪️⚪️⚪️⚪️
	N.945TinySeed          ⚪️⚪️🔘🔘🔘⚪️🔘🔘⚪️⚪️⚪️🔘
	N.946TinySeed          ⚪️⚪️🔘🔘🔘⚪️🔘🔘⚪️⚪️🔘⚪️
	N.947TinySeed          ⚪️⚪️🔘🔘🔘⚪️🔘🔘⚪️⚪️🔘🔘
	N.948TinySeed          ⚪️⚪️🔘🔘🔘⚪️🔘🔘⚪️🔘⚪️⚪️
	N.949TinySeed          ⚪️⚪️🔘🔘🔘⚪️🔘🔘⚪️🔘⚪️🔘
	N.950TinySeed          ⚪️⚪️🔘🔘🔘⚪️🔘🔘⚪️🔘🔘⚪️
	N.951TinySeed          ⚪️⚪️🔘🔘🔘⚪️🔘🔘⚪️🔘🔘🔘
	N.952TinySeed          ⚪️⚪️🔘🔘🔘⚪️🔘🔘🔘⚪️⚪️⚪️
	N.953TinySeed          ⚪️⚪️🔘🔘🔘⚪️🔘🔘🔘⚪️⚪️🔘
	N.954TinySeed          ⚪️⚪️🔘🔘🔘⚪️🔘🔘🔘⚪️🔘⚪️
	N.955TinySeed          ⚪️⚪️🔘🔘🔘⚪️🔘🔘🔘⚪️🔘🔘
	N.956TinySeed          ⚪️⚪️🔘🔘🔘⚪️🔘🔘🔘🔘⚪️⚪️
	N.957TinySeed          ⚪️⚪️🔘🔘🔘⚪️🔘🔘🔘🔘⚪️🔘
	N.958TinySeed          ⚪️⚪️🔘🔘🔘⚪️🔘🔘🔘🔘🔘⚪️
	N.959TinySeed          ⚪️⚪️🔘🔘🔘⚪️🔘🔘🔘🔘🔘🔘
	N.960TinySeed          ⚪️⚪️🔘🔘🔘🔘⚪️⚪️⚪️⚪️⚪️⚪️
	N.961TinySeed          ⚪️⚪️🔘🔘🔘🔘⚪️⚪️⚪️⚪️⚪️🔘
	N.962TinySeed          ⚪️⚪️🔘🔘🔘🔘⚪️⚪️⚪️⚪️🔘⚪️
	N.963TinySeed          ⚪️⚪️🔘🔘🔘🔘⚪️⚪️⚪️⚪️🔘🔘
	N.964TinySeed          ⚪️⚪️🔘🔘🔘🔘⚪️⚪️⚪️🔘⚪️⚪️
	N.965TinySeed          ⚪️⚪️🔘🔘🔘🔘⚪️⚪️⚪️🔘⚪️🔘
	N.966TinySeed          ⚪️⚪️🔘🔘🔘🔘⚪️⚪️⚪️🔘🔘⚪️
	N.967TinySeed          ⚪️⚪️🔘🔘🔘🔘⚪️⚪️⚪️🔘🔘🔘
	N.968TinySeed          ⚪️⚪️🔘🔘🔘🔘⚪️⚪️🔘⚪️⚪️⚪️
	N.969TinySeed          ⚪️⚪️🔘🔘🔘🔘⚪️⚪️🔘⚪️⚪️🔘
	N.970TinySeed          ⚪️⚪️🔘🔘🔘🔘⚪️⚪️🔘⚪️🔘⚪️
	N.971TinySeed          ⚪️⚪️🔘🔘🔘🔘⚪️⚪️🔘⚪️🔘🔘
	N.972TinySeed          ⚪️⚪️🔘🔘🔘🔘⚪️⚪️🔘🔘⚪️⚪️
	N.973TinySeed          ⚪️⚪️🔘🔘🔘🔘⚪️⚪️🔘🔘⚪️🔘
	N.974TinySeed          ⚪️⚪️🔘🔘🔘🔘⚪️⚪️🔘🔘🔘⚪️
	N.975TinySeed          ⚪️⚪️🔘🔘🔘🔘⚪️⚪️🔘🔘🔘🔘
	N.976TinySeed          ⚪️⚪️🔘🔘🔘🔘⚪️🔘⚪️⚪️⚪️⚪️
	N.977TinySeed          ⚪️⚪️🔘🔘🔘🔘⚪️🔘⚪️⚪️⚪️🔘
	N.978TinySeed          ⚪️⚪️🔘🔘🔘🔘⚪️🔘⚪️⚪️🔘⚪️
	N.979TinySeed          ⚪️⚪️🔘🔘🔘🔘⚪️🔘⚪️⚪️🔘🔘
	N.980TinySeed          ⚪️⚪️🔘🔘🔘🔘⚪️🔘⚪️🔘⚪️⚪️
	N.981TinySeed          ⚪️⚪️🔘🔘🔘🔘⚪️🔘⚪️🔘⚪️🔘
	N.982TinySeed          ⚪️⚪️🔘🔘🔘🔘⚪️🔘⚪️🔘🔘⚪️
	N.983TinySeed          ⚪️⚪️🔘🔘🔘🔘⚪️🔘⚪️🔘🔘🔘
	N.984TinySeed          ⚪️⚪️🔘🔘🔘🔘⚪️🔘🔘⚪️⚪️⚪️
	N.985TinySeed          ⚪️⚪️🔘🔘🔘🔘⚪️🔘🔘⚪️⚪️🔘
	N.986TinySeed          ⚪️⚪️🔘🔘🔘🔘⚪️🔘🔘⚪️🔘⚪️
	N.987TinySeed          ⚪️⚪️🔘🔘🔘🔘⚪️🔘🔘⚪️🔘🔘
	N.988TinySeed          ⚪️⚪️🔘🔘🔘🔘⚪️🔘🔘🔘⚪️⚪️
	N.989TinySeed          ⚪️⚪️🔘🔘🔘🔘⚪️🔘🔘🔘⚪️🔘
	N.990TinySeed          ⚪️⚪️🔘🔘🔘🔘⚪️🔘🔘🔘🔘⚪️
	N.991TinySeed          ⚪️⚪️🔘🔘🔘🔘⚪️🔘🔘🔘🔘🔘
	N.992TinySeed          ⚪️⚪️🔘🔘🔘🔘🔘⚪️⚪️⚪️⚪️⚪️
	N.993TinySeed          ⚪️⚪️🔘🔘🔘🔘🔘⚪️⚪️⚪️⚪️🔘
	N.994TinySeed          ⚪️⚪️🔘🔘🔘🔘🔘⚪️⚪️⚪️🔘⚪️
	N.995TinySeed          ⚪️⚪️🔘🔘🔘🔘🔘⚪️⚪️⚪️🔘🔘
	N.996TinySeed          ⚪️⚪️🔘🔘🔘🔘🔘⚪️⚪️🔘⚪️⚪️
	N.997TinySeed          ⚪️⚪️🔘🔘🔘🔘🔘⚪️⚪️🔘⚪️🔘
	N.998TinySeed          ⚪️⚪️🔘🔘🔘🔘🔘⚪️⚪️🔘🔘⚪️
	N.999TinySeed          ⚪️⚪️🔘🔘🔘🔘🔘⚪️⚪️🔘🔘🔘
	N.1000TinySeed          ⚪️⚪️🔘🔘🔘🔘🔘⚪️🔘⚪️⚪️⚪️
	N.1001TinySeed          ⚪️⚪️🔘🔘🔘🔘🔘⚪️🔘⚪️⚪️🔘
	N.1002TinySeed          ⚪️⚪️🔘🔘🔘🔘🔘⚪️🔘⚪️🔘⚪️
	N.1003TinySeed          ⚪️⚪️🔘🔘🔘🔘🔘⚪️🔘⚪️🔘🔘
	N.1004TinySeed          ⚪️⚪️🔘🔘🔘🔘🔘⚪️🔘🔘⚪️⚪️
	N.1005TinySeed          ⚪️⚪️🔘🔘🔘🔘🔘⚪️🔘🔘⚪️🔘
	N.1006TinySeed          ⚪️⚪️🔘🔘🔘🔘🔘⚪️🔘🔘🔘⚪️
	N.1007TinySeed          ⚪️⚪️🔘🔘🔘🔘🔘⚪️🔘🔘🔘🔘
	N.1008TinySeed          ⚪️⚪️🔘🔘🔘🔘🔘🔘⚪️⚪️⚪️⚪️
	N.1009TinySeed          ⚪️⚪️🔘🔘🔘🔘🔘🔘⚪️⚪️⚪️🔘
	N.1010TinySeed          ⚪️⚪️🔘🔘🔘🔘🔘🔘⚪️⚪️🔘⚪️
	N.1011TinySeed          ⚪️⚪️🔘🔘🔘🔘🔘🔘⚪️⚪️🔘🔘
	N.1012TinySeed          ⚪️⚪️🔘🔘🔘🔘🔘🔘⚪️🔘⚪️⚪️
	N.1013TinySeed          ⚪️⚪️🔘🔘🔘🔘🔘🔘⚪️🔘⚪️🔘
	N.1014TinySeed          ⚪️⚪️🔘🔘🔘🔘🔘🔘⚪️🔘🔘⚪️
	N.1015TinySeed          ⚪️⚪️🔘🔘🔘🔘🔘🔘⚪️🔘🔘🔘
	N.1016TinySeed          ⚪️⚪️🔘🔘🔘🔘🔘🔘🔘⚪️⚪️⚪️
	N.1017TinySeed          ⚪️⚪️🔘🔘🔘🔘🔘🔘🔘⚪️⚪️🔘
	N.1018TinySeed          ⚪️⚪️🔘🔘🔘🔘🔘🔘🔘⚪️🔘⚪️
	N.1019TinySeed          ⚪️⚪️🔘🔘🔘🔘🔘🔘🔘⚪️🔘🔘
	N.1020TinySeed          ⚪️⚪️🔘🔘🔘🔘🔘🔘🔘🔘⚪️⚪️
	N.1021TinySeed          ⚪️⚪️🔘🔘🔘🔘🔘🔘🔘🔘⚪️🔘
	N.1022TinySeed          ⚪️⚪️🔘🔘🔘🔘🔘🔘🔘🔘🔘⚪️
	N.1023TinySeed          ⚪️⚪️🔘🔘🔘🔘🔘🔘🔘🔘🔘🔘
	N.1024TinySeed          ⚪️🔘⚪️⚪️⚪️⚪️⚪️⚪️⚪️⚪️⚪️⚪️
	N.1025TinySeed          ⚪️🔘⚪️⚪️⚪️⚪️⚪️⚪️⚪️⚪️⚪️🔘
	N.1026TinySeed          ⚪️🔘⚪️⚪️⚪️⚪️⚪️⚪️⚪️⚪️🔘⚪️
	N.1027TinySeed          ⚪️🔘⚪️⚪️⚪️⚪️⚪️⚪️⚪️⚪️🔘🔘
	N.1028TinySeed          ⚪️🔘⚪️⚪️⚪️⚪️⚪️⚪️⚪️🔘⚪️⚪️
	N.1029TinySeed          ⚪️🔘⚪️⚪️⚪️⚪️⚪️⚪️⚪️🔘⚪️🔘
	N.1030TinySeed          ⚪️🔘⚪️⚪️⚪️⚪️⚪️⚪️⚪️🔘🔘⚪️
	N.1031TinySeed          ⚪️🔘⚪️⚪️⚪️⚪️⚪️⚪️⚪️🔘🔘🔘
	N.1032TinySeed          ⚪️🔘⚪️⚪️⚪️⚪️⚪️⚪️🔘⚪️⚪️⚪️
	N.1033TinySeed          ⚪️🔘⚪️⚪️⚪️⚪️⚪️⚪️🔘⚪️⚪️🔘
	N.1034TinySeed          ⚪️🔘⚪️⚪️⚪️⚪️⚪️⚪️🔘⚪️🔘⚪️
	N.1035TinySeed          ⚪️🔘⚪️⚪️⚪️⚪️⚪️⚪️🔘⚪️🔘🔘
	N.1036TinySeed          ⚪️🔘⚪️⚪️⚪️⚪️⚪️⚪️🔘🔘⚪️⚪️
	N.1037TinySeed          ⚪️🔘⚪️⚪️⚪️⚪️⚪️⚪️🔘🔘⚪️🔘
	N.1038TinySeed          ⚪️🔘⚪️⚪️⚪️⚪️⚪️⚪️🔘🔘🔘⚪️
	N.1039TinySeed          ⚪️🔘⚪️⚪️⚪️⚪️⚪️⚪️🔘🔘🔘🔘
	N.1040TinySeed          ⚪️🔘⚪️⚪️⚪️⚪️⚪️🔘⚪️⚪️⚪️⚪️
	N.1041TinySeed          ⚪️🔘⚪️⚪️⚪️⚪️⚪️🔘⚪️⚪️⚪️🔘
	N.1042TinySeed          ⚪️🔘⚪️⚪️⚪️⚪️⚪️🔘⚪️⚪️🔘⚪️
	N.1043TinySeed          ⚪️🔘⚪️⚪️⚪️⚪️⚪️🔘⚪️⚪️🔘🔘
	N.1044TinySeed          ⚪️🔘⚪️⚪️⚪️⚪️⚪️🔘⚪️🔘⚪️⚪️
	N.1045TinySeed          ⚪️🔘⚪️⚪️⚪️⚪️⚪️🔘⚪️🔘⚪️🔘
	N.1046TinySeed          ⚪️🔘⚪️⚪️⚪️⚪️⚪️🔘⚪️🔘🔘⚪️
	N.1047TinySeed          ⚪️🔘⚪️⚪️⚪️⚪️⚪️🔘⚪️🔘🔘🔘
	N.1048TinySeed          ⚪️🔘⚪️⚪️⚪️⚪️⚪️🔘🔘⚪️⚪️⚪️
	N.1049TinySeed          ⚪️🔘⚪️⚪️⚪️⚪️⚪️🔘🔘⚪️⚪️🔘
	N.1050TinySeed          ⚪️🔘⚪️⚪️⚪️⚪️⚪️🔘🔘⚪️🔘⚪️
	N.1051TinySeed          ⚪️🔘⚪️⚪️⚪️⚪️⚪️🔘🔘⚪️🔘🔘
	N.1052TinySeed          ⚪️🔘⚪️⚪️⚪️⚪️⚪️🔘🔘🔘⚪️⚪️
	N.1053TinySeed          ⚪️🔘⚪️⚪️⚪️⚪️⚪️🔘🔘🔘⚪️🔘
	N.1054TinySeed          ⚪️🔘⚪️⚪️⚪️⚪️⚪️🔘🔘🔘🔘⚪️
	N.1055TinySeed          ⚪️🔘⚪️⚪️⚪️⚪️⚪️🔘🔘🔘🔘🔘
	N.1056TinySeed          ⚪️🔘⚪️⚪️⚪️⚪️🔘⚪️⚪️⚪️⚪️⚪️
	N.1057TinySeed          ⚪️🔘⚪️⚪️⚪️⚪️🔘⚪️⚪️⚪️⚪️🔘
	N.1058TinySeed          ⚪️🔘⚪️⚪️⚪️⚪️🔘⚪️⚪️⚪️🔘⚪️
	N.1059TinySeed          ⚪️🔘⚪️⚪️⚪️⚪️🔘⚪️⚪️⚪️🔘🔘
	N.1060TinySeed          ⚪️🔘⚪️⚪️⚪️⚪️🔘⚪️⚪️🔘⚪️⚪️
	N.1061TinySeed          ⚪️🔘⚪️⚪️⚪️⚪️🔘⚪️⚪️🔘⚪️🔘
	N.1062TinySeed          ⚪️🔘⚪️⚪️⚪️⚪️🔘⚪️⚪️🔘🔘⚪️
	N.1063TinySeed          ⚪️🔘⚪️⚪️⚪️⚪️🔘⚪️⚪️🔘🔘🔘
	N.1064TinySeed          ⚪️🔘⚪️⚪️⚪️⚪️🔘⚪️🔘⚪️⚪️⚪️
	N.1065TinySeed          ⚪️🔘⚪️⚪️⚪️⚪️🔘⚪️🔘⚪️⚪️🔘
	N.1066TinySeed          ⚪️🔘⚪️⚪️⚪️⚪️🔘⚪️🔘⚪️🔘⚪️
	N.1067TinySeed          ⚪️🔘⚪️⚪️⚪️⚪️🔘⚪️🔘⚪️🔘🔘
	N.1068TinySeed          ⚪️🔘⚪️⚪️⚪️⚪️🔘⚪️🔘🔘⚪️⚪️
	N.1069TinySeed          ⚪️🔘⚪️⚪️⚪️⚪️🔘⚪️🔘🔘⚪️🔘
	N.1070TinySeed          ⚪️🔘⚪️⚪️⚪️⚪️🔘⚪️🔘🔘🔘⚪️
	N.1071TinySeed          ⚪️🔘⚪️⚪️⚪️⚪️🔘⚪️🔘🔘🔘🔘
	N.1072TinySeed          ⚪️🔘⚪️⚪️⚪️⚪️🔘🔘⚪️⚪️⚪️⚪️
	N.1073TinySeed          ⚪️🔘⚪️⚪️⚪️⚪️🔘🔘⚪️⚪️⚪️🔘
	N.1074TinySeed          ⚪️🔘⚪️⚪️⚪️⚪️🔘🔘⚪️⚪️🔘⚪️
	N.1075TinySeed          ⚪️🔘⚪️⚪️⚪️⚪️🔘🔘⚪️⚪️🔘🔘
	N.1076TinySeed          ⚪️🔘⚪️⚪️⚪️⚪️🔘🔘⚪️🔘⚪️⚪️
	N.1077TinySeed          ⚪️🔘⚪️⚪️⚪️⚪️🔘🔘⚪️🔘⚪️🔘
	N.1078TinySeed          ⚪️🔘⚪️⚪️⚪️⚪️🔘🔘⚪️🔘🔘⚪️
	N.1079TinySeed          ⚪️🔘⚪️⚪️⚪️⚪️🔘🔘⚪️🔘🔘🔘
	N.1080TinySeed          ⚪️🔘⚪️⚪️⚪️⚪️🔘🔘🔘⚪️⚪️⚪️
	N.1081TinySeed          ⚪️🔘⚪️⚪️⚪️⚪️🔘🔘🔘⚪️⚪️🔘
	N.1082TinySeed          ⚪️🔘⚪️⚪️⚪️⚪️🔘🔘🔘⚪️🔘⚪️
	N.1083TinySeed          ⚪️🔘⚪️⚪️⚪️⚪️🔘🔘🔘⚪️🔘🔘
	N.1084TinySeed          ⚪️🔘⚪️⚪️⚪️⚪️🔘🔘🔘🔘⚪️⚪️
	N.1085TinySeed          ⚪️🔘⚪️⚪️⚪️⚪️🔘🔘🔘🔘⚪️🔘
	N.1086TinySeed          ⚪️🔘⚪️⚪️⚪️⚪️🔘🔘🔘🔘🔘⚪️
	N.1087TinySeed          ⚪️🔘⚪️⚪️⚪️⚪️🔘🔘🔘🔘🔘🔘
	N.1088TinySeed          ⚪️🔘⚪️⚪️⚪️🔘⚪️⚪️⚪️⚪️⚪️⚪️
	N.1089TinySeed          ⚪️🔘⚪️⚪️⚪️🔘⚪️⚪️⚪️⚪️⚪️🔘
	N.1090TinySeed          ⚪️🔘⚪️⚪️⚪️🔘⚪️⚪️⚪️⚪️🔘⚪️
	N.1091TinySeed          ⚪️🔘⚪️⚪️⚪️🔘⚪️⚪️⚪️⚪️🔘🔘
	N.1092TinySeed          ⚪️🔘⚪️⚪️⚪️🔘⚪️⚪️⚪️🔘⚪️⚪️
	N.1093TinySeed          ⚪️🔘⚪️⚪️⚪️🔘⚪️⚪️⚪️🔘⚪️🔘
	N.1094TinySeed          ⚪️🔘⚪️⚪️⚪️🔘⚪️⚪️⚪️🔘🔘⚪️
	N.1095TinySeed          ⚪️🔘⚪️⚪️⚪️🔘⚪️⚪️⚪️🔘🔘🔘
	N.1096TinySeed          ⚪️🔘⚪️⚪️⚪️🔘⚪️⚪️🔘⚪️⚪️⚪️
	N.1097TinySeed          ⚪️🔘⚪️⚪️⚪️🔘⚪️⚪️🔘⚪️⚪️🔘
	N.1098TinySeed          ⚪️🔘⚪️⚪️⚪️🔘⚪️⚪️🔘⚪️🔘⚪️
	N.1099TinySeed          ⚪️🔘⚪️⚪️⚪️🔘⚪️⚪️🔘⚪️🔘🔘
	N.1100TinySeed          ⚪️🔘⚪️⚪️⚪️🔘⚪️⚪️🔘🔘⚪️⚪️
	N.1101TinySeed          ⚪️🔘⚪️⚪️⚪️🔘⚪️⚪️🔘🔘⚪️🔘
	N.1102TinySeed          ⚪️🔘⚪️⚪️⚪️🔘⚪️⚪️🔘🔘🔘⚪️
	N.1103TinySeed          ⚪️🔘⚪️⚪️⚪️🔘⚪️⚪️🔘🔘🔘🔘
	N.1104TinySeed          ⚪️🔘⚪️⚪️⚪️🔘⚪️🔘⚪️⚪️⚪️⚪️
	N.1105TinySeed          ⚪️🔘⚪️⚪️⚪️🔘⚪️🔘⚪️⚪️⚪️🔘
	N.1106TinySeed          ⚪️🔘⚪️⚪️⚪️🔘⚪️🔘⚪️⚪️🔘⚪️
	N.1107TinySeed          ⚪️🔘⚪️⚪️⚪️🔘⚪️🔘⚪️⚪️🔘🔘
	N.1108TinySeed          ⚪️🔘⚪️⚪️⚪️🔘⚪️🔘⚪️🔘⚪️⚪️
	N.1109TinySeed          ⚪️🔘⚪️⚪️⚪️🔘⚪️🔘⚪️🔘⚪️🔘
	N.1110TinySeed          ⚪️🔘⚪️⚪️⚪️🔘⚪️🔘⚪️🔘🔘⚪️
	N.1111TinySeed          ⚪️🔘⚪️⚪️⚪️🔘⚪️🔘⚪️🔘🔘🔘
	N.1112TinySeed          ⚪️🔘⚪️⚪️⚪️🔘⚪️🔘🔘⚪️⚪️⚪️
	N.1113TinySeed          ⚪️🔘⚪️⚪️⚪️🔘⚪️🔘🔘⚪️⚪️🔘
	N.1114TinySeed          ⚪️🔘⚪️⚪️⚪️🔘⚪️🔘🔘⚪️🔘⚪️
	N.1115TinySeed          ⚪️🔘⚪️⚪️⚪️🔘⚪️🔘🔘⚪️🔘🔘
	N.1116TinySeed          ⚪️🔘⚪️⚪️⚪️🔘⚪️🔘🔘🔘⚪️⚪️
	N.1117TinySeed          ⚪️🔘⚪️⚪️⚪️🔘⚪️🔘🔘🔘⚪️🔘
	N.1118TinySeed          ⚪️🔘⚪️⚪️⚪️🔘⚪️🔘🔘🔘🔘⚪️
	N.1119TinySeed          ⚪️🔘⚪️⚪️⚪️🔘⚪️🔘🔘🔘🔘🔘
	N.1120TinySeed          ⚪️🔘⚪️⚪️⚪️🔘🔘⚪️⚪️⚪️⚪️⚪️
	N.1121TinySeed          ⚪️🔘⚪️⚪️⚪️🔘🔘⚪️⚪️⚪️⚪️🔘
	N.1122TinySeed          ⚪️🔘⚪️⚪️⚪️🔘🔘⚪️⚪️⚪️🔘⚪️
	N.1123TinySeed          ⚪️🔘⚪️⚪️⚪️🔘🔘⚪️⚪️⚪️🔘🔘
	N.1124TinySeed          ⚪️🔘⚪️⚪️⚪️🔘🔘⚪️⚪️🔘⚪️⚪️
	N.1125TinySeed          ⚪️🔘⚪️⚪️⚪️🔘🔘⚪️⚪️🔘⚪️🔘
	N.1126TinySeed          ⚪️🔘⚪️⚪️⚪️🔘🔘⚪️⚪️🔘🔘⚪️
	N.1127TinySeed          ⚪️🔘⚪️⚪️⚪️🔘🔘⚪️⚪️🔘🔘🔘
	N.1128TinySeed          ⚪️🔘⚪️⚪️⚪️🔘🔘⚪️🔘⚪️⚪️⚪️
	N.1129TinySeed          ⚪️🔘⚪️⚪️⚪️🔘🔘⚪️🔘⚪️⚪️🔘
	N.1130TinySeed          ⚪️🔘⚪️⚪️⚪️🔘🔘⚪️🔘⚪️🔘⚪️
	N.1131TinySeed          ⚪️🔘⚪️⚪️⚪️🔘🔘⚪️🔘⚪️🔘🔘
	N.1132TinySeed          ⚪️🔘⚪️⚪️⚪️🔘🔘⚪️🔘🔘⚪️⚪️
	N.1133TinySeed          ⚪️🔘⚪️⚪️⚪️🔘🔘⚪️🔘🔘⚪️🔘
	N.1134TinySeed          ⚪️🔘⚪️⚪️⚪️🔘🔘⚪️🔘🔘🔘⚪️
	N.1135TinySeed          ⚪️🔘⚪️⚪️⚪️🔘🔘⚪️🔘🔘🔘🔘
	N.1136TinySeed          ⚪️🔘⚪️⚪️⚪️🔘🔘🔘⚪️⚪️⚪️⚪️
	N.1137TinySeed          ⚪️🔘⚪️⚪️⚪️🔘🔘🔘⚪️⚪️⚪️🔘
	N.1138TinySeed          ⚪️🔘⚪️⚪️⚪️🔘🔘🔘⚪️⚪️🔘⚪️
	N.1139TinySeed          ⚪️🔘⚪️⚪️⚪️🔘🔘🔘⚪️⚪️🔘🔘
	N.1140TinySeed          ⚪️🔘⚪️⚪️⚪️🔘🔘🔘⚪️🔘⚪️⚪️
	N.1141TinySeed          ⚪️🔘⚪️⚪️⚪️🔘🔘🔘⚪️🔘⚪️🔘
	N.1142TinySeed          ⚪️🔘⚪️⚪️⚪️🔘🔘🔘⚪️🔘🔘⚪️
	N.1143TinySeed          ⚪️🔘⚪️⚪️⚪️🔘🔘🔘⚪️🔘🔘🔘
	N.1144TinySeed          ⚪️🔘⚪️⚪️⚪️🔘🔘🔘🔘⚪️⚪️⚪️
	N.1145TinySeed          ⚪️🔘⚪️⚪️⚪️🔘🔘🔘🔘⚪️⚪️🔘
	N.1146TinySeed          ⚪️🔘⚪️⚪️⚪️🔘🔘🔘🔘⚪️🔘⚪️
	N.1147TinySeed          ⚪️🔘⚪️⚪️⚪️🔘🔘🔘🔘⚪️🔘🔘
	N.1148TinySeed          ⚪️🔘⚪️⚪️⚪️🔘🔘🔘🔘🔘⚪️⚪️
	N.1149TinySeed          ⚪️🔘⚪️⚪️⚪️🔘🔘🔘🔘🔘⚪️🔘
	N.1150TinySeed          ⚪️🔘⚪️⚪️⚪️🔘🔘🔘🔘🔘🔘⚪️
	N.1151TinySeed          ⚪️🔘⚪️⚪️⚪️🔘🔘🔘🔘🔘🔘🔘
	N.1152TinySeed          ⚪️🔘⚪️⚪️🔘⚪️⚪️⚪️⚪️⚪️⚪️⚪️
	N.1153TinySeed          ⚪️🔘⚪️⚪️🔘⚪️⚪️⚪️⚪️⚪️⚪️🔘
	N.1154TinySeed          ⚪️🔘⚪️⚪️🔘⚪️⚪️⚪️⚪️⚪️🔘⚪️
	N.1155TinySeed          ⚪️🔘⚪️⚪️🔘⚪️⚪️⚪️⚪️⚪️🔘🔘
	N.1156TinySeed          ⚪️🔘⚪️⚪️🔘⚪️⚪️⚪️⚪️🔘⚪️⚪️
	N.1157TinySeed          ⚪️🔘⚪️⚪️🔘⚪️⚪️⚪️⚪️🔘⚪️🔘
	N.1158TinySeed          ⚪️🔘⚪️⚪️🔘⚪️⚪️⚪️⚪️🔘🔘⚪️
	N.1159TinySeed          ⚪️🔘⚪️⚪️🔘⚪️⚪️⚪️⚪️🔘🔘🔘
	N.1160TinySeed          ⚪️🔘⚪️⚪️🔘⚪️⚪️⚪️🔘⚪️⚪️⚪️
	N.1161TinySeed          ⚪️🔘⚪️⚪️🔘⚪️⚪️⚪️🔘⚪️⚪️🔘
	N.1162TinySeed          ⚪️🔘⚪️⚪️🔘⚪️⚪️⚪️🔘⚪️🔘⚪️
	N.1163TinySeed          ⚪️🔘⚪️⚪️🔘⚪️⚪️⚪️🔘⚪️🔘🔘
	N.1164TinySeed          ⚪️🔘⚪️⚪️🔘⚪️⚪️⚪️🔘🔘⚪️⚪️
	N.1165TinySeed          ⚪️🔘⚪️⚪️🔘⚪️⚪️⚪️🔘🔘⚪️🔘
	N.1166TinySeed          ⚪️🔘⚪️⚪️🔘⚪️⚪️⚪️🔘🔘🔘⚪️
	N.1167TinySeed          ⚪️🔘⚪️⚪️🔘⚪️⚪️⚪️🔘🔘🔘🔘
	N.1168TinySeed          ⚪️🔘⚪️⚪️🔘⚪️⚪️🔘⚪️⚪️⚪️⚪️
	N.1169TinySeed          ⚪️🔘⚪️⚪️🔘⚪️⚪️🔘⚪️⚪️⚪️🔘
	N.1170TinySeed          ⚪️🔘⚪️⚪️🔘⚪️⚪️🔘⚪️⚪️🔘⚪️
	N.1171TinySeed          ⚪️🔘⚪️⚪️🔘⚪️⚪️🔘⚪️⚪️🔘🔘
	N.1172TinySeed          ⚪️🔘⚪️⚪️🔘⚪️⚪️🔘⚪️🔘⚪️⚪️
	N.1173TinySeed          ⚪️🔘⚪️⚪️🔘⚪️⚪️🔘⚪️🔘⚪️🔘
	N.1174TinySeed          ⚪️🔘⚪️⚪️🔘⚪️⚪️🔘⚪️🔘🔘⚪️
	N.1175TinySeed          ⚪️🔘⚪️⚪️🔘⚪️⚪️🔘⚪️🔘🔘🔘
	N.1176TinySeed          ⚪️🔘⚪️⚪️🔘⚪️⚪️🔘🔘⚪️⚪️⚪️
	N.1177TinySeed          ⚪️🔘⚪️⚪️🔘⚪️⚪️🔘🔘⚪️⚪️🔘
	N.1178TinySeed          ⚪️🔘⚪️⚪️🔘⚪️⚪️🔘🔘⚪️🔘⚪️
	N.1179TinySeed          ⚪️🔘⚪️⚪️🔘⚪️⚪️🔘🔘⚪️🔘🔘
	N.1180TinySeed          ⚪️🔘⚪️⚪️🔘⚪️⚪️🔘🔘🔘⚪️⚪️
	N.1181TinySeed          ⚪️🔘⚪️⚪️🔘⚪️⚪️🔘🔘🔘⚪️🔘
	N.1182TinySeed          ⚪️🔘⚪️⚪️🔘⚪️⚪️🔘🔘🔘🔘⚪️
	N.1183TinySeed          ⚪️🔘⚪️⚪️🔘⚪️⚪️🔘🔘🔘🔘🔘
	N.1184TinySeed          ⚪️🔘⚪️⚪️🔘⚪️🔘⚪️⚪️⚪️⚪️⚪️
	N.1185TinySeed          ⚪️🔘⚪️⚪️🔘⚪️🔘⚪️⚪️⚪️⚪️🔘
	N.1186TinySeed          ⚪️🔘⚪️⚪️🔘⚪️🔘⚪️⚪️⚪️🔘⚪️
	N.1187TinySeed          ⚪️🔘⚪️⚪️🔘⚪️🔘⚪️⚪️⚪️🔘🔘
	N.1188TinySeed          ⚪️🔘⚪️⚪️🔘⚪️🔘⚪️⚪️🔘⚪️⚪️
	N.1189TinySeed          ⚪️🔘⚪️⚪️🔘⚪️🔘⚪️⚪️🔘⚪️🔘
	N.1190TinySeed          ⚪️🔘⚪️⚪️🔘⚪️🔘⚪️⚪️🔘🔘⚪️
	N.1191TinySeed          ⚪️🔘⚪️⚪️🔘⚪️🔘⚪️⚪️🔘🔘🔘
	N.1192TinySeed          ⚪️🔘⚪️⚪️🔘⚪️🔘⚪️🔘⚪️⚪️⚪️
	N.1193TinySeed          ⚪️🔘⚪️⚪️🔘⚪️🔘⚪️🔘⚪️⚪️🔘
	N.1194TinySeed          ⚪️🔘⚪️⚪️🔘⚪️🔘⚪️🔘⚪️🔘⚪️
	N.1195TinySeed          ⚪️🔘⚪️⚪️🔘⚪️🔘⚪️🔘⚪️🔘🔘
	N.1196TinySeed          ⚪️🔘⚪️⚪️🔘⚪️🔘⚪️🔘🔘⚪️⚪️
	N.1197TinySeed          ⚪️🔘⚪️⚪️🔘⚪️🔘⚪️🔘🔘⚪️🔘
	N.1198TinySeed          ⚪️🔘⚪️⚪️🔘⚪️🔘⚪️🔘🔘🔘⚪️
	N.1199TinySeed          ⚪️🔘⚪️⚪️🔘⚪️🔘⚪️🔘🔘🔘🔘
	N.1200TinySeed          ⚪️🔘⚪️⚪️🔘⚪️🔘🔘⚪️⚪️⚪️⚪️
	N.1201TinySeed          ⚪️🔘⚪️⚪️🔘⚪️🔘🔘⚪️⚪️⚪️🔘
	N.1202TinySeed          ⚪️🔘⚪️⚪️🔘⚪️🔘🔘⚪️⚪️🔘⚪️
	N.1203TinySeed          ⚪️🔘⚪️⚪️🔘⚪️🔘🔘⚪️⚪️🔘🔘
	N.1204TinySeed          ⚪️🔘⚪️⚪️🔘⚪️🔘🔘⚪️🔘⚪️⚪️
	N.1205TinySeed          ⚪️🔘⚪️⚪️🔘⚪️🔘🔘⚪️🔘⚪️🔘
	N.1206TinySeed          ⚪️🔘⚪️⚪️🔘⚪️🔘🔘⚪️🔘🔘⚪️
	N.1207TinySeed          ⚪️🔘⚪️⚪️🔘⚪️🔘🔘⚪️🔘🔘🔘
	N.1208TinySeed          ⚪️🔘⚪️⚪️🔘⚪️🔘🔘🔘⚪️⚪️⚪️
	N.1209TinySeed          ⚪️🔘⚪️⚪️🔘⚪️🔘🔘🔘⚪️⚪️🔘
	N.1210TinySeed          ⚪️🔘⚪️⚪️🔘⚪️🔘🔘🔘⚪️🔘⚪️
	N.1211TinySeed          ⚪️🔘⚪️⚪️🔘⚪️🔘🔘🔘⚪️🔘🔘
	N.1212TinySeed          ⚪️🔘⚪️⚪️🔘⚪️🔘🔘🔘🔘⚪️⚪️
	N.1213TinySeed          ⚪️🔘⚪️⚪️🔘⚪️🔘🔘🔘🔘⚪️🔘
	N.1214TinySeed          ⚪️🔘⚪️⚪️🔘⚪️🔘🔘🔘🔘🔘⚪️
	N.1215TinySeed          ⚪️🔘⚪️⚪️🔘⚪️🔘🔘🔘🔘🔘🔘
	N.1216TinySeed          ⚪️🔘⚪️⚪️🔘🔘⚪️⚪️⚪️⚪️⚪️⚪️
	N.1217TinySeed          ⚪️🔘⚪️⚪️🔘🔘⚪️⚪️⚪️⚪️⚪️🔘
	N.1218TinySeed          ⚪️🔘⚪️⚪️🔘🔘⚪️⚪️⚪️⚪️🔘⚪️
	N.1219TinySeed          ⚪️🔘⚪️⚪️🔘🔘⚪️⚪️⚪️⚪️🔘🔘
	N.1220TinySeed          ⚪️🔘⚪️⚪️🔘🔘⚪️⚪️⚪️🔘⚪️⚪️
	N.1221TinySeed          ⚪️🔘⚪️⚪️🔘🔘⚪️⚪️⚪️🔘⚪️🔘
	N.1222TinySeed          ⚪️🔘⚪️⚪️🔘🔘⚪️⚪️⚪️🔘🔘⚪️
	N.1223TinySeed          ⚪️🔘⚪️⚪️🔘🔘⚪️⚪️⚪️🔘🔘🔘
	N.1224TinySeed          ⚪️🔘⚪️⚪️🔘🔘⚪️⚪️🔘⚪️⚪️⚪️
	N.1225TinySeed          ⚪️🔘⚪️⚪️🔘🔘⚪️⚪️🔘⚪️⚪️🔘
	N.1226TinySeed          ⚪️🔘⚪️⚪️🔘🔘⚪️⚪️🔘⚪️🔘⚪️
	N.1227TinySeed          ⚪️🔘⚪️⚪️🔘🔘⚪️⚪️🔘⚪️🔘🔘
	N.1228TinySeed          ⚪️🔘⚪️⚪️🔘🔘⚪️⚪️🔘🔘⚪️⚪️
	N.1229TinySeed          ⚪️🔘⚪️⚪️🔘🔘⚪️⚪️🔘🔘⚪️🔘
	N.1230TinySeed          ⚪️🔘⚪️⚪️🔘🔘⚪️⚪️🔘🔘🔘⚪️
	N.1231TinySeed          ⚪️🔘⚪️⚪️🔘🔘⚪️⚪️🔘🔘🔘🔘
	N.1232TinySeed          ⚪️🔘⚪️⚪️🔘🔘⚪️🔘⚪️⚪️⚪️⚪️
	N.1233TinySeed          ⚪️🔘⚪️⚪️🔘🔘⚪️🔘⚪️⚪️⚪️🔘
	N.1234TinySeed          ⚪️🔘⚪️⚪️🔘🔘⚪️🔘⚪️⚪️🔘⚪️
	N.1235TinySeed          ⚪️🔘⚪️⚪️🔘🔘⚪️🔘⚪️⚪️🔘🔘
	N.1236TinySeed          ⚪️🔘⚪️⚪️🔘🔘⚪️🔘⚪️🔘⚪️⚪️
	N.1237TinySeed          ⚪️🔘⚪️⚪️🔘🔘⚪️🔘⚪️🔘⚪️🔘
	N.1238TinySeed          ⚪️🔘⚪️⚪️🔘🔘⚪️🔘⚪️🔘🔘⚪️
	N.1239TinySeed          ⚪️🔘⚪️⚪️🔘🔘⚪️🔘⚪️🔘🔘🔘
	N.1240TinySeed          ⚪️🔘⚪️⚪️🔘🔘⚪️🔘🔘⚪️⚪️⚪️
	N.1241TinySeed          ⚪️🔘⚪️⚪️🔘🔘⚪️🔘🔘⚪️⚪️🔘
	N.1242TinySeed          ⚪️🔘⚪️⚪️🔘🔘⚪️🔘🔘⚪️🔘⚪️
	N.1243TinySeed          ⚪️🔘⚪️⚪️🔘🔘⚪️🔘🔘⚪️🔘🔘
	N.1244TinySeed          ⚪️🔘⚪️⚪️🔘🔘⚪️🔘🔘🔘⚪️⚪️
	N.1245TinySeed          ⚪️🔘⚪️⚪️🔘🔘⚪️🔘🔘🔘⚪️🔘
	N.1246TinySeed          ⚪️🔘⚪️⚪️🔘🔘⚪️🔘🔘🔘🔘⚪️
	N.1247TinySeed          ⚪️🔘⚪️⚪️🔘🔘⚪️🔘🔘🔘🔘🔘
	N.1248TinySeed          ⚪️🔘⚪️⚪️🔘🔘🔘⚪️⚪️⚪️⚪️⚪️
	N.1249TinySeed          ⚪️🔘⚪️⚪️🔘🔘🔘⚪️⚪️⚪️⚪️🔘
	N.1250TinySeed          ⚪️🔘⚪️⚪️🔘🔘🔘⚪️⚪️⚪️🔘⚪️
	N.1251TinySeed          ⚪️🔘⚪️⚪️🔘🔘🔘⚪️⚪️⚪️🔘🔘
	N.1252TinySeed          ⚪️🔘⚪️⚪️🔘🔘🔘⚪️⚪️🔘⚪️⚪️
	N.1253TinySeed          ⚪️🔘⚪️⚪️🔘🔘🔘⚪️⚪️🔘⚪️🔘
	N.1254TinySeed          ⚪️🔘⚪️⚪️🔘🔘🔘⚪️⚪️🔘🔘⚪️
	N.1255TinySeed          ⚪️🔘⚪️⚪️🔘🔘🔘⚪️⚪️🔘🔘🔘
	N.1256TinySeed          ⚪️🔘⚪️⚪️🔘🔘🔘⚪️🔘⚪️⚪️⚪️
	N.1257TinySeed          ⚪️🔘⚪️⚪️🔘🔘🔘⚪️🔘⚪️⚪️🔘
	N.1258TinySeed          ⚪️🔘⚪️⚪️🔘🔘🔘⚪️🔘⚪️🔘⚪️
	N.1259TinySeed          ⚪️🔘⚪️⚪️🔘🔘🔘⚪️🔘⚪️🔘🔘
	N.1260TinySeed          ⚪️🔘⚪️⚪️🔘🔘🔘⚪️🔘🔘⚪️⚪️
	N.1261TinySeed          ⚪️🔘⚪️⚪️🔘🔘🔘⚪️🔘🔘⚪️🔘
	N.1262TinySeed          ⚪️🔘⚪️⚪️🔘🔘🔘⚪️🔘🔘🔘⚪️
	N.1263TinySeed          ⚪️🔘⚪️⚪️🔘🔘🔘⚪️🔘🔘🔘🔘
	N.1264TinySeed          ⚪️🔘⚪️⚪️🔘🔘🔘🔘⚪️⚪️⚪️⚪️
	N.1265TinySeed          ⚪️🔘⚪️⚪️🔘🔘🔘🔘⚪️⚪️⚪️🔘
	N.1266TinySeed          ⚪️🔘⚪️⚪️🔘🔘🔘🔘⚪️⚪️🔘⚪️
	N.1267TinySeed          ⚪️🔘⚪️⚪️🔘🔘🔘🔘⚪️⚪️🔘🔘
	N.1268TinySeed          ⚪️🔘⚪️⚪️🔘🔘🔘🔘⚪️🔘⚪️⚪️
	N.1269TinySeed          ⚪️🔘⚪️⚪️🔘🔘🔘🔘⚪️🔘⚪️🔘
	N.1270TinySeed          ⚪️🔘⚪️⚪️🔘🔘🔘🔘⚪️🔘🔘⚪️
	N.1271TinySeed          ⚪️🔘⚪️⚪️🔘🔘🔘🔘⚪️🔘🔘🔘
	N.1272TinySeed          ⚪️🔘⚪️⚪️🔘🔘🔘🔘🔘⚪️⚪️⚪️
	N.1273TinySeed          ⚪️🔘⚪️⚪️🔘🔘🔘🔘🔘⚪️⚪️🔘
	N.1274TinySeed          ⚪️🔘⚪️⚪️🔘🔘🔘🔘🔘⚪️🔘⚪️
	N.1275TinySeed          ⚪️🔘⚪️⚪️🔘🔘🔘🔘🔘⚪️🔘🔘
	N.1276TinySeed          ⚪️🔘⚪️⚪️🔘🔘🔘🔘🔘🔘⚪️⚪️
	N.1277TinySeed          ⚪️🔘⚪️⚪️🔘🔘🔘🔘🔘🔘⚪️🔘
	N.1278TinySeed          ⚪️🔘⚪️⚪️🔘🔘🔘🔘🔘🔘🔘⚪️
	N.1279TinySeed          ⚪️🔘⚪️⚪️🔘🔘🔘🔘🔘🔘🔘🔘
	N.1280TinySeed          ⚪️🔘⚪️🔘⚪️⚪️⚪️⚪️⚪️⚪️⚪️⚪️
	N.1281TinySeed          ⚪️🔘⚪️🔘⚪️⚪️⚪️⚪️⚪️⚪️⚪️🔘
	N.1282TinySeed          ⚪️🔘⚪️🔘⚪️⚪️⚪️⚪️⚪️⚪️🔘⚪️
	N.1283TinySeed          ⚪️🔘⚪️🔘⚪️⚪️⚪️⚪️⚪️⚪️🔘🔘
	N.1284TinySeed          ⚪️🔘⚪️🔘⚪️⚪️⚪️⚪️⚪️🔘⚪️⚪️
	N.1285TinySeed          ⚪️🔘⚪️🔘⚪️⚪️⚪️⚪️⚪️🔘⚪️🔘
	N.1286TinySeed          ⚪️🔘⚪️🔘⚪️⚪️⚪️⚪️⚪️🔘🔘⚪️
	N.1287TinySeed          ⚪️🔘⚪️🔘⚪️⚪️⚪️⚪️⚪️🔘🔘🔘
	N.1288TinySeed          ⚪️🔘⚪️🔘⚪️⚪️⚪️⚪️🔘⚪️⚪️⚪️
	N.1289TinySeed          ⚪️🔘⚪️🔘⚪️⚪️⚪️⚪️🔘⚪️⚪️🔘
	N.1290TinySeed          ⚪️🔘⚪️🔘⚪️⚪️⚪️⚪️🔘⚪️🔘⚪️
	N.1291TinySeed          ⚪️🔘⚪️🔘⚪️⚪️⚪️⚪️🔘⚪️🔘🔘
	N.1292TinySeed          ⚪️🔘⚪️🔘⚪️⚪️⚪️⚪️🔘🔘⚪️⚪️
	N.1293TinySeed          ⚪️🔘⚪️🔘⚪️⚪️⚪️⚪️🔘🔘⚪️🔘
	N.1294TinySeed          ⚪️🔘⚪️🔘⚪️⚪️⚪️⚪️🔘🔘🔘⚪️
	N.1295TinySeed          ⚪️🔘⚪️🔘⚪️⚪️⚪️⚪️🔘🔘🔘🔘
	N.1296TinySeed          ⚪️🔘⚪️🔘⚪️⚪️⚪️🔘⚪️⚪️⚪️⚪️
	N.1297TinySeed          ⚪️🔘⚪️🔘⚪️⚪️⚪️🔘⚪️⚪️⚪️🔘
	N.1298TinySeed          ⚪️🔘⚪️🔘⚪️⚪️⚪️🔘⚪️⚪️🔘⚪️
	N.1299TinySeed          ⚪️🔘⚪️🔘⚪️⚪️⚪️🔘⚪️⚪️🔘🔘
	N.1300TinySeed          ⚪️🔘⚪️🔘⚪️⚪️⚪️🔘⚪️🔘⚪️⚪️
	N.1301TinySeed          ⚪️🔘⚪️🔘⚪️⚪️⚪️🔘⚪️🔘⚪️🔘
	N.1302TinySeed          ⚪️🔘⚪️🔘⚪️⚪️⚪️🔘⚪️🔘🔘⚪️
	N.1303TinySeed          ⚪️🔘⚪️🔘⚪️⚪️⚪️🔘⚪️🔘🔘🔘
	N.1304TinySeed          ⚪️🔘⚪️🔘⚪️⚪️⚪️🔘🔘⚪️⚪️⚪️
	N.1305TinySeed          ⚪️🔘⚪️🔘⚪️⚪️⚪️🔘🔘⚪️⚪️🔘
	N.1306TinySeed          ⚪️🔘⚪️🔘⚪️⚪️⚪️🔘🔘⚪️🔘⚪️
	N.1307TinySeed          ⚪️🔘⚪️🔘⚪️⚪️⚪️🔘🔘⚪️🔘🔘
	N.1308TinySeed          ⚪️🔘⚪️🔘⚪️⚪️⚪️🔘🔘🔘⚪️⚪️
	N.1309TinySeed          ⚪️🔘⚪️🔘⚪️⚪️⚪️🔘🔘🔘⚪️🔘
	N.1310TinySeed          ⚪️🔘⚪️🔘⚪️⚪️⚪️🔘🔘🔘🔘⚪️
	N.1311TinySeed          ⚪️🔘⚪️🔘⚪️⚪️⚪️🔘🔘🔘🔘🔘
	N.1312TinySeed          ⚪️🔘⚪️🔘⚪️⚪️🔘⚪️⚪️⚪️⚪️⚪️
	N.1313TinySeed          ⚪️🔘⚪️🔘⚪️⚪️🔘⚪️⚪️⚪️⚪️🔘
	N.1314TinySeed          ⚪️🔘⚪️🔘⚪️⚪️🔘⚪️⚪️⚪️🔘⚪️
	N.1315TinySeed          ⚪️🔘⚪️🔘⚪️⚪️🔘⚪️⚪️⚪️🔘🔘
	N.1316TinySeed          ⚪️🔘⚪️🔘⚪️⚪️🔘⚪️⚪️🔘⚪️⚪️
	N.1317TinySeed          ⚪️🔘⚪️🔘⚪️⚪️🔘⚪️⚪️🔘⚪️🔘
	N.1318TinySeed          ⚪️🔘⚪️🔘⚪️⚪️🔘⚪️⚪️🔘🔘⚪️
	N.1319TinySeed          ⚪️🔘⚪️🔘⚪️⚪️🔘⚪️⚪️🔘🔘🔘
	N.1320TinySeed          ⚪️🔘⚪️🔘⚪️⚪️🔘⚪️🔘⚪️⚪️⚪️
	N.1321TinySeed          ⚪️🔘⚪️🔘⚪️⚪️🔘⚪️🔘⚪️⚪️🔘
	N.1322TinySeed          ⚪️🔘⚪️🔘⚪️⚪️🔘⚪️🔘⚪️🔘⚪️
	N.1323TinySeed          ⚪️🔘⚪️🔘⚪️⚪️🔘⚪️🔘⚪️🔘🔘
	N.1324TinySeed          ⚪️🔘⚪️🔘⚪️⚪️🔘⚪️🔘🔘⚪️⚪️
	N.1325TinySeed          ⚪️🔘⚪️🔘⚪️⚪️🔘⚪️🔘🔘⚪️🔘
	N.1326TinySeed          ⚪️🔘⚪️🔘⚪️⚪️🔘⚪️🔘🔘🔘⚪️
	N.1327TinySeed          ⚪️🔘⚪️🔘⚪️⚪️🔘⚪️🔘🔘🔘🔘
	N.1328TinySeed          ⚪️🔘⚪️🔘⚪️⚪️🔘🔘⚪️⚪️⚪️⚪️
	N.1329TinySeed          ⚪️🔘⚪️🔘⚪️⚪️🔘🔘⚪️⚪️⚪️🔘
	N.1330TinySeed          ⚪️🔘⚪️🔘⚪️⚪️🔘🔘⚪️⚪️🔘⚪️
	N.1331TinySeed          ⚪️🔘⚪️🔘⚪️⚪️🔘🔘⚪️⚪️🔘🔘
	N.1332TinySeed          ⚪️🔘⚪️🔘⚪️⚪️🔘🔘⚪️🔘⚪️⚪️
	N.1333TinySeed          ⚪️🔘⚪️🔘⚪️⚪️🔘🔘⚪️🔘⚪️🔘
	N.1334TinySeed          ⚪️🔘⚪️🔘⚪️⚪️🔘🔘⚪️🔘🔘⚪️
	N.1335TinySeed          ⚪️🔘⚪️🔘⚪️⚪️🔘🔘⚪️🔘🔘🔘
	N.1336TinySeed          ⚪️🔘⚪️🔘⚪️⚪️🔘🔘🔘⚪️⚪️⚪️
	N.1337TinySeed          ⚪️🔘⚪️🔘⚪️⚪️🔘🔘🔘⚪️⚪️🔘
	N.1338TinySeed          ⚪️🔘⚪️🔘⚪️⚪️🔘🔘🔘⚪️🔘⚪️
	N.1339TinySeed          ⚪️🔘⚪️🔘⚪️⚪️🔘🔘🔘⚪️🔘🔘
	N.1340TinySeed          ⚪️🔘⚪️🔘⚪️⚪️🔘🔘🔘🔘⚪️⚪️
	N.1341TinySeed          ⚪️🔘⚪️🔘⚪️⚪️🔘🔘🔘🔘⚪️🔘
	N.1342TinySeed          ⚪️🔘⚪️🔘⚪️⚪️🔘🔘🔘🔘🔘⚪️
	N.1343TinySeed          ⚪️🔘⚪️🔘⚪️⚪️🔘🔘🔘🔘🔘🔘
	N.1344TinySeed          ⚪️🔘⚪️🔘⚪️🔘⚪️⚪️⚪️⚪️⚪️⚪️
	N.1345TinySeed          ⚪️🔘⚪️🔘⚪️🔘⚪️⚪️⚪️⚪️⚪️🔘
	N.1346TinySeed          ⚪️🔘⚪️🔘⚪️🔘⚪️⚪️⚪️⚪️🔘⚪️
	N.1347TinySeed          ⚪️🔘⚪️🔘⚪️🔘⚪️⚪️⚪️⚪️🔘🔘
	N.1348TinySeed          ⚪️🔘⚪️🔘⚪️🔘⚪️⚪️⚪️🔘⚪️⚪️
	N.1349TinySeed          ⚪️🔘⚪️🔘⚪️🔘⚪️⚪️⚪️🔘⚪️🔘
	N.1350TinySeed          ⚪️🔘⚪️🔘⚪️🔘⚪️⚪️⚪️🔘🔘⚪️
	N.1351TinySeed          ⚪️🔘⚪️🔘⚪️🔘⚪️⚪️⚪️🔘🔘🔘
	N.1352TinySeed          ⚪️🔘⚪️🔘⚪️🔘⚪️⚪️🔘⚪️⚪️⚪️
	N.1353TinySeed          ⚪️🔘⚪️🔘⚪️🔘⚪️⚪️🔘⚪️⚪️🔘
	N.1354TinySeed          ⚪️🔘⚪️🔘⚪️🔘⚪️⚪️🔘⚪️🔘⚪️
	N.1355TinySeed          ⚪️🔘⚪️🔘⚪️🔘⚪️⚪️🔘⚪️🔘🔘
	N.1356TinySeed          ⚪️🔘⚪️🔘⚪️🔘⚪️⚪️🔘🔘⚪️⚪️
	N.1357TinySeed          ⚪️🔘⚪️🔘⚪️🔘⚪️⚪️🔘🔘⚪️🔘
	N.1358TinySeed          ⚪️🔘⚪️🔘⚪️🔘⚪️⚪️🔘🔘🔘⚪️
	N.1359TinySeed          ⚪️🔘⚪️🔘⚪️🔘⚪️⚪️🔘🔘🔘🔘
	N.1360TinySeed          ⚪️🔘⚪️🔘⚪️🔘⚪️🔘⚪️⚪️⚪️⚪️
	N.1361TinySeed          ⚪️🔘⚪️🔘⚪️🔘⚪️🔘⚪️⚪️⚪️🔘
	N.1362TinySeed          ⚪️🔘⚪️🔘⚪️🔘⚪️🔘⚪️⚪️🔘⚪️
	N.1363TinySeed          ⚪️🔘⚪️🔘⚪️🔘⚪️🔘⚪️⚪️🔘🔘
	N.1364TinySeed          ⚪️🔘⚪️🔘⚪️🔘⚪️🔘⚪️🔘⚪️⚪️
	N.1365TinySeed          ⚪️🔘⚪️🔘⚪️🔘⚪️🔘⚪️🔘⚪️🔘
	N.1366TinySeed          ⚪️🔘⚪️🔘⚪️🔘⚪️🔘⚪️🔘🔘⚪️
	N.1367TinySeed          ⚪️🔘⚪️🔘⚪️🔘⚪️🔘⚪️🔘🔘🔘
	N.1368TinySeed          ⚪️🔘⚪️🔘⚪️🔘⚪️🔘🔘⚪️⚪️⚪️
	N.1369TinySeed          ⚪️🔘⚪️🔘⚪️🔘⚪️🔘🔘⚪️⚪️🔘
	N.1370TinySeed          ⚪️🔘⚪️🔘⚪️🔘⚪️🔘🔘⚪️🔘⚪️
	N.1371TinySeed          ⚪️🔘⚪️🔘⚪️🔘⚪️🔘🔘⚪️🔘🔘
	N.1372TinySeed          ⚪️🔘⚪️🔘⚪️🔘⚪️🔘🔘🔘⚪️⚪️
	N.1373TinySeed          ⚪️🔘⚪️🔘⚪️🔘⚪️🔘🔘🔘⚪️🔘
	N.1374TinySeed          ⚪️🔘⚪️🔘⚪️🔘⚪️🔘🔘🔘🔘⚪️
	N.1375TinySeed          ⚪️🔘⚪️🔘⚪️🔘⚪️🔘🔘🔘🔘🔘
	N.1376TinySeed          ⚪️🔘⚪️🔘⚪️🔘🔘⚪️⚪️⚪️⚪️⚪️
	N.1377TinySeed          ⚪️🔘⚪️🔘⚪️🔘🔘⚪️⚪️⚪️⚪️🔘
	N.1378TinySeed          ⚪️🔘⚪️🔘⚪️🔘🔘⚪️⚪️⚪️🔘⚪️
	N.1379TinySeed          ⚪️🔘⚪️🔘⚪️🔘🔘⚪️⚪️⚪️🔘🔘
	N.1380TinySeed          ⚪️🔘⚪️🔘⚪️🔘🔘⚪️⚪️🔘⚪️⚪️
	N.1381TinySeed          ⚪️🔘⚪️🔘⚪️🔘🔘⚪️⚪️🔘⚪️🔘
	N.1382TinySeed          ⚪️🔘⚪️🔘⚪️🔘🔘⚪️⚪️🔘🔘⚪️
	N.1383TinySeed          ⚪️🔘⚪️🔘⚪️🔘🔘⚪️⚪️🔘🔘🔘
	N.1384TinySeed          ⚪️🔘⚪️🔘⚪️🔘🔘⚪️🔘⚪️⚪️⚪️
	N.1385TinySeed          ⚪️🔘⚪️🔘⚪️🔘🔘⚪️🔘⚪️⚪️🔘
	N.1386TinySeed          ⚪️🔘⚪️🔘⚪️🔘🔘⚪️🔘⚪️🔘⚪️
	N.1387TinySeed          ⚪️🔘⚪️🔘⚪️🔘🔘⚪️🔘⚪️🔘🔘
	N.1388TinySeed          ⚪️🔘⚪️🔘⚪️🔘🔘⚪️🔘🔘⚪️⚪️
	N.1389TinySeed          ⚪️🔘⚪️🔘⚪️🔘🔘⚪️🔘🔘⚪️🔘
	N.1390TinySeed          ⚪️🔘⚪️🔘⚪️🔘🔘⚪️🔘🔘🔘⚪️
	N.1391TinySeed          ⚪️🔘⚪️🔘⚪️🔘🔘⚪️🔘🔘🔘🔘
	N.1392TinySeed          ⚪️🔘⚪️🔘⚪️🔘🔘🔘⚪️⚪️⚪️⚪️
	N.1393TinySeed          ⚪️🔘⚪️🔘⚪️🔘🔘🔘⚪️⚪️⚪️🔘
	N.1394TinySeed          ⚪️🔘⚪️🔘⚪️🔘🔘🔘⚪️⚪️🔘⚪️
	N.1395TinySeed          ⚪️🔘⚪️🔘⚪️🔘🔘🔘⚪️⚪️🔘🔘
	N.1396TinySeed          ⚪️🔘⚪️🔘⚪️🔘🔘🔘⚪️🔘⚪️⚪️
	N.1397TinySeed          ⚪️🔘⚪️🔘⚪️🔘🔘🔘⚪️🔘⚪️🔘
	N.1398TinySeed          ⚪️🔘⚪️🔘⚪️🔘🔘🔘⚪️🔘🔘⚪️
	N.1399TinySeed          ⚪️🔘⚪️🔘⚪️🔘🔘🔘⚪️🔘🔘🔘
	N.1400TinySeed          ⚪️🔘⚪️🔘⚪️🔘🔘🔘🔘⚪️⚪️⚪️
	N.1401TinySeed          ⚪️🔘⚪️🔘⚪️🔘🔘🔘🔘⚪️⚪️🔘
	N.1402TinySeed          ⚪️🔘⚪️🔘⚪️🔘🔘🔘🔘⚪️🔘⚪️
	N.1403TinySeed          ⚪️🔘⚪️🔘⚪️🔘🔘🔘🔘⚪️🔘🔘
	N.1404TinySeed          ⚪️🔘⚪️🔘⚪️🔘🔘🔘🔘🔘⚪️⚪️
	N.1405TinySeed          ⚪️🔘⚪️🔘⚪️🔘🔘🔘🔘🔘⚪️🔘
	N.1406TinySeed          ⚪️🔘⚪️🔘⚪️🔘🔘🔘🔘🔘🔘⚪️
	N.1407TinySeed          ⚪️🔘⚪️🔘⚪️🔘🔘🔘🔘🔘🔘🔘
	N.1408TinySeed          ⚪️🔘⚪️🔘🔘⚪️⚪️⚪️⚪️⚪️⚪️⚪️
	N.1409TinySeed          ⚪️🔘⚪️🔘🔘⚪️⚪️⚪️⚪️⚪️⚪️🔘
	N.1410TinySeed          ⚪️🔘⚪️🔘🔘⚪️⚪️⚪️⚪️⚪️🔘⚪️
	N.1411TinySeed          ⚪️🔘⚪️🔘🔘⚪️⚪️⚪️⚪️⚪️🔘🔘
	N.1412TinySeed          ⚪️🔘⚪️🔘🔘⚪️⚪️⚪️⚪️🔘⚪️⚪️
	N.1413TinySeed          ⚪️🔘⚪️🔘🔘⚪️⚪️⚪️⚪️🔘⚪️🔘
	N.1414TinySeed          ⚪️🔘⚪️🔘🔘⚪️⚪️⚪️⚪️🔘🔘⚪️
	N.1415TinySeed          ⚪️🔘⚪️🔘🔘⚪️⚪️⚪️⚪️🔘🔘🔘
	N.1416TinySeed          ⚪️🔘⚪️🔘🔘⚪️⚪️⚪️🔘⚪️⚪️⚪️
	N.1417TinySeed          ⚪️🔘⚪️🔘🔘⚪️⚪️⚪️🔘⚪️⚪️🔘
	N.1418TinySeed          ⚪️🔘⚪️🔘🔘⚪️⚪️⚪️🔘⚪️🔘⚪️
	N.1419TinySeed          ⚪️🔘⚪️🔘🔘⚪️⚪️⚪️🔘⚪️🔘🔘
	N.1420TinySeed          ⚪️🔘⚪️🔘🔘⚪️⚪️⚪️🔘🔘⚪️⚪️
	N.1421TinySeed          ⚪️🔘⚪️🔘🔘⚪️⚪️⚪️🔘🔘⚪️🔘
	N.1422TinySeed          ⚪️🔘⚪️🔘🔘⚪️⚪️⚪️🔘🔘🔘⚪️
	N.1423TinySeed          ⚪️🔘⚪️🔘🔘⚪️⚪️⚪️🔘🔘🔘🔘
	N.1424TinySeed          ⚪️🔘⚪️🔘🔘⚪️⚪️🔘⚪️⚪️⚪️⚪️
	N.1425TinySeed          ⚪️🔘⚪️🔘🔘⚪️⚪️🔘⚪️⚪️⚪️🔘
	N.1426TinySeed          ⚪️🔘⚪️🔘🔘⚪️⚪️🔘⚪️⚪️🔘⚪️
	N.1427TinySeed          ⚪️🔘⚪️🔘🔘⚪️⚪️🔘⚪️⚪️🔘🔘
	N.1428TinySeed          ⚪️🔘⚪️🔘🔘⚪️⚪️🔘⚪️🔘⚪️⚪️
	N.1429TinySeed          ⚪️🔘⚪️🔘🔘⚪️⚪️🔘⚪️🔘⚪️🔘
	N.1430TinySeed          ⚪️🔘⚪️🔘🔘⚪️⚪️🔘⚪️🔘🔘⚪️
	N.1431TinySeed          ⚪️🔘⚪️🔘🔘⚪️⚪️🔘⚪️🔘🔘🔘
	N.1432TinySeed          ⚪️🔘⚪️🔘🔘⚪️⚪️🔘🔘⚪️⚪️⚪️
	N.1433TinySeed          ⚪️🔘⚪️🔘🔘⚪️⚪️🔘🔘⚪️⚪️🔘
	N.1434TinySeed          ⚪️🔘⚪️🔘🔘⚪️⚪️🔘🔘⚪️🔘⚪️
	N.1435TinySeed          ⚪️🔘⚪️🔘🔘⚪️⚪️🔘🔘⚪️🔘🔘
	N.1436TinySeed          ⚪️🔘⚪️🔘🔘⚪️⚪️🔘🔘🔘⚪️⚪️
	N.1437TinySeed          ⚪️🔘⚪️🔘🔘⚪️⚪️🔘🔘🔘⚪️🔘
	N.1438TinySeed          ⚪️🔘⚪️🔘🔘⚪️⚪️🔘🔘🔘🔘⚪️
	N.1439TinySeed          ⚪️🔘⚪️🔘🔘⚪️⚪️🔘🔘🔘🔘🔘
	N.1440TinySeed          ⚪️🔘⚪️🔘🔘⚪️🔘⚪️⚪️⚪️⚪️⚪️
	N.1441TinySeed          ⚪️🔘⚪️🔘🔘⚪️🔘⚪️⚪️⚪️⚪️🔘
	N.1442TinySeed          ⚪️🔘⚪️🔘🔘⚪️🔘⚪️⚪️⚪️🔘⚪️
	N.1443TinySeed          ⚪️🔘⚪️🔘🔘⚪️🔘⚪️⚪️⚪️🔘🔘
	N.1444TinySeed          ⚪️🔘⚪️🔘🔘⚪️🔘⚪️⚪️🔘⚪️⚪️
	N.1445TinySeed          ⚪️🔘⚪️🔘🔘⚪️🔘⚪️⚪️🔘⚪️🔘
	N.1446TinySeed          ⚪️🔘⚪️🔘🔘⚪️🔘⚪️⚪️🔘🔘⚪️
	N.1447TinySeed          ⚪️🔘⚪️🔘🔘⚪️🔘⚪️⚪️🔘🔘🔘
	N.1448TinySeed          ⚪️🔘⚪️🔘🔘⚪️🔘⚪️🔘⚪️⚪️⚪️
	N.1449TinySeed          ⚪️🔘⚪️🔘🔘⚪️🔘⚪️🔘⚪️⚪️🔘
	N.1450TinySeed          ⚪️🔘⚪️🔘🔘⚪️🔘⚪️🔘⚪️🔘⚪️
	N.1451TinySeed          ⚪️🔘⚪️🔘🔘⚪️🔘⚪️🔘⚪️🔘🔘
	N.1452TinySeed          ⚪️🔘⚪️🔘🔘⚪️🔘⚪️🔘🔘⚪️⚪️
	N.1453TinySeed          ⚪️🔘⚪️🔘🔘⚪️🔘⚪️🔘🔘⚪️🔘
	N.1454TinySeed          ⚪️🔘⚪️🔘🔘⚪️🔘⚪️🔘🔘🔘⚪️
	N.1455TinySeed          ⚪️🔘⚪️🔘🔘⚪️🔘⚪️🔘🔘🔘🔘
	N.1456TinySeed          ⚪️🔘⚪️🔘🔘⚪️🔘🔘⚪️⚪️⚪️⚪️
	N.1457TinySeed          ⚪️🔘⚪️🔘🔘⚪️🔘🔘⚪️⚪️⚪️🔘
	N.1458TinySeed          ⚪️🔘⚪️🔘🔘⚪️🔘🔘⚪️⚪️🔘⚪️
	N.1459TinySeed          ⚪️🔘⚪️🔘🔘⚪️🔘🔘⚪️⚪️🔘🔘
	N.1460TinySeed          ⚪️🔘⚪️🔘🔘⚪️🔘🔘⚪️🔘⚪️⚪️
	N.1461TinySeed          ⚪️🔘⚪️🔘🔘⚪️🔘🔘⚪️🔘⚪️🔘
	N.1462TinySeed          ⚪️🔘⚪️🔘🔘⚪️🔘🔘⚪️🔘🔘⚪️
	N.1463TinySeed          ⚪️🔘⚪️🔘🔘⚪️🔘🔘⚪️🔘🔘🔘
	N.1464TinySeed          ⚪️🔘⚪️🔘🔘⚪️🔘🔘🔘⚪️⚪️⚪️
	N.1465TinySeed          ⚪️🔘⚪️🔘🔘⚪️🔘🔘🔘⚪️⚪️🔘
	N.1466TinySeed          ⚪️🔘⚪️🔘🔘⚪️🔘🔘🔘⚪️🔘⚪️
	N.1467TinySeed          ⚪️🔘⚪️🔘🔘⚪️🔘🔘🔘⚪️🔘🔘
	N.1468TinySeed          ⚪️🔘⚪️🔘🔘⚪️🔘🔘🔘🔘⚪️⚪️
	N.1469TinySeed          ⚪️🔘⚪️🔘🔘⚪️🔘🔘🔘🔘⚪️🔘
	N.1470TinySeed          ⚪️🔘⚪️🔘🔘⚪️🔘🔘🔘🔘🔘⚪️
	N.1471TinySeed          ⚪️🔘⚪️🔘🔘⚪️🔘🔘🔘🔘🔘🔘
	N.1472TinySeed          ⚪️🔘⚪️🔘🔘🔘⚪️⚪️⚪️⚪️⚪️⚪️
	N.1473TinySeed          ⚪️🔘⚪️🔘🔘🔘⚪️⚪️⚪️⚪️⚪️🔘
	N.1474TinySeed          ⚪️🔘⚪️🔘🔘🔘⚪️⚪️⚪️⚪️🔘⚪️
	N.1475TinySeed          ⚪️🔘⚪️🔘🔘🔘⚪️⚪️⚪️⚪️🔘🔘
	N.1476TinySeed          ⚪️🔘⚪️🔘🔘🔘⚪️⚪️⚪️🔘⚪️⚪️
	N.1477TinySeed          ⚪️🔘⚪️🔘🔘🔘⚪️⚪️⚪️🔘⚪️🔘
	N.1478TinySeed          ⚪️🔘⚪️🔘🔘🔘⚪️⚪️⚪️🔘🔘⚪️
	N.1479TinySeed          ⚪️🔘⚪️🔘🔘🔘⚪️⚪️⚪️🔘🔘🔘
	N.1480TinySeed          ⚪️🔘⚪️🔘🔘🔘⚪️⚪️🔘⚪️⚪️⚪️
	N.1481TinySeed          ⚪️🔘⚪️🔘🔘🔘⚪️⚪️🔘⚪️⚪️🔘
	N.1482TinySeed          ⚪️🔘⚪️🔘🔘🔘⚪️⚪️🔘⚪️🔘⚪️
	N.1483TinySeed          ⚪️🔘⚪️🔘🔘🔘⚪️⚪️🔘⚪️🔘🔘
	N.1484TinySeed          ⚪️🔘⚪️🔘🔘🔘⚪️⚪️🔘🔘⚪️⚪️
	N.1485TinySeed          ⚪️🔘⚪️🔘🔘🔘⚪️⚪️🔘🔘⚪️🔘
	N.1486TinySeed          ⚪️🔘⚪️🔘🔘🔘⚪️⚪️🔘🔘🔘⚪️
	N.1487TinySeed          ⚪️🔘⚪️🔘🔘🔘⚪️⚪️🔘🔘🔘🔘
	N.1488TinySeed          ⚪️🔘⚪️🔘🔘🔘⚪️🔘⚪️⚪️⚪️⚪️
	N.1489TinySeed          ⚪️🔘⚪️🔘🔘🔘⚪️🔘⚪️⚪️⚪️🔘
	N.1490TinySeed          ⚪️🔘⚪️🔘🔘🔘⚪️🔘⚪️⚪️🔘⚪️
	N.1491TinySeed          ⚪️🔘⚪️🔘🔘🔘⚪️🔘⚪️⚪️🔘🔘
	N.1492TinySeed          ⚪️🔘⚪️🔘🔘🔘⚪️🔘⚪️🔘⚪️⚪️
	N.1493TinySeed          ⚪️🔘⚪️🔘🔘🔘⚪️🔘⚪️🔘⚪️🔘
	N.1494TinySeed          ⚪️🔘⚪️🔘🔘🔘⚪️🔘⚪️🔘🔘⚪️
	N.1495TinySeed          ⚪️🔘⚪️🔘🔘🔘⚪️🔘⚪️🔘🔘🔘
	N.1496TinySeed          ⚪️🔘⚪️🔘🔘🔘⚪️🔘🔘⚪️⚪️⚪️
	N.1497TinySeed          ⚪️🔘⚪️🔘🔘🔘⚪️🔘🔘⚪️⚪️🔘
	N.1498TinySeed          ⚪️🔘⚪️🔘🔘🔘⚪️🔘🔘⚪️🔘⚪️
	N.1499TinySeed          ⚪️🔘⚪️🔘🔘🔘⚪️🔘🔘⚪️🔘🔘
	N.1500TinySeed          ⚪️🔘⚪️🔘🔘🔘⚪️🔘🔘🔘⚪️⚪️
	N.1501TinySeed          ⚪️🔘⚪️🔘🔘🔘⚪️🔘🔘🔘⚪️🔘
	N.1502TinySeed          ⚪️🔘⚪️🔘🔘🔘⚪️🔘🔘🔘🔘⚪️
	N.1503TinySeed          ⚪️🔘⚪️🔘🔘🔘⚪️🔘🔘🔘🔘🔘
	N.1504TinySeed          ⚪️🔘⚪️🔘🔘🔘🔘⚪️⚪️⚪️⚪️⚪️
	N.1505TinySeed          ⚪️🔘⚪️🔘🔘🔘🔘⚪️⚪️⚪️⚪️🔘
	N.1506TinySeed          ⚪️🔘⚪️🔘🔘🔘🔘⚪️⚪️⚪️🔘⚪️
	N.1507TinySeed          ⚪️🔘⚪️🔘🔘🔘🔘⚪️⚪️⚪️🔘🔘
	N.1508TinySeed          ⚪️🔘⚪️🔘🔘🔘🔘⚪️⚪️🔘⚪️⚪️
	N.1509TinySeed          ⚪️🔘⚪️🔘🔘🔘🔘⚪️⚪️🔘⚪️🔘
	N.1510TinySeed          ⚪️🔘⚪️🔘🔘🔘🔘⚪️⚪️🔘🔘⚪️
	N.1511TinySeed          ⚪️🔘⚪️🔘🔘🔘🔘⚪️⚪️🔘🔘🔘
	N.1512TinySeed          ⚪️🔘⚪️🔘🔘🔘🔘⚪️🔘⚪️⚪️⚪️
	N.1513TinySeed          ⚪️🔘⚪️🔘🔘🔘🔘⚪️🔘⚪️⚪️🔘
	N.1514TinySeed          ⚪️🔘⚪️🔘🔘🔘🔘⚪️🔘⚪️🔘⚪️
	N.1515TinySeed          ⚪️🔘⚪️🔘🔘🔘🔘⚪️🔘⚪️🔘🔘
	N.1516TinySeed          ⚪️🔘⚪️🔘🔘🔘🔘⚪️🔘🔘⚪️⚪️
	N.1517TinySeed          ⚪️🔘⚪️🔘🔘🔘🔘⚪️🔘🔘⚪️🔘
	N.1518TinySeed          ⚪️🔘⚪️🔘🔘🔘🔘⚪️🔘🔘🔘⚪️
	N.1519TinySeed          ⚪️🔘⚪️🔘🔘🔘🔘⚪️🔘🔘🔘🔘
	N.1520TinySeed          ⚪️🔘⚪️🔘🔘🔘🔘🔘⚪️⚪️⚪️⚪️
	N.1521TinySeed          ⚪️🔘⚪️🔘🔘🔘🔘🔘⚪️⚪️⚪️🔘
	N.1522TinySeed          ⚪️🔘⚪️🔘🔘🔘🔘🔘⚪️⚪️🔘⚪️
	N.1523TinySeed          ⚪️🔘⚪️🔘🔘🔘🔘🔘⚪️⚪️🔘🔘
	N.1524TinySeed          ⚪️🔘⚪️🔘🔘🔘🔘🔘⚪️🔘⚪️⚪️
	N.1525TinySeed          ⚪️🔘⚪️🔘🔘🔘🔘🔘⚪️🔘⚪️🔘
	N.1526TinySeed          ⚪️🔘⚪️🔘🔘🔘🔘🔘⚪️🔘🔘⚪️
	N.1527TinySeed          ⚪️🔘⚪️🔘🔘🔘🔘🔘⚪️🔘🔘🔘
	N.1528TinySeed          ⚪️🔘⚪️🔘🔘🔘🔘🔘🔘⚪️⚪️⚪️
	N.1529TinySeed          ⚪️🔘⚪️🔘🔘🔘🔘🔘🔘⚪️⚪️🔘
	N.1530TinySeed          ⚪️🔘⚪️🔘🔘🔘🔘🔘🔘⚪️🔘⚪️
	N.1531TinySeed          ⚪️🔘⚪️🔘🔘🔘🔘🔘🔘⚪️🔘🔘
	N.1532TinySeed          ⚪️🔘⚪️🔘🔘🔘🔘🔘🔘🔘⚪️⚪️
	N.1533TinySeed          ⚪️🔘⚪️🔘🔘🔘🔘🔘🔘🔘⚪️🔘
	N.1534TinySeed          ⚪️🔘⚪️🔘🔘🔘🔘🔘🔘🔘🔘⚪️
	N.1535TinySeed          ⚪️🔘⚪️🔘🔘🔘🔘🔘🔘🔘🔘🔘
	N.1536TinySeed          ⚪️🔘🔘⚪️⚪️⚪️⚪️⚪️⚪️⚪️⚪️⚪️
	N.1537TinySeed          ⚪️🔘🔘⚪️⚪️⚪️⚪️⚪️⚪️⚪️⚪️🔘
	N.1538TinySeed          ⚪️🔘🔘⚪️⚪️⚪️⚪️⚪️⚪️⚪️🔘⚪️
	N.1539TinySeed          ⚪️🔘🔘⚪️⚪️⚪️⚪️⚪️⚪️⚪️🔘🔘
	N.1540TinySeed          ⚪️🔘🔘⚪️⚪️⚪️⚪️⚪️⚪️🔘⚪️⚪️
	N.1541TinySeed          ⚪️🔘🔘⚪️⚪️⚪️⚪️⚪️⚪️🔘⚪️🔘
	N.1542TinySeed          ⚪️🔘🔘⚪️⚪️⚪️⚪️⚪️⚪️🔘🔘⚪️
	N.1543TinySeed          ⚪️🔘🔘⚪️⚪️⚪️⚪️⚪️⚪️🔘🔘🔘
	N.1544TinySeed          ⚪️🔘🔘⚪️⚪️⚪️⚪️⚪️🔘⚪️⚪️⚪️
	N.1545TinySeed          ⚪️🔘🔘⚪️⚪️⚪️⚪️⚪️🔘⚪️⚪️🔘
	N.1546TinySeed          ⚪️🔘🔘⚪️⚪️⚪️⚪️⚪️🔘⚪️🔘⚪️
	N.1547TinySeed          ⚪️🔘🔘⚪️⚪️⚪️⚪️⚪️🔘⚪️🔘🔘
	N.1548TinySeed          ⚪️🔘🔘⚪️⚪️⚪️⚪️⚪️🔘🔘⚪️⚪️
	N.1549TinySeed          ⚪️🔘🔘⚪️⚪️⚪️⚪️⚪️🔘🔘⚪️🔘
	N.1550TinySeed          ⚪️🔘🔘⚪️⚪️⚪️⚪️⚪️🔘🔘🔘⚪️
	N.1551TinySeed          ⚪️🔘🔘⚪️⚪️⚪️⚪️⚪️🔘🔘🔘🔘
	N.1552TinySeed          ⚪️🔘🔘⚪️⚪️⚪️⚪️🔘⚪️⚪️⚪️⚪️
	N.1553TinySeed          ⚪️🔘🔘⚪️⚪️⚪️⚪️🔘⚪️⚪️⚪️🔘
	N.1554TinySeed          ⚪️🔘🔘⚪️⚪️⚪️⚪️🔘⚪️⚪️🔘⚪️
	N.1555TinySeed          ⚪️🔘🔘⚪️⚪️⚪️⚪️🔘⚪️⚪️🔘🔘
	N.1556TinySeed          ⚪️🔘🔘⚪️⚪️⚪️⚪️🔘⚪️🔘⚪️⚪️
	N.1557TinySeed          ⚪️🔘🔘⚪️⚪️⚪️⚪️🔘⚪️🔘⚪️🔘
	N.1558TinySeed          ⚪️🔘🔘⚪️⚪️⚪️⚪️🔘⚪️🔘🔘⚪️
	N.1559TinySeed          ⚪️🔘🔘⚪️⚪️⚪️⚪️🔘⚪️🔘🔘🔘
	N.1560TinySeed          ⚪️🔘🔘⚪️⚪️⚪️⚪️🔘🔘⚪️⚪️⚪️
	N.1561TinySeed          ⚪️🔘🔘⚪️⚪️⚪️⚪️🔘🔘⚪️⚪️🔘
	N.1562TinySeed          ⚪️🔘🔘⚪️⚪️⚪️⚪️🔘🔘⚪️🔘⚪️
	N.1563TinySeed          ⚪️🔘🔘⚪️⚪️⚪️⚪️🔘🔘⚪️🔘🔘
	N.1564TinySeed          ⚪️🔘🔘⚪️⚪️⚪️⚪️🔘🔘🔘⚪️⚪️
	N.1565TinySeed          ⚪️🔘🔘⚪️⚪️⚪️⚪️🔘🔘🔘⚪️🔘
	N.1566TinySeed          ⚪️🔘🔘⚪️⚪️⚪️⚪️🔘🔘🔘🔘⚪️
	N.1567TinySeed          ⚪️🔘🔘⚪️⚪️⚪️⚪️🔘🔘🔘🔘🔘
	N.1568TinySeed          ⚪️🔘🔘⚪️⚪️⚪️🔘⚪️⚪️⚪️⚪️⚪️
	N.1569TinySeed          ⚪️🔘🔘⚪️⚪️⚪️🔘⚪️⚪️⚪️⚪️🔘
	N.1570TinySeed          ⚪️🔘🔘⚪️⚪️⚪️🔘⚪️⚪️⚪️🔘⚪️
	N.1571TinySeed          ⚪️🔘🔘⚪️⚪️⚪️🔘⚪️⚪️⚪️🔘🔘
	N.1572TinySeed          ⚪️🔘🔘⚪️⚪️⚪️🔘⚪️⚪️🔘⚪️⚪️
	N.1573TinySeed          ⚪️🔘🔘⚪️⚪️⚪️🔘⚪️⚪️🔘⚪️🔘
	N.1574TinySeed          ⚪️🔘🔘⚪️⚪️⚪️🔘⚪️⚪️🔘🔘⚪️
	N.1575TinySeed          ⚪️🔘🔘⚪️⚪️⚪️🔘⚪️⚪️🔘🔘🔘
	N.1576TinySeed          ⚪️🔘🔘⚪️⚪️⚪️🔘⚪️🔘⚪️⚪️⚪️
	N.1577TinySeed          ⚪️🔘🔘⚪️⚪️⚪️🔘⚪️🔘⚪️⚪️🔘
	N.1578TinySeed          ⚪️🔘🔘⚪️⚪️⚪️🔘⚪️🔘⚪️🔘⚪️
	N.1579TinySeed          ⚪️🔘🔘⚪️⚪️⚪️🔘⚪️🔘⚪️🔘🔘
	N.1580TinySeed          ⚪️🔘🔘⚪️⚪️⚪️🔘⚪️🔘🔘⚪️⚪️
	N.1581TinySeed          ⚪️🔘🔘⚪️⚪️⚪️🔘⚪️🔘🔘⚪️🔘
	N.1582TinySeed          ⚪️🔘🔘⚪️⚪️⚪️🔘⚪️🔘🔘🔘⚪️
	N.1583TinySeed          ⚪️🔘🔘⚪️⚪️⚪️🔘⚪️🔘🔘🔘🔘
	N.1584TinySeed          ⚪️🔘🔘⚪️⚪️⚪️🔘🔘⚪️⚪️⚪️⚪️
	N.1585TinySeed          ⚪️🔘🔘⚪️⚪️⚪️🔘🔘⚪️⚪️⚪️🔘
	N.1586TinySeed          ⚪️🔘🔘⚪️⚪️⚪️🔘🔘⚪️⚪️🔘⚪️
	N.1587TinySeed          ⚪️🔘🔘⚪️⚪️⚪️🔘🔘⚪️⚪️🔘🔘
	N.1588TinySeed          ⚪️🔘🔘⚪️⚪️⚪️🔘🔘⚪️🔘⚪️⚪️
	N.1589TinySeed          ⚪️🔘🔘⚪️⚪️⚪️🔘🔘⚪️🔘⚪️🔘
	N.1590TinySeed          ⚪️🔘🔘⚪️⚪️⚪️🔘🔘⚪️🔘🔘⚪️
	N.1591TinySeed          ⚪️🔘🔘⚪️⚪️⚪️🔘🔘⚪️🔘🔘🔘
	N.1592TinySeed          ⚪️🔘🔘⚪️⚪️⚪️🔘🔘🔘⚪️⚪️⚪️
	N.1593TinySeed          ⚪️🔘🔘⚪️⚪️⚪️🔘🔘🔘⚪️⚪️🔘
	N.1594TinySeed          ⚪️🔘🔘⚪️⚪️⚪️🔘🔘🔘⚪️🔘⚪️
	N.1595TinySeed          ⚪️🔘🔘⚪️⚪️⚪️🔘🔘🔘⚪️🔘🔘
	N.1596TinySeed          ⚪️🔘🔘⚪️⚪️⚪️🔘🔘🔘🔘⚪️⚪️
	N.1597TinySeed          ⚪️🔘🔘⚪️⚪️⚪️🔘🔘🔘🔘⚪️🔘
	N.1598TinySeed          ⚪️🔘🔘⚪️⚪️⚪️🔘🔘🔘🔘🔘⚪️
	N.1599TinySeed          ⚪️🔘🔘⚪️⚪️⚪️🔘🔘🔘🔘🔘🔘
	N.1600TinySeed          ⚪️🔘🔘⚪️⚪️🔘⚪️⚪️⚪️⚪️⚪️⚪️
	N.1601TinySeed          ⚪️🔘🔘⚪️⚪️🔘⚪️⚪️⚪️⚪️⚪️🔘
	N.1602TinySeed          ⚪️🔘🔘⚪️⚪️🔘⚪️⚪️⚪️⚪️🔘⚪️
	N.1603TinySeed          ⚪️🔘🔘⚪️⚪️🔘⚪️⚪️⚪️⚪️🔘🔘
	N.1604TinySeed          ⚪️🔘🔘⚪️⚪️🔘⚪️⚪️⚪️🔘⚪️⚪️
	N.1605TinySeed          ⚪️🔘🔘⚪️⚪️🔘⚪️⚪️⚪️🔘⚪️🔘
	N.1606TinySeed          ⚪️🔘🔘⚪️⚪️🔘⚪️⚪️⚪️🔘🔘⚪️
	N.1607TinySeed          ⚪️🔘🔘⚪️⚪️🔘⚪️⚪️⚪️🔘🔘🔘
	N.1608TinySeed          ⚪️🔘🔘⚪️⚪️🔘⚪️⚪️🔘⚪️⚪️⚪️
	N.1609TinySeed          ⚪️🔘🔘⚪️⚪️🔘⚪️⚪️🔘⚪️⚪️🔘
	N.1610TinySeed          ⚪️🔘🔘⚪️⚪️🔘⚪️⚪️🔘⚪️🔘⚪️
	N.1611TinySeed          ⚪️🔘🔘⚪️⚪️🔘⚪️⚪️🔘⚪️🔘🔘
	N.1612TinySeed          ⚪️🔘🔘⚪️⚪️🔘⚪️⚪️🔘🔘⚪️⚪️
	N.1613TinySeed          ⚪️🔘🔘⚪️⚪️🔘⚪️⚪️🔘🔘⚪️🔘
	N.1614TinySeed          ⚪️🔘🔘⚪️⚪️🔘⚪️⚪️🔘🔘🔘⚪️
	N.1615TinySeed          ⚪️🔘🔘⚪️⚪️🔘⚪️⚪️🔘🔘🔘🔘
	N.1616TinySeed          ⚪️🔘🔘⚪️⚪️🔘⚪️🔘⚪️⚪️⚪️⚪️
	N.1617TinySeed          ⚪️🔘🔘⚪️⚪️🔘⚪️🔘⚪️⚪️⚪️🔘
	N.1618TinySeed          ⚪️🔘🔘⚪️⚪️🔘⚪️🔘⚪️⚪️🔘⚪️
	N.1619TinySeed          ⚪️🔘🔘⚪️⚪️🔘⚪️🔘⚪️⚪️🔘🔘
	N.1620TinySeed          ⚪️🔘🔘⚪️⚪️🔘⚪️🔘⚪️🔘⚪️⚪️
	N.1621TinySeed          ⚪️🔘🔘⚪️⚪️🔘⚪️🔘⚪️🔘⚪️🔘
	N.1622TinySeed          ⚪️🔘🔘⚪️⚪️🔘⚪️🔘⚪️🔘🔘⚪️
	N.1623TinySeed          ⚪️🔘🔘⚪️⚪️🔘⚪️🔘⚪️🔘🔘🔘
	N.1624TinySeed          ⚪️🔘🔘⚪️⚪️🔘⚪️🔘🔘⚪️⚪️⚪️
	N.1625TinySeed          ⚪️🔘🔘⚪️⚪️🔘⚪️🔘🔘⚪️⚪️🔘
	N.1626TinySeed          ⚪️🔘🔘⚪️⚪️🔘⚪️🔘🔘⚪️🔘⚪️
	N.1627TinySeed          ⚪️🔘🔘⚪️⚪️🔘⚪️🔘🔘⚪️🔘🔘
	N.1628TinySeed          ⚪️🔘🔘⚪️⚪️🔘⚪️🔘🔘🔘⚪️⚪️
	N.1629TinySeed          ⚪️🔘🔘⚪️⚪️🔘⚪️🔘🔘🔘⚪️🔘
	N.1630TinySeed          ⚪️🔘🔘⚪️⚪️🔘⚪️🔘🔘🔘🔘⚪️
	N.1631TinySeed          ⚪️🔘🔘⚪️⚪️🔘⚪️🔘🔘🔘🔘🔘
	N.1632TinySeed          ⚪️🔘🔘⚪️⚪️🔘🔘⚪️⚪️⚪️⚪️⚪️
	N.1633TinySeed          ⚪️🔘🔘⚪️⚪️🔘🔘⚪️⚪️⚪️⚪️🔘
	N.1634TinySeed          ⚪️🔘🔘⚪️⚪️🔘🔘⚪️⚪️⚪️🔘⚪️
	N.1635TinySeed          ⚪️🔘🔘⚪️⚪️🔘🔘⚪️⚪️⚪️🔘🔘
	N.1636TinySeed          ⚪️🔘🔘⚪️⚪️🔘🔘⚪️⚪️🔘⚪️⚪️
	N.1637TinySeed          ⚪️🔘🔘⚪️⚪️🔘🔘⚪️⚪️🔘⚪️🔘
	N.1638TinySeed          ⚪️🔘🔘⚪️⚪️🔘🔘⚪️⚪️🔘🔘⚪️
	N.1639TinySeed          ⚪️🔘🔘⚪️⚪️🔘🔘⚪️⚪️🔘🔘🔘
	N.1640TinySeed          ⚪️🔘🔘⚪️⚪️🔘🔘⚪️🔘⚪️⚪️⚪️
	N.1641TinySeed          ⚪️🔘🔘⚪️⚪️🔘🔘⚪️🔘⚪️⚪️🔘
	N.1642TinySeed          ⚪️🔘🔘⚪️⚪️🔘🔘⚪️🔘⚪️🔘⚪️
	N.1643TinySeed          ⚪️🔘🔘⚪️⚪️🔘🔘⚪️🔘⚪️🔘🔘
	N.1644TinySeed          ⚪️🔘🔘⚪️⚪️🔘🔘⚪️🔘🔘⚪️⚪️
	N.1645TinySeed          ⚪️🔘🔘⚪️⚪️🔘🔘⚪️🔘🔘⚪️🔘
	N.1646TinySeed          ⚪️🔘🔘⚪️⚪️🔘🔘⚪️🔘🔘🔘⚪️
	N.1647TinySeed          ⚪️🔘🔘⚪️⚪️🔘🔘⚪️🔘🔘🔘🔘
	N.1648TinySeed          ⚪️🔘🔘⚪️⚪️🔘🔘🔘⚪️⚪️⚪️⚪️
	N.1649TinySeed          ⚪️🔘🔘⚪️⚪️🔘🔘🔘⚪️⚪️⚪️🔘
	N.1650TinySeed          ⚪️🔘🔘⚪️⚪️🔘🔘🔘⚪️⚪️🔘⚪️
	N.1651TinySeed          ⚪️🔘🔘⚪️⚪️🔘🔘🔘⚪️⚪️🔘🔘
	N.1652TinySeed          ⚪️🔘🔘⚪️⚪️🔘🔘🔘⚪️🔘⚪️⚪️
	N.1653TinySeed          ⚪️🔘🔘⚪️⚪️🔘🔘🔘⚪️🔘⚪️🔘
	N.1654TinySeed          ⚪️🔘🔘⚪️⚪️🔘🔘🔘⚪️🔘🔘⚪️
	N.1655TinySeed          ⚪️🔘🔘⚪️⚪️🔘🔘🔘⚪️🔘🔘🔘
	N.1656TinySeed          ⚪️🔘🔘⚪️⚪️🔘🔘🔘🔘⚪️⚪️⚪️
	N.1657TinySeed          ⚪️🔘🔘⚪️⚪️🔘🔘🔘🔘⚪️⚪️🔘
	N.1658TinySeed          ⚪️🔘🔘⚪️⚪️🔘🔘🔘🔘⚪️🔘⚪️
	N.1659TinySeed          ⚪️🔘🔘⚪️⚪️🔘🔘🔘🔘⚪️🔘🔘
	N.1660TinySeed          ⚪️🔘🔘⚪️⚪️🔘🔘🔘🔘🔘⚪️⚪️
	N.1661TinySeed          ⚪️🔘🔘⚪️⚪️🔘🔘🔘🔘🔘⚪️🔘
	N.1662TinySeed          ⚪️🔘🔘⚪️⚪️🔘🔘🔘🔘🔘🔘⚪️
	N.1663TinySeed          ⚪️🔘🔘⚪️⚪️🔘🔘🔘🔘🔘🔘🔘
	N.1664TinySeed          ⚪️🔘🔘⚪️🔘⚪️⚪️⚪️⚪️⚪️⚪️⚪️
	N.1665TinySeed          ⚪️🔘🔘⚪️🔘⚪️⚪️⚪️⚪️⚪️⚪️🔘
	N.1666TinySeed          ⚪️🔘🔘⚪️🔘⚪️⚪️⚪️⚪️⚪️🔘⚪️
	N.1667TinySeed          ⚪️🔘🔘⚪️🔘⚪️⚪️⚪️⚪️⚪️🔘🔘
	N.1668TinySeed          ⚪️🔘🔘⚪️🔘⚪️⚪️⚪️⚪️🔘⚪️⚪️
	N.1669TinySeed          ⚪️🔘🔘⚪️🔘⚪️⚪️⚪️⚪️🔘⚪️🔘
	N.1670TinySeed          ⚪️🔘🔘⚪️🔘⚪️⚪️⚪️⚪️🔘🔘⚪️
	N.1671TinySeed          ⚪️🔘🔘⚪️🔘⚪️⚪️⚪️⚪️🔘🔘🔘
	N.1672TinySeed          ⚪️🔘🔘⚪️🔘⚪️⚪️⚪️🔘⚪️⚪️⚪️
	N.1673TinySeed          ⚪️🔘🔘⚪️🔘⚪️⚪️⚪️🔘⚪️⚪️🔘
	N.1674TinySeed          ⚪️🔘🔘⚪️🔘⚪️⚪️⚪️🔘⚪️🔘⚪️
	N.1675TinySeed          ⚪️🔘🔘⚪️🔘⚪️⚪️⚪️🔘⚪️🔘🔘
	N.1676TinySeed          ⚪️🔘🔘⚪️🔘⚪️⚪️⚪️🔘🔘⚪️⚪️
	N.1677TinySeed          ⚪️🔘🔘⚪️🔘⚪️⚪️⚪️🔘🔘⚪️🔘
	N.1678TinySeed          ⚪️🔘🔘⚪️🔘⚪️⚪️⚪️🔘🔘🔘⚪️
	N.1679TinySeed          ⚪️🔘🔘⚪️🔘⚪️⚪️⚪️🔘🔘🔘🔘
	N.1680TinySeed          ⚪️🔘🔘⚪️🔘⚪️⚪️🔘⚪️⚪️⚪️⚪️
	N.1681TinySeed          ⚪️🔘🔘⚪️🔘⚪️⚪️🔘⚪️⚪️⚪️🔘
	N.1682TinySeed          ⚪️🔘🔘⚪️🔘⚪️⚪️🔘⚪️⚪️🔘⚪️
	N.1683TinySeed          ⚪️🔘🔘⚪️🔘⚪️⚪️🔘⚪️⚪️🔘🔘
	N.1684TinySeed          ⚪️🔘🔘⚪️🔘⚪️⚪️🔘⚪️🔘⚪️⚪️
	N.1685TinySeed          ⚪️🔘🔘⚪️🔘⚪️⚪️🔘⚪️🔘⚪️🔘
	N.1686TinySeed          ⚪️🔘🔘⚪️🔘⚪️⚪️🔘⚪️🔘🔘⚪️
	N.1687TinySeed          ⚪️🔘🔘⚪️🔘⚪️⚪️🔘⚪️🔘🔘🔘
	N.1688TinySeed          ⚪️🔘🔘⚪️🔘⚪️⚪️🔘🔘⚪️⚪️⚪️
	N.1689TinySeed          ⚪️🔘🔘⚪️🔘⚪️⚪️🔘🔘⚪️⚪️🔘
	N.1690TinySeed          ⚪️🔘🔘⚪️🔘⚪️⚪️🔘🔘⚪️🔘⚪️
	N.1691TinySeed          ⚪️🔘🔘⚪️🔘⚪️⚪️🔘🔘⚪️🔘🔘
	N.1692TinySeed          ⚪️🔘🔘⚪️🔘⚪️⚪️🔘🔘🔘⚪️⚪️
	N.1693TinySeed          ⚪️🔘🔘⚪️🔘⚪️⚪️🔘🔘🔘⚪️🔘
	N.1694TinySeed          ⚪️🔘🔘⚪️🔘⚪️⚪️🔘🔘🔘🔘⚪️
	N.1695TinySeed          ⚪️🔘🔘⚪️🔘⚪️⚪️🔘🔘🔘🔘🔘
	N.1696TinySeed          ⚪️🔘🔘⚪️🔘⚪️🔘⚪️⚪️⚪️⚪️⚪️
	N.1697TinySeed          ⚪️🔘🔘⚪️🔘⚪️🔘⚪️⚪️⚪️⚪️🔘
	N.1698TinySeed          ⚪️🔘🔘⚪️🔘⚪️🔘⚪️⚪️⚪️🔘⚪️
	N.1699TinySeed          ⚪️🔘🔘⚪️🔘⚪️🔘⚪️⚪️⚪️🔘🔘
	N.1700TinySeed          ⚪️🔘🔘⚪️🔘⚪️🔘⚪️⚪️🔘⚪️⚪️
	N.1701TinySeed          ⚪️🔘🔘⚪️🔘⚪️🔘⚪️⚪️🔘⚪️🔘
	N.1702TinySeed          ⚪️🔘🔘⚪️🔘⚪️🔘⚪️⚪️🔘🔘⚪️
	N.1703TinySeed          ⚪️🔘🔘⚪️🔘⚪️🔘⚪️⚪️🔘🔘🔘
	N.1704TinySeed          ⚪️🔘🔘⚪️🔘⚪️🔘⚪️🔘⚪️⚪️⚪️
	N.1705TinySeed          ⚪️🔘🔘⚪️🔘⚪️🔘⚪️🔘⚪️⚪️🔘
	N.1706TinySeed          ⚪️🔘🔘⚪️🔘⚪️🔘⚪️🔘⚪️🔘⚪️
	N.1707TinySeed          ⚪️🔘🔘⚪️🔘⚪️🔘⚪️🔘⚪️🔘🔘
	N.1708TinySeed          ⚪️🔘🔘⚪️🔘⚪️🔘⚪️🔘🔘⚪️⚪️
	N.1709TinySeed          ⚪️🔘🔘⚪️🔘⚪️🔘⚪️🔘🔘⚪️🔘
	N.1710TinySeed          ⚪️🔘🔘⚪️🔘⚪️🔘⚪️🔘🔘🔘⚪️
	N.1711TinySeed          ⚪️🔘🔘⚪️🔘⚪️🔘⚪️🔘🔘🔘🔘
	N.1712TinySeed          ⚪️🔘🔘⚪️🔘⚪️🔘🔘⚪️⚪️⚪️⚪️
	N.1713TinySeed          ⚪️🔘🔘⚪️🔘⚪️🔘🔘⚪️⚪️⚪️🔘
	N.1714TinySeed          ⚪️🔘🔘⚪️🔘⚪️🔘🔘⚪️⚪️🔘⚪️
	N.1715TinySeed          ⚪️🔘🔘⚪️🔘⚪️🔘🔘⚪️⚪️🔘🔘
	N.1716TinySeed          ⚪️🔘🔘⚪️🔘⚪️🔘🔘⚪️🔘⚪️⚪️
	N.1717TinySeed          ⚪️🔘🔘⚪️🔘⚪️🔘🔘⚪️🔘⚪️🔘
	N.1718TinySeed          ⚪️🔘🔘⚪️🔘⚪️🔘🔘⚪️🔘🔘⚪️
	N.1719TinySeed          ⚪️🔘🔘⚪️🔘⚪️🔘🔘⚪️🔘🔘🔘
	N.1720TinySeed          ⚪️🔘🔘⚪️🔘⚪️🔘🔘🔘⚪️⚪️⚪️
	N.1721TinySeed          ⚪️🔘🔘⚪️🔘⚪️🔘🔘🔘⚪️⚪️🔘
	N.1722TinySeed          ⚪️🔘🔘⚪️🔘⚪️🔘🔘🔘⚪️🔘⚪️
	N.1723TinySeed          ⚪️🔘🔘⚪️🔘⚪️🔘🔘🔘⚪️🔘🔘
	N.1724TinySeed          ⚪️🔘🔘⚪️🔘⚪️🔘🔘🔘🔘⚪️⚪️
	N.1725TinySeed          ⚪️🔘🔘⚪️🔘⚪️🔘🔘🔘🔘⚪️🔘
	N.1726TinySeed          ⚪️🔘🔘⚪️🔘⚪️🔘🔘🔘🔘🔘⚪️
	N.1727TinySeed          ⚪️🔘🔘⚪️🔘⚪️🔘🔘🔘🔘🔘🔘
	N.1728TinySeed          ⚪️🔘🔘⚪️🔘🔘⚪️⚪️⚪️⚪️⚪️⚪️
	N.1729TinySeed          ⚪️🔘🔘⚪️🔘🔘⚪️⚪️⚪️⚪️⚪️🔘
	N.1730TinySeed          ⚪️🔘🔘⚪️🔘🔘⚪️⚪️⚪️⚪️🔘⚪️
	N.1731TinySeed          ⚪️🔘🔘⚪️🔘🔘⚪️⚪️⚪️⚪️🔘🔘
	N.1732TinySeed          ⚪️🔘🔘⚪️🔘🔘⚪️⚪️⚪️🔘⚪️⚪️
	N.1733TinySeed          ⚪️🔘🔘⚪️🔘🔘⚪️⚪️⚪️🔘⚪️🔘
	N.1734TinySeed          ⚪️🔘🔘⚪️🔘🔘⚪️⚪️⚪️🔘🔘⚪️
	N.1735TinySeed          ⚪️🔘🔘⚪️🔘🔘⚪️⚪️⚪️🔘🔘🔘
	N.1736TinySeed          ⚪️🔘🔘⚪️🔘🔘⚪️⚪️🔘⚪️⚪️⚪️
	N.1737TinySeed          ⚪️🔘🔘⚪️🔘🔘⚪️⚪️🔘⚪️⚪️🔘
	N.1738TinySeed          ⚪️🔘🔘⚪️🔘🔘⚪️⚪️🔘⚪️🔘⚪️
	N.1739TinySeed          ⚪️🔘🔘⚪️🔘🔘⚪️⚪️🔘⚪️🔘🔘
	N.1740TinySeed          ⚪️🔘🔘⚪️🔘🔘⚪️⚪️🔘🔘⚪️⚪️
	N.1741TinySeed          ⚪️🔘🔘⚪️🔘🔘⚪️⚪️🔘🔘⚪️🔘
	N.1742TinySeed          ⚪️🔘🔘⚪️🔘🔘⚪️⚪️🔘🔘🔘⚪️
	N.1743TinySeed          ⚪️🔘🔘⚪️🔘🔘⚪️⚪️🔘🔘🔘🔘
	N.1744TinySeed          ⚪️🔘🔘⚪️🔘🔘⚪️🔘⚪️⚪️⚪️⚪️
	N.1745TinySeed          ⚪️🔘🔘⚪️🔘🔘⚪️🔘⚪️⚪️⚪️🔘
	N.1746TinySeed          ⚪️🔘🔘⚪️🔘🔘⚪️🔘⚪️⚪️🔘⚪️
	N.1747TinySeed          ⚪️🔘🔘⚪️🔘🔘⚪️🔘⚪️⚪️🔘🔘
	N.1748TinySeed          ⚪️🔘🔘⚪️🔘🔘⚪️🔘⚪️🔘⚪️⚪️
	N.1749TinySeed          ⚪️🔘🔘⚪️🔘🔘⚪️🔘⚪️🔘⚪️🔘
	N.1750TinySeed          ⚪️🔘🔘⚪️🔘🔘⚪️🔘⚪️🔘🔘⚪️
	N.1751TinySeed          ⚪️🔘🔘⚪️🔘🔘⚪️🔘⚪️🔘🔘🔘
	N.1752TinySeed          ⚪️🔘🔘⚪️🔘🔘⚪️🔘🔘⚪️⚪️⚪️
	N.1753TinySeed          ⚪️🔘🔘⚪️🔘🔘⚪️🔘🔘⚪️⚪️🔘
	N.1754TinySeed          ⚪️🔘🔘⚪️🔘🔘⚪️🔘🔘⚪️🔘⚪️
	N.1755TinySeed          ⚪️🔘🔘⚪️🔘🔘⚪️🔘🔘⚪️🔘🔘
	N.1756TinySeed          ⚪️🔘🔘⚪️🔘🔘⚪️🔘🔘🔘⚪️⚪️
	N.1757TinySeed          ⚪️🔘🔘⚪️🔘🔘⚪️🔘🔘🔘⚪️🔘
	N.1758TinySeed          ⚪️🔘🔘⚪️🔘🔘⚪️🔘🔘🔘🔘⚪️
	N.1759TinySeed          ⚪️🔘🔘⚪️🔘🔘⚪️🔘🔘🔘🔘🔘
	N.1760TinySeed          ⚪️🔘🔘⚪️🔘🔘🔘⚪️⚪️⚪️⚪️⚪️
	N.1761TinySeed          ⚪️🔘🔘⚪️🔘🔘🔘⚪️⚪️⚪️⚪️🔘
	N.1762TinySeed          ⚪️🔘🔘⚪️🔘🔘🔘⚪️⚪️⚪️🔘⚪️
	N.1763TinySeed          ⚪️🔘🔘⚪️🔘🔘🔘⚪️⚪️⚪️🔘🔘
	N.1764TinySeed          ⚪️🔘🔘⚪️🔘🔘🔘⚪️⚪️🔘⚪️⚪️
	N.1765TinySeed          ⚪️🔘🔘⚪️🔘🔘🔘⚪️⚪️🔘⚪️🔘
	N.1766TinySeed          ⚪️🔘🔘⚪️🔘🔘🔘⚪️⚪️🔘🔘⚪️
	N.1767TinySeed          ⚪️🔘🔘⚪️🔘🔘🔘⚪️⚪️🔘🔘🔘
	N.1768TinySeed          ⚪️🔘🔘⚪️🔘🔘🔘⚪️🔘⚪️⚪️⚪️
	N.1769TinySeed          ⚪️🔘🔘⚪️🔘🔘🔘⚪️🔘⚪️⚪️🔘
	N.1770TinySeed          ⚪️🔘🔘⚪️🔘🔘🔘⚪️🔘⚪️🔘⚪️
	N.1771TinySeed          ⚪️🔘🔘⚪️🔘🔘🔘⚪️🔘⚪️🔘🔘
	N.1772TinySeed          ⚪️🔘🔘⚪️🔘🔘🔘⚪️🔘🔘⚪️⚪️
	N.1773TinySeed          ⚪️🔘🔘⚪️🔘🔘🔘⚪️🔘🔘⚪️🔘
	N.1774TinySeed          ⚪️🔘🔘⚪️🔘🔘🔘⚪️🔘🔘🔘⚪️
	N.1775TinySeed          ⚪️🔘🔘⚪️🔘🔘🔘⚪️🔘🔘🔘🔘
	N.1776TinySeed          ⚪️🔘🔘⚪️🔘🔘🔘🔘⚪️⚪️⚪️⚪️
	N.1777TinySeed          ⚪️🔘🔘⚪️🔘🔘🔘🔘⚪️⚪️⚪️🔘
	N.1778TinySeed          ⚪️🔘🔘⚪️🔘🔘🔘🔘⚪️⚪️🔘⚪️
	N.1779TinySeed          ⚪️🔘🔘⚪️🔘🔘🔘🔘⚪️⚪️🔘🔘
	N.1780TinySeed          ⚪️🔘🔘⚪️🔘🔘🔘🔘⚪️🔘⚪️⚪️
	N.1781TinySeed          ⚪️🔘🔘⚪️🔘🔘🔘🔘⚪️🔘⚪️🔘
	N.1782TinySeed          ⚪️🔘🔘⚪️🔘🔘🔘🔘⚪️🔘🔘⚪️
	N.1783TinySeed          ⚪️🔘🔘⚪️🔘🔘🔘🔘⚪️🔘🔘🔘
	N.1784TinySeed          ⚪️🔘🔘⚪️🔘🔘🔘🔘🔘⚪️⚪️⚪️
	N.1785TinySeed          ⚪️🔘🔘⚪️🔘🔘🔘🔘🔘⚪️⚪️🔘
	N.1786TinySeed          ⚪️🔘🔘⚪️🔘🔘🔘🔘🔘⚪️🔘⚪️
	N.1787TinySeed          ⚪️🔘🔘⚪️🔘🔘🔘🔘🔘⚪️🔘🔘
	N.1788TinySeed          ⚪️🔘🔘⚪️🔘🔘🔘🔘🔘🔘⚪️⚪️
	N.1789TinySeed          ⚪️🔘🔘⚪️🔘🔘🔘🔘🔘🔘⚪️🔘
	N.1790TinySeed          ⚪️🔘🔘⚪️🔘🔘🔘🔘🔘🔘🔘⚪️
	N.1791TinySeed          ⚪️🔘🔘⚪️🔘🔘🔘🔘🔘🔘🔘🔘
	N.1792TinySeed          ⚪️🔘🔘🔘⚪️⚪️⚪️⚪️⚪️⚪️⚪️⚪️
	N.1793TinySeed          ⚪️🔘🔘🔘⚪️⚪️⚪️⚪️⚪️⚪️⚪️🔘
	N.1794TinySeed          ⚪️🔘🔘🔘⚪️⚪️⚪️⚪️⚪️⚪️🔘⚪️
	N.1795TinySeed          ⚪️🔘🔘🔘⚪️⚪️⚪️⚪️⚪️⚪️🔘🔘
	N.1796TinySeed          ⚪️🔘🔘🔘⚪️⚪️⚪️⚪️⚪️🔘⚪️⚪️
	N.1797TinySeed          ⚪️🔘🔘🔘⚪️⚪️⚪️⚪️⚪️🔘⚪️🔘
	N.1798TinySeed          ⚪️🔘🔘🔘⚪️⚪️⚪️⚪️⚪️🔘🔘⚪️
	N.1799TinySeed          ⚪️🔘🔘🔘⚪️⚪️⚪️⚪️⚪️🔘🔘🔘
	N.1800TinySeed          ⚪️🔘🔘🔘⚪️⚪️⚪️⚪️🔘⚪️⚪️⚪️
	N.1801TinySeed          ⚪️🔘🔘🔘⚪️⚪️⚪️⚪️🔘⚪️⚪️🔘
	N.1802TinySeed          ⚪️🔘🔘🔘⚪️⚪️⚪️⚪️🔘⚪️🔘⚪️
	N.1803TinySeed          ⚪️🔘🔘🔘⚪️⚪️⚪️⚪️🔘⚪️🔘🔘
	N.1804TinySeed          ⚪️🔘🔘🔘⚪️⚪️⚪️⚪️🔘🔘⚪️⚪️
	N.1805TinySeed          ⚪️🔘🔘🔘⚪️⚪️⚪️⚪️🔘🔘⚪️🔘
	N.1806TinySeed          ⚪️🔘🔘🔘⚪️⚪️⚪️⚪️🔘🔘🔘⚪️
	N.1807TinySeed          ⚪️🔘🔘🔘⚪️⚪️⚪️⚪️🔘🔘🔘🔘
	N.1808TinySeed          ⚪️🔘🔘🔘⚪️⚪️⚪️🔘⚪️⚪️⚪️⚪️
	N.1809TinySeed          ⚪️🔘🔘🔘⚪️⚪️⚪️🔘⚪️⚪️⚪️🔘
	N.1810TinySeed          ⚪️🔘🔘🔘⚪️⚪️⚪️🔘⚪️⚪️🔘⚪️
	N.1811TinySeed          ⚪️🔘🔘🔘⚪️⚪️⚪️🔘⚪️⚪️🔘🔘
	N.1812TinySeed          ⚪️🔘🔘🔘⚪️⚪️⚪️🔘⚪️🔘⚪️⚪️
	N.1813TinySeed          ⚪️🔘🔘🔘⚪️⚪️⚪️🔘⚪️🔘⚪️🔘
	N.1814TinySeed          ⚪️🔘🔘🔘⚪️⚪️⚪️🔘⚪️🔘🔘⚪️
	N.1815TinySeed          ⚪️🔘🔘🔘⚪️⚪️⚪️🔘⚪️🔘🔘🔘
	N.1816TinySeed          ⚪️🔘🔘🔘⚪️⚪️⚪️🔘🔘⚪️⚪️⚪️
	N.1817TinySeed          ⚪️🔘🔘🔘⚪️⚪️⚪️🔘🔘⚪️⚪️🔘
	N.1818TinySeed          ⚪️🔘🔘🔘⚪️⚪️⚪️🔘🔘⚪️🔘⚪️
	N.1819TinySeed          ⚪️🔘🔘🔘⚪️⚪️⚪️🔘🔘⚪️🔘🔘
	N.1820TinySeed          ⚪️🔘🔘🔘⚪️⚪️⚪️🔘🔘🔘⚪️⚪️
	N.1821TinySeed          ⚪️🔘🔘🔘⚪️⚪️⚪️🔘🔘🔘⚪️🔘
	N.1822TinySeed          ⚪️🔘🔘🔘⚪️⚪️⚪️🔘🔘🔘🔘⚪️
	N.1823TinySeed          ⚪️🔘🔘🔘⚪️⚪️⚪️🔘🔘🔘🔘🔘
	N.1824TinySeed          ⚪️🔘🔘🔘⚪️⚪️🔘⚪️⚪️⚪️⚪️⚪️
	N.1825TinySeed          ⚪️🔘🔘🔘⚪️⚪️🔘⚪️⚪️⚪️⚪️🔘
	N.1826TinySeed          ⚪️🔘🔘🔘⚪️⚪️🔘⚪️⚪️⚪️🔘⚪️
	N.1827TinySeed          ⚪️🔘🔘🔘⚪️⚪️🔘⚪️⚪️⚪️🔘🔘
	N.1828TinySeed          ⚪️🔘🔘🔘⚪️⚪️🔘⚪️⚪️🔘⚪️⚪️
	N.1829TinySeed          ⚪️🔘🔘🔘⚪️⚪️🔘⚪️⚪️🔘⚪️🔘
	N.1830TinySeed          ⚪️🔘🔘🔘⚪️⚪️🔘⚪️⚪️🔘🔘⚪️
	N.1831TinySeed          ⚪️🔘🔘🔘⚪️⚪️🔘⚪️⚪️🔘🔘🔘
	N.1832TinySeed          ⚪️🔘🔘🔘⚪️⚪️🔘⚪️🔘⚪️⚪️⚪️
	N.1833TinySeed          ⚪️🔘🔘🔘⚪️⚪️🔘⚪️🔘⚪️⚪️🔘
	N.1834TinySeed          ⚪️🔘🔘🔘⚪️⚪️🔘⚪️🔘⚪️🔘⚪️
	N.1835TinySeed          ⚪️🔘🔘🔘⚪️⚪️🔘⚪️🔘⚪️🔘🔘
	N.1836TinySeed          ⚪️🔘🔘🔘⚪️⚪️🔘⚪️🔘🔘⚪️⚪️
	N.1837TinySeed          ⚪️🔘🔘🔘⚪️⚪️🔘⚪️🔘🔘⚪️🔘
	N.1838TinySeed          ⚪️🔘🔘🔘⚪️⚪️🔘⚪️🔘🔘🔘⚪️
	N.1839TinySeed          ⚪️🔘🔘🔘⚪️⚪️🔘⚪️🔘🔘🔘🔘
	N.1840TinySeed          ⚪️🔘🔘🔘⚪️⚪️🔘🔘⚪️⚪️⚪️⚪️
	N.1841TinySeed          ⚪️🔘🔘🔘⚪️⚪️🔘🔘⚪️⚪️⚪️🔘
	N.1842TinySeed          ⚪️🔘🔘🔘⚪️⚪️🔘🔘⚪️⚪️🔘⚪️
	N.1843TinySeed          ⚪️🔘🔘🔘⚪️⚪️🔘🔘⚪️⚪️🔘🔘
	N.1844TinySeed          ⚪️🔘🔘🔘⚪️⚪️🔘🔘⚪️🔘⚪️⚪️
	N.1845TinySeed          ⚪️🔘🔘🔘⚪️⚪️🔘🔘⚪️🔘⚪️🔘
	N.1846TinySeed          ⚪️🔘🔘🔘⚪️⚪️🔘🔘⚪️🔘🔘⚪️
	N.1847TinySeed          ⚪️🔘🔘🔘⚪️⚪️🔘🔘⚪️🔘🔘🔘
	N.1848TinySeed          ⚪️🔘🔘🔘⚪️⚪️🔘🔘🔘⚪️⚪️⚪️
	N.1849TinySeed          ⚪️🔘🔘🔘⚪️⚪️🔘🔘🔘⚪️⚪️🔘
	N.1850TinySeed          ⚪️🔘🔘🔘⚪️⚪️🔘🔘🔘⚪️🔘⚪️
	N.1851TinySeed          ⚪️🔘🔘🔘⚪️⚪️🔘🔘🔘⚪️🔘🔘
	N.1852TinySeed          ⚪️🔘🔘🔘⚪️⚪️🔘🔘🔘🔘⚪️⚪️
	N.1853TinySeed          ⚪️🔘🔘🔘⚪️⚪️🔘🔘🔘🔘⚪️🔘
	N.1854TinySeed          ⚪️🔘🔘🔘⚪️⚪️🔘🔘🔘🔘🔘⚪️
	N.1855TinySeed          ⚪️🔘🔘🔘⚪️⚪️🔘🔘🔘🔘🔘🔘
	N.1856TinySeed          ⚪️🔘🔘🔘⚪️🔘⚪️⚪️⚪️⚪️⚪️⚪️
	N.1857TinySeed          ⚪️🔘🔘🔘⚪️🔘⚪️⚪️⚪️⚪️⚪️🔘
	N.1858TinySeed          ⚪️🔘🔘🔘⚪️🔘⚪️⚪️⚪️⚪️🔘⚪️
	N.1859TinySeed          ⚪️🔘🔘🔘⚪️🔘⚪️⚪️⚪️⚪️🔘🔘
	N.1860TinySeed          ⚪️🔘🔘🔘⚪️🔘⚪️⚪️⚪️🔘⚪️⚪️
	N.1861TinySeed          ⚪️🔘🔘🔘⚪️🔘⚪️⚪️⚪️🔘⚪️🔘
	N.1862TinySeed          ⚪️🔘🔘🔘⚪️🔘⚪️⚪️⚪️🔘🔘⚪️
	N.1863TinySeed          ⚪️🔘🔘🔘⚪️🔘⚪️⚪️⚪️🔘🔘🔘
	N.1864TinySeed          ⚪️🔘🔘🔘⚪️🔘⚪️⚪️🔘⚪️⚪️⚪️
	N.1865TinySeed          ⚪️🔘🔘🔘⚪️🔘⚪️⚪️🔘⚪️⚪️🔘
	N.1866TinySeed          ⚪️🔘🔘🔘⚪️🔘⚪️⚪️🔘⚪️🔘⚪️
	N.1867TinySeed          ⚪️🔘🔘🔘⚪️🔘⚪️⚪️🔘⚪️🔘🔘
	N.1868TinySeed          ⚪️🔘🔘🔘⚪️🔘⚪️⚪️🔘🔘⚪️⚪️
	N.1869TinySeed          ⚪️🔘🔘🔘⚪️🔘⚪️⚪️🔘🔘⚪️🔘
	N.1870TinySeed          ⚪️🔘🔘🔘⚪️🔘⚪️⚪️🔘🔘🔘⚪️
	N.1871TinySeed          ⚪️🔘🔘🔘⚪️🔘⚪️⚪️🔘🔘🔘🔘
	N.1872TinySeed          ⚪️🔘🔘🔘⚪️🔘⚪️🔘⚪️⚪️⚪️⚪️
	N.1873TinySeed          ⚪️🔘🔘🔘⚪️🔘⚪️🔘⚪️⚪️⚪️🔘
	N.1874TinySeed          ⚪️🔘🔘🔘⚪️🔘⚪️🔘⚪️⚪️🔘⚪️
	N.1875TinySeed          ⚪️🔘🔘🔘⚪️🔘⚪️🔘⚪️⚪️🔘🔘
	N.1876TinySeed          ⚪️🔘🔘🔘⚪️🔘⚪️🔘⚪️🔘⚪️⚪️
	N.1877TinySeed          ⚪️🔘🔘🔘⚪️🔘⚪️🔘⚪️🔘⚪️🔘
	N.1878TinySeed          ⚪️🔘🔘🔘⚪️🔘⚪️🔘⚪️🔘🔘⚪️
	N.1879TinySeed          ⚪️🔘🔘🔘⚪️🔘⚪️🔘⚪️🔘🔘🔘
	N.1880TinySeed          ⚪️🔘🔘🔘⚪️🔘⚪️🔘🔘⚪️⚪️⚪️
	N.1881TinySeed          ⚪️🔘🔘🔘⚪️🔘⚪️🔘🔘⚪️⚪️🔘
	N.1882TinySeed          ⚪️🔘🔘🔘⚪️🔘⚪️🔘🔘⚪️🔘⚪️
	N.1883TinySeed          ⚪️🔘🔘🔘⚪️🔘⚪️🔘🔘⚪️🔘🔘
	N.1884TinySeed          ⚪️🔘🔘🔘⚪️🔘⚪️🔘🔘🔘⚪️⚪️
	N.1885TinySeed          ⚪️🔘🔘🔘⚪️🔘⚪️🔘🔘🔘⚪️🔘
	N.1886TinySeed          ⚪️🔘🔘🔘⚪️🔘⚪️🔘🔘🔘🔘⚪️
	N.1887TinySeed          ⚪️🔘🔘🔘⚪️🔘⚪️🔘🔘🔘🔘🔘
	N.1888TinySeed          ⚪️🔘🔘🔘⚪️🔘🔘⚪️⚪️⚪️⚪️⚪️
	N.1889TinySeed          ⚪️🔘🔘🔘⚪️🔘🔘⚪️⚪️⚪️⚪️🔘
	N.1890TinySeed          ⚪️🔘🔘🔘⚪️🔘🔘⚪️⚪️⚪️🔘⚪️
	N.1891TinySeed          ⚪️🔘🔘🔘⚪️🔘🔘⚪️⚪️⚪️🔘🔘
	N.1892TinySeed          ⚪️🔘🔘🔘⚪️🔘🔘⚪️⚪️🔘⚪️⚪️
	N.1893TinySeed          ⚪️🔘🔘🔘⚪️🔘🔘⚪️⚪️🔘⚪️🔘
	N.1894TinySeed          ⚪️🔘🔘🔘⚪️🔘🔘⚪️⚪️🔘🔘⚪️
	N.1895TinySeed          ⚪️🔘🔘🔘⚪️🔘🔘⚪️⚪️🔘🔘🔘
	N.1896TinySeed          ⚪️🔘🔘🔘⚪️🔘🔘⚪️🔘⚪️⚪️⚪️
	N.1897TinySeed          ⚪️🔘🔘🔘⚪️🔘🔘⚪️🔘⚪️⚪️🔘
	N.1898TinySeed          ⚪️🔘🔘🔘⚪️🔘🔘⚪️🔘⚪️🔘⚪️
	N.1899TinySeed          ⚪️🔘🔘🔘⚪️🔘🔘⚪️🔘⚪️🔘🔘
	N.1900TinySeed          ⚪️🔘🔘🔘⚪️🔘🔘⚪️🔘🔘⚪️⚪️
	N.1901TinySeed          ⚪️🔘🔘🔘⚪️🔘🔘⚪️🔘🔘⚪️🔘
	N.1902TinySeed          ⚪️🔘🔘🔘⚪️🔘🔘⚪️🔘🔘🔘⚪️
	N.1903TinySeed          ⚪️🔘🔘🔘⚪️🔘🔘⚪️🔘🔘🔘🔘
	N.1904TinySeed          ⚪️🔘🔘🔘⚪️🔘🔘🔘⚪️⚪️⚪️⚪️
	N.1905TinySeed          ⚪️🔘🔘🔘⚪️🔘🔘🔘⚪️⚪️⚪️🔘
	N.1906TinySeed          ⚪️🔘🔘🔘⚪️🔘🔘🔘⚪️⚪️🔘⚪️
	N.1907TinySeed          ⚪️🔘🔘🔘⚪️🔘🔘🔘⚪️⚪️🔘🔘
	N.1908TinySeed          ⚪️🔘🔘🔘⚪️🔘🔘🔘⚪️🔘⚪️⚪️
	N.1909TinySeed          ⚪️🔘🔘🔘⚪️🔘🔘🔘⚪️🔘⚪️🔘
	N.1910TinySeed          ⚪️🔘🔘🔘⚪️🔘🔘🔘⚪️🔘🔘⚪️
	N.1911TinySeed          ⚪️🔘🔘🔘⚪️🔘🔘🔘⚪️🔘🔘🔘
	N.1912TinySeed          ⚪️🔘🔘🔘⚪️🔘🔘🔘🔘⚪️⚪️⚪️
	N.1913TinySeed          ⚪️🔘🔘🔘⚪️🔘🔘🔘🔘⚪️⚪️🔘
	N.1914TinySeed          ⚪️🔘🔘🔘⚪️🔘🔘🔘🔘⚪️🔘⚪️
	N.1915TinySeed          ⚪️🔘🔘🔘⚪️🔘🔘🔘🔘⚪️🔘🔘
	N.1916TinySeed          ⚪️🔘🔘🔘⚪️🔘🔘🔘🔘🔘⚪️⚪️
	N.1917TinySeed          ⚪️🔘🔘🔘⚪️🔘🔘🔘🔘🔘⚪️🔘
	N.1918TinySeed          ⚪️🔘🔘🔘⚪️🔘🔘🔘🔘🔘🔘⚪️
	N.1919TinySeed          ⚪️🔘🔘🔘⚪️🔘🔘🔘🔘🔘🔘🔘
	N.1920TinySeed          ⚪️🔘🔘🔘🔘⚪️⚪️⚪️⚪️⚪️⚪️⚪️
	N.1921TinySeed          ⚪️🔘🔘🔘🔘⚪️⚪️⚪️⚪️⚪️⚪️🔘
	N.1922TinySeed          ⚪️🔘🔘🔘🔘⚪️⚪️⚪️⚪️⚪️🔘⚪️
	N.1923TinySeed          ⚪️🔘🔘🔘🔘⚪️⚪️⚪️⚪️⚪️🔘🔘
	N.1924TinySeed          ⚪️🔘🔘🔘🔘⚪️⚪️⚪️⚪️🔘⚪️⚪️
	N.1925TinySeed          ⚪️🔘🔘🔘🔘⚪️⚪️⚪️⚪️🔘⚪️🔘
	N.1926TinySeed          ⚪️🔘🔘🔘🔘⚪️⚪️⚪️⚪️🔘🔘⚪️
	N.1927TinySeed          ⚪️🔘🔘🔘🔘⚪️⚪️⚪️⚪️🔘🔘🔘
	N.1928TinySeed          ⚪️🔘🔘🔘🔘⚪️⚪️⚪️🔘⚪️⚪️⚪️
	N.1929TinySeed          ⚪️🔘🔘🔘🔘⚪️⚪️⚪️🔘⚪️⚪️🔘
	N.1930TinySeed          ⚪️🔘🔘🔘🔘⚪️⚪️⚪️🔘⚪️🔘⚪️
	N.1931TinySeed          ⚪️🔘🔘🔘🔘⚪️⚪️⚪️🔘⚪️🔘🔘
	N.1932TinySeed          ⚪️🔘🔘🔘🔘⚪️⚪️⚪️🔘🔘⚪️⚪️
	N.1933TinySeed          ⚪️🔘🔘🔘🔘⚪️⚪️⚪️🔘🔘⚪️🔘
	N.1934TinySeed          ⚪️🔘🔘🔘🔘⚪️⚪️⚪️🔘🔘🔘⚪️
	N.1935TinySeed          ⚪️🔘🔘🔘🔘⚪️⚪️⚪️🔘🔘🔘🔘
	N.1936TinySeed          ⚪️🔘🔘🔘🔘⚪️⚪️🔘⚪️⚪️⚪️⚪️
	N.1937TinySeed          ⚪️🔘🔘🔘🔘⚪️⚪️🔘⚪️⚪️⚪️🔘
	N.1938TinySeed          ⚪️🔘🔘🔘🔘⚪️⚪️🔘⚪️⚪️🔘⚪️
	N.1939TinySeed          ⚪️🔘🔘🔘🔘⚪️⚪️🔘⚪️⚪️🔘🔘
	N.1940TinySeed          ⚪️🔘🔘🔘🔘⚪️⚪️🔘⚪️🔘⚪️⚪️
	N.1941TinySeed          ⚪️🔘🔘🔘🔘⚪️⚪️🔘⚪️🔘⚪️🔘
	N.1942TinySeed          ⚪️🔘🔘🔘🔘⚪️⚪️🔘⚪️🔘🔘⚪️
	N.1943TinySeed          ⚪️🔘🔘🔘🔘⚪️⚪️🔘⚪️🔘🔘🔘
	N.1944TinySeed          ⚪️🔘🔘🔘🔘⚪️⚪️🔘🔘⚪️⚪️⚪️
	N.1945TinySeed          ⚪️🔘🔘🔘🔘⚪️⚪️🔘🔘⚪️⚪️🔘
	N.1946TinySeed          ⚪️🔘🔘🔘🔘⚪️⚪️🔘🔘⚪️🔘⚪️
	N.1947TinySeed          ⚪️🔘🔘🔘🔘⚪️⚪️🔘🔘⚪️🔘🔘
	N.1948TinySeed          ⚪️🔘🔘🔘🔘⚪️⚪️🔘🔘🔘⚪️⚪️
	N.1949TinySeed          ⚪️🔘🔘🔘🔘⚪️⚪️🔘🔘🔘⚪️🔘
	N.1950TinySeed          ⚪️🔘🔘🔘🔘⚪️⚪️🔘🔘🔘🔘⚪️
	N.1951TinySeed          ⚪️🔘🔘🔘🔘⚪️⚪️🔘🔘🔘🔘🔘
	N.1952TinySeed          ⚪️🔘🔘🔘🔘⚪️🔘⚪️⚪️⚪️⚪️⚪️
	N.1953TinySeed          ⚪️🔘🔘🔘🔘⚪️🔘⚪️⚪️⚪️⚪️🔘
	N.1954TinySeed          ⚪️🔘🔘🔘🔘⚪️🔘⚪️⚪️⚪️🔘⚪️
	N.1955TinySeed          ⚪️🔘🔘🔘🔘⚪️🔘⚪️⚪️⚪️🔘🔘
	N.1956TinySeed          ⚪️🔘🔘🔘🔘⚪️🔘⚪️⚪️🔘⚪️⚪️
	N.1957TinySeed          ⚪️🔘🔘🔘🔘⚪️🔘⚪️⚪️🔘⚪️🔘
	N.1958TinySeed          ⚪️🔘🔘🔘🔘⚪️🔘⚪️⚪️🔘🔘⚪️
	N.1959TinySeed          ⚪️🔘🔘🔘🔘⚪️🔘⚪️⚪️🔘🔘🔘
	N.1960TinySeed          ⚪️🔘🔘🔘🔘⚪️🔘⚪️🔘⚪️⚪️⚪️
	N.1961TinySeed          ⚪️🔘🔘🔘🔘⚪️🔘⚪️🔘⚪️⚪️🔘
	N.1962TinySeed          ⚪️🔘🔘🔘🔘⚪️🔘⚪️🔘⚪️🔘⚪️
	N.1963TinySeed          ⚪️🔘🔘🔘🔘⚪️🔘⚪️🔘⚪️🔘🔘
	N.1964TinySeed          ⚪️🔘🔘🔘🔘⚪️🔘⚪️🔘🔘⚪️⚪️
	N.1965TinySeed          ⚪️🔘🔘🔘🔘⚪️🔘⚪️🔘🔘⚪️🔘
	N.1966TinySeed          ⚪️🔘🔘🔘🔘⚪️🔘⚪️🔘🔘🔘⚪️
	N.1967TinySeed          ⚪️🔘🔘🔘🔘⚪️🔘⚪️🔘🔘🔘🔘
	N.1968TinySeed          ⚪️🔘🔘🔘🔘⚪️🔘🔘⚪️⚪️⚪️⚪️
	N.1969TinySeed          ⚪️🔘🔘🔘🔘⚪️🔘🔘⚪️⚪️⚪️🔘
	N.1970TinySeed          ⚪️🔘🔘🔘🔘⚪️🔘🔘⚪️⚪️🔘⚪️
	N.1971TinySeed          ⚪️🔘🔘🔘🔘⚪️🔘🔘⚪️⚪️🔘🔘
	N.1972TinySeed          ⚪️🔘🔘🔘🔘⚪️🔘🔘⚪️🔘⚪️⚪️
	N.1973TinySeed          ⚪️🔘🔘🔘🔘⚪️🔘🔘⚪️🔘⚪️🔘
	N.1974TinySeed          ⚪️🔘🔘🔘🔘⚪️🔘🔘⚪️🔘🔘⚪️
	N.1975TinySeed          ⚪️🔘🔘🔘🔘⚪️🔘🔘⚪️🔘🔘🔘
	N.1976TinySeed          ⚪️🔘🔘🔘🔘⚪️🔘🔘🔘⚪️⚪️⚪️
	N.1977TinySeed          ⚪️🔘🔘🔘🔘⚪️🔘🔘🔘⚪️⚪️🔘
	N.1978TinySeed          ⚪️🔘🔘🔘🔘⚪️🔘🔘🔘⚪️🔘⚪️
	N.1979TinySeed          ⚪️🔘🔘🔘🔘⚪️🔘🔘🔘⚪️🔘🔘
	N.1980TinySeed          ⚪️🔘🔘🔘🔘⚪️🔘🔘🔘🔘⚪️⚪️
	N.1981TinySeed          ⚪️🔘🔘🔘🔘⚪️🔘🔘🔘🔘⚪️🔘
	N.1982TinySeed          ⚪️🔘🔘🔘🔘⚪️🔘🔘🔘🔘🔘⚪️
	N.1983TinySeed          ⚪️🔘🔘🔘🔘⚪️🔘🔘🔘🔘🔘🔘
	N.1984TinySeed          ⚪️🔘🔘🔘🔘🔘⚪️⚪️⚪️⚪️⚪️⚪️
	N.1985TinySeed          ⚪️🔘🔘🔘🔘🔘⚪️⚪️⚪️⚪️⚪️🔘
	N.1986TinySeed          ⚪️🔘🔘🔘🔘🔘⚪️⚪️⚪️⚪️🔘⚪️
	N.1987TinySeed          ⚪️🔘🔘🔘🔘🔘⚪️⚪️⚪️⚪️🔘🔘
	N.1988TinySeed          ⚪️🔘🔘🔘🔘🔘⚪️⚪️⚪️🔘⚪️⚪️
	N.1989TinySeed          ⚪️🔘🔘🔘🔘🔘⚪️⚪️⚪️🔘⚪️🔘
	N.1990TinySeed          ⚪️🔘🔘🔘🔘🔘⚪️⚪️⚪️🔘🔘⚪️
	N.1991TinySeed          ⚪️🔘🔘🔘🔘🔘⚪️⚪️⚪️🔘🔘🔘
	N.1992TinySeed          ⚪️🔘🔘🔘🔘🔘⚪️⚪️🔘⚪️⚪️⚪️
	N.1993TinySeed          ⚪️🔘🔘🔘🔘🔘⚪️⚪️🔘⚪️⚪️🔘
	N.1994TinySeed          ⚪️🔘🔘🔘🔘🔘⚪️⚪️🔘⚪️🔘⚪️
	N.1995TinySeed          ⚪️🔘🔘🔘🔘🔘⚪️⚪️🔘⚪️🔘🔘
	N.1996TinySeed          ⚪️🔘🔘🔘🔘🔘⚪️⚪️🔘🔘⚪️⚪️
	N.1997TinySeed          ⚪️🔘🔘🔘🔘🔘⚪️⚪️🔘🔘⚪️🔘
	N.1998TinySeed          ⚪️🔘🔘🔘🔘🔘⚪️⚪️🔘🔘🔘⚪️
	N.1999TinySeed          ⚪️🔘🔘🔘🔘🔘⚪️⚪️🔘🔘🔘🔘
	N.2000TinySeed          ⚪️🔘🔘🔘🔘🔘⚪️🔘⚪️⚪️⚪️⚪️
	N.2001TinySeed          ⚪️🔘🔘🔘🔘🔘⚪️🔘⚪️⚪️⚪️🔘
	N.2002TinySeed          ⚪️🔘🔘🔘🔘🔘⚪️🔘⚪️⚪️🔘⚪️
	N.2003TinySeed          ⚪️🔘🔘🔘🔘🔘⚪️🔘⚪️⚪️🔘🔘
	N.2004TinySeed          ⚪️🔘🔘🔘🔘🔘⚪️🔘⚪️🔘⚪️⚪️
	N.2005TinySeed          ⚪️🔘🔘🔘🔘🔘⚪️🔘⚪️🔘⚪️🔘
	N.2006TinySeed          ⚪️🔘🔘🔘🔘🔘⚪️🔘⚪️🔘🔘⚪️
	N.2007TinySeed          ⚪️🔘🔘🔘🔘🔘⚪️🔘⚪️🔘🔘🔘
	N.2008TinySeed          ⚪️🔘🔘🔘🔘🔘⚪️🔘🔘⚪️⚪️⚪️
	N.2009TinySeed          ⚪️🔘🔘🔘🔘🔘⚪️🔘🔘⚪️⚪️🔘
	N.2010TinySeed          ⚪️🔘🔘🔘🔘🔘⚪️🔘🔘⚪️🔘⚪️
	N.2011TinySeed          ⚪️🔘🔘🔘🔘🔘⚪️🔘🔘⚪️🔘🔘
	N.2012TinySeed          ⚪️🔘🔘🔘🔘🔘⚪️🔘🔘🔘⚪️⚪️
	N.2013TinySeed          ⚪️🔘🔘🔘🔘🔘⚪️🔘🔘🔘⚪️🔘
	N.2014TinySeed          ⚪️🔘🔘🔘🔘🔘⚪️🔘🔘🔘🔘⚪️
	N.2015TinySeed          ⚪️🔘🔘🔘🔘🔘⚪️🔘🔘🔘🔘🔘
	N.2016TinySeed          ⚪️🔘🔘🔘🔘🔘🔘⚪️⚪️⚪️⚪️⚪️
	N.2017TinySeed          ⚪️🔘🔘🔘🔘🔘🔘⚪️⚪️⚪️⚪️🔘
	N.2018TinySeed          ⚪️🔘🔘🔘🔘🔘🔘⚪️⚪️⚪️🔘⚪️
	N.2019TinySeed          ⚪️🔘🔘🔘🔘🔘🔘⚪️⚪️⚪️🔘🔘
	N.2020TinySeed          ⚪️🔘🔘🔘🔘🔘🔘⚪️⚪️🔘⚪️⚪️
	N.2021TinySeed          ⚪️🔘🔘🔘🔘🔘🔘⚪️⚪️🔘⚪️🔘
	N.2022TinySeed          ⚪️🔘🔘🔘🔘🔘🔘⚪️⚪️🔘🔘⚪️
	N.2023TinySeed          ⚪️🔘🔘🔘🔘🔘🔘⚪️⚪️🔘🔘🔘
	N.2024TinySeed          ⚪️🔘🔘🔘🔘🔘🔘⚪️🔘⚪️⚪️⚪️
	N.2025TinySeed          ⚪️🔘🔘🔘🔘🔘🔘⚪️🔘⚪️⚪️🔘
	N.2026TinySeed          ⚪️🔘🔘🔘🔘🔘🔘⚪️🔘⚪️🔘⚪️
	N.2027TinySeed          ⚪️🔘🔘🔘🔘🔘🔘⚪️🔘⚪️🔘🔘
	N.2028TinySeed          ⚪️🔘🔘🔘🔘🔘🔘⚪️🔘🔘⚪️⚪️
	N.2029TinySeed          ⚪️🔘🔘🔘🔘🔘🔘⚪️🔘🔘⚪️🔘
	N.2030TinySeed          ⚪️🔘🔘🔘🔘🔘🔘⚪️🔘🔘🔘⚪️
	N.2031TinySeed          ⚪️🔘🔘🔘🔘🔘🔘⚪️🔘🔘🔘🔘
	N.2032TinySeed          ⚪️🔘🔘🔘🔘🔘🔘🔘⚪️⚪️⚪️⚪️
	N.2033TinySeed          ⚪️🔘🔘🔘🔘🔘🔘🔘⚪️⚪️⚪️🔘
	N.2034TinySeed          ⚪️🔘🔘🔘🔘🔘🔘🔘⚪️⚪️🔘⚪️
	N.2035TinySeed          ⚪️🔘🔘🔘🔘🔘🔘🔘⚪️⚪️🔘🔘
	N.2036TinySeed          ⚪️🔘🔘🔘🔘🔘🔘🔘⚪️🔘⚪️⚪️
	N.2037TinySeed          ⚪️🔘🔘🔘🔘🔘🔘🔘⚪️🔘⚪️🔘
	N.2038TinySeed          ⚪️🔘🔘🔘🔘🔘🔘🔘⚪️🔘🔘⚪️
	N.2039TinySeed          ⚪️🔘🔘🔘🔘🔘🔘🔘⚪️🔘🔘🔘
	N.2040TinySeed          ⚪️🔘🔘🔘🔘🔘🔘🔘🔘⚪️⚪️⚪️
	N.2041TinySeed          ⚪️🔘🔘🔘🔘🔘🔘🔘🔘⚪️⚪️🔘
	N.2042TinySeed          ⚪️🔘🔘🔘🔘🔘🔘🔘🔘⚪️🔘⚪️
	N.2043TinySeed          ⚪️🔘🔘🔘🔘🔘🔘🔘🔘⚪️🔘🔘
	N.2044TinySeed          ⚪️🔘🔘🔘🔘🔘🔘🔘🔘🔘⚪️⚪️
	N.2045TinySeed          ⚪️🔘🔘🔘🔘🔘🔘🔘🔘🔘⚪️🔘
	N.2046TinySeed          ⚪️🔘🔘🔘🔘🔘🔘🔘🔘🔘🔘⚪️
	N.2047TinySeed          ⚪️🔘🔘🔘🔘🔘🔘🔘🔘🔘🔘🔘
	N.2048TinySeed          🔘⚪️⚪️⚪️⚪️⚪️⚪️⚪️⚪️⚪️⚪️⚪️
    """)
    input("Continue...")

#--------------------------------- NYMs -----------------------------------

def get_ansi_color_code(r, g, b):
    if r == g == b:
        if r < 8:
            return 16
        return 231 if r > 248 else round(((r - 8) / 247) * 24) + 232
    return 16 + (36 * round(r / 255 * 5)) + (6 * round(g / 255 * 5)) + round(b / 255 * 5)


def get_color(r, g, b):
    return f"\x1b[48;5;{int(get_ansi_color_code(r, g, b))}m \x1b[0m"


def robotNym():
    try:
        if path['bitcoincli']:
            lncli = " getinfo"
            lsd = os.popen(lndconnectload['ln'] + lncli).read()
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
    except:
        menuSelection()


#---------------------------------Sat Sale----------------------------------
def callGitSatSale():
    if not os.path.isdir('SatSale'):
        git = "git clone https://github.com/nickfarrow/SatSale.git"
        os.system(git)
    os.system("cd SatSale && python3 satsale.py")

#---------------------------------Cashu----------------------------------
def callGitCashu():
    if not os.path.isdir('Cashu'):
        git = "pip3 install cashu && mkdir Cashu"
        os.system(git)
    os.system("cd Cashu && cashu")

#-----------------------------Block Templates--------------------------------

def blockTmpConn():
    try:
        conn = """curl -s https://miningpool.observer/template-and-block | html2text | grep "Template and Block for" -A 13 """
        a = os.popen(conn).read()
        clear()
        blogo()
        closed()
        output = render("Templates and Blocks", colors=['yellow'], align='left', font='tiny')
        print(output)
        print(a)
        input("\a\nContinue...")
    except:
        pass

#-----------------------------END Block Templates--------------------------------

#---------------------------------Warden Terminal----------------------------------
def callGitWardenTerminal():
    if not os.path.isdir('warden_terminal'):
        git = "git clone https://github.com/pxsocs/warden_terminal.git"
        os.system(git)
    os.system("cd warden_terminal && python3 node_warden.py")

#---------------------------------Nostr Terminal----------------------------------

def callGitNostrLinTerminal():
    try:
        clear()
        blogo()
        output = render(
            "Nostr Console Linux", colors=['yellow'], align='left', font='tiny'
        )
        if os.path.isdir ('nostr_console_pyblock'):
            os.system("cd nostr_console_pyblock && rm -rf nostr_console_linux_amd64 && wget https://raw.githubusercontent.com/curly60e/pyblock/master/pybitblock/nostr_console_pyblock/nostr_console_linux_amd64 && chmod 777 *")
        else: # Check if the file 'bclock.conf' is in the same folder
            os.system("mkdir nostr_console_pyblock && cd nostr_console_pyblock && wget https://raw.githubusercontent.com/curly60e/pyblock/master/pybitblock/nostr_console_pyblock/nostr_console_linux_amd64 && chmod 777 *")
        clear()
        blogo()
        print(output)
        responseC = input("Paste your PrivateKey: ")
        os.system(f"cd nostr_console_pyblock && ./nostr_console_linux_amd64 -k {responseC} -l")
    except:
        menuSelection()
        
def callGitNostrLinarmTerminal():
    try:
        clear()
        blogo()
        output = render(
            "Nostr Console Linux", colors=['yellow'], align='left', font='tiny'
        )
        if os.path.isdir ('nostr_console_pyblock'):
            os.system("cd nostr_console_pyblock && rm -rf nostr_console_linux_arm64 && wget https://raw.githubusercontent.com/curly60e/pyblock/master/pybitblock/nostr_console_pyblock/nostr_console_linux_arm64 && chmod 777 *")
        else: # Check if the file 'bclock.conf' is in the same folder
            os.system("mkdir nostr_console_pyblock && cd nostr_console_pyblock && wget https://raw.githubusercontent.com/curly60e/pyblock/master/pybitblock/nostr_console_pyblock/nostr_console_linux_arm64 && chmod 777 *")
        clear()
        blogo()
        print(output)
        responseC = input("Paste your PrivateKey: ")
        os.system(f"cd nostr_console_pyblock && ./nostr_console_linux_arm64 -k {responseC} -l")
    except:
        menuSelection()
        
def callGitNostrMacTerminal():
    try:
        clear()
        blogo()
        output = render(
            "Nostr Console macOS", colors=['yellow'], align='left', font='tiny'
        )
        if os.path.isdir ('nostr_console_pyblock'):
            os.system("cd nostr_console_pyblock && rm -rf nostr_console_macos_amd64 && wget https://raw.githubusercontent.com/curly60e/pyblock/master/pybitblock/nostr_console_pyblock/nostr_console_macos_amd64")
        else: # Check if the file 'bclock.conf' is in the same folder
            os.system("mkdir nostr_console_pyblock && cd nostr_console_pyblock && wget https://raw.githubusercontent.com/curly60e/pyblock/master/pybitblock/nostr_console_pyblock/nostr_console_macos_amd64")
        clear()
        blogo()

        print(output)
        responseC = input("Paste your PrivateKey: ")
        os.system(f"cd nostr_console_pyblock && ./nostr_console_macos_amd64 -k {responseC} -l")
    except:
        menuSelection()

def callGitNostrMacarmTerminal():
    try:
        clear()
        blogo()
        output = render(
            "Nostr Console macOS", colors=['yellow'], align='left', font='tiny'
        )
        if os.path.isdir ('nostr_console_pyblock'):
            os.system("cd nostr_console_pyblock && rm -rf nostr_console_elf64 && wget https://raw.githubusercontent.com/curly60e/pyblock/master/pybitblock/nostr_console_pyblock/nostr_console_elf64 && chmod 777 *")
        else: # Check if the file 'bclock.conf' is in the same folder
            os.system("mkdir nostr_console_pyblock && cd nostr_console_pyblock && wget https://raw.githubusercontent.com/curly60e/pyblock/master/pybitblock/nostr_console_pyblock/nostr_console_elf64 && chmod 777 *")
        clear()
        blogo()
        print(output)
        responseC = input("Paste your PrivateKey: ")
        os.system(f"cd nostr_console_pyblock && ./nostr_console_elf64 -k {responseC} -l")
    except:
        menuSelection()
        
def callGitNostrWinTerminal():
    try:
        clear()
        blogo()
        output = render(
            "Nostr Console Windows", colors=['yellow'], align='left', font='tiny'
        )
        if os.path.isdir ('nostr_console_pyblock'):
            os.system("cd nostr_console_pyblock && rm -rf nostr_console_windows_amd64.exe && wget https://raw.githubusercontent.com/curly60e/pyblock/master/pybitblock/nostr_console_pyblock/nostr_console_windows_amd64.exe")
        else: # Check if the file 'bclock.conf' is in the same folder
            os.system("mkdir nostr_console_pyblock && cd nostr_console_pyblock && wget https://raw.githubusercontent.com/curly60e/pyblock/master/pybitblock/nostr_console_pyblock/nostr_console_windows_amd64.exe")
        clear()
        blogo()
        print(output)
        responseC = input("Paste your PrivateKey: ")
        os.system(f"cd nostr_console_pyblock && ./nostr_console_windows_amd64.exe -k {responseC} -l")
    except:
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
            os.system("mkdir nostr_seed && cd nostr_seed && wget https://gist.githubusercontent.com/odudex/93cfb5628b22f8675ab1939fd43133f4/raw/b48f047c0358a9ae50c2027106bdf5e37ee1fe5c/nostr_seed.py")
        clear()
        blogo()
        print(output)
        responseC = input("Hex to BIP39 & BIP39 to Hex: ")
        os.system(f"cd nostr_seed && python3 nostr_seed.py {responseC}")
        input("\a\nContinue...")
    except:
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
            os.system("mkdir nostr_QRseed && cd nostr_QRseed && wget https://gist.githubusercontent.com/odudex/9e848a91d23e967309bd1719910021e6/raw/dbe04893f4ee2e0aa020735528f7f19bb2d13a7e/nostr_c_seed_qr.py")
        clear()
        blogo()
        print(output)
        responseC = input("Hex to BIP39 QR & BIP39 to Hex QR: ")
        os.system(f"cd nostr_QRseed && python3 nostr_c_seed_qr.py {responseC}")
        input("\a\nContinue...")
    except:
        menuSelection()
        
def callGitBija():
    if not os.path.isdir('bija'):
        git = "git clone --recurse-submodules https://github.com/BrightonBTC/bija"
        os.system(git)
    os.system("cd bija && docker-compose up")
    input("\a\nYou can now access Bija at http://localhost:5000")
    
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
                git = "git clone https://github.com/jamesob/coldcore.git"
                install = "cd coldcore && chmod +x coldcore && cp coldcore ~/.local/bin/coldcore"
                os.system(git)
                os.system(install)
            os.system("coldcore")
    except:
        menuSelection()

#--------------------------------- Menu section -----------------------------------

def MainMenuLOCAL(): #Main Menu
    clear()
    blogo()
    sysinfo()
    pathexec()
    lndconnectexec()
    n = "Local" if path['bitcoincli'] else "Remote"
    bitcoincli = " getblockchaininfo"
    a = os.popen(path['bitcoincli'] + bitcoincli).read()
    b = json.loads(a)
    d = b

    lncli = " getinfo"
    lsd = os.popen(lndconnectload['ln'] + lncli).read()
    lsd0 = str(lsd)
    alias = json.loads(lsd0)
    print("""\t\t
    \033[1;37;40m{}\033[0;37;40m: \033[1;31;40mPyBLOCK\033[0;37;40m
    \033[1;37;40mNode\033[0;37;40m: \033[1;33;40m{}\033[0;37;40m
    \033[1;37;40mBlock\033[0;37;40m: \033[1;32;40m{}\033[0;37;40m\a
    \033[1;37;40mVersion\033[0;37;40m: {}


    \u001b[31;1mA.\033[0;37;40m PyBLOCK
    \u001b[38;5;202mB.\033[0;37;40m Bitcoin Core
    \u001b[33;1mL.\033[0;37;40m Lightning Network
    \u001b[38;5;40mP.\033[0;37;40m Platforms
    \u001b[38;5;27mS.\033[0;37;40m Settings
    \u001b[38;5;15mX.\033[0;37;40m Donate
    \u001b[38;5;93mQ.\033[0;37;40m Exit
    \n\n\x1b[?25h""".format(n, alias['alias'], d['blocks'], version, checkupdate()))
    mainmenuLOCALcontrol(input("\033[1;32;40mSelect option: \033[0;37;40m"))

def MainMenuLOCALChainONLY(): #Main Menu
    clear()
    blogo()
    sysinfo()
    pathexec()
    #lndconnectexec()
    n = "Local" if path['bitcoincli'] else "Remote"
    bitcoincli = " getblockchaininfo"
    a = os.popen(path['bitcoincli'] + bitcoincli).read()
    b = json.loads(a)
    d = b
    print("""\t\t
    \033[1;37;40m{}\033[0;37;40m: \033[1;31;40mPyBLOCK\033[0;37;40m
    \033[1;37;40mBlock\033[0;37;40m: \033[1;32;40m{}\033[0;37;40m\a
    \033[1;37;40mVersion\033[0;37;40m: {}


    \u001b[31;1mA.\033[0;37;40m PyBLOCK
    \u001b[38;5;202mB.\033[0;37;40m Bitcoin Core
    \u001b[38;5;40mP.\033[0;37;40m Platforms
    \u001b[38;5;27mS.\033[0;37;40m Settings
    \u001b[38;5;15mX.\033[0;37;40m Donate
    \u001b[38;5;93mQ.\033[0;37;40m Exit
    \n\n\x1b[?25h""".format(n,d['blocks'], version, checkupdate()))
    mainmenuLOCALcontrolOnchainONLY(input("\033[1;32;40mSelect option: \033[0;37;40m"))

def MainMenuREMOTE(): #Main Menu
    clear()
    blogo()
    sysinfo()
    pathexec()
    lndconnectexec()
    path = {"ip_port":"", "rpcuser":"", "rpcpass":"", "bitcoincli":""}
    pathv = pickle.load(open("config/bclock.conf", "rb")) # Load the file 'bclock.conf'
    path = pathv # Copy the variable pathv to 'path'
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
    \033[1;37;40mBlock\033[0;37;40m: \033[1;32;40m{}\033[0;37;40m\a
    \033[1;37;40mVersion\033[0;37;40m: {}


    \u001b[31;1mA.\033[0;37;40m PyBLOCK
    \u001b[38;5;202mB.\033[0;37;40m Bitcoin Core
    \u001b[33;1mL.\033[0;37;40m Lightning Network
    \u001b[38;5;40mP.\033[0;37;40m Platforms
    \u001b[38;5;27mS.\033[0;37;40m Settings
    \u001b[38;5;15mX.\033[0;37;40m Donate
    \u001b[38;5;93mQ.\033[0;37;40m Exit
    \n\n\x1b[?25h""".format(a, alias['alias'], d['blocks'], version, checkupdate()))
    mainmenuREMOTEcontrol(input("\033[1;32;40mSelect option: \033[0;37;40m"))

def bitcoincoremenuLOCAL():
    clear()
    blogo()
    sysinfo()
    pathexec()
    lndconnectexec()
    n = "Local" if path['bitcoincli'] else "Remote"
    bitcoincli = " getblockchaininfo"
    a = os.popen(path['bitcoincli'] + bitcoincli).read()
    b = json.loads(a)
    d = b

    lncli = " getinfo"
    lsd = os.popen(lndconnectload['ln'] + lncli).read()
    lsd0 = str(lsd)
    alias = json.loads(lsd0)

    print("""\t\t
    \033[1;37;40m{}\033[0;37;40m: \033[1;31;40mPyBLOCK\033[0;37;40m
    \033[1;37;40mNode\033[0;37;40m: \033[1;33;40m{}\033[0;37;40m
    \033[1;37;40mBlock\033[0;37;40m: \033[1;32;40m{}\033[0;37;40m
    \033[1;37;40mVersion\033[0;37;40m: {}

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
    \u001b[38;5;202mM.\033[0;37;40m Moscow Time
    \u001b[38;5;202mO.\033[0;37;40m OP_RETURN
    \u001b[38;5;202mZ.\033[0;37;40m Stats
    \u001b[38;5;202mQ.\033[0;37;40m Hashrate
    \u001b[38;5;202mU.\033[0;37;40m Unconfirmed Txs
    \u001b[38;5;202mS.\033[0;37;40m Mempool
    \u001b[33;1mR.\033[0;37;40m Return
    \n\n\x1b[?25h""".format(n, alias['alias'], d['blocks'], version, checkupdate()))
    bitcoincoremenuLOCALcontrolA(input("\033[1;32;40mSelect option: \033[0;37;40m"))

def bitcoincoremenuLOCALOnchainONLY():
    clear()
    blogo()
    sysinfo()
    pathexec()
    #lndconnectexec()
    n = "Local" if path['bitcoincli'] else "Remote"
    bitcoincli = " getblockchaininfo"
    a = os.popen(path['bitcoincli'] + bitcoincli).read()
    b = json.loads(a)
    d = b

    print("""\t\t
    \033[1;37;40m{}\033[0;37;40m: \033[1;31;40mPyBLOCK\033[0;37;40m
    \033[1;37;40mBlock\033[0;37;40m: \033[1;32;40m{}\033[0;37;40m
    \033[1;37;40mVersion\033[0;37;40m: {}

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
    \u001b[38;5;202mM.\033[0;37;40m Moscow Time
    \u001b[38;5;202mO.\033[0;37;40m OP_RETURN
    \u001b[38;5;202mW.\033[0;37;40m Wallet
    \u001b[38;5;202mZ.\033[0;37;40m Stats
    \u001b[38;5;202mQ.\033[0;37;40m Hashrate
    \u001b[38;5;202mU.\033[0;37;40m Unconfirmed Txs
    \u001b[38;5;202mS.\033[0;37;40m Mempool
    \u001b[33;1mR.\033[0;37;40m Return
    \n\n\x1b[?25h""".format(n,d['blocks'], version, checkupdate()))
    bitcoincoremenuLOCALcontrolAOnchainONLY(input("\033[1;32;40mSelect option: \033[0;37;40m"))

def walletmenuLOCALOnchainONLY():
    clear()
    blogo()
    sysinfo()
    pathexec()
    #lndconnectexec()
    n = "Local" if path['bitcoincli'] else "Remote"
    bitcoincli = " getblockchaininfo"
    a = os.popen(path['bitcoincli'] + bitcoincli).read()
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
    \u001b[33;1mR.\033[0;37;40m Return
    \n\n\x1b[?25h""".format(n,d['blocks'], version, checkupdate()))
    walletmenuLOCALcontrolAOnchainONLY(input("\033[1;32;40mSelect option: \033[0;37;40m"))

def bitcoincoremenuLOCALOPRETURN():
    clear()
    blogo()
    sysinfo()
    pathexec()
    lndconnectexec()
    n = "Local" if path['bitcoincli'] else "Remote"
    bitcoincli = " getblockchaininfo"
    a = os.popen(path['bitcoincli'] + bitcoincli).read()
    b = json.loads(a)
    d = b

    lncli = " getinfo"
    lsd = os.popen(lndconnectload['ln'] + lncli).read()
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
    \u001b[33;1mR.\033[0;37;40m Return
    \n\n\x1b[?25h""".format(n, alias['alias'], d['blocks'], version, checkupdate()))
    bitcoincoremenuLOCALcontrolO(input("\033[1;32;40mSelect option: \033[0;37;40m"))

def bitcoincoremenuLOCALOPRETURNOnchainONLY():
    clear()
    blogo()
    sysinfo()
    pathexec()
    #lndconnectexec()
    n = "Local" if path['bitcoincli'] else "Remote"
    bitcoincli = " getblockchaininfo"
    a = os.popen(path['bitcoincli'] + bitcoincli).read()
    b = json.loads(a)
    d = b

    print("""\t\t
    \033[1;37;40m{}\033[0;37;40m: \033[1;31;40mPyBLOCK\033[0;37;40m
    \033[1;37;40mNode\033[0;37;40m: \033[1;33;40m{}\033[0;37;40m
    \033[1;37;40mBlock\033[0;37;40m: \033[1;32;40m{}\033[0;37;40m
    \033[1;37;40mVersion\033[0;37;40m: {}

    \u001b[38;5;202mA.\033[0;37;40m Send OP_RETURN
    \u001b[38;5;202mB.\033[0;37;40m View OP_RETURN
    \u001b[38;5;202mC.\033[0;37;40m View Decoded Coinbase
    \u001b[33;1mR.\033[0;37;40m Return
    \n\n\x1b[?25h""".format(n, d['blocks'], version, checkupdate()))
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
    \u001b[33;1mR.\033[0;37;40m Return
    \n\n\x1b[?25h""".format(a, alias['alias'], d['blocks'], version, checkupdate()))
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
    \u001b[33;1mR.\033[0;37;40m Return
    \n\n\x1b[?25h""".format(a, alias['alias'], d['blocks'], version, checkupdate()))
    bitcoincoremenuREMOTEcontrolO(input("\033[1;32;40mSelect option: \033[0;37;40m"))

def lightningnetworkLOCAL():
    clear()
    blogo()
    sysinfo()
    pathexec()
    lndconnectexec()
    n = "Local" if path['bitcoincli'] else "Remote"
    bitcoincli = " getblockchaininfo"
    a = os.popen(path['bitcoincli'] + bitcoincli).read()
    b = json.loads(a)
    d = b

    lncli = " getinfo"
    lsd = os.popen(lndconnectload['ln'] + lncli).read()
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
    \u001b[31;1mR.\033[0;37;40m Return
    \n\n\x1b[?25h""".format(n, alias['alias'], d['blocks'], version, checkupdate(), lnbitspaid = "UNLOCKED" if os.path.isfile("lnbitSN.conf") else "LOCKED"))
    lightningnetworkLOCALcontrol(input("\033[1;32;40mSelect option: \033[0;37;40m"))

def chatConn():
    clear()
    blogo()
    sysinfo()
    pathexec()
    lndconnectexec()
    n = "Local" if path['bitcoincli'] else "Remote"
    bitcoincli = " getblockchaininfo"
    a = os.popen(path['bitcoincli'] + bitcoincli).read()
    b = json.loads(a)
    d = b

    lncli = " getinfo"
    lsd = os.popen(lndconnectload['ln'] + lncli).read()
    lsd0 = str(lsd)
    alias = json.loads(lsd0)

    print("""\t\t
    \033[1;37;40m{}\033[0;37;40m: \033[1;31;40mPyBLOCK\033[0;37;40m
    \033[1;37;40mBlock\033[0;37;40m: \033[1;32;40m{}\033[0;37;40m
    \033[1;37;40mVersion\033[0;37;40m: {}

    \u001b[38;5;202mA.\033[0;37;40m Open
    \u001b[38;5;202mB.\033[0;37;40m Close
    \u001b[38;5;202mC.\033[0;37;40m Hidden
    \u001b[31;1mQ.\033[0;37;40m Return
    \n\n\x1b[?25h""".format(n, d['blocks'], version, checkupdate()))
    chatConnA(input("\033[1;32;40mSelect option: \033[0;37;40m"))

def pyCHATA():
    clear()
    blogo()
    sysinfo()
    pathexec()
    lndconnectexec()
    n = "Local" if path['bitcoincli'] else "Remote"
    bitcoincli = " getblockchaininfo"
    a = os.popen(path['bitcoincli'] + bitcoincli).read()
    b = json.loads(a)
    d = b

    lncli = " getinfo"
    lsd = os.popen(lndconnectload['ln'] + lncli).read()
    lsd0 = str(lsd)
    alias = json.loads(lsd0)

    print("""\t\t
    \033[1;37;40m{}\033[0;37;40m: \033[1;31;40mPyBLOCK\033[0;37;40m
    \033[1;37;40mBlock\033[0;37;40m: \033[1;32;40m{}\033[0;37;40m
    \033[1;37;40mVersion\033[0;37;40m: {}

    \u001b[38;5;202mA.\033[0;37;40m Write
    \u001b[38;5;202mB.\033[0;37;40m Read
    \u001b[38;5;202mC.\033[0;37;40m List
    \u001b[31;1mQ.\033[0;37;40m Return
    \n\n\x1b[?25h""".format(n, d['blocks'], version, checkupdate()))
    chatConnB(input("\033[1;32;40mSelect option: \033[0;37;40m"))

def pyCHATB():
    clear()
    blogo()
    sysinfo()
    pathexec()
    lndconnectexec()
    n = "Local" if path['bitcoincli'] else "Remote"
    bitcoincli = " getblockchaininfo"
    a = os.popen(path['bitcoincli'] + bitcoincli).read()
    b = json.loads(a)
    d = b

    lncli = " getinfo"
    lsd = os.popen(lndconnectload['ln'] + lncli).read()
    lsd0 = str(lsd)
    alias = json.loads(lsd0)

    print("""\t\t
    \033[1;37;40m{}\033[0;37;40m: \033[1;31;40mPyBLOCK\033[0;37;40m
    \033[1;37;40mBlock\033[0;37;40m: \033[1;32;40m{}\033[0;37;40m
    \033[1;37;40mVersion\033[0;37;40m: {}

    \u001b[38;5;202mA.\033[0;37;40m Write
    \u001b[38;5;202mB.\033[0;37;40m Read
    \u001b[38;5;202mC.\033[0;37;40m List
    \u001b[31;1mQ.\033[0;37;40m Return
    \n\n\x1b[?25h""".format(n, d['blocks'], version, checkupdate()))
    chatConnC(input("\033[1;32;40mSelect option: \033[0;37;40m"))

def pyCHATC():
    clear()
    blogo()
    sysinfo()
    pathexec()
    lndconnectexec()
    n = "Local" if path['bitcoincli'] else "Remote"
    bitcoincli = " getblockchaininfo"
    a = os.popen(path['bitcoincli'] + bitcoincli).read()
    b = json.loads(a)
    d = b

    lncli = " getinfo"
    lsd = os.popen(lndconnectload['ln'] + lncli).read()
    lsd0 = str(lsd)
    alias = json.loads(lsd0)

    print("""\t\t
    \033[1;37;40m{}\033[0;37;40m: \033[1;31;40mPyBLOCK\033[0;37;40m
    \033[1;37;40mBlock\033[0;37;40m: \033[1;32;40m{}\033[0;37;40m
    \033[1;37;40mVersion\033[0;37;40m: {}

    \u001b[38;5;202mA.\033[0;37;40m Write
    \u001b[38;5;202mB.\033[0;37;40m Read
    \u001b[38;5;202mC.\033[0;37;40m List
    \u001b[31;1mQ.\033[0;37;40m Return
    \n\n\x1b[?25h""".format(n, d['blocks'], version, checkupdate()))
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
    \u001b[31;1mR.\033[0;37;40m Return
    \n\n\x1b[?25h""".format(a, alias['alias'], d['blocks'], version, checkupdate(), lnbitspaid = "UNLOCKED" if os.path.isfile("lnbitSN.conf") else "LOCKED"))
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
        a = os.popen(path['bitcoincli'] + bitcoincli).read()
        b = json.loads(a)
        d = b

        lncli = " getinfo"
        lsd = os.popen(lndconnectload['ln'] + lncli).read()
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
    \033[1;32;40mS.\033[0;37;40m Braiins Pool FREE
    \033[1;32;40mT.\033[0;37;40m TinySeed     FREE
    \033[1;32;40mW.\033[0;37;40m CKPool       FREE
    \u001b[31;1mR.\033[0;37;40m Return
    \n\n\x1b[?25h""".format(n if path['bitcoincli'] else a , alias['alias'], d['blocks'], version, checkupdate(),lnbitspaid = "PAID" if os.path.isfile("lnbitSN.conf") else "PREMIUM", lnpaypaid = "PAID" if os.path.isfile("lnpaySN.conf") else "PREMIUM", opennodepaid = "PAID" if os.path.isfile("opennodeSN.conf") else "PREMIUM"))
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
        a = os.popen(path['bitcoincli'] + bitcoincli).read()
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
    \033[1;32;40mS.\033[0;37;40m Braiins Pool  FREE
    \033[1;32;40mT.\033[0;37;40m TinySeed      FREE
    \033[1;32;40mW.\033[0;37;40m CKPool        FREE
    \u001b[31;1mR.\033[0;37;40m Return
    \n\n\x1b[?25h""".format(n if path['bitcoincli'] else a, d['blocks'], version, checkupdate(),lnbitspaid = "PAID" if os.path.isfile("lnbitSN.conf") else "PREMIUM", lnpaypaid = "PAID" if os.path.isfile("lnpaySN.conf") else "PREMIUM", opennodepaid = "PAID" if os.path.isfile("opennodeSN.conf") else "PREMIUM"))
    platfformsLOCALcontrolOnchainONLY(input("\033[1;32;40mSelect option: \033[0;37;40m"))

def decodeHex():
    clear()
    blogo()
    sysinfo()
    pathexec()
    lndconnectexec()
    n = "Local" if path['bitcoincli'] else "Remote"
    bitcoincli = " getblockchaininfo"
    a = os.popen(path['bitcoincli'] + bitcoincli).read()
    b = json.loads(a)
    d = b

    lncli = " getinfo"
    lsd = os.popen(lndconnectload['ln'] + lncli).read()
    lsd0 = str(lsd)
    alias = json.loads(lsd0)

    print("""\t\t
    \033[1;37;40m{}\033[0;37;40m: \033[1;31;40mPyBLOCK\033[0;37;40m
    \033[1;37;40mNode\033[0;37;40m: \033[1;33;40m{}\033[0;37;40m
    \033[1;37;40mBlock\033[0;37;40m: \033[1;32;40m{}\033[0;37;40m
    \033[1;37;40mVersion\033[0;37;40m: {}

    \u001b[38;5;202mA.\033[0;37;40m Decode Blocks in HEX
    \u001b[38;5;202mB.\033[0;37;40m Decode Transactions in HEX
    \u001b[31;1mQ.\033[0;37;40m Return
    \n\n\x1b[?25h""".format(n, alias['alias'], d['blocks'], version, checkupdate()))
    decodeHexLOCAL(input("\033[1;32;40mSelect option: \033[0;37;40m"))

def decodeHexOnchainONLY():
    clear()
    blogo()
    sysinfo()
    pathexec()
    #lndconnectexec()
    n = "Local" if path['bitcoincli'] else "Remote"
    bitcoincli = " getblockchaininfo"
    a = os.popen(path['bitcoincli'] + bitcoincli).read()
    b = json.loads(a)
    d = b

    print("""\t\t
    \033[1;37;40m{}\033[0;37;40m: \033[1;31;40mPyBLOCK\033[0;37;40m
    \033[1;37;40mBlock\033[0;37;40m: \033[1;32;40m{}\033[0;37;40m
    \033[1;37;40mVersion\033[0;37;40m: {}

    \u001b[38;5;202mA.\033[0;37;40m Decode Blocks in HEX
    \u001b[38;5;202mB.\033[0;37;40m Decode Transactions in HEX
    \u001b[31;1mQ.\033[0;37;40m Return
    \n\n\x1b[?25h""".format(n, d['blocks'], version, checkupdate()))
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
        a = os.popen(path['bitcoincli'] + bitcoincli).read()
        b = json.loads(a)
        d = b

        lncli = " getinfo"
        lsd = os.popen(lndconnectload['ln'] + lncli).read()
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
    \u001b[38;5;202mP.\033[0;37;40m PGP
    \u001b[38;5;202mS.\033[0;37;40m Satoshi Nakamoto
    \u001b[31;1mR.\033[0;37;40m Return
    \n\n\x1b[?25h""".format(n if path['bitcoincli'] else a , alias['alias'], d['blocks'], version, checkupdate()))
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
        a = os.popen(path['bitcoincli'] + bitcoincli).read()
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
    \u001b[38;5;202mP.\033[0;37;40m PGP
    \u001b[38;5;202mS.\033[0;37;40m Satoshi Nakamoto
    \u001b[31;1mR.\033[0;37;40m Return
    \n\n\x1b[?25h""".format(n if path['bitcoincli'] else a, d['blocks'], version, checkupdate()))
    miscellaneousLOCALmenuOnchainONLY(input("\033[1;32;40mSelect option: \033[0;37;40m"))

def slushpoolREMOTEOnchainONLY():
    clear()
    blogo()
    sysinfo()
    pathexec()
    #lndconnectexec()
    if path['bitcoincli']:
        n = "Local" if path['bitcoincli'] else "Remote"
        bitcoincli = " getblockchaininfo"
        a = os.popen(path['bitcoincli'] + bitcoincli).read()
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
    \u001b[38;5;202mB.\033[0;37;40m Hash Rate
    \u001b[38;5;202mC.\033[0;37;40m Pool
    \u001b[38;5;202mD.\033[0;37;40m History
    \u001b[38;5;202mE.\033[0;37;40m Miner
    \u001b[31;1mR.\033[0;37;40m Return
    \n\n\x1b[?25h""".format(n if path['bitcoincli'] else a, d['blocks'], version, checkupdate()))
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
        a = os.popen(path['bitcoincli'] + bitcoincli).read()
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
    \u001b[38;5;202mB.\033[0;37;40m Hash Rate
    \u001b[38;5;202mC.\033[0;37;40m Pool
    \u001b[38;5;202mD.\033[0;37;40m History
    \u001b[38;5;202mE.\033[0;37;40m Miner
    \u001b[31;1mR.\033[0;37;40m Return
    \n\n\x1b[?25h""".format(n if path['bitcoincli'] else a, d['blocks'], version, checkupdate()))
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
        a = os.popen(path['bitcoincli'] + bitcoincli).read()
        b = json.loads(a)
        d = b

        lncli = " getinfo"
        lsd = os.popen(lndconnectload['ln'] + lncli).read()
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
    \u001b[31;1mR.\033[0;37;40m Return
    \n\n\x1b[?25h""".format(n if path['bitcoincli'] else a , alias['alias'], d['blocks'], version, checkupdate()))
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
        a = os.popen(path['bitcoincli'] + bitcoincli).read()
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
    \u001b[31;1mR.\033[0;37;40m Return
    \n\n\x1b[?25h""".format(n if path['bitcoincli'] else a, d['blocks'], version, checkupdate()))
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
        a = os.popen(path['bitcoincli'] + bitcoincli).read()
        b = json.loads(a)
        d = b

        lncli = " getinfo"
        lsd = os.popen(lndconnectload['ln'] + lncli).read()
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
    \u001b[31;1mR.\033[0;37;40m Return
    \n\n\x1b[?25h""".format(n if path['bitcoincli'] else a , alias['alias'], d['blocks'], version, checkupdate()))
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
        a = os.popen(path['bitcoincli'] + bitcoincli).read()
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
    \u001b[31;1mR.\033[0;37;40m Return
    \n\n\x1b[?25h""".format(n if path['bitcoincli'] else a, d['blocks'], version, checkupdate()))
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
        a = os.popen(path['bitcoincli'] + bitcoincli).read()
        b = json.loads(a)
        d = b

        lncli = " getinfo"
        lsd = os.popen(lndconnectload['ln'] + lncli).read()
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
    \u001b[31;1mR.\033[0;37;40m Return
    \n\n\x1b[?25h""".format(n if path['bitcoincli'] else a , alias['alias'], d['blocks'], version, checkupdate()))
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
        a = os.popen(path['bitcoincli'] + bitcoincli).read()
        b = json.loads(a)
        d = b

        lncli = " getinfo"
        lsd = os.popen(lndconnectload['ln'] + lncli).read()
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
    \u001b[31;1mR.\033[0;37;40m Return
    \n\n\x1b[?25h""".format(n if path['bitcoincli'] else a , alias['alias'], d['blocks'], version, checkupdate()))
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
        a = os.popen(path['bitcoincli'] + bitcoincli).read()
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
    \u001b[31;1mR.\033[0;37;40m Return
    \n\n\x1b[?25h""".format(n if path['bitcoincli'] else a, d['blocks'], version, checkupdate()))
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
        a = os.popen(path['bitcoincli'] + bitcoincli).read()
        b = json.loads(a)
        d = b

        lncli = " getinfo"
        lsd = os.popen(lndconnectload['ln'] + lncli).read()
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
    \u001b[31;1mR.\033[0;37;40m Return
    \n\n\x1b[?25h""".format(n if path['bitcoincli'] else a , alias['alias'], d['blocks'], version, checkupdate()))
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
        a = os.popen(path['bitcoincli'] + bitcoincli).read()
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
    \u001b[31;1mR.\033[0;37;40m Return
    \n\n\x1b[?25h""".format(n if path['bitcoincli'] else a, d['blocks'], version, checkupdate()))
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
        a = os.popen(path['bitcoincli'] + bitcoincli).read()
        b = json.loads(a)
        d = b

        lncli = " getinfo"
        lsd = os.popen(lndconnectload['ln'] + lncli).read()
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
    \u001b[31;1mR.\033[0;37;40m Return
    \n\n\x1b[?25h""".format(n if path['bitcoincli'] else a , alias['alias'], d['blocks'], version, checkupdate()))
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
        a = os.popen(path['bitcoincli'] + bitcoincli).read()
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
    \u001b[31;1mR.\033[0;37;40m Return
    \n\n\x1b[?25h""".format(n if path['bitcoincli'] else a, d['blocks'], version, checkupdate()))
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
        a = os.popen(path['bitcoincli'] + bitcoincli).read()
        b = json.loads(a)
        d = b

        lncli = " getinfo"
        lsd = os.popen(lndconnectload['ln'] + lncli).read()
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
    \u001b[31;1mR.\033[0;37;40m Return
    \n\n\x1b[?25h""".format(n if path['bitcoincli'] else a , alias['alias'], d['blocks'], version, checkupdate()))
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
        a = os.popen(path['bitcoincli'] + bitcoincli).read()
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
    \u001b[31;1mR.\033[0;37;40m Return
    \n\n\x1b[?25h""".format(n if path['bitcoincli'] else a, d['blocks'], version, checkupdate()))
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
        a = os.popen(path['bitcoincli'] + bitcoincli).read()
        b = json.loads(a)
        d = b

        lncli = " getinfo"
        lsd = os.popen(lndconnectload['ln'] + lncli).read()
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
    \u001b[31;1mR.\033[0;37;40m Return
    \n\n\x1b[?25h""".format(n if path['bitcoincli'] else a , alias['alias'], d['blocks'], version, checkupdate()))
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
        a = os.popen(path['bitcoincli'] + bitcoincli).read()
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
    \u001b[31;1mR.\033[0;37;40m Return
    \n\n\x1b[?25h""".format(n if path['bitcoincli'] else a, d['blocks'], version, checkupdate()))
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
        a = os.popen(path['bitcoincli'] + bitcoincli).read()
        b = json.loads(a)
        d = b

        lncli = " getinfo"
        lsd = os.popen(lndconnectload['ln'] + lncli).read()
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
    \u001b[31;1mR.\033[0;37;40m Return
    \n\n\x1b[?25h""".format(n if path['bitcoincli'] else a , alias['alias'], d['blocks'], version, checkupdate()))
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
        a = os.popen(path['bitcoincli'] + bitcoincli).read()
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
    \u001b[31;1mR.\033[0;37;40m Return
    \n\n\x1b[?25h""".format(n if path['bitcoincli'] else a, d['blocks'], version, checkupdate()))
    mempoolmenuSOnchainONLY(input("\033[1;32;40mSelect option: \033[0;37;40m"))


def APILnbit():
    bitLN = {"NN":"","pd":""}
    if os.path.isfile('lnbitSN.conf'): # Check if the file 'bclock.conf' is in the same folder
        bitData= pickle.load(open("lnbitSN.conf", "rb")) # Load the file 'bclock.conf'
        bitLN = bitData # Copy the variable pathv to 'path'
    clear()
    blogo()
    sysinfo()
    pathexec()
    lndconnectexec()
    if path['bitcoincli']:
        n = "Local" if path['bitcoincli'] else "Remote"
        bitcoincli = " getblockchaininfo"
        a = os.popen(path['bitcoincli'] + bitcoincli).read()
        b = json.loads(a)
        d = b

        lncli = " getinfo"
        lsd = os.popen(lndconnectload['ln'] + lncli).read()
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
    \u001b[31;1mR.\033[0;37;40m Return
    \n\n\x1b[?25h""".format(n if path['bitcoincli'] else a , alias['alias'], d['blocks'], version, bitLN['NN'], checkupdate()))
    menuLNBPI(input("\033[1;32;40mSelect option: \033[0;37;40m"))

def APILnbitOnchainONLY():
    path = {"ip_port":"", "rpcuser":"", "rpcpass":"", "bitcoincli":""}
    pathv = pickle.load(open("config/bclock.conf", "rb")) # Load the file 'bclock.conf'
    path = pathv # Copy the variable pathv to 'path'
    lndconnectData = pickle.load(open("config/blndconnect.conf", "rb")) # Load the file 'bclock.conf'
    lndconnectload = lndconnectData # Copy the variable pathv to 'path'
    bitLN = {"NN":"","pd":""}
    if os.path.isfile('lnbitSN.conf'): # Check if the file 'bclock.conf' is in the same folder
        bitData= pickle.load(open("lnbitSN.conf", "rb")) # Load the file 'bclock.conf'
        bitLN = bitData # Copy the variable pathv to 'path'
    clear()
    blogo()
    sysinfo()
    pathexec()
    #lndconnectexec()
    if path['bitcoincli']:
        n = "Local" if path['bitcoincli'] else "Remote"
        bitcoincli = " getblockchaininfo"
        a = os.popen(path['bitcoincli'] + bitcoincli).read()
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
    \u001b[31;1mR.\033[0;37;40m Return
    \n\n\x1b[?25h""".format(n if path['bitcoincli'] else a, d['blocks'], version, bitLN['NN'], checkupdate()))
    menuLNBPIOnchainONLY(input("\033[1;32;40mSelect option: \033[0;37;40m"))

def APILnPay():
    bitLN = {"NN":"","pd":""}
    if os.path.isfile('lnpaySN.conf'): # Check if the file 'bclock.conf' is in the same folder
        bitData= pickle.load(open("lnpaySN.conf", "rb")) # Load the file 'bclock.conf'
        bitLN = bitData # Copy the variable pathv to 'path'
    clear()
    blogo()
    sysinfo()
    pathexec()
    lndconnectexec()
    if path['bitcoincli']:
        n = "Local" if path['bitcoincli'] else "Remote"
        bitcoincli = " getblockchaininfo"
        a = os.popen(path['bitcoincli'] + bitcoincli).read()
        b = json.loads(a)
        d = b

        lncli = " getinfo"
        lsd = os.popen(lndconnectload['ln'] + lncli).read()
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
    \u001b[31;1mR.\033[0;37;40m Return
    \n\n\x1b[?25h""".format(n if path['bitcoincli'] else a , alias['alias'], d['blocks'], version, bitLN['NN'], checkupdate()))
    menuLNPAY(input("\033[1;32;40mSelect option: \033[0;37;40m"))

def APILnPayOnchainONLY():
    bitLN = {"NN":"","pd":""}
    if os.path.isfile('lnpaySN.conf'): # Check if the file 'bclock.conf' is in the same folder
        bitData= pickle.load(open("lnpaySN.conf", "rb")) # Load the file 'bclock.conf'
        bitLN = bitData # Copy the variable pathv to 'path'
    clear()
    blogo()
    sysinfo()
    pathexec()
    #lndconnectexec()
    if path['bitcoincli']:
        n = "Local" if path['bitcoincli'] else "Remote"
        bitcoincli = " getblockchaininfo"
        a = os.popen(path['bitcoincli'] + bitcoincli).read()
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
    \u001b[31;1mR.\033[0;37;40m Return
    \n\n\x1b[?25h""".format(n if path['bitcoincli'] else a, d['blocks'], version, bitLN['NN'], checkupdate()))
    menuLNPAYOnchainONLY(input("\033[1;32;40mSelect option: \033[0;37;40m"))

def APIOpenNode():
    bitLN = {"NN":"","pd":""}
    if os.path.isfile('opennodeSN.conf'): # Check if the file 'bclock.conf' is in the same folder
        bitData= pickle.load(open("opennodeSN.conf", "rb")) # Load the file 'bclock.conf'
        bitLN = bitData # Copy the variable pathv to 'path'
    clear()
    blogo()
    sysinfo()
    pathexec()
    lndconnectexec()
    if path['bitcoincli']:
        n = "Local" if path['bitcoincli'] else "Remote"
        bitcoincli = " getblockchaininfo"
        a = os.popen(path['bitcoincli'] + bitcoincli).read()
        b = json.loads(a)
        d = b

        lncli = " getinfo"
        lsd = os.popen(lndconnectload['ln'] + lncli).read()
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
    \u001b[31;1mR.\033[0;37;40m Return
    \n\n\x1b[?25h""".format(n if path['bitcoincli'] else a , alias['alias'], d['blocks'], version, bitLN['NN'], checkupdate()))
    menuOpenNode(input("\033[1;32;40mSelect option: \033[0;37;40m"))

def APIOpenNodeOnchainONLY():
    bitLN = {"NN":"","pd":""}
    if os.path.isfile('opennodeSN.conf'): # Check if the file 'bclock.conf' is in the same folder
        bitData= pickle.load(open("opennodeSN.conf", "rb")) # Load the file 'bclock.conf'
        bitLN = bitData # Copy the variable pathv to 'path'
    clear()
    blogo()
    sysinfo()
    pathexec()
    lndconnectexec()
    if path['bitcoincli']:
        n = "Local" if path['bitcoincli'] else "Remote"
        bitcoincli = " getblockchaininfo"
        a = os.popen(path['bitcoincli'] + bitcoincli).read()
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
    \u001b[31;1mR.\033[0;37;40m Return
    \n\n\x1b[?25h""".format(n if path['bitcoincli'] else a , d['blocks'], version, bitLN['NN'], checkupdate()))
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
        a = os.popen(path['bitcoincli'] + bitcoincli).read()
        b = json.loads(a)
        d = b

        lncli = " getinfo"
        lsd = os.popen(lndconnectload['ln'] + lncli).read()
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
    \u001b[31;1mR.\033[0;37;40m Return
    \n\n\x1b[?25h""".format(n if path['bitcoincli'] else a , alias['alias'], d['blocks'], version, checkupdate()))
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
        a = os.popen(path['bitcoincli'] + bitcoincli).read()
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
    \u001b[31;1mR.\033[0;37;40m Return
    \n\n\x1b[?25h""".format(n if path['bitcoincli'] else a, d['blocks'], version, checkupdate()))
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
        a = os.popen(path['bitcoincli'] + bitcoincli).read()
        b = json.loads(a)
        d = b

        lncli = " getinfo"
        lsd = os.popen(lndconnectload['ln'] + lncli).read()
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
    \u001b[31;1mR.\033[0;37;40m Return
    \n\n\x1b[?25h""".format(n if path['bitcoincli'] else a , alias['alias'], d['blocks'], version, checkupdate()))
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
        a = os.popen(path['bitcoincli'] + bitcoincli).read()
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
    \u001b[31;1mR.\033[0;37;40m Return
    \n\n\x1b[?25h""".format(n if path['bitcoincli'] else a , d['blocks'], version, checkupdate()))
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
    a = os.popen(path['bitcoincli'] + bitcoincli).read()
    b = json.loads(a)
    d = b

    lncli = " getinfo"
    lsd = os.popen(lndconnectload['ln'] + lncli).read()
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
    \u001b[31;1mR.\033[0;37;40m Return
    \n\n\x1b[?25h""".format(n, alias['alias'], d['blocks'], version, checkupdate()))
    menuSettingsLocal(input("\033[1;32;40mSelect option: \033[0;37;40m"))

def settings4LocalOnchainONLY():
    clear()
    blogo()
    sysinfo()
    pathexec()
    #lndconnectexec()
    n = "Local" if path['bitcoincli'] else "Remote"
    bitcoincli = " getblockchaininfo"
    a = os.popen(path['bitcoincli'] + bitcoincli).read()
    b = json.loads(a)
    d = b

    print("""\t\t
    \033[1;37;40m{}\033[0;37;40m: \033[1;31;40mPyBLOCK\033[0;37;40m
    \033[1;37;40mBlock\033[0;37;40m: \033[1;32;40m{}\033[0;37;40m
    \033[1;37;40mVersion\033[0;37;40m: {}

    \u001b[38;5;27mA.\033[0;37;40m Change Logo Design
    \u001b[38;5;27mB.\033[0;37;40m Change Logo Colors
    \u001b[38;5;27mC.\033[0;37;40m Change Clock Colors
    \u001b[31;1mR.\033[0;37;40m Return
    \n\n\x1b[?25h""".format(n, d['blocks'], version, checkupdate()))
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
    \u001b[31;1mR.\033[0;37;40m Return
    \n\n\x1b[?25h""".format(a, alias['alias'], d['blocks'], version, checkupdate()))
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
        a = os.popen(path['bitcoincli'] + bitcoincli).read()
        b = json.loads(a)
        d = b

        lncli = " getinfo"
        lsd = os.popen(lndconnectload['ln'] + lncli).read()
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
    \033[1;36;40mR.\033[0;37;40m Return
    \n\n\x1b[?25h""".format(n if path['bitcoincli'] else a , alias['alias'], d['blocks'], version, checkupdate()))
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
        a = os.popen(path['bitcoincli'] + bitcoincli).read()
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
    \033[1;36;40mR.\033[0;37;40m Return
    \n\n\x1b[?25h""".format(n if path['bitcoincli'] else a, d['blocks'], version, checkupdate()))
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
        a = os.popen(path['bitcoincli'] + bitcoincli).read()
        b = json.loads(a)
        d = b

        lncli = " getinfo"
        lsd = os.popen(lndconnectload['ln'] + lncli).read()
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
    \033[1;36;40mR.\033[0;37;40m Return
    \n\n\x1b[?25h""".format(n if path['bitcoincli'] else a , alias['alias'], d['blocks'], version, checkupdate()))
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
        a = os.popen(path['bitcoincli'] + bitcoincli).read()
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
    \033[1;36;40mR.\033[0;37;40m Return
    \n\n\x1b[?25h""".format(n if path['bitcoincli'] else a, d['blocks'], version, checkupdate()))
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
        a = os.popen(path['bitcoincli'] + bitcoincli).read()
        b = json.loads(a)
        d = b

        lncli = " getinfo"
        lsd = os.popen(lndconnectload['ln'] + lncli).read()
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
    \033[1;36;40mR.\033[0;37;40m Return
    \n\n\x1b[?25h""".format(n if path['bitcoincli'] else a , alias['alias'], d['blocks'], version, checkupdate()))
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
        a = os.popen(path['bitcoincli'] + bitcoincli).read()
        b = json.loads(a)
        d = b

        lncli = " getinfo"
        lsd = os.popen(lndconnectload['ln'] + lncli).read()
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
    \033[1;36;40mR.\033[0;37;40m Return
    \n\n\x1b[?25h""".format(n if path['bitcoincli'] else a , alias['alias'], d['blocks'], version, checkupdate()))
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
        a = os.popen(path['bitcoincli'] + bitcoincli).read()
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
    \033[1;36;40mR.\033[0;37;40m Return
    \n\n\x1b[?25h""".format(n if path['bitcoincli'] else a, d['blocks'], version, checkupdate()))
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
        a = os.popen(path['bitcoincli'] + bitcoincli).read()
        b = json.loads(a)
        d = b

        lncli = " getinfo"
        lsd = os.popen(lndconnectload['ln'] + lncli).read()
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
    \033[1;36;40mR.\033[0;37;40m Return
    \n\n\x1b[?25h""".format(n if path['bitcoincli'] else a , alias['alias'], d['blocks'], version, checkupdate()))
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
        a = os.popen(path['bitcoincli'] + bitcoincli).read()
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
    \033[1;36;40mR.\033[0;37;40m Return
    \n\n\x1b[?25h""".format(n if path['bitcoincli'] else a, d['blocks'], version, checkupdate()))
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
        a = os.popen(path['bitcoincli'] + bitcoincli).read()
        b = json.loads(a)
        d = b

        lncli = " getinfo"
        lsd = os.popen(lndconnectload['ln'] + lncli).read()
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
    \033[1;36;40mR.\033[0;37;40m Return
    \n\n\x1b[?25h""".format(n if path['bitcoincli'] else a , alias['alias'], d['blocks'], version, checkupdate()))
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
        a = os.popen(path['bitcoincli'] + bitcoincli).read()
        b = json.loads(a)
        d = b

        lncli = " getinfo"
        lsd = os.popen(lndconnectload['ln'] + lncli).read()
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
    \033[1;36;40mR.\033[0;37;40m Return
    \n\n\x1b[?25h""".format(n if path['bitcoincli'] else a , alias['alias'], d['blocks'], version, checkupdate()))
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
        a = os.popen(path['bitcoincli'] + bitcoincli).read()
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
    \033[1;36;40mR.\033[0;37;40m Return
    \n\n\x1b[?25h""".format(n if path['bitcoincli'] else a ,d['blocks'], version, checkupdate()))
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
        a = os.popen(path['bitcoincli'] + bitcoincli).read()
        b = json.loads(a)
        d = b

        lncli = " getinfo"
        lsd = os.popen(lndconnectload['ln'] + lncli).read()
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
    \033[1;36;40mR.\033[0;37;40m Return
    \n\n\x1b[?25h""".format(n if path['bitcoincli'] else a , alias['alias'], d['blocks'], version, checkupdate()))
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
        a = os.popen(path['bitcoincli'] + bitcoincli).read()
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
    \033[1;36;40mR.\033[0;37;40m Return
    \n\n\x1b[?25h""".format(n if path['bitcoincli'] else a , d['blocks'], version, checkupdate()))
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
        a = os.popen(path['bitcoincli'] + bitcoincli).read()
        b = json.loads(a)
        d = b

        lncli = " getinfo"
        lsd = os.popen(lndconnectload['ln'] + lncli).read()
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
    \033[1;36;40mR.\033[0;37;40m Return
    \n\n\x1b[?25h""".format(n if path['bitcoincli'] else a , alias['alias'], d['blocks'], version, checkupdate()))
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
        a = os.popen(path['bitcoincli'] + bitcoincli).read()
        b = json.loads(a)
        d = b

        lncli = " getinfo"
        lsd = os.popen(lndconnectload['ln'] + lncli).read()
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
    \033[1;36;40mR.\033[0;37;40m Return
    \n\n\x1b[?25h""".format(n if path['bitcoincli'] else a , alias['alias'], d['blocks'], version, checkupdate()))
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
        a = os.popen(path['bitcoincli'] + bitcoincli).read()
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
    \033[1;36;40mR.\033[0;37;40m Return
    \n\n\x1b[?25h""".format(n if path['bitcoincli'] else a, d['blocks'], version, checkupdate()))
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
        a = os.popen(path['bitcoincli'] + bitcoincli).read()
        b = json.loads(a)
        d = b
        lncli = " getinfo"
        lsd = os.popen(lndconnectload['ln'] + lncli).read()
        lsd0 = str(lsd)
        alias = json.loads(lsd0)

        lncli = " getinfo"
        lsd = os.popen(lndconnectload['ln'] + lncli).read()
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
    \033[1;36;40mR.\033[0;37;40m Return
    \n\n\x1b[?25h""".format(n if path['bitcoincli'] else a , alias['alias'], d['blocks'], version, checkupdate()))
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
        a = os.popen(path['bitcoincli'] + bitcoincli).read()
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
    \033[1;36;40mR.\033[0;37;40m Return
    \n\n\x1b[?25h""".format(n if path['bitcoincli'] else a , d['blocks'], version, checkupdate()))
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
        a = os.popen(path['bitcoincli'] + bitcoincli).read()
        b = json.loads(a)
        d = b

        lncli = " getinfo"
        lsd = os.popen(lndconnectload['ln'] + lncli).read()
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
    \033[1;36;40mR.\033[0;37;40m Return
    \n\n\x1b[?25h""".format(n if path['bitcoincli'] else a , alias['alias'], d['blocks'], version, checkupdate()))
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
        a = os.popen(path['bitcoincli'] + bitcoincli).read()
        b = json.loads(a)
        d = b

        lncli = " getinfo"
        lsd = os.popen(lndconnectload['ln'] + lncli).read()
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
    \033[1;36;40mR.\033[0;37;40m Return
    \n\n\x1b[?25h""".format(n if path['bitcoincli'] else a , alias['alias'], d['blocks'], version, checkupdate()))
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
        a = os.popen(path['bitcoincli'] + bitcoincli).read()
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
    \033[1;36;40mR.\033[0;37;40m Return
    \n\n\x1b[?25h""".format(n if path['bitcoincli'] else a , d['blocks'], version, checkupdate()))
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
        a = os.popen(path['bitcoincli'] + bitcoincli).read()
        b = json.loads(a)
        d = b

        lncli = " getinfo"
        lsd = os.popen(lndconnectload['ln'] + lncli).read()
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
    \033[1;36;40mR.\033[0;37;40m Return
    \n\n\x1b[?25h""".format(n if path['bitcoincli'] else a , alias['alias'], d['blocks'], version, checkupdate()))
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
        a = os.popen(path['bitcoincli'] + bitcoincli).read()
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
    \033[1;36;40mR.\033[0;37;40m Return
    \n\n\x1b[?25h""".format(n if path['bitcoincli'] else a ,  d['blocks'], version, checkupdate()))
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
        a = os.popen(path['bitcoincli'] + bitcoincli).read()
        b = json.loads(a)
        d = b

        lncli = " getinfo"
        lsd = os.popen(lndconnectload['ln'] + lncli).read()
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
    \033[1;36;40mR.\033[0;37;40m Return
    \n\n\x1b[?25h""".format(n if path['bitcoincli'] else a , alias['alias'], d['blocks'], version, checkupdate()))
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
        a = os.popen(path['bitcoincli'] + bitcoincli).read()
        b = json.loads(a)
        d = b

        lncli = " getinfo"
        lsd = os.popen(lndconnectload['ln'] + lncli).read()
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
    \033[1;36;40mR.\033[0;37;40m Return
    \n\n\x1b[?25h""".format(n if path['bitcoincli'] else a , d['blocks'], version, checkupdate()))
    menuColorsSelectRainbowEndOnchainONLY(input("\033[1;32;40mSelect option: \033[0;37;40m"))

def menuSelection():
    chln = {"fullbtclnd":"","fullbtc":"","cropped":""}
    if os.path.isfile('config/intro.conf'):
        chain = pickle.load(open("config/intro.conf", "rb"))
        chln = chain
        print(chln + "\n")
        if chln == "B":
            path = {"ip_port":"", "rpcuser":"", "rpcpass":"", "bitcoincli":""}
            pathv = pickle.load(open("config/bclock.conf", "rb")) # Load the file 'bclock.conf'
            path = pathv # Copy the variable pathv to 'path'
            MainMenuLOCALChainONLY()
        elif chln == "A":
            path = {"ip_port":"", "rpcuser":"", "rpcpass":"", "bitcoincli":""}
            pathv = pickle.load(open("config/bclock.conf", "rb")) # Load the file 'bclock.conf'
            path = pathv # Copy the variable pathv to 'path'
            MainMenuLOCAL()
        elif chln == "C":
            MainMenuCROPPED()
    else:
        if os.path.isfile('config/blndconnect.conf'):
            chln['offchain'] = "offchain"
        else:
            chln['onchain'] = "onchain"

        pickle.dump(chln, open("config/selection.conf", "wb"))


def menuSelectionLN():
    lndconnectload = {"ip_port":"", "tls":"", "macaroon":"", "lncli":""}
    lndconnectData = pickle.load(open("config/blndconnect.conf", "rb")) # Load the file 'bclock.conf'
    lndconnectload = lndconnectData # Copy the variable pathv to 'path'
    if lndconnectload['ln']:
        menuLNDLOCAL()
    else:
        menuLND()

def aaccPPiLNBits():
    try:
        bitLN = {"NN":"","pd":""}
        if os.path.isfile('config/lnbitSN.conf'):
            bitData= pickle.load(open("config/lnbitSN.conf", "rb"))
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
            curl = 'curl -X POST https://lnbits.com/api/v1/payments -d ' + "'{" + """"out": false, "amount": 1000, "memo": "LNBits on PyBLOCK {}" """.format(bitLN['NN']) + "}'" + """ -H "X-Api-Key: 1d646820055e4e2da218e801eaacfc94 " -H "Content-type: application/json" """
            sh = os.popen(curl).read()
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
                checkcurl = 'curl -X GET https://lnbits.com/api/v1/payments/' + dn + """ -H "X-Api-Key: 1d646820055e4e2da218e801eaacfc94" -H "Content-type: application/json" """
                rsh = os.popen(checkcurl).read()
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
                pickle.dump(bitLN, open("config/lnbitSN.conf", "wb"))
                createFileConnLNBits()
                break
    except:
        clear()
        blogo()
        print("\n\tSERIAL NUMBER NOT FOUND\n")
        input("Continue...")

def aaccPPiLNPay():
    try:
        bitLN = {"NN":"","pd":""}
        if os.path.isfile('config/lnpaySN.conf'): # Check if the file 'bclock.conf' is in the same folder
            bitData= pickle.load(open("config/lnpaySN.conf", "rb")) # Load the file 'bclock.conf'
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
            curl = 'curl -X POST https://lnbits.com/api/v1/payments -d ' + "'{" + """"out": false, "amount": 1000, "memo": "LNPay on PyBLOCK {}" """.format(bitLN['NN']) + "}'" + """ -H "X-Api-Key: 1d646820055e4e2da218e801eaacfc94 " -H "Content-type: application/json" """
            sh = os.popen(curl).read()
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
                checkcurl = 'curl -X GET https://lnbits.com/api/v1/payments/' + dn + """ -H "X-Api-Key: 1d646820055e4e2da218e801eaacfc94" -H "Content-type: application/json" """
                rsh = os.popen(checkcurl).read()
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
                pickle.dump(bitLN, open("config/lnpaySN.conf", "wb"))
                createFileConnLNPay()
                break

    except:
        clear()
        blogo()
        print("\n\tSERIAL NUMBER NOT FOUND\n")
        input("Continue...")

def aaccPPiOpenNode():
    try:
        bitLN = {"NN":"","pd":""}
        if os.path.isfile('config/opennodeSN.conf'): # Check if the file 'bclock.conf' is in the same folder
            bitData= pickle.load(open("config/opennodeSN.conf", "rb")) # Load the file 'bclock.conf'
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
            curl = 'curl -X POST https://lnbits.com/api/v1/payments -d ' + "'{" + """"out": false, "amount": 1000, "memo": "OpenNode on PyBLOCK {}" """.format(bitLN['NN']) + "}'" + """ -H "X-Api-Key: 1d646820055e4e2da218e801eaacfc94 " -H "Content-type: application/json" """
            sh = os.popen(curl).read()
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
                checkcurl = 'curl -X GET https://lnbits.com/api/v1/payments/' + dn + """ -H "X-Api-Key: 1d646820055e4e2da218e801eaacfc94" -H "Content-type: application/json" """
                rsh = os.popen(checkcurl).read()
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
                pickle.dump(bitLN, open("config/opennodeSN.conf", "wb"))
                createFileConnOpenNode()
                break

    except:
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

def checkupdate():
    r = requests.get('https://raw.githubusercontent.com/curly60e/pyblock/master/ver.txt')
    r.headers['Content-Type']
    n = r.text
    di = json.loads(n)
    if di['version'] == version:
        q = print(" ")
    else:
        print("\n    ------------------------------------------")
        q = print("    \033[1;31;40mNew version available\033[0;37;40m > Exit and $pip3 install pybitblock -U ")
        print("    ------------------------------------------")

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
        pickle.dump(settings, open("config/pyblocksettings.conf", "wb"))
    except:
        pass

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
        pickle.dump(settings, open("config/pyblocksettings.conf", "wb"))
    except:
        pass

def testClock():
    pathexec()
    #lndconnectexec()
    bitcoinclient = path['bitcoincli'] + " getblockcount"
    block = os.popen(str(bitcoinclient)).read() # 'getblockcount' convert to string
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
        pickle.dump(settingsClock, open("config/pyblocksettingsClock.conf", "wb"))
    except:
        pass

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
    if menuCF in ["A", "a"]:
        clear()
        blogo()
        settings["colorB"] = "black"
        testlogoRB()
    elif menuCF in ["B", "b"]:
        clear()
        blogo()
        settings["colorB"] = "red"
        testlogoRB()
    elif menuCF in ["C", "c"]:
        clear()
        blogo()
        settings["colorB"] = "green"
        testlogoRB()
    elif menuCF in ["D", "d"]:
        clear()
        blogo()
        settings["colorB"] = "yellow"
        testlogo()
    elif menuCF in ["E", "e"]:
        clear()
        blogo()
        settings["colorB"] = "blue"
        testlogoRB()
    elif menuCF in ["F", "f"]:
        clear()
        blogo()
        settings["colorB"] = "magenta"
        testlogoRB()
    elif menuCF in ["G", "g"]:
        clear()
        blogo()
        settings["colorB"] = "cyan"
        testlogoRB()
    elif menuCF in ["H", "h"]:
        clear()
        blogo()
        settings["colorB"] = "white"
        testlogoRB()
    elif menuCF in ["I", "i"]:
        clear()
        blogo()
        settings["colorB"] = "gray"
        testlogoRB()
    elif menuCF in ["R", "r"]:
        colors()

def menuColorsSelectRainbowEndOnchainONLY(menuCF):
    if menuCF in ["A", "a"]:
        clear()
        blogo()
        settings["colorB"] = "black"
        testlogoRB()
    elif menuCF in ["B", "b"]:
        clear()
        blogo()
        settings["colorB"] = "red"
        testlogoRB()
    elif menuCF in ["C", "c"]:
        clear()
        blogo()
        settings["colorB"] = "green"
        testlogoRB()
    elif menuCF in ["D", "d"]:
        clear()
        blogo()
        settings["colorB"] = "yellow"
        testlogo()
    elif menuCF in ["E", "e"]:
        clear()
        blogo()
        settings["colorB"] = "blue"
        testlogoRB()
    elif menuCF in ["F", "f"]:
        clear()
        blogo()
        settings["colorB"] = "magenta"
        testlogoRB()
    elif menuCF in ["G", "g"]:
        clear()
        blogo()
        settings["colorB"] = "cyan"
        testlogoRB()
    elif menuCF in ["H", "h"]:
        clear()
        blogo()
        settings["colorB"] = "white"
        testlogoRB()
    elif menuCF in ["I", "i"]:
        clear()
        blogo()
        settings["colorB"] = "gray"
        testlogoRB()
    elif menuCF in ["R", "r"]:
        colorsOnchainONLY()

def menuColorsSelectRainbowStart(menuCF):
    if menuCF in ["A", "a"]:
        clear()
        blogo()
        settings["colorA"] = "black"
        testlogoRB()
    elif menuCF in ["B", "b"]:
        clear()
        blogo()
        settings["colorA"] = "red"
        testlogoRB()
    elif menuCF in ["C", "c"]:
        clear()
        blogo()
        settings["colorA"] = "green"
        testlogoRB()
    elif menuCF in ["D", "d"]:
        clear()
        blogo()
        settings["colorA"] = "yellow"
        testlogoRB()
    elif menuCF in ["E", "e"]:
        clear()
        blogo()
        settings["colorA"] = "blue"
        testlogoRB()
    elif menuCF in ["F", "f"]:
        clear()
        blogo()
        settings["colorA"] = "magenta"
        testlogoRB()
    elif menuCF in ["G", "g"]:
        clear()
        blogo()
        settings["colorA"] = "cyan"
        testlogoRB()
    elif menuCF in ["H", "h"]:
        clear()
        blogo()
        settings["colorA"] = "white"
        testlogoRB()
    elif menuCF in ["I", "i"]:
        clear()
        blogo()
        settings["colorA"] = "gray"
        testlogoRB()
    elif menuCF in ["R", "r"]:
        colors()

def menuColorsSelectRainbowStartOnchainONLY(menuCF):
    if menuCF in ["A", "a"]:
        clear()
        blogo()
        settings["colorA"] = "black"
        testlogoRB()
    elif menuCF in ["B", "b"]:
        clear()
        blogo()
        settings["colorA"] = "red"
        testlogoRB()
    elif menuCF in ["C", "c"]:
        clear()
        blogo()
        settings["colorA"] = "green"
        testlogoRB()
    elif menuCF in ["D", "d"]:
        clear()
        blogo()
        settings["colorA"] = "yellow"
        testlogoRB()
    elif menuCF in ["E", "e"]:
        clear()
        blogo()
        settings["colorA"] = "blue"
        testlogoRB()
    elif menuCF in ["F", "f"]:
        clear()
        blogo()
        settings["colorA"] = "magenta"
        testlogoRB()
    elif menuCF in ["G", "g"]:
        clear()
        blogo()
        settings["colorA"] = "cyan"
        testlogoRB()
    elif menuCF in ["H", "h"]:
        clear()
        blogo()
        settings["colorA"] = "white"
        testlogoRB()
    elif menuCF in ["I", "i"]:
        clear()
        blogo()
        settings["colorA"] = "gray"
        testlogoRB()
    elif menuCF in ["R", "r"]:
        colorsOnchainONLY()

def menuColorsSelectBack(menuCF):
    if menuCF in ["A", "a"]:
        clear()
        blogo()
        settings["colorB"] = "black"
        testlogo()
    elif menuCF in ["B", "b"]:
        clear()
        blogo()
        settings["colorB"] = "red"
        testlogo()
    elif menuCF in ["C", "c"]:
        clear()
        blogo()
        settings["colorB"] = "green"
        testlogo()
    elif menuCF in ["D", "d"]:
        clear()
        blogo()
        settings["colorB"] = "yellow"
        testlogo()
    elif menuCF in ["E", "e"]:
        clear()
        blogo()
        settings["colorB"] = "blue"
        testlogo()
    elif menuCF in ["F", "f"]:
        clear()
        blogo()
        settings["colorB"] = "magenta"
        testlogo()
    elif menuCF in ["G", "g"]:
        clear()
        blogo()
        settings["colorB"] = "cyan"
        testlogo()
    elif menuCF in ["H", "h"]:
        clear()
        blogo()
        settings["colorB"] = "white"
        testlogo()
    elif menuCF in ["I", "i"]:
        clear()
        blogo()
        settings["colorB"] = "gray"
        testlogo()
    elif menuCF in ["R", "r"]:
        colors()

def menuColorsSelectBackOnchainONLY(menuCF):
    if menuCF in ["A", "a"]:
        clear()
        blogo()
        settings["colorB"] = "black"
        testlogo()
    elif menuCF in ["B", "b"]:
        clear()
        blogo()
        settings["colorB"] = "red"
        testlogo()
    elif menuCF in ["C", "c"]:
        clear()
        blogo()
        settings["colorB"] = "green"
        testlogo()
    elif menuCF in ["D", "d"]:
        clear()
        blogo()
        settings["colorB"] = "yellow"
        testlogo()
    elif menuCF in ["E", "e"]:
        clear()
        blogo()
        settings["colorB"] = "blue"
        testlogo()
    elif menuCF in ["F", "f"]:
        clear()
        blogo()
        settings["colorB"] = "magenta"
        testlogo()
    elif menuCF in ["G", "g"]:
        clear()
        blogo()
        settings["colorB"] = "cyan"
        testlogo()
    elif menuCF in ["H", "h"]:
        clear()
        blogo()
        settings["colorB"] = "white"
        testlogo()
    elif menuCF in ["I", "i"]:
        clear()
        blogo()
        settings["colorB"] = "gray"
        testlogo()
    elif menuCF in ["R", "r"]:
        colorsOnchainONLY()

def menuColorsSelectFront(menuCF):
    if menuCF in ["A", "a"]:
        clear()
        blogo()
        settings["colorA"] = "black"
        testlogo()
    elif menuCF in ["B", "b"]:
        clear()
        blogo()
        settings["colorA"] = "red"
        testlogo()
    elif menuCF in ["C", "c"]:
        clear()
        blogo()
        settings["colorA"] = "green"
        testlogo()
    elif menuCF in ["D", "d"]:
        clear()
        blogo()
        settings["colorA"] = "yellow"
        testlogo()
    elif menuCF in ["E", "e"]:
        clear()
        blogo()
        settings["colorA"] = "blue"
        testlogo()
    elif menuCF in ["F", "f"]:
        clear()
        blogo()
        settings["colorA"] = "magenta"
        testlogo()
    elif menuCF in ["G", "g"]:
        clear()
        blogo()
        settings["colorA"] = "cyan"
        testlogo()
    elif menuCF in ["H", "h"]:
        clear()
        blogo()
        settings["colorA"] = "white"
        testlogo()
    elif menuCF in ["I", "i"]:
        clear()
        blogo()
        settings["colorA"] = "gray"
        testlogo()
    elif menuCF in ["R", "r"]:
        colors()

def menuColorsSelectFrontOncainONLY(menuCF):
    if menuCF in ["A", "a"]:
        clear()
        blogo()
        settings["colorA"] = "black"
        testlogo()
    elif menuCF in ["B", "b"]:
        clear()
        blogo()
        settings["colorA"] = "red"
        testlogo()
    elif menuCF in ["C", "c"]:
        clear()
        blogo()
        settings["colorA"] = "green"
        testlogo()
    elif menuCF in ["D", "d"]:
        clear()
        blogo()
        settings["colorA"] = "yellow"
        testlogo()
    elif menuCF in ["E", "e"]:
        clear()
        blogo()
        settings["colorA"] = "blue"
        testlogo()
    elif menuCF in ["F", "f"]:
        clear()
        blogo()
        settings["colorA"] = "magenta"
        testlogo()
    elif menuCF in ["G", "g"]:
        clear()
        blogo()
        settings["colorA"] = "cyan"
        testlogo()
    elif menuCF in ["H", "h"]:
        clear()
        blogo()
        settings["colorA"] = "white"
        testlogo()
    elif menuCF in ["I", "i"]:
        clear()
        blogo()
        settings["colorA"] = "gray"
        testlogo()
    elif menuCF in ["R", "r"]:
        colorsOnchainONLY()

def menuColorsSelectFrontClock(menuCF):
    if menuCF in ["A", "a"]:
        clear()
        blogo()
        settingsClock["colorA"] = "black"
        testClock()
    elif menuCF in ["B", "b"]:
        clear()
        blogo()
        settingsClock["colorA"] = "red"
        testClock()
    elif menuCF in ["C", "c"]:
        clear()
        blogo()
        settingsClock["colorA"] = "green"
        testClock()
    elif menuCF in ["D", "d"]:
        clear()
        blogo()
        settingsClock["colorA"] = "yellow"
        testClock()
    elif menuCF in ["E", "e"]:
        clear()
        blogo()
        settingsClock["colorA"] = "blue"
        testClock()
    elif menuCF in ["F", "f"]:
        clear()
        blogo()
        settingsClock["colorA"] = "magenta"
        testClock()
    elif menuCF in ["G", "g"]:
        clear()
        blogo()
        settingsClock["colorA"] = "cyan"
        testClock()
    elif menuCF in ["H", "h"]:
        clear()
        blogo()
        settingsClock["colorA"] = "white"
        testClock()
    elif menuCF in ["I", "i"]:
        clear()
        blogo()
        settingsClock["colorA"] = "gray"
        testClock()
    elif menuCF in ["R", "r"]:
        colors()

def menuColorsSelectFrontClockOnchainONLY(menuCF):
    if menuCF in ["A", "a"]:
        clear()
        blogo()
        settingsClock["colorA"] = "black"
        testClock()
    elif menuCF in ["B", "b"]:
        clear()
        blogo()
        settingsClock["colorA"] = "red"
        testClock()
    elif menuCF in ["C", "c"]:
        clear()
        blogo()
        settingsClock["colorA"] = "green"
        testClock()
    elif menuCF in ["D", "d"]:
        clear()
        blogo()
        settingsClock["colorA"] = "yellow"
        testClock()
    elif menuCF in ["E", "e"]:
        clear()
        blogo()
        settingsClock["colorA"] = "blue"
        testClock()
    elif menuCF in ["F", "f"]:
        clear()
        blogo()
        settingsClock["colorA"] = "magenta"
        testClock()
    elif menuCF in ["G", "g"]:
        clear()
        blogo()
        settingsClock["colorA"] = "cyan"
        testClock()
    elif menuCF in ["H", "h"]:
        clear()
        blogo()
        settingsClock["colorA"] = "white"
        testClock()
    elif menuCF in ["I", "i"]:
        clear()
        blogo()
        settingsClock["colorA"] = "gray"
        testClock()
    elif menuCF in ["R", "r"]:
        colorsOnchainONLY()

def menuColorsSelectBackClock(menuCF):
    if menuCF in ["A", "a"]:
        clear()
        blogo()
        settingsClock["colorB"] = "black"
        testClock()
    elif menuCF in ["B", "b"]:
        clear()
        blogo()
        settingsClock["colorB"] = "red"
        testClock()
    elif menuCF in ["C", "c"]:
        clear()
        blogo()
        settingsClock["colorB"] = "green"
        testClock()
    elif menuCF in ["D", "d"]:
        clear()
        blogo()
        settingsClock["colorB"] = "yellow"
        testClock()
    elif menuCF in ["E", "e"]:
        clear()
        blogo()
        settingsClock["colorB"] = "blue"
        testClock()
    elif menuCF in ["F", "f"]:
        clear()
        blogo()
        settingsClock["colorB"] = "magenta"
        testClock()
    elif menuCF in ["G", "g"]:
        clear()
        blogo()
        settingsClock["colorB"] = "cyan"
        testClock()
    elif menuCF in ["H", "h"]:
        clear()
        blogo()
        settingsClock["colorB"] = "white"
        testClock()
    elif menuCF in ["I", "i"]:
        clear()
        blogo()
        settingsClock["colorB"] = "gray"
        testClock()
    elif menuCF in ["R", "r"]:
        colors()

def menuColorsSelectBackClockOnchainONLY(menuCF):
    if menuCF in ["A", "a"]:
        clear()
        blogo()
        settingsClock["colorB"] = "black"
        testClock()
    elif menuCF in ["B", "b"]:
        clear()
        blogo()
        settingsClock["colorB"] = "red"
        testClock()
    elif menuCF in ["C", "c"]:
        clear()
        blogo()
        settingsClock["colorB"] = "green"
        testClock()
    elif menuCF in ["D", "d"]:
        clear()
        blogo()
        settingsClock["colorB"] = "yellow"
        testClock()
    elif menuCF in ["E", "e"]:
        clear()
        blogo()
        settingsClock["colorB"] = "blue"
        testClock()
    elif menuCF in ["F", "f"]:
        clear()
        blogo()
        settingsClock["colorB"] = "magenta"
        testClock()
    elif menuCF in ["G", "g"]:
        clear()
        blogo()
        settingsClock["colorB"] = "cyan"
        testClock()
    elif menuCF in ["H", "h"]:
        clear()
        blogo()
        settingsClock["colorB"] = "white"
        testClock()
    elif menuCF in ["I", "i"]:
        clear()
        blogo()
        settingsClock["colorB"] = "gray"
        testClock()
    elif menuCF in ["R", "r"]:
        colorsOnchainONLY()

def menuColorsSelectFrontClockRemote(menuCF):
    if menuCF in ["A", "a"]:
        clear()
        blogo()
        settingsClock["colorA"] = "black"
        testClockRemote()
    elif menuCF in ["B", "b"]:
        clear()
        blogo()
        settingsClock["colorA"] = "red"
        testClockRemote()
    elif menuCF in ["C", "c"]:
        clear()
        blogo()
        settingsClock["colorA"] = "green"
        testClockRemote()
    elif menuCF in ["D", "d"]:
        clear()
        blogo()
        settingsClock["colorA"] = "yellow"
        testClockRemote()
    elif menuCF in ["E", "e"]:
        clear()
        blogo()
        settingsClock["colorA"] = "blue"
        testClockRemote()
    elif menuCF in ["F", "f"]:
        clear()
        blogo()
        settingsClock["colorA"] = "magenta"
        testClockRemote()
    elif menuCF in ["G", "g"]:
        clear()
        blogo()
        settingsClock["colorA"] = "cyan"
        testClockRemote()
    elif menuCF in ["H", "h"]:
        clear()
        blogo()
        settingsClock["colorA"] = "white"
        testClockRemote()
    elif menuCF in ["I", "i"]:
        clear()
        blogo()
        settingsClock["colorA"] = "gray"
        testClockRemote()
    elif menuCF in ["R", "r"]:
        colors()

def menuColorsSelectBackClockRemote(menuCF):
    if menuCF in ["A", "a"]:
        clear()
        blogo()
        settingsClock["colorB"] = "black"
        testClockRemote()
    elif menuCF in ["B", "b"]:
        clear()
        blogo()
        settingsClock["colorB"] = "red"
        testClockRemote()
    elif menuCF in ["C", "c"]:
        clear()
        blogo()
        settingsClock["colorB"] = "green"
        testClockRemote()
    elif menuCF in ["D", "d"]:
        clear()
        blogo()
        settingsClock["colorB"] = "yellow"
        testClockRemote()
    elif menuCF in ["E", "e"]:
        clear()
        blogo()
        settingsClock["colorB"] = "blue"
        testClockRemote()
    elif menuCF in ["F", "f"]:
        clear()
        blogo()
        settingsClock["colorB"] = "magenta"
        testClockRemote()
    elif menuCF in ["G", "g"]:
        clear()
        blogo()
        settingsClock["colorB"] = "cyan"
        testClockRemote()
    elif menuCF in ["H", "h"]:
        clear()
        blogo()
        settingsClock["colorB"] = "white"
        testClockRemote()
    elif menuCF in ["I", "i"]:
        clear()
        blogo()
        settingsClock["colorB"] = "gray"
        testClockRemote()
    elif menuCF in ["R", "r"]:
        colors()

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

def mempoolmenuS(menuMem):
    if menuMem in ["A", "a"]:
        blocks()
    elif menuMem in ["B", "b"]:
        fee()
    elif menuMem in ["R", "r"]:
        menuSelection()

def mempoolmenuSOnchainONLY(menuMem):
    if menuMem in ["A", "a"]:
        blocks()
    elif menuMem in ["B", "b"]:
        fee()
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

def mainmenuLOCALcontrol(menuS): #Execution of the Main Menu options
    if menuS in ["A", "a"]:
        artist()
    elif menuS in ["B", "b"]:
        bitcoincoremenuLOCAL()
    elif menuS in ["L", "l"]:
        lightningnetworkLOCAL()
    elif menuS in ["S", "s"]:
        settings4Local()
    elif menuS in ["P", "p"]:
        APIMenuLOCAL()
    elif menuS in ["X", "x"]:
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
    elif menuS in ["CA", "ca", "Ca", "cA"]:
        clear()
        blogo()
        callGitCashu()

def mainmenuLOCALcontrolOnchainONLY(menuS): #Execution of the Main Menu options
    if menuS in ["A", "a"]:
        artist()
    elif menuS in ["B", "b"]:
        bitcoincoremenuLOCALOnchainONLY()
    elif menuS in ["S", "s"]:
        settings4LocalOnchainONLY()
    elif menuS in ["P", "p"]:
        APIMenuLOCALOnchainONLY()
    elif menuS in ["X", "x"]:
        dntOnchainONLY()
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
    elif menuS in ["CA", "ca", "Ca", "cA"]:
        clear()
        blogo()
        callGitCashu()

def slushpoolLOCALOnchainONLYMenu(slush):
    if slush in ["A", "a"]:
        clear()
        blogo()
        slDIFFConn()
    elif slush in ["B", "b"]:
        clear()
        blogo()
        slHASHConn()
    elif slush in ["C", "c"]:
        clear()
        blogo()
        slPOOLConn()
    elif slush in ["D", "d"]:
        clear()
        blogo()
        slHISTConn()
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

def bitcoincoremenuLOCALcontrolA(bcore):
    if bcore in ["A", "a"]:
        while True:
            try:
                clear()
                blogo()
                sysinfo()
                close()
                console()
                t.sleep(5)
            except:
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
        runTheNumbersMenu()
    elif bcore in ["E", "e"]:
        decodeHex()
    elif bcore in ["F", "f"]:
        try:
            clear()
            blogo()
            sysinfo()
            close()
            decodeQR()
            input("Continue...")
        except:
            pass
    elif bcore in ["G", "g"]:
        getrawtx()
    elif bcore in ["H", "h"]:
        miscellaneousLOCAL()
    elif bcore in ["I", "i"]:
        callColdCore()
    elif bcore in ["J", "j"]:
        pdfconvert()
    elif bcore in ["M", "m"]:
        mtConn()
    elif bcore in ["O", "o"]:
        bitcoincoremenuLOCALOPRETURN()
    elif bcore in ["Z", "z"]:
        statsConn()
    elif bcore in ["Q", "q"]:
        miningConn()
    elif bcore in ["U", "u"]:
        untxsConn()
    elif bcore in ["Q", "q"]:
        searchTXS()
    elif bcore in ["S", "s"]:
        counttxs()

def bitcoincoremenuLOCALcontrolAOnchainONLY(bcore):
    if bcore in ["A", "a"]:
        while True:
            try:
                clear()
                blogo()
                sysinfo()
                close()
                console()
                t.sleep(5)
            except:
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
        except:
            pass
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
    elif bcore in ["Q", "q"]:
        searchTXS()
    elif bcore in ["S", "s"]:
        counttxs()

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
        opreturnOnchainONLY()
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
            except:
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
    elif misce in ["P", "p"]:
        clear()
        blogo()
        pgpConn()
    elif misce in ["S", "s"]:
        clear()
        blogo()
        satoshiConn()
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
            except:
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
    elif misce in ["P", "p"]:
        clear()
        blogo()
        pgpConn()
    elif misce in ["S", "s"]:
        clear()
        blogo()
        satoshiConn()
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
        except:
            pass
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
        except:
            pass

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
        except:
            pass
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
        except:
            pass

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
            except:
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
    elif platf in ["S", "s"]:
        slushpoolLOCALOnchainONLY()
    elif platf in ["T", "t"]:
        bip39convert()
    elif platf in ["W", "w"]:
        ckpoolpoolLOCALOnchainONLY()
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
    elif platf in ["S", "s"]:
        slushpoolLOCALOnchainONLY()
    elif platf in ["T", "t"]:
        bip39convert()    
    elif platf in ["W", "w"]:
        ckpoolpoolLOCALOnchainONLY()
    elif platf in ["R", "r"]:
        menuSelection()


def ckpool(menuch):
    if menuch in ["A", "a"]:
        ckpool()


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
    if menuS in ["A", "a"]:
        while True:
            try:
                clear()
                close()
                remotegetblock()
                tmp()
            except:
                break
    elif menuS in ["B", "b"]:
        bitcoincoremenuREMOTE()
    elif menuS in ["L", "l"]:
        lightningnetworkREMOTE()
    elif menuS in ["P", "p"]:
        APIMenuLOCAL()
    elif menuS in ["X", "x"]:
        dnt()
    elif menuS in ["S", "s"]:
        settings4Remote()
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
    elif menuS in ["T", "t"]: #Test feature fast access
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
            except:
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
        except:
            pass
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
                except:
                    menuSelection()
            elif message in ["T", "t"]:
                try:
                    clear()
                    blogo()
                    close()
                    apisender()
                    t.sleep(30)
                    menuSelection()
                except:
                    menuSelection()
        except:
            menuSelection()
    elif menuN in ["C", "c"]:
        try:
            print("\n\t This only will work on Linux or Unix systems.\n")
            a = input("Do we continue? Y/n: ")
            if a in ["Y", "y"]:
                gitclone()
            else:
                menuSelection()
        except:
            pass
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
        except:
            menuSelection()
    elif menuQ in ["B", "b"]:
        try:
            clear()
            blogo()
            close()
            donationAddr()
            t.sleep(50)
            menuSelection()
        except:
            menuSelection()
    elif menuQ in ["C", "c"]:
        try:
            clear()
            blogo()
            close()
            donationLN()
            t.sleep(50)
            menuSelection()
        except:
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
        except:
            menuSelection()
    elif menuQ in ["B", "b"]:
        try:
            clear()
            blogo()
            close()
            donationAddr()
            t.sleep(50)
            menuSelection()
        except:
            menuSelection()
    elif menuQ in ["C", "c"]:
        try:
            clear()
            blogo()
            close()
            donationLN()
            t.sleep(50)
            menuSelection()
        except:
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
        except:
            menuSelection()
    elif menuV in ["B", "b"]:
        try:
            clear()
            blogo()
            close()
            donationLNTst()
            t.sleep(50)
            menuSelection()
        except:
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
        except:
            menuSelection()
    elif menuV in ["B", "b"]:
        try:
            clear()
            blogo()
            close()
            donationLNTst()
            t.sleep(50)
            menuSelection()
        except:
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
        a = os.popen(path['bitcoincli'] + bitcoincli).read()
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
    \n\n\x1b[?25h""".format(n if path['bitcoincli'] else a, d['blocks'], version, checkupdate()))
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
        pickle.dump(settingsClock, open("pyblocksettingsClock.conf", "wb"))
    except:
        pass


def commandsINIT(initCONF):
    intCONF = {"fullbtclnd":"","fullbtc":"","cropped":""}

    if not os.path.isdir("config"):
        dir = 'mkdir config'
        os.system(dir)

    if os.path.isfile('config/intro.conf'):
        intro = pickle.load(open("config/intro.conf", "rb"))
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
            pickle.dump(initPATH, open("config/intro.conf", "wb"))
            clear()
            fullbtclnd()
        elif initCONF in ["B", "b"]:
            initDATA = "B"
            intCONF['fullbtc'] = initDATA
            initPATH = intCONF['fullbtc']
            pickle.dump(initPATH, open("config/intro.conf", "wb"))
            clear()
            fullbtc()
        elif initCONF in ["C", "c"]:
            initDATA = "C"
            intCONF['cropped'] = initDATA
            initPATH = intCONF['cropped']
            pickle.dump(initPATH, open("config/intro.conf", "wb"))
            clear()
            menuSelection()

def fullbtc():
    path = {"ip_port":"", "rpcuser":"", "rpcpass":"", "bitcoincli":""}
    if not os.path.isdir("config"):
        dir = 'mkdir config'
        os.system(dir)

    if os.path.isfile('config/bclock.conf') or os.path.isfile('config/blnclock.conf'): # Check if the file 'bclock.conf' is in the same folder
        pathv = pickle.load(open("config/bclock.conf", "rb")) # Load the file 'bclock.conf'
        path = pathv # Copy the variable pathv to 'path'
    else:
        blogo()
        print("Welcome to \033[1;31;40mPyBLOCK\033[0;37;40m\n\n")
        print("\n\tIf you are going to use your local node leave IP:PORT/USER/PASSWORD in blank.\n")
        path['ip_port'] = "http://{}".format(input("Insert IP:PORT to access your remote Bitcoin-Cli node: "))
        path['rpcuser'] = input("RPC User: ")
        path['rpcpass'] = input("RPC Password: ")
        print("\n\tLocal Bitcoin Core Node connection.\n")
        path['bitcoincli']= input("Insert the Path to Bitcoin-Cli: ")
        pickle.dump(path, open("config/bclock.conf", "wb"))
    menuSelection()

def fullbtclnd():
    path = {"ip_port":"", "rpcuser":"", "rpcpass":"", "bitcoincli":""}
    lndconnectload = {"ip_port":"", "tls":"", "macaroon":"", "ln":""}
    if not os.path.isdir("config"):
        dir = 'mkdir config'
        os.system(dir)

    if os.path.isfile('config/bclock.conf') or os.path.isfile('config/blnclock.conf'): # Check if the file 'bclock.conf' is in the same folder
        pathv = pickle.load(open("config/bclock.conf", "rb")) # Load the file 'bclock.conf'
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
        pickle.dump(path, open("config/bclock.conf", "wb"))

    if os.path.isfile('config/blndconnect.conf'): # Check if the file 'bclock.conf' is in the same folder
        lndconnectData= pickle.load(open("config/blndconnect.conf", "rb")) # Load the file 'bclock.conf'
        lndconnectload = lndconnectData # Copy the variable pathv to 'path'
    else:
        clear()
        blogo()
        if os.path.isfile('config/init.conf'):
            pqr = pickle.load(open("config/init.conf", "rb"))
            yesno = pqr
        else:
            yesno = input("Do you want to connect your Lightning Node? yes/no: ")
            pickle.dump(yesno, open("config/init.conf", "wb"))
            if yesno in ["YES", "yes", "yES", "yeS", "Yes", "YEs"]:
                print("\n\tIf you are going to use your local node leave IP:PORT/CERT/MACAROONS in 𝗕𝗟𝗔𝗡𝗞.\n")
                lndconnectload["ip_port"] = input("Insert IP:PORT to your node: ") # path to the bitcoin-cli
                lndconnectload["tls"] = input("Insert the path to tls.cert file: ")
                lndconnectload["macaroon"] = input("Insert the path to admin.macaroon: ")
                print("\n\tLocal Lightning Node connection.\n")
                lndconnectload["ln"] = input("Insert the Path to Lncli. Normally you just need to type 𝙡𝙣𝙘𝙡𝙞: ")
                pickle.dump(lndconnectload, open("config/blndconnect.conf", "wb")) # Save the file 'bclock.conf'
    menuSelection()


def introINIT():
    if not os.path.isdir("config"):
        dir = 'mkdir config'
        os.system(dir)
    clear()
    blogo()
    #sysinfo()
    print("""\t\t
    Welcome 𝓒𝔂𝓹𝓱𝓮𝓻𝓹𝓾𝓷𝓴.

    Connect 𝗣𝘆𝗕𝗟Ø𝗖𝗞 to your Nodes or Run the Cropped option.


    \u001b[31;1mA.\033[0;37;40m 𝗣𝘆𝗕𝗟Ø𝗖𝗞 (Bitcoin & Lightning)
    \u001b[38;5;202mB.\033[0;37;40m 𝗣𝘆𝗕𝗟Ø𝗖𝗞 (Bitcoin)
    \u001b[33;1mC.\033[0;37;40m 𝗣𝘆𝗕𝗟Ø𝗖𝗞 (Cropped)
    \n\n\x1b[?25h""")
    commandsINIT(input("\033[1;32;40mSelect option: \033[0;37;40m"))

#--------------------------------- End Main Menu execution --------------------------------

settings = {"gradient":"", "design":"block", "colorA":"green", "colorB":"yellow"}
settingsClock = {"gradient":"", "colorA":"green", "colorB":"yellow"}
while True: # Loop
    try:
        path = {"ip_port":"", "rpcuser":"", "rpcpass":"", "bitcoincli":""}
        if os.path.isfile('config/bclock.conf') or os.path.isfile('config/blnclock.conf'): # Check if the file 'bclock.conf' is in the same folder
            pathv = pickle.load(open("config/bclock.conf", "rb")) # Load the file 'bclock.conf'
            path = pathv # Copy the variable pathv to 'path'
        if os.path.isfile('config/blndconnect.conf'): # Check if the file 'bclock.conf' is in the same folder
            lndconnectData= pickle.load(open("config/blndconnect.conf", "rb")) # Load the file 'bclock.conf'
            lndconnectload = lndconnectData # Copy the variable pathv to 'path'
        clear()
        if not os.path.isfile('config/intro.conf'):
            introINIT()
        else:
            menuSelection()
    except:
        print("\n")
        sys.exit(101)
