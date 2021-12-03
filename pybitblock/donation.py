#Developer: Curly60e
#PyBLOCK its a clock of the Bitcoin blockchain.


import requests
import qrcode
import pickle
from nodeconnection import *

def donationAddr():
    qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
    )
    url = 'bc1qjzaz34nv2ev55vfdu9m5qh0zq0fwcn6c7pkcrv'
    print("\033[1;30;47m")
    qr.add_data(url)
    qr.print_ascii()
    print("\033[0;37;40m")
    qr.clear()
    print("Bitcoin Address Bech32: " + url)

def donationPayNym():
    qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
    )
    url = 'PM8TJhNTTq3YVocXuPtLjKx7pKkdUxqwTerWJ2j2a7dNitgyMmBPN6gK61yE17N2vgvQvKYokXktt6D6GZFTmocvDJhaUJfHt7ehEMmthjsT3NQHseFM'
    print("\033[1;30;47m")
    qr.add_data(url)
    qr.print_ascii()
    print("\033[0;37;40m")
    qr.clear()
    print("PayNym: " + url)

#Dev LN
def donationLN():
    qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
    )
    amt = input("Amount: ")
    curl = 'curl -X POST https://lnbits.com/api/v1/payments -d ' + "'{" + """"out": false, "amount": {}, "memo": "Donation" """.format(amt) + "}'" + """ -H "X-Api-Key: 1d646820055e4e2da218e801eaacfc94 " -H "Content-type: application/json" """
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

#Tester Address
def donationAddrTst():
    qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
    )
    url = 'bc1qwtzwu2evtchkvnf3ey6520yprsyv7vrjvhula5'
    print("\033[1;30;47m")
    qr.add_data(url)
    qr.print_ascii()
    print("\033[0;37;40m")
    qr.clear()
    print("Bitcoin Address Bech32: " + url)

#Tester LN
def donationLNTst():
    qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
    )
    url = 'https://api.tippin.me/v1/public/addinvoice/__B__T__C__'
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
        qr.clear()
        response.close()

def decodeQR():
    qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
    )
    url = input("Insert your Bitcoin Address to show the QRCode: ")
    print("\033[1;30;47m")
    qr.add_data(url)
    qr.print_ascii()
    print("\033[0;37;40m")
    qr.clear()
    print("Bitcoin Address: " + url)
