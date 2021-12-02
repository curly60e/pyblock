#Developer: Curly60e
#PyBLOCK its a clock of the Bitcoin blockchain.


import base64, codecs, json, requests
import pickle
import os
import os.path
import qrcode
import sys
import simplejson as json
import time as t
import numpy as np
from cfonts import render, say
from art import *
from pblogo import *
from PIL import Image
from robohash import Robohash


lndconnectload = {"ip_port":"", "tls":"", "macaroon":"", "ln":""}
settingsClock = {"gradient":"", "design":"", "colorA":"", "colorB":""}

def clear(): # clear the screen
    os.system('cls' if os.name=='nt' else 'clear')
def closed():
    print("<<< Back Control + C.\n\n")

#-------------------------RPC BITCOIN NODE CONNECTION

def rpc(method, params=[]):
    payload = json.dumps({
        "jsonrpc": "2.0",
        "id": "minebet",
        "method": method,
        "params": params
    })
    path = {"ip_port":"", "rpcuser":"", "rpcpass":"", "bitcoincli":""}
    if os.path.isfile('bclock.conf'): # Check if the file 'bclock.conf' is in the same folder
        pathv = pickle.load(open("bclock.conf", "rb")) # Load the file 'bclock.conf'
        path = pathv # Copy the variable pathv to 'path'
    return requests.post(path['ip_port'], auth=(path['rpcuser'], path['rpcpass']), data=payload).json()['result']

def remoteHalving():
    b = rpc('getblockcount')
    c = str(b)
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
    \033[0;37;40m------------------- HALVING HISTORY -------------------

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


def remotegetblock():
    if os.path.isfile('pyblocksettingsClock.conf') or os.path.isfile('pyblocksettingsClock.conf'): # Check if the file 'bclock.conf' is in the same folder
        settingsv = pickle.load(open("pyblocksettingsClock.conf", "rb")) # Load the file 'bclock.conf'
        settingsClock = settingsv # Copy the variable pathv to 'path'
    else:
        settingsClock = {"gradient":"", "design":"block", "colorA":"green", "colorB":"yellow"}
        pickle.dump(settingsClock, open("pyblocksettingsClock.conf", "wb"))
    b = rpc('getblockcount')
    c = str(b)
    a = c
    output = render(str(c), colors=[settingsClock['colorA'], settingsClock['colorB']], align='center')
    print("\x1b[?25l" + output)
    while True:
        x = a
        b = rpc('getblockcount')
        c = str(b)
        if c > a:
            clear()
            closed()
            output = render(str(c), colors=[settingsClock['colorA'], settingsClock['colorB']], align='center')
            print("\a\x1b[?25l" + output)
            a = c

def remotegetblockcount(): # get access to bitcoin-cli with the command getblockcount
    while True:
        try:
            a = rpc('getblockchaininfo')
            d = a
            clear()
            blogo()
            closed()
            print("""
            ----------------------------------------------------------------------------
            \tGET BLOCKCHAIN INFORMATION
            Chain: {}
            Blocks: {}
            Best BlockHash: {}
            Difficulty: {}
            Verification Progress: {}
            Size on Disk: {}
            Pruned: {}
            ----------------------------------------------------------------------------
            """.format(d['chain'], d['blocks'], d['bestblockhash'], d['difficulty'], d['verificationprogress'], d['size_on_disk'], d['pruned']))
            t.sleep(2)
        except:
            break

def remoteconsole(): # get into the console from bitcoin-cli
    print("\t\033[0;37;40mThis is \033[1;33;40mBitcoin-cli's \033[0;37;40mconsole. Type your respective commands you want to display.\n\n")
    while True:
        cle = input("\033[1;32;40mconsole $>: \033[0;37;40m")
        a = rpc(cle)
        print(a)

def runthenumbersConn():
    try:
        b = rpc('gettxoutsetinfo')
        c = str(b)
        print(c)
        input("\nContinue...")
    except:
        pass

#-------------------------END RPC BITCOIN NODE CONNECTION

def consoleLN(): # get into the console from bitcoin-cli
    print("\t\033[0;37;40mThis is \033[1;33;40mLncli's \033[0;37;40mconsole. Type your respective commands you want to display.\n\n")
    while True:
        cle = input("\033[1;32;40mconsole $>: \033[0;37;40m")
        lsd = os.popen(lndconnectload['ln'] + " " + cle)
        lsd0 = lsd.read()
        lsd1 = str(lsd0)
        print(lsd1)
        lsd.close()

def locallistpeersQQ():
    qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
    )
    lncli = " listpeers"
    while True:
        clear()
        print("\033[1;32;40m")
        blogo()
        print("\033[0;37;40m")
        print("<<< Back to the Main Menu Press Control + C.\n\n")
        lsd = os.popen(lndconnectload['ln'] + lncli).read()
        lsd0 = str(lsd)
        d = json.loads(lsd0)
        n = d['peers']
        try:
            print("\n\tLIST PEERS\n")
            for item_ in n:
                s = item_
                hash = s['pub_key']
                rh = Robohash(hash)
                rh.assemble(roboset='set1')
                if not os.path.isfile(str(hash + ".png")):
                    with open(hash +".png", "wb") as f:
                    	rh.img.save(f, format="png")

                    img_path = open(hash +".png", "rb")
                    img = Image.open(img_path)

                    h = 1
                    w = int((img.width / img.height) * 5)

                    img = img.resize((w,h), Image.ANTIALIAS)
                    img_arr = np.asarray(img)
                    h,w,c = img_arr.shape

                img_path = open(hash +".png", "rb")
                img = Image.open(img_path)

                h = 1
                w = int((img.width / img.height) * 5)

                img = img.resize((w,h), Image.ANTIALIAS)
                img_arr = np.asarray(img)
                h,w,c = img_arr.shape

                for x in range(h):
                    for y in range(w):
                        pix = img_arr[x][y]
                        print(get_color(pix[0], pix[1], pix[2]), sep='', end='')
                    print()
                print("PubKey: " + s['pub_key'] + " @" + s['address'])

            nd = input("\nSelect PubKey: ")
            for item in n:
                s = item
                nn = s['pub_key']
                if nd == nn:
                    hash = s['pub_key']
                    rh = Robohash(hash)
                    rh.assemble(roboset='set1')

                    img_path = open(hash +".png", "rb")
                    img = Image.open(img_path)

                    h = 20
                    w = int((img.width / img.height) * 50)

                    img = img.resize((w,h), Image.ANTIALIAS)
                    img_arr = np.asarray(img)
                    h,w,c = img_arr.shape

                    for x in range(h):
                        for y in range(w):
                            pix = img_arr[x][y]
                            print(get_color(pix[0], pix[1], pix[2]), sep='', end='')
                        print()
                    print("\n----------------------------------------------------------------------------------------------------")
                    print("""
                        PEER DECODED\n
                        Bytes Sent: {}
                        Bytes Recv: {}
                        Sat Sent: {} sats
                        Sat Recv: {} sats
                    """.format(s['bytes_sent'], s['bytes_recv'], s['sat_sent'], s['sat_recv']))
                    print("-----------------------------------------------------------------------------------------------------\n")
                    print("\n\tPeer: " + nd)
                    print("\033[1;30;47m")
                    qr.add_data(s['pub_key'])
                    qr.print_ascii()
                    print("\033[0;37;40m")
                    qr.clear()

            pp = input("\nDo you want to disconnect? Y/n: ")
            if pp in ["Y", "y"]:
                lsd = os.popen(lndconnectload['ln'] + " disconnect" + " " + nd).read()
                lsd0 = str(lsd)
                d = json.loads(lsd0)
                print("\n\tDisconnected from peer " + nd)
                input("\nContinue... ")
            elif pp in ["N", "n"]:
                input("\nContinue... ")
        except:
            break

