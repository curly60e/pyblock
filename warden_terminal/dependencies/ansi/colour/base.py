#pylint: disable=C0103,R0903

from ansi.sequence import sequence
from ansi._compat import string_types


__all__ = ['Graphic']


class Graphic(object):
    '''
    Compose a Select Graphic Rendition (SGR) ANSI escape sequence.
    '''

    def __init__(self, *values):
        self.values = values
        self.sequence = sequence('m', fields=-1)(*values)

    def __add__(self, their):
        if isinstance(their, str):
            return ''.join([str(self), their])
        elif isinstance(their, string_types):
            raise ValueError('Use str, nothing else.')
        else:
            return Graphic(*(self.values + their.values))

    def __call__(self, text, reset=True):
        result = self.sequence + text
        if reset:
            result += str(Graphic('0'))
        return result

    def __str__(self):
        return self.sequence
