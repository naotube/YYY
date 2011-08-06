# -*- coding: utf-8 -*-
"""
YYY, the myon-myon programming language interpreter.
derived from examples of PyPy tutorial by Andrew Brown
"""

import os
import sys
import codecs

class ParseError(SyntaxError):
    pass

def get_matching_bracket(bracket_map, pc):
    return bracket_map[pc]

def mainloop(program, bracket_map):
    pc = 0
    tape = Tape()

    while pc < len(program):
        code = program[pc]

        if code == ">":
            tape.advance()

        elif code == "<":
            tape.devance()

        elif code == "+":
            tape.inc()

        elif code == "-":
            tape.dec()

        elif code == ".":
            # print
            os.write(1, chr(tape.get()))

        elif code == ",":
            # read from stdin
            tape.set(ord(os.read(0, 1)[0]))

        elif code == "[" and tape.get() == 0:
            # Skip forward to the matching ]
            pc = get_matching_bracket(bracket_map, pc)

        elif code == "]" and tape.get() != 0:
            # Skip back to the matching [
            pc = get_matching_bracket(bracket_map, pc)

        pc += 1

class Tape(object):
    def __init__(self):
        self.thetape = [0]
        self.position = 0

    def get(self):
        return self.thetape[self.position]
    def set(self, val):
        self.thetape[self.position] = val
    def inc(self):
        self.thetape[self.position] += 1
    def dec(self):
        self.thetape[self.position] -= 1
    def advance(self):
        self.position += 1
        if len(self.thetape) <= self.position:
            self.thetape.append(0)
    def devance(self):
        self.position -= 1

def parse(program):
    parsed = []
    bracket_map = {}
    leftstack = []

    pc = 0
    for char in program:
        if char in ('[', ']', '<', '>', '+', '-', ',', '.'):
            parsed.append(char)

            if char == '[':
                leftstack.append(pc)
            elif char == ']':
                left = leftstack.pop()
                right = pc
                bracket_map[left] = right
                bracket_map[right] = left
            pc += 1

    return "".join(parsed), bracket_map

def YYYtoBF(program):
    """change YYY code to brainfuck code"""
    bf = ""
    pattern = ""
    Y = 0
    for c in program:
        if Y == 0 and c == u'妖':
            Y = 1
            pattern += c
        elif Y > 0 and c == u'夢':
            Y = 0
            pattern += c
        elif Y == 1:
            if c in (u'妖', u'々'):
                Y = 2
                pattern += c
        if pattern == u'妖妖夢妖妖':
            Y = 1
            pattern = u'妖妖夢妖'
        if len(pattern) >= 4 and pattern[-1] == u'夢':
            pattern = "".join(pattern)
            if pattern == u'妖々夢妖夢':
                bf += '+'
            elif pattern == u'妖夢妖々夢':
                bf += '-'
            elif pattern == u'妖夢妖夢':
                bf += '>'
            elif pattern == u'妖々夢妖々夢':
                bf += '<'
            elif pattern == u'妖夢妖妖夢':
                bf += ','
            elif pattern == u'妖妖夢妖夢':
                bf += '.'
            elif pattern == u'妖々夢妖妖夢':
                bf += '['
            elif pattern == u'妖妖夢妖々夢':
                bf += ']'
            else:
                raise ParseError(pattern)
            pattern = []
            Y = 0

    return bf

def run(argv):
    try:
        filename = argv[1]
    except IndexError:
        print "You must supply a filename"
        return 1

    program_file = codecs.open(filename, 'r', 'utf-8')
    program_contents = program_file.read()

    YYYprogram = YYYtoBF(program_contents)
    program, bm = parse(YYYprogram)
    mainloop(program, bm)

if __name__ == "__main__":
    run(sys.argv)
