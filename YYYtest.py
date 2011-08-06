# -*- coding: utf-8 -*-
import YYY
import unittest

class testYYYtoBF(unittest.TestCase):
    def testIncrement(self):
        """increment where the pointer is, when the input is '妖々夢妖夢'"""
        program = u"妖々夢妖夢".encode('utf-8')
        self.assertEqual(YYY.YYYtoBF(program), '+')

if __name__ == "__main__":
    unittest.main()
