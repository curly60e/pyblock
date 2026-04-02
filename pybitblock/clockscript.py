import json
import os
import subprocess
import sys
import base64, codecs, requests
import time as t
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

def blogo():

    if os.path.isfile('config/pyblocksettings.conf') or os.path.isfile('config/pyblocksettings.conf'): # Check if the file 'bclock.conf' is in the same folder
        with open("config/pyblocksettings.conf", "r") as f:
            settingsv = json.load(f) # Load the file 'bclock.conf'
            settings = settingsv # Copy the variable pathv to 'path'
    else:
        settings = {"gradient":"", "design":"block", "colorA":"green", "colorB":"yellow"}
        with open("config/pyblocksettings.conf", "w") as f:
            json.dump(settings, f, indent=2)

    if settings["gradient"] == "grd":
        output = render('PyBLOCK', gradient=[settings['colorA'], settings['colorB']], align='center', font=settings['design'])
    else:
        output = render('PyBLOCK', colors=[settings['colorA'], settings['colorB']], align='center', font=settings['design'])

    print(output)

def artist(): # here we convert the result of the command 'getblockcount' on a random art design
    while True:
        try:
            clear()
            design()
        except Exception:
            break

def pathexec():
    global path
    path = {"ip_port":"", "rpcuser":"", "rpcpass":"", "bitcoincli":""}
    with open("config/bclock.conf", "r") as f:
        pathv = json.load(f) # Load the file 'bclock.conf'
        path = pathv # Copy the variable pathv to 'path'

def design():
    while True:
        if os.path.isfile('config/pyblocksettingsClock.conf') or os.path.isfile('config/pyblocksettingsClock.conf'): # Check if the file 'bclock.conf' is in the same folder
            with open("config/pyblocksettingsClock.conf", "r") as f:
                settingsv = json.load(f) # Load the file 'bclock.conf'
                settingsClock = settingsv # Copy the variable pathv to 'path'
        else:
            settingsClock = {"gradient":"", "design":"block", "colorA":"green", "colorB":"yellow"}
            with open("config/pyblocksettingsClock.conf", "w") as f:
                json.dump(settingsClock, f, indent=2)
        block = subprocess.run([path['bitcoincli'], 'getblockcount'], capture_output=True, text=True).stdout # 'getblockcount' convert to string
        b = block
        a = b
        blogo()
        output = render(str(b), colors=[settingsClock['colorA'], settingsClock['colorB']], align='center')
        print("\x1b[?25l" + output)
        bb = subprocess.run([path['bitcoincli'], 'getbestblockhash'], capture_output=True, text=True).stdout
        ll = bb
        qq = subprocess.run([path['bitcoincli'], 'getblock', ll.strip()], capture_output=True, text=True).stdout
        yy = json.loads(qq)
        mm = yy
        outputsize = render(str(mm['size']) + " bytes", colors=[settingsClock['colorA'], settingsClock['colorB']], align='center', font='tiny')
        print("\x1b[?25l" + outputsize)
        outputtxs = render(str(mm['nTx']) + " txs", colors=[settingsClock['colorA'], settingsClock['colorB']], align='center', font='tiny')
        print("\x1b[?25l" + outputtxs)
        sh = int(mm['nTx']) / 4
        shq = int(sh)
        ss = str(rectangle(shq))
        print(ss.replace("None",""))
        while True:
            x = a
            block = subprocess.run([path['bitcoincli'], 'getblockcount'], capture_output=True, text=True).stdout # 'getblockcount' convert to string
            b = block
            if b > a:
                clear()
                blogo()
                output = render(str(b), colors=[settingsClock['colorA'], settingsClock['colorB']], align='center')
                print("\a\x1b[?25l" + output)
                bb = subprocess.run([path['bitcoincli'], 'getbestblockhash'], capture_output=True, text=True).stdout
                ll = bb
                qq = subprocess.run([path['bitcoincli'], 'getblock', ll.strip()], capture_output=True, text=True).stdout
                yy = json.loads(qq)
                mm = yy
                outputsize = render(str(mm['size']) + " bytes", colors=[settingsClock['colorA'], settingsClock['colorB']], align='center', font='tiny')
                print("\x1b[?25l" + outputsize)
                outputtxs = render(str(mm['nTx']) + " txs", colors=[settingsClock['colorA'], settingsClock['colorB']], align='center', font='tiny')
                print("\x1b[?25l" + outputtxs)
                sh = int(mm['nTx']) / 4
                shq = int(sh)
                ss = str(rectangle(shq))
                print(ss.replace("None",""))
                t.sleep(10)
                txs = str(mm['nTx'])
                if txs == "1":
                    try:
                        p = subprocess.Popen(['curl', 'http://ascii.live/forrest'])
                        p.wait(5)
                    except subprocess.TimeoutExpired:
                        p.kill()
                print("\033[0;37;40m\x1b[?25l")
                clear()
                close()
                a = b
                output = render(str(b), colors=[settingsClock['colorA'], settingsClock['colorB']], align='center')
                print("\x1b[?25l" + output)

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
        artist()


    except Exception:
        print("\n")
        sys.exit(101)
