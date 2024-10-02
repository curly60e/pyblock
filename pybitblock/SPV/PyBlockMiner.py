import requests
import hashlib
import binascii
import json
import random
import socket
import time
from threading import Thread
from colorthon import Colors as Fore
import sys, logging
import signal
signal.signal(signal.SIGINT, lambda x, y: sys.exit(0))

# Define your Bitcoin address
address = "1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa.SatoshiNakamoto"
# Initialize the current block height
cHeight = 0
solopyblockminer = '''
⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⣴⣶⣾⣿⣿⣿⣿⣷⣶⣦⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣠⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⣄⠀⠀⠀⠀⠀
⠀⠀⠀⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣄⠀⠀⠀
⠀⠀⣴⣿⣿⣿⣿⣿⣿⣿⠟⠿⠿⡿⠀⢰⣿⠁⢈⣿⣿⣿⣿⣿⣿⣿⣿⣦⠀⠀
⠀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣤⣄⠀⠀⠀⠈⠉⠀⠸⠿⣿⣿⣿⣿⣿⣿⣿⣿⣧⠀
⢰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡏⠀⠀⢠⣶⣶⣤⡀⠀⠈⢻⣿⣿⣿⣿⣿⣿⣿⡆
⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃⠀⠀⠼⣿⣿⡿⠃⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣷
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠀⠀⢀⣀⣀⠀⠀⠀⠀⢴⣿⣿⣿⣿⣿⣿⣿⣿⣿
⢿⣿⣿⣿⣿⣿⣿⣿⢿⣿⠁⠀⠀⣼⣿⣿⣿⣦⠀⠀⠈⢻⣿⣿⣿⣿⣿⣿⣿⡿
⠸⣿⣿⣿⣿⣿⣿⣏⠀⠀⠀⠀⠀⠛⠛⠿⠟⠋⠀⠀⠀⣾⣿⣿⣿⣿⣿⣿⣿⠇
⠀⢻⣿⣿⣿⣿⣿⣿⣿⣿⠇⠀⣤⡄⠀⣀⣀⣀⣀⣠⣾⣿⣿⣿⣿⣿⣿⣿⡟⠀
⠀⠀⠻⣿⣿⣿⣿⣿⣿⣿⣄⣰⣿⠁⢀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠀⠀
⠀⠀⠀⠙⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠋⠀⠀⠀
⠀⠀⠀⠀⠀⠙⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠋⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⠻⠿⢿⣿⣿⣿⣿⡿⠿⠟⠛⠉⠀⠀⠀⠀⠀⠀⠀⠀
          M I N I N G
         B I T C O I N⠀
'''

def delay_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.1)


print(Fore.RED, solopyblockminer, Fore.RESET)
cHeight = 0
inpAdd = input(
    f'{Fore.MAGENTA}[*]{Fore.RESET}{Fore.WHITE} INSERT HERE YOUR ADDRESS BITCOIN WALLET{Fore.RESET} : ')
address = str(inpAdd)
print(f'\n{Fore.GREY}Bitcoin Wallet Address{Fore.RESET} ===>> {Fore.MAGENTA}{address}{Fore.RESET}')
print(f"{Fore.GREY}{'-' * 66}{Fore.RESET}")
delay_print('Bitcoin Wallet Address Added For Mining Now ...')
print(f"\n{Fore.GREY}{'-' * 66}{Fore.RESET}")

time.sleep(3)


def logg(msg):
    logging.basicConfig(level=logging.INFO, filename="miner.log", format='%(asctime)s %(message)s')  # include timestamp
    logging.info(msg)


# Function to get the current network block height
def get_current_block_height():
    r = requests.get('https://blockchain.info/latestblock')
    return int(r.json()['height'])


