##SN PyVanityGen Vanity Generator PyBLOCK Crew##

import os
from bitcoinlib.keys import HDKey
import timeit
import random
import multiprocessing


witness_type = 'segwit'

def address_search(search_for='l200wd'):
    global witness_type
    privkey = random.randrange(2**256)
    address = ''
    count = 0
    start = timeit.default_timer()

    bech32 = "qpzry9x8gf2tvdw0s3jn54khce6mua7l"
    base58 = '123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz'
    is_bech32 = True
    is_base58 = True
    for letter in search_for:
        if letter not in bech32:
            is_bech32 = False
        if letter not in base58:
            is_base58 = False
    if not (is_bech32 or is_base58):
        raise ValueError(f"This is not a valid base58 or bech32 search string: {search_for}")
    if is_base58 and not is_bech32:
        witness_type = 'p2sh-segwit'

    print(f"PyBLOCK Searching for {search_for}, witness_type is {witness_type} (pid {os.getpid()})")

    while not search_for in address:
        privkey += 1
        k = HDKey(witness_type=witness_type)
        address = k.address()
        count += 1
        if not count % 10000:
            print("PyBLOCK Searched %d in %d seconds (pid %d)" % (count, timeit.default_timer()-start, os.getpid()))

    print("PyBLOCK Found Address %s" % address)
    print("Private Key HEX %s" % k.private_hex)
    return((address, k.private_hex))


def main():
    processors = 8
    print("PyBLOCK Starting %d processes" % processors)
    ps = []
    for i in range(processors):
        print("PyBLOCK Starting process %d" % i)
        p = multiprocessing.Process(target=address_search)
        p.start()
        ps.append(p)


main()
