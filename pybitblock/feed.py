#Developer: Curly60e
#PyBLOCK its a clock of the Bitcoin blockchain.


import os
import os.path
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
                os.system("cat downloads/*")
                os.system("rm downloads/*")

    except:
        os.system("ps -ef | grep api_data_reader.py | grep -v grep | awk '{print $2}' | xargs kill -9")
        os.system("ps -ef | grep demo-rx.py | grep -v grep | awk '{print $2}' | xargs kill -9")
