#Developer: Curly60e
#PyBLOCK its a clock of the Bitcoin blockchain.
#Version: 0.5.0

import base64, codecs, json, requests
import pickle
import os
import os.path
import qrcode
import lnpay_py
import simplejson as json
import time as t
from art import *
from pblogo import *
from lnpay_py.wallet import LNPayWallet

def clear(): # clear the screen
    os.system('cls' if os.name=='nt' else 'clear')

#-----------------------------LNBITS--------------------------------

def loadFileConnLNBits(lnbitLoad):
    lnbitLoad = {"wallet_name":"", "wallet_id":"", "admin_key":"", "invoice_read_key":""}

    if os.path.isfile('lnbit.conf'): # Check if the file 'bclock.conf' is in the same folder
        lnbitData= pickle.load(open("lnbit.conf", "rb")) # Load the file 'bclock.conf'
        lnbitLoad = lnbitData # Copy the variable pathv to 'path'
    else:
        clear()
        blogo()
        print("""\n\t   \033[1;33;40mATENTION\033[0;37;40m: YOU ARE GOING TO CREATE A FILE WITH YOUR INFORMATION OF CONNECTION TO LNBITS.COM.
                   WE WILL NEED SOME INFORMATION FROM YOUR ACCOUNT THAT THE ONLY ONE THAT WILL HAVE ACCESS IS YOU.
                          IF YOU DELETE THIS FILE YOU WILL NEED TO PAY AGAIN TO GET ACCESS FROM PyBLOCK.
                                           SAVE THE FILE '\033[1;33;40mlnbitSN.conf\033[0;37;40m' IN A SAFE PLACE.\n
        """)
        lnbitLoad["wallet_name"] = input("Wallet name: ") # path to the bitcoin-cli
        lnbitLoad["wallet_id"] = input("Wallet ID: ")
        lnbitLoad["admin_key"] = input("Admin key: ")
        lnbitLoad["invoice_read_key"] = input("Invoice/read key: ")
        pickle.dump(lnbitLoad, open("lnbit.conf", "wb"))
    return lnbitLoad

def createFileConnLNBits():
    lnbitLoad = {"wallet_name":"", "wallet_id":"", "admin_key":"", "invoice_read_key":""}

    clear()
    blogo()
    print("""\n\t   \033[1;33;40mATENTION\033[0;37;40m: YOU ARE GOING TO CREATE A FILE WITH YOUR INFORMATION OF CONNECTION TO LNBITS.COM.
               WE WILL NEED SOME INFORMATION FROM YOUR ACCOUNT THAT THE ONLY ONE THAT WILL HAVE ACCESS IS YOU.
                      IF YOU DELETE THIS FILE YOU WILL NEED TO PAY AGAIN TO GET ACCESS FROM PyBLOCK.
                                       SAVE THE FILE '\033[1;33;40mlnbitSN.conf\033[0;37;40m' IN A SAFE PLACE.\n
    """)
    lnbitLoad["wallet_name"] = input("Wallet name: ") # path to the bitcoin-cli
    lnbitLoad["wallet_id"] = input("Wallet ID: ")
    lnbitLoad["admin_key"] = input("Admin key: ")
    lnbitLoad["invoice_read_key"] = input("Invoice/read key: ")

    pickle.dump(lnbitLoad, open("lnbit.conf", "wb"))

def lnbitCreateNewInvoice():
    qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
    )
    try:
        amt = input("Amount: ")
        memo = input("Memo: ")
        a = loadFileConnLNBits(['invoice_read_key'])
        b = str(a['invoice_read_key'])
        curl = 'curl -X POST https://lnbits.com/api/v1/payments -d ' + "'{" + """"out": false, "amount": {}, "memo": "{} -PyBLOCK" """.format(amt,memo) + "}'" + """ -H "X-Api-Key: {} " -H "Content-type: application/json" """.format(b)
        sh = os.popen(curl).read()
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
            t.sleep(10)
            dn = str(d['checking_id'])
            checkcurl = 'curl -X GET https://lnbits.com/api/v1/payments/' + dn + """ -H "X-Api-Key: {}" -H "Content-type: application/json" """.format(b)
            rsh = os.popen(checkcurl).read()
            clear()
            blogo()
            nn = str(rsh)
            dd = json.loads(nn)
            db = dd['paid']
            if db == True:
                clear()
                blogo()
                tick()
                t.sleep(2)
                break
            else:
                continue
    except:
        pass