def localconnectpeer():
    try:
        clear()
        print("\033[1;32;40m")
        blogo()
        print("\033[0;37;40m")
        print("<<< Back to the Main Menu Press Control + C.\n\n")
        print("\n\tCONNECT TO NEW PEER\n")
        a = input("Insert PeerID@IP:PORT: ")
        lncli = " connect "
        lsd = os.popen(lndconnectload['ln'] + lncli + a).read()
        lsd0 = str(lsd)
        print(lsd0)
        input("\nContinue... ")
    except:
        pass

def locallistchaintxns():
    qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
    )
    lncli = " listchaintxns"
    lsd = os.popen(lndconnectload['ln'] + lncli).read()
    lsd0 = str(lsd)
    d = json.loads(lsd0)
    n = d['transactions']
    while True:
        clear()
        print("\033[1;32;40m")
        blogo()
        print("\033[0;37;40m")
        print("<<< Back to the Main Menu Press Control + C.\n\n")
        print("\t\nTransactions\n")
        try:
            print("\n\tLIST ONCHAIN TRANSACTIONS\n")
            for item_ in n:
                s = item_

                print("Transaction Hash: " + s['tx_hash'] + " " + s['amount'] + " sats")
            nd = input("\nSelect RHash: ")

            for item in n:
                s = item
                nn = s['tx_hash']
                trx = s['dest_addresses']
                if nd == nn:
                    print("\n----------------------------------------------------------------------------------------------------")
                    print("""
                    \nONCHAIN TRANSACTION DECODED
                    Amount: {} sats
                    Tx Hash: {}
                    Block Hash: {}
                    Block Height: {}
                    Confirmations: {}
                    Destination: {}
                    """.format(s['amount'], s['tx_hash'], s['block_hash'], s['block_height'], s['num_confirmations'], trx))
                    print("-----------------------------------------------------------------------------------------------------\n")
                    print("\nTransaction Hash")
                    print("\033[1;30;47m")
                    qr.add_data(s['tx_hash'])
                    qr.print_ascii()
                    print("\033[0;37;40m")
                    qr.clear()
            input("\nContinue... ")
        except:
            break

