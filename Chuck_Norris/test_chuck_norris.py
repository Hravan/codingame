import unittest

from chuck_norris import *

class TestEncodeToUnary(unittest.TestCase):

    def test_C(self):
        m = 'C'
        self.assertEqual(encode_to_unary(m), '0 0 00 0000 0 00')

    def test_CC(self):
        m = 'CC'
        self.assertEqual(encode_to_unary(m), '0 0 00 0000 0 000 00 0000 0 00')

    def test_empty_str(self):
        m = ''
        self.assertEqual(encode_to_unary(m), '')

    def test_percent(self):
        m = '%'
        self.assertEqual(encode_to_unary(m), '00 0 0 0 00 00 0 0 00 0 0 0')

    #def test_three_chars(self):
    #    m = 'ABC'
    #    self.assertEqual(encode_to_unary(m), '')


class TestASCIIToBinary(unittest.TestCase):

    def test_C(self):
        t = 'C'
        self.assertEqual(asci_to_binary(t), '1000011')

    def test_CC(self):
        t = 'CC'
        self.assertEqual(asci_to_binary(t), '10000111000011')

    def test_empty_str(self):
        t = ''
        self.assertEqual(asci_to_binary(t), '')

if __name__ == '__main__':
    unittest.main()
