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
                subprocess.run(["cat", "downloads/*"])
                subprocess.run(["rm", "downloads/*"])

    except Exception:
        subprocess.run(["pkill", "-9", "-f", "api_data_reader.py"])
        subprocess.run(["pkill", "-9", "-f", "demo-rx.py"])