def locallistinvoices():
    qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
    )
    lncli = " listinvoices"
    lsd = os.popen(lndconnectload['ln'] + lncli).read()
    lsd0 = str(lsd)
    d = json.loads(lsd0)
    n = d['invoices']
    while True:
        clear()
        print("\033[1;32;40m")
        blogo()
        print("\033[0;37;40m")
        print("<<< Back to the Main Menu Press Control + C.\n\n")
        print("\tInvoices\n")
        try:
            print("\n\tLIST INVOICES\n")
            for item_ in n:
                s = item_

                print("Invoice: " + s['r_hash'] + " " + s['state'])

            nd = input("\nSelect RHash: ")

            for item in n:
                s = item
                nn = s['r_hash']
                if nd == nn:
                    print("\n----------------------------------------------------------------------------------------------------")
                    print("""
                    \nINVOICE DECODED
                    Memo: {}
                    Invoice: {}
                    Amount: {} sats
                    State: {}
                    """.format(s['memo'], s['payment_request'], s['amt_paid_sat'], s['state']))
                    print("----------------------------------------------------------------------------------------------------\n")
                    print("\033[1;30;47m")
                    qr.add_data(s['payment_request'])
                    qr.print_ascii()
                    print("\033[0;37;40m")
                    qr.clear()
            input("\nContinue... ")
        except:
            break

def locallistchannels():
    lncli = " listchannels"
    lsd = os.popen(lndconnectload['ln'] + lncli).read()
    lsd0 = str(lsd)
    d = json.loads(lsd0)
    n = d['channels']
    while True:
        clear()
        print("\033[1;32;40m")
        blogo()
        print("\033[0;37;40m")
        print("<<< Back to the Main Menu Press Control + C.\n\n")
        print("\t\nChannels\n")
        try:
            print("\n\tLIST CHANNELS\n")
            for item_ in n:
                s = item_
                hash = s['remote_pubkey']
                rh = Robohash(hash)
                rh.assemble(roboset='set1')
                if not os.path.isfile(str(hash + ".png")):
                    with open(hash +".png", "wb") as f:
                    	rh.img.save(f, format="png")

                    img_path = open(hash +".png", "rb")
                    img = Image.open(img_path)

                    h = 1
                    w = int((img.width / img.height) * 5)

                    img = img.resize((w,h), Image.ANTIALIAS)
                    img_arr = np.asarray(img)
                    h,w,c = img_arr.shape

                img_path = open(hash +".png", "rb")
                img = Image.open(img_path)

                h = 1
                w = int((img.width / img.height) * 5)

                img = img.resize((w,h), Image.ANTIALIAS)
                img_arr = np.asarray(img)
                h,w,c = img_arr.shape

                for x in range(h):
                    for y in range(w):
                        pix = img_arr[x][y]
                        print(get_color(pix[0], pix[1], pix[2]), sep='', end='')
                    print()
                print("Node ID: " + s['remote_pubkey'])

            nd = input("\nSelect a Node ID: ")
            for item in n:
                s = item
                nn = s['remote_pubkey']
                if nd == nn:
                    hash = s['remote_pubkey']
                    rh = Robohash(hash)
                    rh.assemble(roboset='set1')

                    img_path = open(hash +".png", "rb")
                    img = Image.open(img_path)

                    h = 20
                    w = int((img.width / img.height) * 50)

                    img = img.resize((w,h), Image.ANTIALIAS)
                    img_arr = np.asarray(img)
                    h,w,c = img_arr.shape

                    for x in range(h):
                        for y in range(w):
                            pix = img_arr[x][y]
                            print(get_color(pix[0], pix[1], pix[2]), sep='', end='')
                        print()
                    print("\n----------------------------------------------------------------------------------------------------")
                    print("""
                    \tCHANNEL DECODED
                    Active: {}
                    Node ID: {}
                    Channel Point: {}
                    Channel Capacity: {} sats
                    Local Balance: {} sats
                    Remote Balance: {} sats
                    Total Sent: {} sats
                    Total Received: {} sats
                    """.format(s['active'], s['remote_pubkey'], s['channel_point'], s['capacity'], s['local_balance'], s['remote_balance'], s['total_satoshis_sent'], s['total_satoshis_received']))
                    print("----------------------------------------------------------------------------------------------------\n")

            input("\nContinue... ")
        except:
            break

