# 7 Blocks by PyBLOCK Crew.

import hashlib
from time import sleep
import signal
import sys
signal.signal(signal.SIGINT, lambda x, y: sys.exit(0))

def hash_256(string):
    return hashlib.sha256(string.encode('utf-8')).hexdigest()


class TransactionGenerator:
    def __init__(self):
        self.random_seed = 0

    def generate_transaction(self):
        transaction_payload = 'This is a transaction between A and B. ' \
                              'We add a random seed here {} to make its hash unique'.format(self.random_seed)
        transaction_hash = hash_256(transaction_payload)
        self.random_seed += 1
        return transaction_hash


class Block:
    def __init__(self, hash_prev_block, target):
        self.transactions = []
        self.hash_prev_block = hash_prev_block
        self.hash_merkle_block = None
        self.target = target
        self.nounce = 0

    def add_transaction(self, new_transac):
        if not self.is_block_full():
            self.transactions.append(new_transac)
            self.hash_merkle_block = hash_256(str('-'.join(self.transactions)))

    def is_block_full(self):
        return len(self.transactions) >= 1000

    def is_block_ready_to_mine(self):
        return self.is_block_full()

    def __str__(self):
        return '-'.join([self.hash_merkle_block, str(self.nounce)])

    def apply_mining_step(self):
        current_block_hash = hash_256(self.__str__())
        print('CURRENT BLOCK HASH = {}, TARGET = {}'.format(current_block_hash, self.target))
        if int(current_block_hash, 16) < int(self.target, 16):
            print('\nBlock was successfully mined! You will get a reward of 50 BTC!')
            print('\nAccepted Hash Target {}.'.format(current_block_hash))
            print('\nIt took {} steps to mine it.\n'.format(self.nounce))
            return True
        else:
            self.nounce += 1
        return False


class BlockChain:
    def __init__(self):
        self.block_chain = []

    def push(self, block):
        self.block_chain.append(block)

    def notify_everybody(self):
        print('-' * 80)
        print('SPREADING TO ALL THE NODES OF THE NETWORK, THIS BLOCK HAS BEEN ADDED:\n')
        print('[Block #{}] : {}'.format(len(self.block_chain), self.get_last_block()))
        print('-' * 80)
        print('\nGenerating New Difficulty...\n')

    def get_last_block(self):
        return self.block_chain[-1]


def my_first_miner():
    last_block_header = '0e0fdddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd'
    last_block_target = '00dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd'

    block_chain = BlockChain()

    transaction_generator = TransactionGenerator()

    block = Block(last_block_header, last_block_target)
    for i in range(1500):
        block.add_transaction(transaction_generator.generate_transaction())

    assert block.is_block_full()
    assert block.is_block_ready_to_mine()

    while not block.apply_mining_step():
        continue

    block_chain.push(block)
    block_chain.notify_everybody()
    sleep(7)

    last_block_header = hash_256(str(block_chain.get_last_block()))

    block_1 = Block(last_block_header, last_block_target)

    for i in range(1232):
        block_1.add_transaction(transaction_generator.generate_transaction())

    assert block_1.is_block_full()
    assert block_1.is_block_ready_to_mine()

    while not block_1.apply_mining_step():
        continue

    block_chain.push(block_1)
    block_chain.notify_everybody()
    sleep(7)

    last_block_target = '000ddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd'

    last_block_header = hash_256(str(block_chain.get_last_block()))

    block_2 = Block(last_block_header, last_block_target)

    for i in range(1876):
        block_2.add_transaction(transaction_generator.generate_transaction())

    assert block_2.is_block_full()
    assert block_2.is_block_ready_to_mine()

    while not block_2.apply_mining_step():
        continue

    block_chain.push(block_2)
    block_chain.notify_everybody()
    sleep(7)

    last_block_target = '0000dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd'

    last_block_header = hash_256(str(block_chain.get_last_block()))

    block_3 = Block(last_block_header, last_block_target)

    for i in range(1876):
        block_3.add_transaction(transaction_generator.generate_transaction())

    assert block_3.is_block_full()
    assert block_3.is_block_ready_to_mine()

    while not block_3.apply_mining_step():
        continue

    block_chain.push(block_3)
    block_chain.notify_everybody()
    sleep(7)

    last_block_target = '00000ddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd'

    last_block_header = hash_256(str(block_chain.get_last_block()))

    block_4 = Block(last_block_header, last_block_target)

    for i in range(1876):
        block_4.add_transaction(transaction_generator.generate_transaction())

    assert block_4.is_block_full()
    assert block_4.is_block_ready_to_mine()

    while not block_4.apply_mining_step():
        continue

    block_chain.push(block_4)
    block_chain.notify_everybody()
    sleep(7)

    last_block_target = '000000dddddddddddddddddddddddddddddddddddddddddddddddddddddddddd'

    last_block_header = hash_256(str(block_chain.get_last_block()))

    block_5 = Block(last_block_header, last_block_target)

    for i in range(1876):
        block_5.add_transaction(transaction_generator.generate_transaction())

    assert block_5.is_block_full()
    assert block_5.is_block_ready_to_mine()

    while not block_5.apply_mining_step():
        continue

    block_chain.push(block_5)
    block_chain.notify_everybody()
    sleep(7)

    last_block_target = '0000000ddddddddddddddddddddddddddddddddddddddddddddddddddddddddd'

    last_block_header = hash_256(str(block_chain.get_last_block()))

    block_6 = Block(last_block_header, last_block_target)

    for i in range(1876):
        block_6.add_transaction(transaction_generator.generate_transaction())

    assert block_6.is_block_full()
    assert block_6.is_block_ready_to_mine()

    while not block_6.apply_mining_step():
        continue

    block_chain.push(block_6)
    block_chain.notify_everybody()
    sleep(7)

    print('')
    print('SUMMARY')
    print('')
    for i, block_added in enumerate(block_chain.block_chain):
        print('Block #{} was added. It took {} steps to find it.'.format(i, block_added.nounce))
    print('\nDifficulty was increased for the last 7 Blocks!\n')
    print('\n7 Blocks Mined Successfully!\n')


if __name__ == '__main__':
    my_first_miner()
