#Developer: Curly60e
#Tester: __B__T__C__
#ℙ𝕪𝔹𝕃𝕆ℂ𝕂 𝕚𝕥𝕤 𝕒 𝔹𝕚𝕥𝕔𝕠𝕚𝕟 𝔻𝕒𝕤𝕙𝕓𝕠𝕒𝕣𝕕 𝕨𝕚𝕥𝕙 ℂ𝕪𝕡𝕙𝕖𝕣𝕡𝕦𝕟𝕜 𝕒𝕖𝕤𝕥𝕙𝕖𝕥𝕚𝕔.


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
    print(f"Bitcoin Address Bech32: {url}")

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
    print(f"PayNym: {url}")

#Dev LN
def donationLN():
    qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
    )
    amt = input("Amount: ")
    curl = (
        'curl -X POST https://lnbits.com/api/v1/payments -d '
        + "'{"
        + f""""out": false, "amount": {amt}, "memo": "Donation" """
        + "}'"
        + """ -H "X-Api-Key: 1d646820055e4e2da218e801eaacfc94 " -H "Content-type: application/json" """
    )

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
        print(f"Lightning Invoice: {c}")
        dn = str(d['checking_id'])
        t.sleep(10)
        checkcurl = (
            f'curl -X GET https://lnbits.com/api/v1/payments/{dn}'
            + """ -H "X-Api-Key: 1d646820055e4e2da218e801eaacfc94" -H "Content-type: application/json" """
        )

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
    print(f"Bitcoin Address Bech32: {url}")

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
    lnurl = lnreq[1]
    lnurlS = str(lnbc1)
    node_not = input("Are you Satoshi? Y/n: ")
    if node_not in ["Y", "y", "N", "n"]:
        print("\033[1;30;47m")
        lnurlR = lnurlS.split(':')
        lnurlW = lnurlR[1]
        ln = str(lnurlW)
        ln1 = ln.strip('"')
        qr.add_data(ln1)
        qr.print_ascii()
        print("\033[0;37;40m")
        print(f"LNURL: {ln1}")
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
    print(f"Bitcoin Address: {url}")