def localgetinfo():
    qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
    )
    lncli = " getinfo"
    lsd = os.popen(lndconnectload['ln'] + lncli).read()
    lsd0 = str(lsd)
    d = json.loads(lsd0)
    hash = d['identity_pubkey']
    rh = Robohash(hash)
    rh.assemble(roboset='set1')
    if not os.path.isfile(str(hash + ".png")):
        with open(hash +".png", "wb") as f:
        	rh.img.save(f, format="png")

        img_path = open(hash +".png", "rb")
        img = Image.open(img_path)

        h = 20
        w = int((img.width / img.height) * 50)

        img = img.resize((w,h), Image.ANTIALIAS)
        img_arr = np.asarray(img)
        h,w,c = img_arr.shape

    img_path = open(hash +".png", "rb")
    img = Image.open(img_path)

    h = 20
    w = int((img.width / img.height) * 50)

    img = img.resize((w,h), Image.ANTIALIAS)
    img_arr = np.asarray(img)
    h,w,c = img_arr.shape

    for x in range(h):
        for y in range(w):
            pix = img_arr[x][y]
            print(get_color(pix[0], pix[1], pix[2]), sep='', end='')
        print()
    print("\n----------------------------------------------------------------------------------------------------")
    print("""
    \tNODE INFORMATION

    Version: {}
    Node ID: {}
    Alias: {}
    Color: {}
    Pending Channels: {}
    Active Channels: {}
    Inactive Channels: {}
    Peers: {}
    URLS: {}
    """.format(d['version'], d['identity_pubkey'], d['alias'], d['color'], d['num_pending_channels'], d['num_active_channels'], d['num_inactive_channels'], d['num_peers'], d['uris']))
    print("\033[1;30;47m")
    qr.add_data(d['identity_pubkey'])
    qr.print_ascii()
    print("\033[0;37;40m")
    qr.clear()
    print("----------------------------------------------------------------------------------------------------\n")
    input("\nContinue... ")

def localaddinvoice():
    lncli = " addinvoice"
    lsd = os.popen(lndconnectload['ln'] + lncli).read()
    lsd0 = str(lsd)
    d = json.loads(lsd0)
    qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
    )
    try:
        amount = input("Amount in sats: ")
        mem = input("Memo: ")
        memo = mem.replace(" ","_")
        lsd = os.popen(lndconnectload['ln'] + lncli + " --memo {}-PyBLOCK --amt {}".format(memo, amount)).read()
        lsd0 = str(lsd)
        d = json.loads(lsd0)
        print("\033[1;30;47m")
        qr.add_data(d['payment_request'])
        qr.print_ascii()
        print("\033[0;37;40m")
        qr.clear()
        print("Lightning Invoice: " + d['payment_request'])
        b = str(d['payment_request'])
        while True:
            lsd = os.popen(lndconnectload['ln'] + " decodepayreq " + b).read()
            lsd0 = str(lsd)
            d = json.loads(lsd0)
            r = d['payment_hash']
            lsdn = os.popen(lndconnectload['ln'] + " lookupinvoice " + r).read()
            lsdn0 = str(lsdn)
            n = json.loads(lsdn0)
            if n['state'] == 'SETTLED':
                print("\033[1;32;40m")
                clear()
                blogo()
                tick()
                print("\033[0;37;40m")
                t.sleep(2)
                break
            elif n['state'] == 'CANCELED':
                print("\033[1;31;40m")
                clear()
                blogo()
                canceled()
                print("\033[0;37;40m")
                t.sleep(2)
                break
    except:
        pass

def localpayinvoice():
    try:
        invoiceN = input("Insert the invoice to pay: ")
        invoice = invoiceN.lower()
        lncli = " payinvoice "
        lsd = os.popen(lndconnectload['ln'] + " decodepayreq " + invoice).read()
        lsd0 = str(lsd)
        d = json.loads(lsd0)
        if d['num_satoshis'] == "0":
            amt = " --amt "
            amount =  input("Amount in satoshis: ")
            os.system(lndconnectload['ln'] + lncli + invoice + amt + amount)
        else:
            os.system(lndconnectload['ln'] + lncli + invoice )
        t.sleep(2)
    except:
        pass

def localgetnetworkinfo():
    lncli = " getnetworkinfo"
    lsd = os.popen(lndconnectload['ln'] + lncli).read()
    lsd0 = str(lsd)
    d = json.loads(lsd0)
    print("\n----------------------------------------------------------------------------------------------------")
    print("""
    \tLIGHTNING NETWORK INFORMATION
    Numbers of Nodes: {}
    Numbers of Channels: {}
    Total Network Capacity: {} sats
    Average Channel Size: {}
    Minimum Channel Size: {}
    Maximum Channel Size: {}
    Median Channel Size: {} sats
    Zombie channels: {}
    """.format(d['num_nodes'], d['num_channels'], d['total_network_capacity'], d['avg_channel_size'], d['min_channel_size'], d['max_channel_size'], d['median_channel_size_sat'], d['num_zombie_chans']))
    print("----------------------------------------------------------------------------------------------------\n")
    input("\nContinue... ")

