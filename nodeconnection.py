#Developer: Curly60e
#PyBLOCK its a clock of the Bitcoin blockchain.
#Version: 0.5.0

import base64, codecs, json, requests
import pickle
import os
import os.path
import qrcode
import simplejson as json
import time as t
from art import *
from pblogo import *

lndconnectload = {"ip_port":"", "tls":"", "macaroon":"", "ln":""}

def clear(): # clear the screen
    os.system('cls' if os.name=='nt' else 'clear')

if os.path.isfile('blndconnect.conf'): # Check if the file 'bclock.conf' is in the same folder
    lndconnectData= pickle.load(open("blndconnect.conf", "rb")) # Load the file 'bclock.conf'
    lndconnectload = lndconnectData # Copy the variable pathv to 'path'
else:
    clear()
    blogo()
    print("\n\tIf you are going to use your local node leave IP:PORT/CERT/MACAROONS in blank.\n")
    lndconnectload["ip_port"] = input("Insert IP:PORT to your node: ") # path to the bitcoin-cli
    lndconnectload["tls"] = input("Insert the path to tls.cert file: ")
    lndconnectload["macaroon"] = input("Insert the path to admin.macaroon: ")
    print("\n\tLocal Lightning Node connection.\n")
    lndconnectload["ln"] = input("Insert the path to lncli: ")
    pickle.dump(lndconnectload, open("blndconnect.conf", "wb")) # Save the file 'bclock.conf'

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

def remotegetblock():
    try:
        b = rpc('getblockcount')
        c = str(b)
        print("\033[1;32;40m")
        tprint(c, font="rnd-large")
        print("\033[0;37;40m")
    except:
        pass

def remotegetblockcount(): # get access to bitcoin-cli with the command getblockcount
    try:
        a = rpc('getblockchaininfo')
        d = a
        print(d)
        clear()
        print("\033[1;32;40m")
        blogo()
        print("\033[0;37;40m")
        print("<<< Back to the Main Menu Press Control + C.\n\n")
        print("\n----------------------------------------------------------------------------------------------------")
        print("""
        \tGET BLOCKCHAIN INFORMATION
        Chain: {}
        Blocks: {}
        Best BlockHash: {}
        Difficulty: {}
        Verification Progress: {}
        Size on Disk: {}
        Pruned: {}
        """.format(d['chain'], d['blocks'], d['bestblockhash'], d['difficulty'], d['verificationprogress'], d['size_on_disk'], d['pruned']))
        print("----------------------------------------------------------------------------------------------------\n")
    except:
        pass

def remoteconsole(): # get into the console from bitcoin-cli
    print("\t\033[0;37;40mThis is \033[1;33;40mBitcoin-cli's \033[0;37;40mconsole. Type your respective commands you want to display.\n\n")
    while True:
        cle = input("\033[1;32;40mconsole $>: \033[0;37;40m")
        a = rpc(cle)
        print(a)

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

                print("Transaction Hash: " + s['tx_hash'])
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
                print("Node ID: " + s['remote_pubkey'])

            nd = input("\nSelect a Node ID: ")
            for item in n:
                s = item
                nn = s['remote_pubkey']
                if nd == nn:
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
    lncli = " getinfo"
    lsd = os.popen(lndconnectload['ln'] + lncli).read()
    lsd0 = str(lsd)
    d = json.loads(lsd0)
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
        print("\n\tYou ar going to send a payment using KeySend - Note: You don't need any invoice, just your peer ID.")
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
    print("\n----------------------------------------------------------------------------------------------------")
    print("""
    \tLOCAL CHANNEL BALANCE
    Balance: {} sats
    Pending Channels: {} sats
    """.format(d['balance'], d['pending_open_balance']))
    print("----------------------------------------------------------------------------------------------------\n")
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
    try:
        cert_path = lndconnectload["tls"]
        macaroon = codecs.encode(open(lndconnectload["macaroon"], 'rb').read(), 'hex')
        headers = {'Grpc-Metadata-macaroon': macaroon}
        url = 'https://{}/v1/getinfo'.format(lndconnectload["ip_port"])
        r = requests.get(url, headers=headers, verify=cert_path)
        a = r.json()
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
        print("----------------------------------------------------------------------------------------------------\n")
        input("\nContinue... ")
    except:
        pass

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
                print("Node ID: " + s['remote_pubkey'])

            nd = input("\nSelect a Node ID: ")
            for item in n:
                s = item
                nn = s['remote_pubkey']
                if nd == nn:
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
    print("\n----------------------------------------------------------------------------------------------------")
    print("""
    \tLOCAL CHANNEL BALANCE
    Balance: {} sats
    Pending Channels: {} sats
    """.format(a['balance'], a['pending_open_balance']))
    print("----------------------------------------------------------------------------------------------------\n")
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
                print("Transaction Hash: " + s['tx_hash'])
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
