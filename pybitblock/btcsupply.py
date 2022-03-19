#!/usr/bin/env python
# -*- coding: utf8 -*-


def btcSupplyAtBlock(b):
    if b >= 33 * 210000:
        return 20999999.9769
    reward = 50e8
    supply = 0
    y = 210000  # reward changes all y blocks
    while b > y - 1:
        supply = supply + y * reward
        reward = int(reward / 2.0)
        b = b - y
    supply = supply + b * reward
    return (supply + reward) / 1e8


if __name__ == "__main__":
    block = 777777  # you want the supply after which block?
    print(btcSupplyAtBlock(block))
