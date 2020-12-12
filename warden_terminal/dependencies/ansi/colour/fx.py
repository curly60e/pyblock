#pylint: disable=C0103,R0903

from ansi.colour.base import Graphic


# ECMA-048 standard names
reset            = Graphic('0')
bold             = Graphic('1')
faint            = Graphic('2')
italic           = Graphic('3')
underline        = Graphic('4')
blink_slow       = Graphic('5')
blink            = Graphic('6')
negative         = Graphic('7')
conceal          = Graphic('8')
crossed_out      = Graphic('9')
font_reset       = Graphic('10')
font_1           = Graphic('11')
font_2           = Graphic('12')
font_3           = Graphic('13')
font_4           = Graphic('14')
font_5           = Graphic('15')
font_6           = Graphic('16')
font_7           = Graphic('17')
font_8           = Graphic('18')
font_9           = Graphic('19')
fraktur          = Graphic('20')
gothic           = Graphic('20')
underline_double = Graphic('21')
normal           = Graphic('22')
not_italic       = Graphic('23')
not_fraktur      = Graphic('23')
not_gothic       = Graphic('23')
not_underline    = Graphic('24')
steady           = Graphic('25')
positive         = Graphic('27')
reveal           = Graphic('28')
framed           = Graphic('51')
encircled        = Graphic('52')
overlined        = Graphic('53')
not_framed       = Graphic('54')
not_encircled    = Graphic('54')
not_overlined    = Graphic('55')

# Convenience wrappers
inverse          = negative
bright           = bold
not_blink        = steady
blink_off        = steady
