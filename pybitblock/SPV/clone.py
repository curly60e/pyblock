#Developer: Curly60e
#PyBLOCK its a clock of the Bitcoin blockchain.


import os
import os.path
import time as t


def gitclone():
    url = "https://github.com/curly60e/satellite"
    os.system("git clone " + url)
    os.system("mkdir satellite/api/examples/.gnupg")
    os.system("gpg --full-generate-key --homedir satellite/api/examples/.gnupg")

def satnode():
    try:
        os.system("python3 satellite/api/examples/demo-rx.py &")
        t.sleep(5)
        os.system("python3 satellite/api/examples/api_data_reader.py --demo  --plaintext ")
    except:
        os.system("ps -ef | grep api_data_reader.py | grep -v grep | awk '{print $2}' | xargs kill -9")
        os.system("ps -ef | grep demo-rx.py | grep -v grep | awk '{print $2}' | xargs kill -9")

def matrixsc():
    if os.path.isdir('$HOME/pyblock/terminal_matrix'):
        print("OK Pass")
    else:
        url = "https://github.com/curly60e/terminal_matrix.git"
        os.system("git clone " + url)
