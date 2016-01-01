# coding: utf-8
from __future__ import unicode_literals
import unittest

import locale
import sys


def preferredencoding():
    """Get preferred encoding.

    Returns the best encoding scheme for the system, based on
    locale.getpreferredencoding() and some further tweaks.
    """
    try:
        pref = locale.getpreferredencoding()
        'TEST'.encode(pref)
    except Exception:
        pref = 'UTF-8'

    return pref


def write_string(s, out=sys.stdout, encoding=None):
    if ('b' in getattr(out, 'mode', '') or
            sys.version_info[0] < 3):  # Python 2 lies about mode of sys.stderr
        byt = s.encode(encoding or preferredencoding(), 'ignore')
        out.write(byt)
    elif hasattr(out, 'buffer'):
        enc = encoding or getattr(out, 'encoding', None) or preferredencoding()
        byt = s.encode(enc, 'ignore')
        out.buffer.write(byt)
    else:
        out.write(s)
    out.flush()


class TestFoo(unittest.TestCase):
    def test_failed(self):
        write_string('a' * 1000)
        write_string('中文')
        sys.stdout.write('中文')

        raise Exception('中文')

if __name__ == '__main__':
    unittest.main()
