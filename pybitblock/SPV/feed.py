#Developer: Curly60e
#PyBLOCK its a clock of the Bitcoin blockchain.


import os
import os.path
import subprocess
import time as t


def readFile():
    try:
        print ("\n\033[1;34;40mWaiting for new data...\n")
        downloadsFolder = 'downloads/'
        while True:
            if not os.listdir(downloadsFolder):
                continue
            else:
                print("\t\t\n\033[1;33;40mNew message from Space just arrived...\033[0;37;40m\n")
                subprocess.run(['cat'] + [os.path.join('downloads', f) for f in os.listdir('downloads')])
                subprocess.run(['rm'] + [os.path.join('downloads', f) for f in os.listdir('downloads')])

    except Exception:
        subprocess.run(['pkill', '-f', 'api_data_reader.py'])
        subprocess.run(['pkill', '-f', 'demo-rx.py'])