def lnbitPayInvoice():
    bolt = input("Invoice: ")
    a = loadFileConnLNBits(['admin_key'])
    b = str(a['admin_key'])
    curl = 'curl -X POST https://lnbits.com/api/v1/payments -d ' + "'{" + """"out": true, "bolt11": "{}" """.format(bolt) + "}'" + """ -H "X-Api-Key: {}" -H "Content-type: application/json" """.format(b)
    try:
        sh = os.popen(curl).read()
        n = str(sh)
        d = json.loads(n)
        dn = str(d['checking_id'])
        a = loadFileConnLNBits(['invoice_read_key'])
        b = str(a['invoice_read_key'])
        while True:
            checkcurl = 'curl -X GET https://lnbits.com/api/v1/payments/' + dn + """ -H "X-Api-Key: {}" -H "Content-type: application/json" """.format(b)
            rsh = os.popen(checkcurl).read()
            clear()
            blogo()
            nn = str(rsh)
            dd = json.loads(nn)
            db = dd['paid']
            if db == True:
                tick()
                t.sleep(2)
                break
            else:
                continue
    except:
        pass

def lnbitCreatePayWall():
    while True:
        try:
            url = input("Url: ")
            memo = input("Memo: ")
            desc = input("Description: ")
            amt = input("Amount in sats: ")
            remb = input("Remembers Y/n: ")
            a = loadFileConnLNBits(['admin_key'])
            b = str(a['admin_key'])
            if remb == "Y" or remb == "y":
                remember = "true"
            elif remb == "N" or remb == "n":
                remember = "false"
            curl = 'curl -X POST https://lnbits.com/paywall/api/v1/paywalls -d ' + "'{" + """"url": "{}", "memo": "{}", "description": "{}", "amount": {}, "remembers": {} """.format(url,memo,desc,amt,remember) + "}'" + """ -H  "Content-type: application/json" -H "X-Api-Key: {}" """.format(b)
            sh = os.popen(curl).read()
            clear()
            blogo()
            n = str(sh)
            d = json.loads(n)
            print("\n\tPAYWALL CREATED SUCCESSFULLY\n")
            t.sleep(2)
            clear()
            aa = loadFileConnLNBits(['invoice_read_key'])
            bb = str(a['invoice_read_key'])
            checkcurl = 'curl -X GET https://lnbits.com/paywall/api/v1/paywalls -H' + """ "X-Api-Key: {}" """.format(bb)
            sh = os.popen(checkcurl).read()
            clear()
            blogo()
            n = str(sh)
            d = json.loads(n)
            while True:
                for r in range(len(d)):
                    s = d[r]
                    print("ID: " + s['id'])
                nd = input("\nSelect ID: ")
                for r in range(len(d)):
                    s = d[r]
                    nn = s['id']
                    if nd == nn:
                        print("\n----------------------------------------------------------------------------------------------------------------")
                        print("""
                        ID: {}
                        Amount: {} sats
                        Description: {}
                        Memo: {}
                        Extras: {}
                        Remembers: {}
                        URL: {}
                        Wallet: {}
                        """.format(s['id'], s['amount'], s['description'], s['memo'], s['extras'], s['remembers'], s['url'], s['wallet']))
                        print("----------------------------------------------------------------------------------------------------------------\n")
                input("Continue...")
            clear()
            blogo()
        except:
            break