def localkeysend():
    try:
        closed()
        print("\n\tYou ar going to send a payment using KeySend - Note: You don't need any invoice, just your peer ID.\n")
        lncli = " sendpayment "
        node = input("Send to NodeID: ")
        amount = input("Amount in sats: ")
        while True:
            if amount in ["", "0"]:
                amount = input("\nAmount in sats: ")
            else:
                break
        os.system(lndconnectload['ln'] + lncli + "--keysend --d=" + node + " --amt=" + amount + " --final_cltv_delta=40")
    except:
        pass

def localchannelbalance():
    lncli = " channelbalance"
    lsd = os.popen(lndconnectload['ln'] + lncli).read()
    lsd0 = str(lsd)
    d = json.loads(lsd0)
    print("""
    ---------------------------------------------------------

    \tLOCAL CHANNEL BALANCE

    Balance: {} sats
    Pending Channels: {} sats

    ---------------------------------------------------------
    """.format(d['balance'], d['pending_open_balance']))
    input("\nContinue... ")

def localnewaddress():
    lncli = " newaddress p2wkh"
    lsd = os.popen(lndconnectload['ln'] + lncli).read()
    lsd0 = str(lsd)
    d = json.loads(lsd0)
    qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
    )
    print("\033[1;30;47m")
    qr.add_data(d['address'])
    qr.print_ascii()
    print("\033[0;37;40m")
    qr.clear()
    print("Bitcoin Address: " + d['address'])
    input("\nContinue... ")

def localbalanceOC():
    lncli = " walletbalance"
    lsd = os.popen(lndconnectload['ln'] + lncli).read()
    lsd0 = str(lsd)
    d = json.loads(lsd0)
    print("\n----------------------------------------------------------------------------------------------------")
    print("\n\tLOCAL ONCHAIN BALANCE\n")
    print("Total Balance: " + d['total_balance'] + " sats")
    print("Confirmed Balance: " + d['confirmed_balance'] + " sats")
    print("Unconfirmed Balance: " + d['unconfirmed_balance'] + " sats")
    print("----------------------------------------------------------------------------------------------------\n")
    input("\nContinue... ")


def localrebalancelnd():
    lncli = " listchannels"
    while True:
        lsd = os.popen(lndconnectload['ln'] + lncli).read()
        lsd0 = str(lsd)
        d = json.loads(lsd0)
        n = d['channels']
        clear()
        print("\033[1;32;40m")
        blogo()
        print("\033[0;37;40m")
        print("<<< Back to the Main Menu Press Control + C.\n\n")
        print("\t\nChannels\n")
        try:
            print("""\n\tLIST CHANNELS TO REBALANCE\n
                                 \t\033[1;32;40mLOCAL\033[0;37;40m BALANCE \t\033[1;31;40mREMOTE\033[0;37;40m BALANCE
            """)

            for item in n:
                s = item
                if int(s['local_balance']) >= int(s['remote_balance']):
                    total = int(s['local_balance']) - int(s['remote_balance'])
                elif int(s['local_balance']) <= int(s['remote_balance']):
                    total = int(s['remote_balance']) - int(s['local_balance'])
                print("Node ID: " + str(s['chan_id']) + "\t\033[1;32;40m " + str(s['local_balance']) + "\033[0;37;40m sats \033[1;31;40m\t" + str(s['remote_balance']) + "\033[0;37;40m sats \033[3;33;40m" + "\tDIFFERENCE: {}\033[0;37;40m sats".format(str(total)) )
            fromnode = input("\nSelect FROM a Node ID : ")
            tonode = input("\nSelect TO a Node ID : ")
            amt = input("\nAmount in sats: ")
            fee = input("\nMax Fee factor in sats: ")
            fromtonode = "python3 rebalance.py -f {} -t {} -a {} --max-fee-factor {}".format(fromnode,tonode,amt,fee)
            os.system(str(fromtonode))
            input("Continue...")
        except:
            break

# Remote connection with rest -------------------------------------

def getnewinvoice():
    cert_path = lndconnectload["tls"]
    macaroon = codecs.encode(open(lndconnectload["macaroon"], 'rb').read(), 'hex')
    headers = {'Grpc-Metadata-macaroon': macaroon}
    qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
    )
    try:
        amount = input("Amount in sats: ")
        memo = input("Memo: ")
        url = 'https://{}/v1/invoices'.format(lndconnectload["ip_port"])
        data = {

            }
        if amount == "":
            r = requests.post(
                    url,
                    headers=headers, verify=cert_path,
                    json={"memo": memo + " -PyBLOCK"},
                )
        else:
            r = requests.post(
                    url,
                    headers=headers, verify=cert_path,
                    json={"value": amount, "memo": memo + " -PyBLOCK"},
                )

        a = r.json()
        print("\033[1;30;47m")
        qr.add_data(a['payment_request'])
        qr.print_ascii()
        print("\033[0;37;40m")
        qr.clear()
        print("Lightning Invoice: " + a['payment_request'])
        b = str(a['payment_request'])
        while True:
            url = 'https://{}/v1/payreq/{}'.format(lndconnectload["ip_port"], b)
            r = requests.get(url, headers=headers, verify=cert_path)
            a = r.json()
            url = 'https://{}/v1/invoice/{}'.format(lndconnectload["ip_port"],a['payment_hash'])
            rr = requests.get(url, headers=headers, verify=cert_path)
            m = rr.json()
            if m['state'] == 'SETTLED':
                print("\033[1;32;40m")
                clear()
                blogo()
                tick()
                print("\033[0;37;40m")
                t.sleep(2)
                break
            elif m['state'] == 'CANCELED':
                print("\033[1;31;40m")
                clear()
                blogo()
                canceled()
                print("\033[0;37;40m")
                t.sleep(2)
                break
    except:
        pass

