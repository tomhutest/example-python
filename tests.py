import unittest

import awesome


class TestMethods(unittest.TestCase):
    def test_smile(self):
        self.assertEqual(awesome.smile(), ":)")
        
    def test_frowny(self):
        self.assertEqual(awesome.frown(), ":(")


if __name__ == '__main__':
    unittest.main()