def lnbitListPawWall():
    a = loadFileConnLNBits(['invoice_read_key'])
    b = str(a['invoice_read_key'])
    checkcurl = 'curl -X GET https://lnbits.com/paywall/api/v1/paywalls -H' + """ "X-Api-Key: {}" """.format(b)
    sh = os.popen(checkcurl).read()
    clear()
    blogo()
    n = str(sh)
    d = json.loads(n)
    while True:
        print("\n\tLNBITS PAYWALL LIST\n")
        try:
            for r in range(len(d)):
                s = d[r]
                print("ID: " + s['id'])
            nd = input("\nSelect ID: ")
            for r in range(len(d)):
                s = d[r]
                nn = s['id']
                if nd == nn:
                    print("\n----------------------------------------------------------------------------------------------------------------")
                    print("""
                    ID: {}
                    Amount: {} sats
                    Description: {}
                    Memo: {}
                    Extras: {}
                    Remembers: {}
                    URL: {}
                    Wallet: {}
                    """.format(s['id'], s['amount'], s['description'], s['memo'], s['extras'], s['remembers'], s['url'], s['wallet']))
                    print("----------------------------------------------------------------------------------------------------------------\n")
        except:
            break
        input("Continue...")
        clear()
        blogo()


def lnbitDeletePayWall():
    while True:
        try:
            a = loadFileConnLNBits(['invoice_read_key'])
            b = str(a['invoice_read_key'])
            checkcurl = 'curl -X GET https://lnbits.com/paywall/api/v1/paywalls -H' + """ "X-Api-Key: {}" """.format(b)
            sh = os.popen(checkcurl).read()
            clear()
            blogo()
            n = str(sh)
            d = json.loads(n)
            while True:
                print("\n\tLNBITS PAYWALL LIST\n")
                try:
                    for r in range(len(d)):
                        s = d[r]
                        print("ID: " + s['id'])
                    nd = input("\nSelect ID: ")
                    for r in range(len(d)):
                        s = d[r]
                        nn = s['id']
                        if nd == nn:
                            print("\n----------------------------------------------------------------------------------------------------------------")
                            print("""
                            ID: {}
                            Amount: {} sats
                            Description: {}
                            Memo: {}
                            Extras: {}
                            Remembers: {}
                            URL: {}
                            Wallet: {}
                            """.format(s['id'], s['amount'], s['description'], s['memo'], s['extras'], s['remembers'], s['url'], s['wallet']))
                            print("----------------------------------------------------------------------------------------------------------------\n")
                except:
                    break
                input("Continue...")
                break
            print("\n\tDELETE PAYWALL\n")
            a = loadFileConnLNBits(['admin_key'])
            b = str(a['admin_key'])
            id = input("Insert PayWall ID: ")
            curl = "curl -X DELETE https://lnbits.com/paywall/api/v1/paywalls/{}".format(id) + """ -H "X-Api-Key: {}" """.format(b)
            sh = os.popen(curl).read()
            clear()
            blogo()
            print("\n\tPAYWALL DELETED SUCCESSFULLY\n")
            t.sleep(2)
            clear()
        except:
            break

#-----------------------------END LNBITS--------------------------------

#-----------------------------LNPAY--------------------------------
def loadFileConnLNPay(lnpayLoad):
    lnpayLoad = {"key":""}

    if os.path.isfile('lnpay.conf'): # Check if the file 'bclock.conf' is in the same folder
        lnpayData= pickle.load(open("lnpay.conf", "rb")) # Load the file 'bclock.conf'
        lnpayLoad = lnpayData # Copy the variable pathv to 'path'
    else:
        clear()
        blogo()
        print("""\n\t   \033[1;33;40mATENTION\033[0;37;40m: YOU ARE GOING TO CREATE A FILE WITH YOUR INFORMATION OF CONNECTION TO LNPAY.CO.
                   WE WILL NEED SOME INFORMATION FROM YOUR ACCOUNT THAT THE ONLY ONE THAT WILL HAVE ACCESS IS YOU.
                          IF YOU DELETE THIS FILE YOU WILL NEED TO PAY AGAIN TO GET ACCESS FROM PyBLOCK.
                                           SAVE THE FILE '\033[1;33;40mlnpaySN.conf\033[0;37;40m' IN A SAFE PLACE.\n
        """)
        lnpayLoad["key"] = input("API Key: ")
        print("\n\tWALLET ACCESS KEYS\n")
        lnpayLoad["wallet_key_id"] = input("Wallet Admin: ")
        pickle.dump(lnpayLoad, open("lnpay.conf", "wb"))
    clear()
    blogo()
    return lnpayLoad

