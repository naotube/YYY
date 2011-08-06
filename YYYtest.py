# -*- coding: utf-8 -*-
import YYY
import unittest

class YYYtoBFGoodInput(unittest.TestCase):
    def testIncrement(self):
        """increment where the pointer is, when the input is '妖々夢妖夢'"""
        program = unicode("妖々夢妖夢", 'utf-8')
        self.assertEqual(YYY.YYYtoBF(program), '+')

    def testDecrement(self):
        """decrement where the pointer is, when the input is '妖夢妖々夢'"""
        program = unicode("妖夢妖々夢", 'utf-8')
        self.assertEqual(YYY.YYYtoBF(program), '-')

    def testRight(self):
        """increment the pointer, when the input is '妖夢妖夢'"""
        program = unicode("妖夢妖夢", 'utf-8')
        self.assertEqual(YYY.YYYtoBF(program), '>')

    def testLeft(self):
        """decrement the pointer, when the input is '妖々夢妖々夢'"""
        program = unicode("妖々夢妖々夢", 'utf-8')
        self.assertEqual(YYY.YYYtoBF(program), '<')

    def testRead(self):
        """read from stdin, when the input is '妖夢妖妖夢'"""
        program = unicode("妖夢妖妖夢", 'utf-8')
        self.assertEqual(YYY.YYYtoBF(program), ',')

    def testWrite(self):
        """write to stdout, when the input is '妖妖夢妖夢'"""
        program = unicode("妖妖夢妖夢", 'utf-8')
        self.assertEqual(YYY.YYYtoBF(program), '.')

    def testLeftBracket(self):
        """jump to the matching '妖妖夢妖々夢', when the input is '妖々夢妖妖夢'"""
        program = unicode("妖々夢妖妖夢", 'utf-8')
        self.assertEqual(YYY.YYYtoBF(program), '[')

    def testRightBracket(self):
        """jump to the matching '妖々夢妖妖夢', when the input is '妖妖夢妖々夢'"""
        program = unicode("妖妖夢妖々夢", 'utf-8')
        self.assertEqual(YYY.YYYtoBF(program), ']')

class YYYtoBFDirtyInput(unittest.TestCase):
    def testUndefinedPattern(self):
        """'妖妖夢妖妖夢' is read as '妖妖夢妖夢'"""
        program = unicode("妖妖夢妖妖夢", 'utf-8')
        self.assertEqual(YYY.YYYtoBF(program), '.')

    def testSkipCharacter(self):
        """any character will be ignored if it is not matched to the syntax"""
        program = unicode("妖妖夢妖妖々夢", 'utf-8')
        self.assertEqual(YYY.YYYtoBF(program), ']')

    def testAlphabet(self):
        """alphabets are ignored"""
        program = unicode("ab妖々cd夢妖夢xyz", 'utf-8')
        self.assertEqual(YYY.YYYtoBF(program), '+')

    def testDigit(self):
        """digits are ignored"""
        program = unicode("1妖夢2妖々2夢", 'utf-8')
        self.assertEqual(YYY.YYYtoBF(program), '-')

    def testJapaneseKana(self):
        """Japanese Kana are ignored"""
        program = unicode("あの妖夢は妖夢か？", 'utf-8')
        self.assertEqual(YYY.YYYtoBF(program), '>')

if __name__ == "__main__":
    unittest.main()
