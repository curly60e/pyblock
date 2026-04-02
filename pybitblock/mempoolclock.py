import json
import os
import subprocess
import sys
import base64, codecs, requests
import time as t
from pblogo import blogo
from cfonts import render, say



def clear(): # clear the screen
    subprocess.run(['clear'] if os.name != 'nt' else ['cls'], shell=(os.name == 'nt'))

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
                f'\033[A\u001b[38;5;27m{"█"*(x-1)}\033[A'
            )
            for i in range(y)
        )
    ]

def pathexec():
    global path
    path = {"ip_port":"", "rpcuser":"", "rpcpass":"", "bitcoincli":""}
    with open("config/bclock.conf", "r") as f:
        pathv = json.load(f) # Load the file 'bclock.conf'
        path = pathv # Copy the variable pathv to 'path'

def counttxs():
    try:
        block = subprocess.run([path["bitcoincli"], "getblockcount"], capture_output=True, text=True).stdout # 'getblockcount' convert to string
        b = block
        a = b
        pathexec()
        clear()
        gnaa = subprocess.run([path['bitcoincli'], "getrawmempool"], capture_output=True, text=True).stdout
        gna1 = str(gnaa)
        d = json.loads(gna1)
        e = len(d)
        n = e / 10
        nn = n
        while True:
            x = a
            block = subprocess.run([path["bitcoincli"], "getblockcount"], capture_output=True, text=True).stdout # 'getblockcount' convert to string
            b = block
            pathexec()
            gnaa = subprocess.run([path['bitcoincli'], "getrawmempool"], capture_output=True, text=True).stdout
            gna1 = str(gnaa)
            d = json.loads(gna1)
            e = len(d)
            n = e / 10
            if e > nn:
                clear()
                outputtxs = render(
                    f'{e} txs',
                    colors=[settingsClock['colorA'], settingsClock['colorB']],
                    align='center',
                    font='tiny',
                )

                print("\x1b[?25l" + outputtxs)
                shq = int(n)
                ss = str(rectangle(shq))
                qq = ss.replace("None","")
                print(f"\033[A{qq}\033[A")
                nn = e
            if b > a:
                print("\n\n\n")
                output = render(str(b), colors=[settingsClock['colorA'], settingsClock['colorB']], align='center', font='tiny')
                print("\a\x1b[?25l" + output)
                bb = subprocess.run([path["bitcoincli"], "getbestblockhash"], capture_output=True, text=True).stdout
                ll = bb
                qq = subprocess.run([path["bitcoincli"], "getblock", ll.strip()], capture_output=True, text=True).stdout
                yy = json.loads(qq)
                mm = yy
                outputtxs = render(str(mm['nTx']) + " txs", colors=[settingsClock['colorA'], settingsClock['colorB']], align='center', font='tiny')
                print("\x1b[?25l" + outputtxs)
                sh = int(mm['nTx']) / 10
                shq = int(sh)
                ss = str(rectangle(shq))
                print(ss.replace("None",""))
                t.sleep(5)
                txs = str(mm['nTx'])
                if txs == "1":
                    try:
                        p = subprocess.Popen(['curl', 'http://ascii.live/forrest'])
                        p.wait(5)
                    except subprocess.TimeoutExpired:
                        p.kill()
                print("\033[0;37;40m\x1b[?25l")
                a = b
                nn = e
    except Exception:
        pass


settings = {"gradient":"", "design":"block", "colorA":"green", "colorB":"yellow"}
settingsClock = {"gradient":"", "colorA":"green", "colorB":"yellow"}
while True: # Loop
    try:
        clear()
        path = {"ip_port":"", "rpcuser":"", "rpcpass":"", "bitcoincli":""}

        if os.path.isfile('config/bclock.conf') or os.path.isfile('config/blnclock.conf'): # Check if the file 'bclock.conf' is in the same folder
            with open("config/bclock.conf", "r") as f:
                pathv = json.load(f) # Load the file 'bclock.conf'
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
            print("\n\tLocal Bitcoin Node connection.\n")
            path['bitcoincli']= input("Insert the Path to Bitcoin-Cli: ")
            with open("config/bclock.conf", "w") as f:
                json.dump(path, f, indent=2)
        counttxs()


    except Exception:
        print("\n")
        sys.exit(101)
