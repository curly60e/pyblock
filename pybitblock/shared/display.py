"""
Shared display utilities for PyBLOCK.

These functions are used by both PyBlock.py and SPV/spvblock.py.
"""

import os
import subprocess
import sys
import time

import psutil


def clear():
    subprocess.run(['clear'] if os.name != 'nt' else ['cls'], shell=(os.name == 'nt'))


def close():
    print("<<< Ctrl + C.\n\n")


def sysinfo():
    try:
        from shared.rich_ui import rich_sysinfo
        cpu = psutil.cpu_percent()
        mem = int(psutil.virtual_memory().percent)
        rich_sysinfo(cpu, mem)
    except ImportError:
        print("    \033[0;37;40m----------------------")
        print("    \033[3;33;40mCPU Usage: \033[1;32;40m" + str(psutil.cpu_percent()) + "%\033[0;37;40m")
        print(
            f"    \033[3;33;40mMemory Usage: \033[1;32;40m{int(psutil.virtual_memory().percent)}% \033[0;37;40m"
        )
        print("    \033[0;37;40m----------------------")


def rectangle(n):
    x = n - 3
    y = n - x
    [
        print(''.join(i))
        for i in
        (
            '' * x
            if i in (0, y - 1)
            else
            (
                f'{"" * n}{"|" * n}{"" * n}'
                if i >= (n + 1) / 2 and i <= (1 * n) / 2
                else f'{"" * n}{"|" * n}{"" * n}'
            )
            for i in range(y)
        )
    ]


def delay_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.25)
