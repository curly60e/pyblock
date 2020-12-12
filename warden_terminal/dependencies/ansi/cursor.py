#pylint: disable=C0103

from ansi.sequence import sequence


# Cursor movement
up          = sequence('A')
down        = sequence('B')
forward     = sequence('C')
back        = sequence('D')
next_line   = sequence('E')
prev_line   = sequence('F')
goto_x      = sequence('G')
goto        = sequence('H', 2)
erase       = sequence('J')
erase_data  = erase
erase_line  = sequence('K')
scroll_up   = sequence('S')
scroll_down = sequence('T')
save_cursor = sequence('s')
load_cursor = sequence('u')
