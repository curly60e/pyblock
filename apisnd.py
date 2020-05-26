import os
import qrcode
import time as t

def apisender():
    qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
    )
    url = 'https://api.blockstream.space/order'
    message = input("\nInsert your Message: ")
    sentby = ". Message sent from PyBlock."
    
    curl = 'curl -F "bid=10000" -F ' + ' "message=' + message + sentby + '" ' + url
    sh = os.popen(str(curl)).read()
    shh = sh.split(',')
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
    print("\033[1;30;47m")
    qr.add_data(cln)
    qr.print_ascii()
    print("\033[0;37;40m")
    print("\nLND Invoice: " + cln)
    print(cln)

def apisenderFile():
    qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
    )
    url = 'https://api.blockstream.space/order'
    message = input("\nInsert the path to the File: ")
    
    curl = 'curl -F "bid=10000" -F ' + ' "file=@' + message + '" ' + url
    sh = os.popen(str(curl)).read()
    shh = sh.split(',')
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
    print("\033[1;30;47m")
    qr.add_data(cln)
    qr.print_ascii()
    print("\033[0;37;40m")
    print("\nLND Invoice: " + cln)
    print(cln)