def createFileConnLNPay():
    clear()
    blogo()
    print("""\n\t   \033[1;33;40mATENTION\033[0;37;40m: YOU ARE GOING TO CREATE A FILE WITH YOUR INFORMATION OF CONNECTION TO LNPAY.CO.
               WE WILL NEED SOME INFORMATION FROM YOUR ACCOUNT THAT THE ONLY ONE THAT WILL HAVE ACCESS IS YOU.
                      IF YOU DELETE THIS FILE YOU WILL NEED TO PAY AGAIN TO GET ACCESS FROM PyBLOCK.
                                       SAVE THE FILE '\033[1;33;40mlnpaySN.conf\033[0;37;40m' IN A SAFE PLACE.\n
    """)
    lnpayLoad["key"] = input("API Key: ")
    print("\n\tWALLET ACCESS KEYS\n")
    lnpayLoad["wallet_key_id"] = input("Wallet Admin: ")
    pickle.dump(lnpayLoad, open("lnpay.conf", "wb"))


def lnpayGetBalance():
    a = loadFileConnLNPay(['key'])
    b = str(a['key'])
    n = loadFileConnLNPay(['wallet_key_id'])
    q = str(n['wallet_key_id'])
    lnpay_py.initialize(b)
    my_wallet = LNPayWallet(q)
    info = my_wallet.get_info()
    print("\n---------------------------------------------------------------------------------------------------")
    print("""
    Wallet ID: {}
    Wallet Name: {}
    Balance: {} sats
    """.format(info['id'], info['user_label'], info['balance']))
    print("---------------------------------------------------------------------------------------------------\n")
    input("\nContinue... ")

def lnpayCreateInvoice():
    qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
    )
    a = loadFileConnLNPay(['key'])
    b = str(a['key'])
    n = loadFileConnLNPay(['wallet_key_id'])
    q = str(n['wallet_key_id'])
    lnpay_py.initialize(b)

    my_wallet = LNPayWallet(q)
    amt = input("\nAmount in Sats: ")
    memo = input("Memo: ")
    invoice_params = {
        'num_satoshis': amt,
        'memo': memo + ' -PyBLOCK'
    }
    invoice = my_wallet.create_invoice(invoice_params)
    while True:
        print("\033[1;30;47m")
        qr.add_data(invoice['payment_request'])
        qr.print_ascii()
        print("\033[0;37;40m")
        qr.clear()
        print("Lightning Invoice: " + invoice['payment_request'])
        t.sleep(10)
        curl = 'curl -u ' + b + ': https://lnpay.co/v1/lntx/' + invoice['id'] + '?fields=settled,num_satoshis'
        rsh = os.popen(curl).read()
        clear()
        blogo()
        nn = str(rsh)
        dd = json.loads(nn)
        db = dd['settled']
        if db == 1:
            clear()
            blogo()
            tick()
            t.sleep(2)
            break
        else:
            continue


