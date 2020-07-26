#Developer: Curly60e
#PyBLOCK its a clock of the Bitcoin blockchain.

import os
import pickle
from cfonts import render, say

def blogo():

    if os.path.isfile('pyblocksettings.conf') or os.path.isfile('pyblocksettings.conf'): # Check if the file 'bclock.conf' is in the same folder
        settingsv = pickle.load(open("pyblocksettings.conf", "rb")) # Load the file 'bclock.conf'
        settings = settingsv # Copy the variable pathv to 'path'
    else:
        settings = {"gradient":"", "design":"block", "colorA":"green", "colorB":"yellow"}
        pickle.dump(settings, open("pyblocksettings.conf", "wb"))

    if settings["gradient"] == "grd":
        output = render('PyBLOCK', gradient=[settings['colorA'], settings['colorB']], align='left', font=settings['design'])
    else:
        output = render('PyBLOCK', colors=[settings['colorA'], settings['colorB']], align='left', font=settings['design'])

    print(output)

def tick():
    print("""\033[1;32;40m




                             @
                              @
                               @
                               @@
                                @@
                                @@@
                            @@@  @@.
                             @@@@@@@
                             @@@@@@@@
                              @@@@
                               @@@@
                           @    @@@@
                            @@@@@@@@
                             @@@@@@@@
                              @@@
                               @@@
                                @@
                                 @@
                                   @
                                    @






\033[0;37;40m""")

def canceled():
    print("""
                   )              (         (
   (     (      ( /(    (         )\ )      )\ )
   )\    )\     )\())   )\   (   (()/(  (  (()/(
 (((_)((((_)(  ((_)\  (((_)  )\   /(_)) )\  /(_))
 )\___ )\ _ )\  _((_) )\___ ((_) (_))  ((_)(_))_
((/ __|(_)_\(_)| \| |((/ __|| __|| |   | __||   \
 | (__  / _ \  | .` | | (__ | _| | |__ | _| | |) |
  \___|/_/ \_\ |_|\_|  \___||___||____||___||___/

""")
