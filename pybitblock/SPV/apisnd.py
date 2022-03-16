#Developer: Curly60e
#PyBLOCK its a clock of the Bitcoin blockchain.

import os
import qrcode
import requests
import time as t
import sys
from nodeconnection import *
from pblogo import *
from logos import *

def clear(): # clear the screen
    os.system('cls' if os.name=='nt' else 'clear')

def apisender():
    qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
    )
    message = input("\nInsert your Message: ")
    a = sys.getsizeof(message)
    mini = 6000
    n = (a * 50)
    if n <= mini:
        q = str(mini)
    elif n >= mini:
        k = n + mini
        q = str(k)

    url = 'https://api.blockstream.space/order'
    sentby = " - PyBLOCK."
    print("\n\tATENTION: YOU NEED TO PAY \033[1;31;40m" + q + "\033[0;37;40m MilliSats")
    amountmsat = input("\nInsert the amount in MSats: ")
    curl = 'curl -F ' "bid={} ".format(amountmsat) + '-F ' + ' "message=' + message + sentby + '" ' + url
    sh = os.popen(curl)
    clear()
    blogo()
    sh0 = sh.read()
    while True:
        if 'Bid too low' in sh0:
            print("\n\t\033[1;31;40mATENTION: Per byte bid cannot be below 50 millisatoshis per byte.\033[0;37;40m\n")
            print("Try again...\n")
            message = input("\nInsert your Message: ")
            a = sys.getsizeof(message)
            mini = 6000
            n = (a * 50)
            if n <= mini:
                q = str(mini)
            elif n >= mini:
                k = n + mini
                q = str(k)

            url = 'https://api.blockstream.space/order'
            sentby = " - PyBLOCK."
            print("\n\tATENTION: YOU NEED TO PAY \033[1;31;40m" + q + "\033[0;37;40m MilliSats")
            amountmsat = input("\nInsert the amount in MSats: ")
            curl = 'curl -F ' "bid={} ".format(amountmsat) + '-F ' + ' "message=' + message + sentby + '" ' + url
            sh = os.popen(curl)
            clear()
            blogo()
            sh0 = sh.read()
        elif 'lightning_invoice' in sh0:
            break

    sh1 = str(sh0)
    shh = sh1.split(',')
    invoice = str(shh[6])

    #---------------Token-----------
    authtoken = str(shh[0])
    authtoken1 = authtoken.split(':')
    token = authtoken1[1]
    #---------------End Token-------

    #---------------Order-----------
    uuid = str(shh[1])
    uuid1 = uuid.split(':')
    order = uuid1[1]
    #---------------End Order-------

    #---------------Amount----------
    msat = str(shh[3])
    msat1 = msat.split(':')
    amount = msat1[1]
    #---------------End Amount------

    orderid = str(shh[1])
    ln1 = invoice.split(':')
    ln2 = str(ln1[1])
    cln = ln2.strip('"')
    print("\n\033[0;37;40mYour Token Authorization: \033[1;31;40m" + token + "\033[0;37;40m")
    print("\033[0;37;40mYour Order Number: \033[1;31;40m" + order + "\033[0;37;40m")
    print("\033[0;37;40mAmount in MSats: \033[1;33;40m" + amount + "\033[0;37;40m\n")
    clear()
    blogo()
    node_not = input("Do you want to pay this message with your node? Y/n: ")
    if node_not in ["Y", "y"]:
        lndconnectload = {"ip_port":"", "tls":"", "macaroon":"", "ln":""}
        lndconnectData = pickle.load(open("blndconnect.conf", "rb")) # Load the file 'bclock.conf'
        lndconnectload = lndconnectData # Copy the variable pathv to 'path'
        if lndconnectload['ip_port']:
            print("\nInvoice: " + cln + "\n")
            payinvoice()
        elif lndconnectload['ln']:
            print("\nInvoice: " + cln + "\n")
            localpayinvoice()
    elif node_not in ["N", "n"]:
        print("\033[1;30;47m")
        qr.add_data(cln)
        qr.print_ascii()
        print("\033[0;37;40m")
        print("\nLND Invoice: " + cln + "\n")
        sh.close()
        continue1 = input("Continue? Y: ")
        if continue1 == "Y" or continue1 == "y":
            donate()
        else:
            t.sleep(2)

