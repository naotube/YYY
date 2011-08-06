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
        """jump to the matching '妖妖夢妖々夢', when the input is '妖々夢妖妖夢'"""
        program = u"妖々夢妖妖夢".encode('utf-8')
        self.assertEqual(YYY.YYYtoBF(program), '[')

    def testRightBracket(self):
        """jump to the matching '妖々夢妖妖夢', when the input is '妖妖夢妖々夢'"""
        program = u"妖妖夢妖々夢".encode('utf-8')
        self.assertEqual(YYY.YYYtoBF(program), ']')

class YYYtoBFDirtyInput(unittest.TestCase):
    def testUndefinedPattern(self):
        """'妖妖夢妖妖夢' is read as '妖妖夢妖夢'"""
        program = u"妖妖夢妖妖夢".encode('utf-8')
        self.assertEqual(YYY.YYYtoBF(program), '.')

    def testSkipCharacter(self):
        """any character will be ignored if it is not matched to the syntax"""
        program = u"妖妖夢妖妖々夢".encode('utf-8')
        self.assertEqual(YYY.YYYtoBF(program), ']')

    def testAlphabet(self):
        """alphabets are ignored"""
        program = u"ab妖々cd夢妖夢xyz".encode('utf-8')
        self.assertEqual(YYY.YYYtoBF(program), '+')

    def testDigit(self):
        """digits are ignored"""
        program = u"1妖夢2妖々2夢".encode('utf-8')
        self.assertEqual(YYY.YYYtoBF(program), '-')

    def testJapaneseKana(self):
        """Japanese Kana are ignored"""
        program = u"あの妖夢は妖夢か？".encode('utf-8')
        self.assertEqual(YYY.YYYtoBF(program), '>')

if __name__ == "__main__":
    unittest.main()
