#Developer: Curly60e
#PyBLOCK its a clock of the Bitcoin blockchain.


import os
import os.path
import subprocess
import time as t


def readFile():
    import glob
    import logging
    logger = logging.getLogger(__name__)
    try:
        print("\n\033[1;34;40mWaiting for new data...\n")
        downloadsFolder = 'downloads/'
        while True:
            files = glob.glob(os.path.join(downloadsFolder, '*'))
            if not files:
                continue
            else:
                print("\t\t\n\033[1;33;40mNew message from Space just arrived...\033[0;37;40m\n")
                for f in files:
                    with open(f, 'r', errors='replace') as fh:
                        print(fh.read())
                    os.remove(f)
    except KeyboardInterrupt:
        pass
    except (OSError, IOError) as e:
        logger.debug("readFile error: %s", e)
