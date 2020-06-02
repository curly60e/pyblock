#Developer: Curly60e
#PyBLOCK its a clock of the Bitcoin blockchain.
#Version: 0.3.0

import os
import os.path
import time as t


def readFile():
    try:
        while True:
            downloadsFolder = 'downloads/'
            if not os.listdir(downloadsFolder):
                print ("\n\033[1;34;40mWaiting for new data...\n")
                t.sleep(50)
            else:
                print("\t\t\n\033[1;33;40mNew message from Space just arrived...\033[0;37;40m\n")
                os.system("cat downloads/*")
                os.system("rm downloads/*")
                
    except (KeyboardInterrupt, SystemExit):
        os.system("ps -ef | grep api_data_reader.py | grep -v grep | awk '{print $2}' | xargs kill -9")
        

        
