import base64, codecs, json, requests
import os
import subprocess
import sys
import simplejson as json
from cfonts import render, say

ndconnectload = {"ip_port":"", "tls":"", "macaroon":"", "ln":""}
settingsClock = {"gradient":"", "design":"", "colorA":"", "colorB":""}

def blogo():

    if os.path.isfile('pyblocksettings.conf') or os.path.isfile('pyblocksettings.conf'): # Check if the file 'bclock.conf' is in the same folder
        settingsv = json.load(open("pyblocksettings.conf", "r")) # Load the file 'bclock.conf'
        settings = settingsv # Copy the variable pathv to 'path'
    else:
        settings = {"gradient":"", "design":"block", "colorA":"green", "colorB":"yellow"}
        with open("pyblocksettings.conf", "w") as f:
            json.dump(settings, f, indent=2)

    if settings["gradient"] == "grd":
        output = render('PyBLOCK', gradient=[settings['colorA'], settings['colorB']], align='center', font=settings['design'])
    else:
        output = render('PyBLOCK', colors=[settings['colorA'], settings['colorB']], align='center', font=settings['design'])

    print(output)

def clear(): # clear the screen
    subprocess.run(['clear'] if os.name != 'nt' else ['cls'], shell=(os.name == 'nt'))

if os.path.isfile('blndconnect.conf'): # Check if the file 'bclock.conf' is in the same folder
    lndconnectData= json.load(open("blndconnect.conf", "r")) # Load the file 'bclock.conf'
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
    with open("blndconnect.conf", "w") as f:
        json.dump(lndconnectload, f, indent=2) # Save the file 'bclock.conf'

def rpc(method, params=[]):
    payload = json.dumps({
        "jsonrpc": "2.0",
        "id": "minebet",
        "method": method,
        "params": params
    })
    path = {"ip_port":"", "rpcuser":"", "rpcpass":"", "bitcoincli":""}
    if os.path.isfile('bclock.conf'): # Check if the file 'bclock.conf' is in the same folder
        pathv = json.load(open("bclock.conf", "r")) # Load the file 'bclock.conf'
        path = pathv # Copy the variable pathv to 'path'
    return requests.post(path['ip_port'], auth=(path['rpcuser'], path['rpcpass']), data=payload).json()['result']


def remotegetblock():
    if os.path.isfile('pyblocksettingsClock.conf') or os.path.isfile('pyblocksettingsClock.conf'): # Check if the file 'bclock.conf' is in the same folder
        settingsv = json.load(open("pyblocksettingsClock.conf", "r")) # Load the file 'bclock.conf'
        settingsClock = settingsv # Copy the variable pathv to 'path'
    else:
        settingsClock = {"gradient":"", "design":"block", "colorA":"green", "colorB":"yellow"}
        with open("pyblocksettingsClock.conf", "w") as f:
            json.dump(settingsClock, f, indent=2)
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
            blogo()
            output = render(str(c), colors=[settingsClock['colorA'], settingsClock['colorB']], align='center')
            print("\a\x1b[?25l" + output)
            a = c

while True:
    try:
        clear()
        blogo()
        remotegetblock()
        tmp()
    except:
        print("\n")
        sys.exit(101)
