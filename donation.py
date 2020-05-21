import requests
import qrcode




def donationPN():
    qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
    )
    url = 'PM8TJbSH9iCPZ2bz9D7MTHpaCnT35Pm4kfJ6gRccoKmMjz5qsQ6rBWpBRCnJHMpTo8kc5K2SF4MADA9f4uKwc5iC8A3FtKJc7eb5wFDF3vcuSfneaC15'
    qr.add_data(url)
    qr.print_ascii()
    print("PayNym: " + url)
    
def donationAddr():
    qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
    )
    url = 'bc1qf5c88chttajazrlwudt7x9xx5u0qf8y2lguj62'
    qr.add_data(url)
    qr.print_ascii()
    print("Bitcoin Address Bech32: " + url)
    
def donationLN():
    qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
    )
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
    qr.add_data(ln1)
    qr.print_ascii()
    print("LND Invoice: " + ln1)

def decodeQR():
    qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
    )
    url = input("Insert your Bitcoin Address to show the QRCode: ")
    qr.add_data(url)
    qr.print_ascii()
    print("Bitcoin Address: " + url)