# Function for the mining process
def BitcoinMiner(restart=False):
    # Function to handle the mining process

    if restart:
        time.sleep(2)
        logg('[*] Bitcoin Miner Restarted')
    else:
        logg('[*] Bitcoin Miner Started')
        print('[*] Bitcoin Miner Started')

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(('pool.pyblock.xyz', 3333))

    sock.sendall(b'{"id": 1, "method": "mining.subscribe", "params": []}\n')

    lines = sock.recv(1024).decode().split('\n')

    response = json.loads(lines[0])
    sub_details, extranonce1, extranonce2_size = response['result']

    sock.sendall(b'{"params": ["' + address.encode() + b'", "password"], "id": 2, "method": "mining.authorize"}\n')

    response = b''
    while response.count(b'\n') < 4 and not (b'mining.notify' in response): response += sock.recv(1024)

    responses = [json.loads(res) for res in response.decode().split('\n') if
                 len(res.strip()) > 0 and 'mining.notify' in res]
    job_id, prevhash, coinb1, coinb2, merkle_branch, version, nbits, ntime, clean_jobs = responses[0]['params']
    target = (nbits[2:] + '00' * (int(nbits[:2], 16) - 3)).zfill(64)
    extranonce2 = hex(random.randint(0, 2 ** 32 - 1))[2:].zfill(2 * extranonce2_size)  # create random

    coinbase = coinb1 + extranonce1 + extranonce2 + coinb2
    coinbase_hash_bin = hashlib.sha256(hashlib.sha256(binascii.unhexlify(coinbase)).digest()).digest()

    merkle_root = coinbase_hash_bin
    for h in merkle_branch:
        merkle_root = hashlib.sha256(hashlib.sha256(merkle_root + binascii.unhexlify(h)).digest()).digest()

    merkle_root = binascii.hexlify(merkle_root).decode()

    merkle_root = ''.join([merkle_root[i] + merkle_root[i + 1] for i in range(0, len(merkle_root), 2)][::-1])

    work_on = get_current_block_height()
    print(Fore.GREEN, 'Working on current Network height', Fore.WHITE, work_on)
    print(Fore.YELLOW, 'Current TARGET =', Fore.RED, target)
    z = 0
    while True:
        if cHeight > work_on:
            logg('[*] Restarting Miner')
            BitcoinMiner(restart=True)
            break

        nonce = hex(random.randint(0, 2 ** 32 - 1))[2:].zfill(8)  # nnonve   #hex(int(nonce,16)+1)[2:]
        blockheader = version + prevhash + merkle_root + nbits + ntime + nonce + \
                      '000000800000000000000000000000000000000000000000000000000000000000000000000000000000000080020000'
        hash = hashlib.sha256(hashlib.sha256(binascii.unhexlify(blockheader)).digest()).digest()
        hash = binascii.hexlify(hash).decode()

        if hash.startswith('000000000000000000000'): logg('hash: {}'.format(hash))
        print(Fore.GREEN, str(z), ' HASH :', Fore.YELLOW, ' 000000000000000000000{}'.format(hash), end='\r')
        z += 1
        if hash.startswith('000000000000000000'): logg('hash: {}'.format(hash))
        z += 1

        print(Fore.YELLOW, str(z), 'HASH :', Fore.RED, ' 000000000000000000{}'.format(hash), end='\r')
        z += 1

        if hash.startswith('000000000000000'): logg('hash: {}'.format(hash))
        print(Fore.BLUE, str(z), 'HASH :', Fore.GREEN, ' 000000000000000{}'.format(hash), end='\r')
        z += 1

        if hash.startswith('000000000000'): logg('hash: {}'.format(hash))
        print(Fore.MAGENTA, str(z), 'HASH :', Fore.YELLOW, ' 000000000000{}'.format(hash), end='\r')
        z += 1

        if hash.startswith('0000000'): logg('hash: {}'.format(hash))
        print(Fore.CYAN, str(z), 'HASH :', Fore.YELLOW, '0000000{}'.format(hash), end='\r')
        z += 1

        if hash < target:
            print('[*] New block mined')
            logg('[*] success!!')
            logg(blockheader)
            logg('hash: {}'.format(hash))

            payload = bytes(
                '{"params": ["' + address + '", "' + job_id + '", "' + extranonce2 \
                + '", "' + ntime + '", "' + nonce + '"], "id": 1, "method": "mining.submit"}\n', 'utf-8')
            sock.sendall(payload)
            logg(payload)
            ret = sock.recv(1024)
            logg(ret)

            return True


# Function to listen for new blocks
def newBlockListener():
    global cHeight

    while True:
        network_height = get_current_block_height()

        if network_height > cHeight:
            logg('[*] Network has new height %d ' % network_height)
            logg('[*] Our local is %d' % cHeight)
            cHeight = network_height
            logg('[*] Our new local after update is %d' % cHeight)

        # respect Api
        time.sleep(40)


# Main function to start the miner and block listener
if __name__ == '__main__':
    # Start the block listener and miner threads
    Thread(target=newBlockListener).start()
    time.sleep(2)
    Thread(target=BitcoinMiner).start()