def lnpayGetTransactions():
    qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
    )
    a = loadFileConnLNPay(['key'])
    b = str(a['key'])
    n = loadFileConnLNPay(['wallet_key_id'])
    q = str(n['wallet_key_id'])
    lnpay_py.initialize(b)
    my_wallet = LNPayWallet(q)

    transactions = my_wallet.get_transactions()
    while True:
        try:
            for r in range(len(transactions)):
                s = transactions[r]
                q = s['lnTx']
                print("ID: " + s['id'])
            nd = input("\nSelect ID: ")
            for r in range(len(transactions)):
                s = transactions[r]
                nn = s['id']
                nnn = s['lnTx']
                if nd == nn:
                    print("\n----------------------------------------------------------------------------------------------------")
                    print("""
                    ID: {}
                    Amount: {} sats
                    Memo: {}
                    Invoice: {}
                    RHash: {}
                    """.format(nnn['id'], nnn['num_satoshis'], nnn['memo'], nnn['payment_request'], nnn['r_hash_decoded']))
                    print("----------------------------------------------------------------------------------------------------\n")
                    print("\033[1;30;47m")
                    qr.add_data(nnn['payment_request'])
                    qr.print_ascii()
                    print("\033[0;37;40m")
                    qr.clear()
            input("Continue...")
            clear()
            blogo()
        except:
            break
    clear()
    blogo()

def lnpayPayInvoice():
    a = loadFileConnLNPay(['key'])
    b = str(a['key'])
    n = loadFileConnLNPay(['wallet_key_id'])
    q = str(n['wallet_key_id'])
    lnpay_py.initialize(b)
    my_wallet = LNPayWallet(q)
    try:
        inv = input("\nInvoice: ")
        curl = 'curl -u' + b +': https://lnpay.co/v1/node/default/payments/decodeinvoice?payment_request=' + inv
        clear()
        rsh = os.popen(curl).read()
        nn = str(rsh)
        dd = json.loads(nn)
        clear()
        blogo()
        print("\n----------------------------------------------------------------------------------------------------")
        print("""
        Destination: {}
        Amount: {} sats
        Memo: {}
        Invoice: {}
        """.format(dd['destination'], dd['num_satoshis'], dd['description'], inv))
        print("----------------------------------------------------------------------------------------------------\n")
        print("<<< Cancel Control + C")
        input("\nEnter to Continue... ")
        invoice_params = {
            'payment_request': inv
        }
        pay_result = my_wallet.pay_invoice(invoice_params)
    except:
        pass

def lnpayTransBWallets():
    a = loadFileConnLNPay(['key'])
    b = str(a['key'])
    n = loadFileConnLNPay(['wallet_key_id'])
    q = str(n['wallet_key_id'])
    lnpay_py.initialize(b)
    print("""\n\tTRANSFER BETWEEN WALLETS
    \nCaution: If you Transfer to another of your LNPay wallets
    you will only access to your funds via Web.\n""")
    try:
        wall = input("Wallet destination ID: ")
        amt = input("Amount in Sats: ")
        memo = input("Memo: ")
        my_wallet = LNPayWallet(q)
        transfer_params = {
            'dest_wallet_id': wall,
            'num_satoshis': amt,
            'memo': memo
        }
        transfer_result = my_wallet.internal_transfer(transfer_params)
        p = transfer_result['wtx_transfer_in']
        e = transfer_result['wtx_transfer_out']
        f = e['wal']
        v = p['wal']
        print("\n----------------------------------------------------------------------------------------------------")
        print("""
        ID: {}
        Amount: {} sats
        Memo: {}
        To Wallet: {}
        From Wallet: {}
        """.format(p['id'], p['num_satoshis'], p['user_label'], v['user_label'], f['user_label']))
        print("----------------------------------------------------------------------------------------------------\n")
        input("Continue...")
    except:
        pass


#-----------------------------END LNPAY--------------------------------

#-----------------------------OPENNODE--------------------------------

def loadFileConnOpenNode(lnpayLoad):
    opennodeLoad = {"key":""}

    if os.path.isfile('opennode.conf'): # Check if the file 'bclock.conf' is in the same folder
        opennodeData= pickle.load(open("opennode.conf", "rb")) # Load the file 'bclock.conf'
        opennodeLoad = opennodeData # Copy the variable pathv to 'path'
    else:
        clear()
        blogo()
        print("""\n\t   \033[1;33;40mATENTION\033[0;37;40m: YOU ARE GOING TO CREATE A FILE WITH YOUR INFORMATION OF CONNECTION TO LNPAY.CO.
                   WE WILL NEED SOME INFORMATION FROM YOUR ACCOUNT THAT THE ONLY ONE THAT WILL HAVE ACCESS IS YOU.
                          IF YOU DELETE THIS FILE YOU WILL NEED TO PAY AGAIN TO GET ACCESS FROM PyBLOCK.
                                           SAVE THE FILE '\033[1;33;40mlnpaySN.conf\033[0;37;40m' IN A SAFE PLACE.\n
        """)
        opennodeLoad["key"] = input("API Key: ")
        pickle.dump(opennodeLoad, open("opennode.conf", "wb"))
    clear()
    blogo()
    return opennodeLoad