def payinvoice():
    cert_path = lndconnectload["tls"]
    macaroon = codecs.encode(open(lndconnectload["macaroon"], 'rb').read(), 'hex')
    headers = {'Grpc-Metadata-macaroon': macaroon}
    try:
        while True:
            bolt11N = input("Insert the invoice to pay: ")
            url = 'https://{}/v1/payreq/{}'.format(lndconnectload["ip_port"],bolt11N)
            r = requests.get(url, headers=headers, verify=cert_path)
            s = r.json()
            print("\n----------------------------------------------------------------------------------------------------")
            print("""
            \tINVOICE DECODED
            Destination: {}
            Payment Hash: {}
            Amount: {} sats
            Description: {}
            """.format(s['destination'], s['payment_hash'], s['num_satoshis'], s['description']))
            print("----------------------------------------------------------------------------------------------------\n")
            print("<<< Cancel Control + C")
            input("\nEnter to Continue... ")
            bolt11 = bolt11N.lower()
            r = requests.post(
                url='https://{}/v1/channels/transactions'.format(lndconnectload["ip_port"]), headers=headers, verify=cert_path, json={"payment_request": bolt11}
            )
            try:
                r.json()['error']
                print("\nThe Invoice don't have an amount. Please insert an Invoice with amount. \n")
                continue
            except:
                break
        ok, checking_id, fee_msat, error_message = r.ok, None, 0, None
        r = requests.get(url='https://{}/v1/payreq/{}'.format(lndconnectload["ip_port"],bolt11), headers=headers, verify=cert_path,)
        t.sleep(5)
        if r.ok:
            checking_id = r.json()["payment_hash"]
            print("\033[1;32;40m")
            clear()
            blogo()
            tick()
        else:
            error_message = r.json()["error"]
            print("\033[1;31;40m")
            clear()
            blogo()
            canceled()
        print("\033[0;37;40m")
        t.sleep(2)
    except:
        pass

def getnewaddress():
    cert_path = lndconnectload["tls"]
    macaroon = codecs.encode(open(lndconnectload["macaroon"], 'rb').read(), 'hex')
    headers = {'Grpc-Metadata-macaroon': macaroon}
    qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
    )
    try:
        url = 'https://{}/v1/newaddress'.format(lndconnectload["ip_port"])
        r = requests.get(url, headers=headers, verify=cert_path)
        addr = r.json()
        print("\033[1;30;47m")
        qr.add_data(addr['address'])
        qr.print_ascii()
        print("\033[0;37;40m")
        print("Bitcoin Address: " + addr['address'])
        qr.clear()
        input("\nContinue... ")
    except:
        pass

def listinvoice():
    qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
    )
    cert_path = lndconnectload["tls"]
    macaroon = codecs.encode(open(lndconnectload["macaroon"], 'rb').read(), 'hex')
    headers = {'Grpc-Metadata-macaroon': macaroon}
    url = 'https://{}/v1/invoices'.format(lndconnectload["ip_port"])
    r = requests.get(url, headers=headers, verify=cert_path)
    a = r.json()
    n = a['invoices']
    while True:
        clear()
        print("\033[1;32;40m")
        blogo()
        print("\033[0;37;40m")
        print("<<< Back to the Main Menu Press Control + C.\n\n")
        print("\tInvoices\n")
        try:
            print("\n\tLIST INVOICES\n")
            for r in range(len(n)):
                s = n[r]
                print("Invoice: " + s['r_hash'] + " " + s['state'])

            nd = input("\nSelect RHash: ")
            for item in n:
                s = item
                nn = s['r_hash']
                if nd == nn:
                    print("\n----------------------------------------------------------------------------------------------------")
                    print("""
                    \tINVOICE DECODED
                    Memo: {}
                    Invoice: {}
                    Amount: {} sats
                    State: {}
                    """.format(s['memo'], s['payment_request'], s['amt_paid_sat'], s['state']))
                    print("----------------------------------------------------------------------------------------------------\n")
                    print("\033[1;30;47m")
                    qr.add_data(s['payment_request'])
                    qr.print_ascii()
                    print("\033[0;37;40m")
                    qr.clear()
            input("\nContinue... ")
        except:
            break
    input("\nContinue... ")