def apisenderFile():
    qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
    )
    url = 'https://api.blockstream.space/order'
    message = input("\nInsert the path to the File: ")
    print("ATENTION: Minimum amount for sending a File is 50000 MSats")
    amountmsat = input("\nInsert the amount in MSats: ")
    curl = 'curl -F ' "bid={} ".format(amountmsat) + '-F ' + ' "file=@' + message + '" ' + url
    sh = os.popen(curl)
    sh0 = sh.read()
    while True:
        try:
            if 'Bid too low' in sh0:
                print("\n\t\033[1;31;40mATENTION: Per byte bid cannot be below 50 millisatoshis per byte.\033[0;37;40m\n")
                print("Try again...\n")
                url = 'https://api.blockstream.space/order'
                message = input("\nInsert the path to the File: ")
                print("ATENTION: Minimum amount for sending a File is 50000 MSats")
                amountmsat = input("\nInsert the amount in MSats: ")
                curl = 'curl -F ' "bid={} ".format(amountmsat) + '-F ' + ' "file=@' + message + '" ' + url
                sh = os.popen(curl)
                sh0 = sh.read()
            elif 'lightning_invoice' in sh0:
                break
        except:
            break

    sh1 = str(sh0)
    shh = sh1.split(',')
    invoice = str(shh[6])

    #---------------Token-----------
    authtoken = str(shh[0])
    authtoken1 = authtoken.split(':')
    token = authtoken1[1]
    #---------------End Token-------

    #---------------Order-----------
    uuid = str(shh[1])
    uuid1 = uuid.split(':')
    order = uuid1[1]
    #---------------End Order-------

    #---------------Amount----------
    msat = str(shh[3])
    msat1 = msat.split(':')
    amount = msat1[1]
    #---------------End Amount------

    orderid = str(shh[1])
    ln1 = invoice.split(':')
    ln2 = str(ln1[1])
    cln = ln2.strip('"')
    print("\n\033[0;37;40mYour Token Authorization: \033[1;31;40m" + token + "\033[0;37;40m")
    print("\033[0;37;40mYour Order Number: \033[1;31;40m" + order + "\033[0;37;40m")
    print("\033[0;37;40mAmount in MSats: \033[1;33;40m" + amount + "\033[0;37;40m")
    clear()
    blogo()
    try:
        node_not = input("Do you want to pay this message with your node? Y/n: ")
        if node_not in ["Y", "y"]:
            lndconnectload = {"ip_port":"", "tls":"", "macaroon":"", "ln":""}
            lndconnectData = pickle.load(open("blndconnect.conf", "rb")) # Load the file 'bclock.conf'
            lndconnectload = lndconnectData # Copy the variable pathv to 'path'
            if lndconnectload['ip_port']:
                print("\nInvoice: " + cln + "\n")
                payinvoice()
            elif lndconnectload['ln']:
                print("\nInvoice: " + cln + "\n")
                localpayinvoice()
        elif node_not in ["N", "n"]:
            print("\033[1;30;47m")
            qr.add_data(cln)
            qr.print_ascii()
            print("\033[0;37;40m")
            print("\nLND Invoice: " + cln)
            sh.close()
            continue1 = input("Continue? Y: ")
            if continue1 == "Y" or continue1 == "y":
                donate()
            else:
                t.sleep(2)
    except:
        pass

def devAddr():
    qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
    )
    print("\n\t\t\033[1;33;44mGive us some love and \033[1;31;44mDONATE\033[1;33;44m us! We will appreciate it. This will be a boost to continue this beautiful project! \033[0;37;40m")
    url = 'https://api.tippin.me/v1/public/addinvoice/royalfield370'
    response = requests.get(url)
    responseB = str(response.text)
    responseC = responseB
    lnreq = responseC.split(',')
    lnbc1 = lnreq[1]
    lnbc1S = str(lnbc1)
    lnbc1R = lnbc1S.split(':')
    lnbc1W = lnbc1R[1]
    ln = str(lnbc1W)
    ln1 = ln.strip('"')
    clear()
    blogo()
    try:
        node_not = input("Do you want to pay this tip with your node? Y/n: ")
        if node_not in ["Y", "y"]:
            lndconnectload = {"ip_port":"", "tls":"", "macaroon":"", "ln":""}
            lndconnectData = pickle.load(open("blndconnect.conf", "rb")) # Load the file 'bclock.conf'
            lndconnectload = lndconnectData # Copy the variable pathv to 'path'
            if lndconnectload['ip_port']:
                print("\nInvoice: " + ln1 + "\n")
                payinvoice()
            elif lndconnectload['ln']:
                print("\nInvoice: " + ln1 + "\n")
                localpayinvoice()
        elif node_not in ["N", "n"]:
            print("\033[1;30;47m")
            qr.add_data(ln1)
            qr.print_ascii()
            print("\033[0;37;40m")
            print("LND Invoice: " + ln1)
            response.close()
    except:
        pass

def donate():
    print("""\t\t
    \033[1;31;40mPyBLOCK\033[0;37;40m Menu

    \033[1;32;40mA.\033[0;37;40m Donate
    <<< Back Control + C
    \n\n""")
    menuB = (input("\033[1;32;40mSelect option: \033[0;37;40m"))
    if menuB in ["A", "a"]:
        devAddr()
