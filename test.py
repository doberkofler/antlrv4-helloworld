#!/usr/bin/env python3

import sys

from antlr4 import FileStream, CommonTokenStream, ParseTreeWalker

from out.HelloLexer import HelloLexer
from out.HelloListener import HelloListener
from out.HelloParser import HelloParser

class HelloPrintListener(HelloListener):
    def enterR(self, ctx):
        print("Hello: %s" % ctx.ID())

def main(argv):
    inp = FileStream(argv[1])
    lexer = HelloLexer(inp)
    stream = CommonTokenStream(lexer)
    parser = HelloParser(stream)
    tree = parser.r()
    printer = HelloPrintListener()
    walker = ParseTreeWalker()
    walker.walk(printer, tree)

if __name__ == "__main__":
    main(sys.argv)