import pickle
import os
import sys
import base64, codecs, json, requests
import time as t
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
                f'\033[A\u001b[38;5;27m{"█"*(x-1)}\033[A'
            )
            for i in range(y)
        )
    ]

def blogo():

    if os.path.isfile('config/pyblocksettings.conf') or os.path.isfile('config/pyblocksettings.conf'): # Check if the file 'bclock.conf' is in the same folder
        settingsv = pickle.load(open("config/pyblocksettings.conf", "rb")) # Load the file 'bclock.conf'
        settings = settingsv # Copy the variable pathv to 'path'
    else:
        settings = {"gradient":"", "design":"block", "colorA":"green", "colorB":"yellow"}
        pickle.dump(settings, open("config/pyblocksettings.conf", "wb"))

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
        except:
            break

def pathexec():
    global path
    path = {"ip_port":"", "rpcuser":"", "rpcpass":"", "bitcoincli":""}
    pathv = pickle.load(open("config/bclock.conf", "rb")) # Load the file 'bclock.conf'
    path = pathv # Copy the variable pathv to 'path'

def design():
    while True:
        if os.path.isfile('config/pyblocksettingsClock.conf') or os.path.isfile('config/pyblocksettingsClock.conf'): # Check if the file 'bclock.conf' is in the same folder
            settingsv = pickle.load(open("config/pyblocksettingsClock.conf", "rb")) # Load the file 'bclock.conf'
            settingsClock = settingsv # Copy the variable pathv to 'path'
        else:
            settingsClock = {"gradient":"", "design":"block", "colorA":"green", "colorB":"yellow"}
            pickle.dump(settingsClock, open("config/pyblocksettingsClock.conf", "wb"))
        bitcoinclient = path['bitcoincli'] + " getblockcount"
        block = os.popen(str(bitcoinclient)).read() # 'getblockcount' convert to string
        b = block
        a = b
        blogo()
        output = render(str(b), colors=[settingsClock['colorA'], settingsClock['colorB']], align='center')
        print("\x1b[?25l" + output)
        bitcoinclient = path['bitcoincli'] + " getbestblockhash"
        bb = os.popen(str(bitcoinclient)).read()
        ll = bb
        bitcoinclientgetblock = path['bitcoincli'] + " getblock " + ll
        qq = os.popen(bitcoinclientgetblock).read()
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
            bitcoinclient = path['bitcoincli'] + " getblockcount"
            block = os.popen(str(bitcoinclient)).read() # 'getblockcount' convert to string
            b = block
            if b > a:
                clear()
                blogo()
                output = render(str(b), colors=[settingsClock['colorA'], settingsClock['colorB']], align='center')
                print("\a\x1b[?25l" + output)
                bitcoinclient = path['bitcoincli'] + " getbestblockhash"
                bb = os.popen(str(bitcoinclient)).read()
                ll = bb
                bitcoinclientgetblock = path['bitcoincli'] + " getblock " + ll
                qq = os.popen(bitcoinclientgetblock).read()
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
                        p = subprocess.Popen(['curl', 'https://poptart.spinda.net'])
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
        artist()


    except:
        print("\n")
        sys.exit(101)
