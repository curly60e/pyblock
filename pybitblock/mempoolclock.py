import pickle
import os
import sys
import base64, codecs, json, requests
import time as t
from pblogo import *
from cfonts import render, say



def clear(): # clear the screen
    os.system('cls' if os.name=='nt' else 'clear')

def rectangle(n):
    x = n - 3
    y = n - x
    [
        print(''.join(i))
        for i in
        (
            ''*x
            if i in (0,y-1)
            else
            (
                f'{""*n}{"|"*n}{""*n}'
                if i >= (n+1)/2 and i <= (1*n)/2
                else
                f'\033[A\u001b[38;5;27m{"❑"*(x-1)}\033[A'
            )
            for i in range(y)
        )
    ]

def pathexec():
    global path
    path = {"ip_port":"", "rpcuser":"", "rpcpass":"", "bitcoincli":""}
    pathv = pickle.load(open("config/bclock.conf", "rb")) # Load the file 'bclock.conf'
    path = pathv # Copy the variable pathv to 'path'

def counttxs():
    while True:
        try:
            pathexec()
            clear()
            getrawmempool = " getrawmempool"
            gna = os.popen(path['bitcoincli'] + getrawmempool)
            gnaa = gna.read()
            gna1 = str(gnaa)
            d = json.loads(gna1)
            e = len(d)
            outputtxs = render(
                f'{e} unconfirmed txs',
                colors=[settingsClock['colorA'], settingsClock['colorB']],
                align='center',
                font='tiny',
            )

            print("\x1b[?25l" + outputtxs)
            shq = e // 10
            ss = str(rectangle(shq))
            qq = ss.replace("None","")
            print(f"\033[A{qq}\033[A")
            t.sleep(10)
        except:
            break

settings = {"gradient":"", "design":"block", "colorA":"green", "colorB":"yellow"}
settingsClock = {"gradient":"", "colorA":"green", "colorB":"yellow"}
while True: # Loop
    try:
        clear()
        path = {"ip_port":"", "rpcuser":"", "rpcpass":"", "bitcoincli":""}

        if os.path.isfile('config/bclock.conf') or os.path.isfile('config/blnclock.conf'): # Check if the file 'bclock.conf' is in the same folder
            pathv = pickle.load(open("config/bclock.conf", "rb")) # Load the file 'bclock.conf'
            path = pathv # Copy the variable pathv to 'path'
        else:
            blogo()
            print("Welcome to \033[1;31;40mPyBLOCK\033[0;37;40m\n\n")
            print("\n\tIf you are going to use your local node leave IP:PORT/USER/PASSWORD in blank.\n")
            path[
                'ip_port'
            ] = f'http://{input("Insert IP:PORT to access your remote Bitcoin-Cli node: ")}'

            path['rpcuser'] = input("RPC User: ")
            path['rpcpass'] = input("RPC Password: ")
            print("\n\tLocal Bitcoin Core Node connection.\n")
            path['bitcoincli']= input("Insert the Path to Bitcoin-Cli: ")
            pickle.dump(path, open("config/bclock.conf", "wb"))
        counttxs()


    except:
        print("\n")
        sys.exit(101)
