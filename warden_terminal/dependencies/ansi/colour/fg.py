#pylint: disable=C0103,R0903

from ansi.colour.base import Graphic
from ansi.colour.fx import bold


# ECMA-048 standard names
black           = Graphic('30')
red             = Graphic('31')
green           = Graphic('32')
yellow          = Graphic('33')
blue            = Graphic('34')
magenta         = Graphic('35')
cyan            = Graphic('36')
white           = Graphic('37')
default         = Graphic('39')

# ECMA-048 bold variants
boldblack       = bold + black
boldred         = bold + red
boldgreen       = bold + green
boldyellow      = bold + yellow
boldblue        = bold + blue
boldmagenta     = bold + magenta
boldcyan        = bold + cyan
boldwhite       = bold + white

# High intensity variants
brightblack     = Graphic('90')
brightred       = Graphic('91')
brightgreen     = Graphic('92')
brightyellow    = Graphic('93')
brightblue      = Graphic('94')
brightmagenta   = Graphic('95')
brightcyan      = Graphic('96')
brightwhite     = Graphic('97')

# Convenience wrappers
brown           = yellow                # Not in ANSI/ECMA-048 standard
grey            = white                 # Not in ANSI/ECMA-048 standard
gray            = white                 # US English
darkgrey        = boldblack
darkgray        = boldblack             # US English
brightbrown     = boldyellow            # Not in ANSI/ECMA-048 standard
brightgrey      = boldwhite             # Not in ANSI/ECMA-048 standard
brightgray      = boldwhite             # Us English