def getinfo():
    qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
    )
    cert_path = lndconnectload["tls"]
    macaroon = codecs.encode(open(lndconnectload["macaroon"], 'rb').read(), 'hex')
    headers = {'Grpc-Metadata-macaroon': macaroon}
    url = 'https://{}/v1/getinfo'.format(lndconnectload["ip_port"])
    r = requests.get(url, headers=headers, verify=cert_path)
    a = r.json()
    hash = a['identity_pubkey']
    rh = Robohash(hash)
    rh.assemble(roboset='set1')
    if not os.path.isfile(str(hash + ".png")):
        with open(hash +".png", "wb") as f:
        	rh.img.save(f, format="png")

        img_path = open(hash +".png", "rb")
        img = Image.open(img_path)

        h = 20
        w = int((img.width / img.height) * 50)

        img = img.resize((w,h), Image.ANTIALIAS)
        img_arr = np.asarray(img)
        h,w,c = img_arr.shape

    img_path = open(hash +".png", "rb")
    img = Image.open(img_path)

    h = 20
    w = int((img.width / img.height) * 50)

    img = img.resize((w,h), Image.ANTIALIAS)
    img_arr = np.asarray(img)
    h,w,c = img_arr.shape

    for x in range(h):
        for y in range(w):
            pix = img_arr[x][y]
            print(get_color(pix[0], pix[1], pix[2]), sep='', end='')
        print()
    print("\n----------------------------------------------------------------------------------------------------")
    print("""
    \t NODE INFORMATION
    Version: {}
    Node ID: {}
    Alias: {}
    Color: {}
    Pending Channels: {}
    Active Channels: {}
    Inactive Channels: {}
    Peers: {}
    URLS: {}
    """.format(a['version'], a['identity_pubkey'], a['alias'], a['color'], a['num_pending_channels'], a['num_active_channels'], a['num_inactive_channels'], a['num_peers'], a['uris']))
    print("\033[1;30;47m")
    qr.add_data(a['identity_pubkey'])
    qr.print_ascii()
    print("\033[0;37;40m")
    qr.clear()
    print("----------------------------------------------------------------------------------------------------\n")
    input("\nContinue... ")

#--------------------------------- NYMs -----------------------------------

def get_ansi_color_code(r, g, b):
    if r == g and g == b:
        if r < 8:
            return 16
        if r > 248:
            return 231
        return round(((r - 8) / 247) * 24) + 232
    return 16 + (36 * round(r / 255 * 5)) + (6 * round(g / 255 * 5)) + round(b / 255 * 5)


def get_color(r, g, b):
    return "\x1b[48;5;{}m \x1b[0m".format(int(get_ansi_color_code(r,g,b)))

def channels():
    cert_path = lndconnectload["tls"]
    macaroon = codecs.encode(open(lndconnectload["macaroon"], 'rb').read(), 'hex')
    headers = {'Grpc-Metadata-macaroon': macaroon}
    url = 'https://{}/v1/channels'.format(lndconnectload["ip_port"])
    r = requests.get(url, headers=headers, verify=cert_path)
    a = r.json()
    n = a['channels']
    while True:
        clear()
        print("\033[1;32;40m")
        blogo()
        print("\033[0;37;40m")
        print("<<< Back to the Main Menu Press Control + C.\n\n")
        print("\t\nChannels\n")
        try:
            print("\n\tLIST CHANNELS\n")
            for r in range(len(n)):
                s = n[r]
                hash = s['remote_pubkey']
                rh = Robohash(hash)
                rh.assemble(roboset='set1')
                if not os.path.isfile(str(hash + ".png")):
                    with open(hash +".png", "wb") as f:
                    	rh.img.save(f, format="png")

                    img_path = open(hash +".png", "rb")
                    img = Image.open(img_path)

                    h = 1
                    w = int((img.width / img.height) * 5)

                    img = img.resize((w,h), Image.ANTIALIAS)
                    img_arr = np.asarray(img)
                    h,w,c = img_arr.shape

                img_path = open(hash +".png", "rb")
                img = Image.open(img_path)

                h = 1
                w = int((img.width / img.height) * 5)

                img = img.resize((w,h), Image.ANTIALIAS)
                img_arr = np.asarray(img)
                h,w,c = img_arr.shape

                for x in range(h):
                    for y in range(w):
                        pix = img_arr[x][y]
                        print(get_color(pix[0], pix[1], pix[2]), sep='', end='')
                    print()
                print("Node ID: " + s['remote_pubkey'])

            nd = input("\nSelect a Node ID: ")
            for item in n:
                s = item
                nn = s['remote_pubkey']
                if nd == nn:
                    hash = s['remote_pubkey']
                    rh = Robohash(hash)
                    rh.assemble(roboset='set1')

                    img_path = open(hash +".png" , "rb")
                    img = Image.open(img_path)

                    h = 20
                    w = int((img.width / img.height) * 50)

                    img = img.resize((w,h), Image.ANTIALIAS)
                    img_arr = np.asarray(img)
                    h,w,c = img_arr.shape

                    for x in range(h):
                        for y in range(w):
                            pix = img_arr[x][y]
                            print(get_color(pix[0], pix[1], pix[2]), sep='', end='')
                        print()
                    print("\n----------------------------------------------------------------------------------------------------")
                    print("""
                    \tCHANNEL DECODED
                    Active: {}
                    Node ID: {}
                    Channel Point: {}
                    Channel Capacity: {} sats
                    Local Balance: {} sats
                    Remote Balance: {} sats
                    Total Sent: {} sats
                    Total Received: {} sats
                    """.format(s['active'], s['remote_pubkey'], s['channel_point'], s['capacity'], s['local_balance'], s['remote_balance'], s['total_satoshis_sent'], s['total_satoshis_received']))
                    print("----------------------------------------------------------------------------------------------------\n")

            input("\nContinue... ")
        except:
            break

