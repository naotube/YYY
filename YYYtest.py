# -*- coding: utf-8 -*-
import YYY
import unittest

class YYYtoBFGoodInput(unittest.TestCase):
    def testIncrement(self):
        """increment where the pointer is, when the input is '妖々夢妖夢'"""
        program = u"妖々夢妖夢".encode('utf-8')
        self.assertEqual(YYY.YYYtoBF(program), '+')

    def testDecrement(self):
        """decrement where the pointer is, when the input is '妖夢妖々夢'"""
        program = u"妖夢妖々夢".encode('utf-8')
        self.assertEqual(YYY.YYYtoBF(program), '-')

    def testRight(self):
        """increment the pointer, when the input is '妖夢妖夢'"""
        program = u"妖夢妖夢".encode('utf-8')
        self.assertEqual(YYY.YYYtoBF(program), '>')

    def testLeft(self):
        """decrement the pointer, when the input is '妖々夢妖々夢'"""
        program = u"妖々夢妖々夢".encode('utf-8')
        self.assertEqual(YYY.YYYtoBF(program), '<')

    def testRead(self):
        """read from stdin, when the input is '妖夢妖妖夢'"""
        program = u"妖夢妖妖夢".encode('utf-8')
        self.assertEqual(YYY.YYYtoBF(program), ',')

    def testWrite(self):
        """write to stdout, when the input is '妖妖夢妖夢'"""
        program = u"妖妖夢妖夢".encode('utf-8')
        self.assertEqual(YYY.YYYtoBF(program), '.')

    def testLeftBracket(self):
        """increment where the pointer is, when the input is '妖々夢妖夢'"""
        program = u"妖々夢妖妖夢".encode('utf-8')
        self.assertEqual(YYY.YYYtoBF(program), '[')

    def testRightBracket(self):
        """increment where the pointer is, when the input is '妖々夢妖夢'"""
        program = u"妖妖夢妖々夢".encode('utf-8')
        self.assertEqual(YYY.YYYtoBF(program), ']')

if __name__ == "__main__":
    unittest.main()
