import time 
import os

def countdown(t):
    while t > 0:
        screensv()
        t -= 1
        time.sleep(1)
    print("BLAST OFF!")

def screensv():
    os.system("python3 terminal_matrix/matrix.py")

print("How many seconds to count down? Enter an integer:")
seconds = input()
while not seconds.isdigit():
    screensv()
    seconds = input()
seconds = int(seconds)
countdown(seconds)
    