def channelbalance():
    cert_path = lndconnectload["tls"]
    macaroon = codecs.encode(open(lndconnectload["macaroon"], 'rb').read(), 'hex')
    headers = {'Grpc-Metadata-macaroon': macaroon}
    url = 'https://{}/v1/balance/channels'.format(lndconnectload["ip_port"])
    r = requests.get(url, headers=headers, verify=cert_path)
    a = r.json()
    print("""
    ---------------------------------------------------------

    \tLOCAL CHANNEL BALANCE

    Balance: {} sats
    Pending Channels: {} sats

    ---------------------------------------------------------
    """.format(a['balance'], a['pending_open_balance']))
    input("\nContinue... ")

def listonchaintxs():
    qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
    )
    cert_path = lndconnectload["tls"]
    macaroon = codecs.encode(open(lndconnectload["macaroon"], 'rb').read(), 'hex')
    headers = {'Grpc-Metadata-macaroon': macaroon}
    url = 'https://{}/v1/transactions'.format(lndconnectload["ip_port"])
    r = requests.get(url, headers=headers, verify=cert_path)
    a = r.json()
    n = a['transactions']
    while True:
        clear()
        print("\033[1;32;40m")
        blogo()
        print("\033[0;37;40m")
        print("<<< Back to the Main Menu Press Control + C.\n\n")
        print("\t\nTransactions\n")
        try:
            print("\n\tLIST ONCHAIN TRANSACTIONS\n")
            for r in range(len(n)):
                s = n[r]
                print("Transaction Hash: " + " " + s['tx_hash'] + " sats")
            nd = input("\nSelect RHash: ")

            for item in n:
                s = item
                nn = s['tx_hash']
                trx = s['dest_addresses']
                if nd == nn:
                    print("\n----------------------------------------------------------------------------------------------------")
                    print("""
                    \tONCHAIN TRANSACTION DECODED
                    Amount: {} sats
                    Tx Hash: {}
                    Block Hash: {}
                    Block Height: {}
                    Confirmations: {}
                    Destination: {}
                    """.format(s['amount'], s['tx_hash'], s['block_hash'], s['block_height'], s['num_confirmations'], trx))
                    print("----------------------------------------------------------------------------------------------------\n")
                    print("\nTransaction Hash")
                    print("\033[1;30;47m")
                    qr.add_data(s['tx_hash'])
                    qr.print_ascii()
                    print("\033[0;37;40m")
                    qr.clear()
            input("\nContinue... ")
        except:
            break

def balanceOC():
    cert_path = lndconnectload["tls"]
    macaroon = codecs.encode(open(lndconnectload["macaroon"], 'rb').read(), 'hex')
    headers = {'Grpc-Metadata-macaroon': macaroon}
    url = 'https://{}/v1/balance/blockchain'.format(lndconnectload["ip_port"])
    r = requests.get(url, headers=headers, verify=cert_path)
    a = r.json()
    print("\n----------------------------------------------------------------------------------------------------")
    print("\n\tLOCAL ONCHAIN BALANCE\n")
    print("Total Balance: " + a['total_balance'] + " sats")
    print("Confirmed Balance: " + a['confirmed_balance'] + " sats")
    print("Unconfirmed Balance: " + a['unconfirmed_balance'] + " sats")
    print("----------------------------------------------------------------------------------------------------\n")
    input("\nContinue... ")

# END Remote connection with rest -------------------------------------
#---------------------------------OPENDIME-----------------------------

def ADDRbalance():
    import os, sys; sys.path.insert(0, os.path.normpath(__file__ + '/support/pycode.zip'))
    import support.pycode.od_wallet; support.pycode.od_wallet.main()
