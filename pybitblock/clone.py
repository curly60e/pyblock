#Developer: Curly60e
#PyBLOCK its a clock of the Bitcoin blockchain.


import logging
import os
import os.path
import subprocess
import time as t


def gitclone():
    url = "https://github.com/curly60e/satellite"
    subprocess.run(["git", "clone", url])
    subprocess.run(["mkdir", "satellite/api/examples/.gnupg"])
    subprocess.run(["gpg", "--full-generate-key", "--homedir", "satellite/api/examples/.gnupg"])

def satnode():
    try:
        subprocess.run(["python3", "satellite/api/examples/demo-rx.py"])
        t.sleep(5)
        subprocess.run(["python3", "satellite/api/examples/api_data_reader.py", "--demo", "--plaintext"])
    except (OSError, subprocess.SubprocessError) as e:
        logging.getLogger(__name__).debug("satnode error: %s", e)

def matrixsc():
    if os.path.isdir('$HOME/pyblock/terminal_matrix'):
        print("OK Pass")
    else:
        url = "https://github.com/curly60e/terminal_matrix.git"
        subprocess.run(["git", "clone", url])
