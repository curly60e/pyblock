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

def clear(): # clear the screen
    os.system('cls' if os.name=='nt' else 'clear')

#-----------------------------LNBITS--------------------------------

def loadFileConnLNBits(lnbitLoad):
    lnbitLoad = {"wallet_name":"", "wallet_id":"", "admin_key":"", "invoice_read_key":""}

    if os.path.isfile('lnbit.conf'): # Check if the file 'bclock.conf' is in the same folder
        lnbitData= pickle.load(open("lnbit.conf", "rb")) # Load the file 'bclock.conf'
        lnbitLoad = lnbitData # Copy the variable pathv to 'path'
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
        curl = 'curl -X POST https://lnbits.com/api/v1/payments -d ' + "'{" + """"out": false, "amount": {}, "memo": "{}" """.format(amt,memo) + "}'" + """ -H "X-Api-Key: {} " -H "Content-type: application/json" """.format(b)
        sh = os.popen(curl).read()
        n = str(sh)
        d = json.loads(n)
        q = d['payment_request']
        c = q.lower()
        print("\033[1;30;47m")
        qr.add_data(c)
        qr.print_ascii()
        print("\033[0;37;40m")
        print("Lightning Invoice: " + c)
        dn = str(d['checking_id'])
        t.sleep(20)
        while True:
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
    return lnpayLoad

def createFileConnLNPay():
    lnpayLoad = {"key":""}

    clear()
    blogo()
    print("""\n\t   \033[1;33;40mATENTION\033[0;37;40m: YOU ARE GOING TO CREATE A FILE WITH YOUR INFORMATION OF CONNECTION TO LNPAY.CO.
               WE WILL NEED SOME INFORMATION FROM YOUR ACCOUNT THAT THE ONLY ONE THAT WILL HAVE ACCESS IS YOU.
                      IF YOU DELETE THIS FILE YOU WILL NEED TO PAY AGAIN TO GET ACCESS FROM PyBLOCK.
                                       SAVE THE FILE '\033[1;33;40mlnpaySN.conf\033[0;37;40m' IN A SAFE PLACE.\n
    """)
    lnpayLoad["key"] = input("API Key: ")
    pickle.dump(lnpayLoad, open("lnpay.conf", "wb"))

def lnpayCreatNewWallet():
    a = loadFileConnLNPay(['key'])
    b = str(a['key'])
    lnpay_py.initialize(b)

    wallet_params = {
        'user_label': 'My wallet'
    }
    new_wallet = lnpay_py.create_wallet(wallet_params)
    print(new_wallet)

def lnpayGetBalance():
    a = loadFileConnLNPay(['key'])
    b = str(a['key'])
    lnpay_py.initialize(b)
    LNPayWallet = 'waka_bWJX7bbs95C13ER1KLZQGGAb'
    my_wallet = LNPayWallet

    info = my_wallet.get_info()
    print(info)

lnpayGetBalance()
#-----------------------------END LNPAY--------------------------------
