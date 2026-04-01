#Developer: Curly60e
#Tester: __B__T__C__
#ℙ𝕪𝔹𝕃𝕆ℂ𝕂 𝕚𝕥𝕤 𝕒 𝔹𝕚𝕥𝕔𝕠𝕚𝕟 𝔻𝕒𝕤𝕙𝕓𝕠𝕒𝕣𝕕 𝕨𝕚𝕥𝕙 ℂ𝕪𝕡𝕙𝕖𝕣𝕡𝕦𝕟𝕜 𝕒𝕖𝕤𝕥𝕙𝕖𝕥𝕚𝕔.


import base64, codecs, json, requests
import subprocess
import os
import os.path
import qrcode
import sys
import time as t
import numpy as np
from cfonts import render, say
from pblogo import blogo
from PIL import Image
from robohash import Robohash
from config import cfg
from log import get_logger
logger = get_logger("SPV.nodeconnection")


lndconnectload = {"ip_port":"", "tls":"", "macaroon":"", "ln":""}
settingsClock = {"gradient":"", "design":"", "colorA":"", "colorB":""}


def clear(): # clear the screen
    subprocess.run(['clear'] if os.name != 'nt' else ['cls'], shell=(os.name == 'nt'))
def closed():
    print("<<< Back Control + C.\n\n")

#-------------------------RPC BITCOIN NODE CONNECTION

def rpc(method, params=None):
    if params is None:
        params = []
    payload = json.dumps({
        "jsonrpc": "2.0",
        "id": "minebet",
        "method": method,
        "params": params
    })
    path = cfg.path
    return requests.post(path['ip_port'], auth=(path['rpcuser'], path['rpcpass']), data=payload).json()['result']

def remoteHalving():
    try:
        output = render("run your node", colors=['yellow'], align='left', font='tiny')
        print(output)
        input("\a\nContinue...")
    except Exception as e:
        logger.debug("nodeconnection: %s", e)

def remotegetblock():
    try:
        output = render("run your node", colors=['yellow'], align='left', font='tiny')
        print(output)
        input("\a\nContinue...")
    except Exception as e:
        logger.debug("nodeconnection: %s", e)

def remotegetblockcount(): # get access to bitcoin-cli with the command getblockcount
    try:
        output = render("run your node", colors=['yellow'], align='left', font='tiny')
        print(output)
        input("\a\nContinue...")
    except Exception as e:
        logger.debug("nodeconnection: %s", e)

def remoteconsole(): # get into the console from bitcoin-cli
    try:
        output = render("run your node", colors=['yellow'], align='left', font='tiny')
        print(output)
        input("\a\nContinue...")
    except Exception as e:
        logger.debug("nodeconnection: %s", e)

def runthenumbersConn():
    try:
        conn = 'curl -s https://get.txoutset.info/ | html2text | grep -v -E "UTC" | jq -C '
        a = subprocess.run(conn, shell=True, capture_output=True, text=True).stdout
        clear()
        blogo()
        closed()
        output = render("run the numbers", colors=['yellow'], align='left', font='tiny')
        print(output)
        print(a)
        input("\a\nContinue...")
    except Exception as e:
        logger.debug("nodeconnection: %s", e)

#-------------------------END RPC BITCOIN NODE CONNECTION

def localFullProtocol():
    lndconnectload = cfg.lndconnectload

    proto1 = """lncli listinvoices | grep "34349334" | tr -d '"' | tr -d ',' | sed 's/34349334/0a0a2d5079424c4f434b204d6573736167652052656365697665643a200a/g' | html2text | xxd -r -p | xargs --null"""
    proto2 = """lncli listinvoices | grep "7629171" | tr -d '"' | tr -d ',' | sed 's/7629171/0a0a2d5079424c4f434b204d6573736167652052656365697665643a200a/g' | html2text | xxd -r -p | xargs --null"""
    proto3 = """lncli listinvoices | grep "34343434" | tr -d '"' | tr -d ',' | sed 's/34343434/0a0a2d5079424c4f434b204d6573736167652052656365697665643a200a/g' | html2text | xxd -r -p | xargs --null"""
    p1 = subprocess.run(proto1, shell=True, capture_output=True, text=True).stdout
    p2 = subprocess.run(proto2, shell=True, capture_output=True, text=True).stdout
    p3 = subprocess.run(proto3, shell=True, capture_output=True, text=True).stdout

    proto1 = """lncli listpayments | grep "34349334" | tr -d '"' | tr -d ',' | sed 's/34349334/0a0a202d5079424c4f434b204d6573736167653a200a/g' | html2text | xxd -r -p | xargs --null"""
    proto2 = """lncli listpayments | grep "7629171" | tr -d '"' | tr -d ',' | sed 's/7629171/0a0a202d5079424c4f434b204d6573736167653a200a/g' | html2text | xxd -r -p | xargs --null"""
    proto3 = """lncli listpayments | grep "34343434" | tr -d '"' | tr -d ',' | sed 's/34343434/0a0a202d5079424c4f434b204d6573736167653a200a/g' | html2text | xxd -r -p | xargs --null"""
    p1 = subprocess.run(proto1, shell=True, capture_output=True, text=True).stdout
    p2 = subprocess.run(proto2, shell=True, capture_output=True, text=True).stdout
    p3 = subprocess.run(proto3, shell=True, capture_output=True, text=True).stdout

#--------------------------------- NYMs -----------------------------------

def get_ansi_color_code(r, g, b):
    if r == g == b:
        if r < 8:
            return 16
        if r > 248:
            return 231
        return round(((r - 8) / 247) * 24) + 232
    return 16 + (36 * round(r / 255 * 5)) + (6 * round(g / 255 * 5)) + round(b / 255 * 5)


def get_color(r, g, b):
    return "\x1b[48;5;{}m \x1b[0m".format(int(get_ansi_color_code(r,g,b)))

def channels():
    lndconnectload = cfg.lndconnectload
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
                if not os.path.isfile(str(f'{hash}.png')):
                    with open(f'{hash}.png', "wb") as f:
                        rh.img.save(f, format="png")

                    img_path = open(f'{hash}.png', "rb")
                    img = Image.open(img_path)

                    h = 1
                    w = int((img.width / img.height) * 5)

                    img = img.resize((w,h), Image.ANTIALIAS)
                    img_arr = np.asarray(img)
                    h,w,c = img_arr.shape

                img_path = open(f'{hash}.png', "rb")
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

                    img_path = open(f'{hash}.png', "rb")
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
        except Exception as e:
            logger.debug("nodeconnection: %s", e)
            break

def channelbalance():
    try:
        output = render("run your node", colors=['yellow'], align='left', font='tiny')
        print(output)
        input("\a\nContinue...")
    except Exception as e:
        logger.debug("nodeconnection: %s", e)

def listonchaintxs():
    try:
        output = render("run your node", colors=['yellow'], align='left', font='tiny')
        print(output)
        input("\a\nContinue...")
    except Exception as e:
        logger.debug("nodeconnection: %s", e)

def balanceOC():
    try:
        output = render("run your node", colors=['yellow'], align='left', font='tiny')
        print(output)
        input("\a\nContinue...")
    except Exception as e:
        logger.debug("nodeconnection: %s", e)

# END Remote connection with rest -------------------------------------
#---------------------------------OPENDIME-----------------------------

def ADDRbalance():
    import os, sys; sys.path.insert(0, os.path.normpath(__file__ + '/support/pycode.zip'))
    import support.pycode.od_wallet; support.pycode.od_wallet.main()
