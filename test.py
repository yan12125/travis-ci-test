# coding: utf-8
import unittest


class TestFoo(unittest.TestCase):
    def test_failed(self):
        print('中文')
        raise Exception('中文')

if __name__ == '__main__':
    unittest.main()