def createFileConnOpenNode():
    opennodeLoad = {"key":""}

    clear()
    blogo()
    print("""\n\t   \033[1;33;40mATENTION\033[0;37;40m: YOU ARE GOING TO CREATE A FILE WITH YOUR INFORMATION OF CONNECTION TO OPENNODE.COM.
               WE WILL NEED SOME INFORMATION FROM YOUR ACCOUNT THAT THE ONLY ONE THAT WILL HAVE ACCESS IS YOU.
                      IF YOU DELETE THIS FILE YOU WILL NEED TO PAY AGAIN TO GET ACCESS FROM PyBLOCK.
                                       SAVE THE FILE '\033[1;33;40mopennodeSN.conf\033[0;37;40m' IN A SAFE PLACE.\n
    """)
    opennodeLoad["key"] = input("API Key: ")
    pickle.dump(opennodeLoad, open("opennode.conf", "wb"))


def OpenNodelistfunds():
    a = loadFileConnOpenNode(['key'])
    b = str(a['key'])
    curl = "curl https://api.opennode.co/v1/account/balance -H "+ '"Content-Type: application/json" -H "Authorization: {}"'.format(b)
    sh = os.popen(curl).read()
    clear()
    blogo()
    n = str(sh)
    d = json.loads(n)
    r = d['data']
    p = r['balance']
    print("\n----------------------------------------------------------------------------------------------------")
    print("""
    OPENNODE BALANCE

    Amount: {} sats
    Amount: {} USD
    """.format(p['BTC'], p['USD']))
    print("----------------------------------------------------------------------------------------------------\n")
    input("Continue...")

