import os
import os.path
import time as t


def gitclone():
    if os.path.isdir('$HOME/pyblock/satellite'):
        print("OK Pass")
        
    else:
        url = "https://github.com/curly60e/satellite"
        os.system("git clone " + url)
        os.system("mkdir $HOME/pyblock/satellite/api/examples/.gnupg")
        os.system("cp -r $HOME/pyblock/satellite/api/examples $HOME/pyblock/")
        os.system("gpg --full-generate-key --homedir $HOME/pyblock/examples/.gnupg")
        
def satnode():
    try:
        os.system("python3 $HOME/pyblock/examples/demo-rx.py &")
        t.sleep(5)
        os.system("python3 $HOME/pyblock/examples/api_data_reader.py --demo  --plaintext ")
    except (KeyboardInterrupt, SystemExit):
        os.system("ps -ef | grep demo-rx.py | grep -v grep | awk '{print $2}' | xargs kill -9")
    

def matrixsc():
    if os.path.isdir('$HOME/pyblock/terminal_matrix'):
        print("OK Pass")
        
    else:
        url = "https://github.com/curly60e/terminal_matrix.git"
        os.system("git clone " + url)