def OpenNodecreatecharge():
    qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
    )
    a = loadFileConnOpenNode(['key'])
    b = str(a['key'])
    fiat = input("Are you going to pay in FIAT? Y/n:")
    if fiat == "Y" or fiat == "y":
        print("\n----------------------------------------------------------------------------------------------------")
        print("""
        FIAT supported on OpenNode:

        AED,AFN,ALL,AMD,ANG,AOA,ARS,AUD,AWG,AZN,BAM,BBD,BDT,BGN,BHD,BIF,BMD,BND,BOB,BRL,BSD,BTN,BWP,
        BYN,BZD,CAD,CDF,CHF,CLF,CLP,CNH,CNY,COP,CRC,CUC,CUP,CVE,CZK,DJF,DKK,DOP,DZD,EGP,ERN,ETB,EUR,
        FJD,FKP,GBP,GEL,GGP,GHS,GIP,GMD,GNF,GTQ,GYD,HKD,HNL,HRK,HTG,HUF,IDR,ILS,IMP,INR,IQD,IRR,ISK,
        JEP,JMD,JOD,JPY,KES,KGS,KHR,KMF,KPW,KRW,KWD,KYD,KZT,LAK,LBP,LKR,LRD,LSL,LYD,MAD,MDL,MGA,MKD,
        MMK,MNT,MOP,MRO,MUR,MVR,MWK,MXN,MYR,MZN,NAD,NGN,NIO,NOK,NPR,NZD,OMR,PAB,PEN,PGK,PHP,PKR,PLN,
        PYG,QAR,RON,RSD,RUB,RWF,SAR,SBD,SCR,SDG,SEK,SGD,SHP,SLL,SOS,SRD,SSP,STD,SVC,SYP,SZL,THB,TJS,
        TMT,TND,TOP,TRY,TTD,TWD,TZS,UAH,UGX,USD,UYU,UZS,VES,VND,VUV,WST,XAF,XAG,XAU,XCD,XDR,XOF,XPD,
        XPF,XPT,YER,ZAR,ZMW,ZWL,USDC.
        """)
        print("\n----------------------------------------------------------------------------------------------------")
        selection = input("Select a FIAT currency: ")
        amt = input("Amount in {}: ".format(selection))
        curl = 'curl https://api.opennode.co/v1/charges -X POST -H ' + '"Authorization: {}"'.format(b) + ' -H "Content-Type: application/json" -d ' + "'{" + '"amount": "{}", "currency": "{}"'.format(amt,selection.upper()) +  "}'"
        sh = os.popen(curl).read()
        clear()
        blogo()
        n = str(sh)
        d = json.loads(n)
        dd = d['data']
        qq = dd['lightning_invoice']
        pp = dd['chain_invoice']
        while True:
            try:
                print("\n----------------------------------------------------------------------------------------------------")
                print("""
                OPENNODE PAYMENT

                Amount: {} {}
                ID: {}
                Status: {}
                Invoice: {}
                Onchain Address: {}
                Amount: {} sats
                """.format(amt, selection.upper(), dd['id'], dd['status'], qq['payreq'], pp['address'], dd['amount']))
                print("----------------------------------------------------------------------------------------------------\n")
                q = qq['payreq']
                p = pp['address']
                pay = input("Invoice or Onchain Address? I/O: ")
                if pay =="I" or pay == "i":
                    print("\033[1;30;47m")
                    qr.add_data(q)
                    qr.print_ascii()
                    print("\033[0;37;40m")
                    qr.clear()
                    print("\nLightning Invoice: " + q)
                elif pay =="O" or pay == "o":
                    print("\033[1;30;47m")
                    qr.add_data(p)
                    qr.print_ascii()
                    print("\033[0;37;40m")
                    qr.clear()
                    print("\nAmount in sats: {} sats".format(dd['amount']))
                    print("\nOnchain Address: " + p)
                input("\nContinue...")
                clear()
                blogo()
            except:
                break
    elif fiat == "N" or fiat == "n":
        amt = input("Amount in sats: ")
        curl = 'curl https://api.opennode.co/v1/charges -X POST -H' + '"Authorization: {}"'.format(b) + ' -H "Content-Type: application/json" -d ' + "'{" + '"amount": "{}", "currency": "BTC"'.format(amt) +  "}'"
        sh = os.popen(curl).read()
        clear()
        blogo()
        n = str(sh)
        d = json.loads(n)
        dd = d['data']
        qq = dd['lightning_invoice']
        pp = dd['chain_invoice']
        while True:
            try:
                print("\n----------------------------------------------------------------------------------------------------")
                print("""
                OPENNODE PAYMENT

                Amount: {} sats
                ID: {}
                Status: {}
                Invoice: {}
                Onchain Address: {}
                Amount: {} sats
                """.format(amt, dd['id'], dd['status'], qq['payreq'], pp['address'], dd['amount']))
                print("----------------------------------------------------------------------------------------------------\n")
                q = qq['payreq']
                p = pp['address']
                pay = input("Invoice or Onchain Address? I/O: ")
                if pay =="I" or pay == "i":
                    print("\033[1;30;47m")
                    qr.add_data(q)
                    qr.print_ascii()
                    print("\033[0;37;40m")
                    qr.clear()
                    print("\nLightning Invoice: " + q)
                elif pay =="O" or pay == "o":
                    print("\033[1;30;47m")
                    qr.add_data(p)
                    qr.print_ascii()
                    print("\033[0;37;40m")
                    qr.clear()
                    print("\nAmount in sats: {} sats".format(dd['amount']))
                    print("\nOnchain Address: " + p)
                input("\nContinue...")
                clear()
                blogo()
            except:
                break


#-----------------------------END OPENNODE--------------------------------
