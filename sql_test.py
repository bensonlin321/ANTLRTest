from antlr4 import *
from pockets.grammar.pocketsLexer import pocketsLexer
from pockets.grammar.pocketsListener import pocketsListener
from pockets.grammar.pocketsParser import pocketsParser
import sys

class PocketsPrintListener(pocketsListener):
    '''
    def enterStatement(self, ctx):
        print("=== all the attributes ===")
        print(dir(ctx))
        print("=== ctx object ===")
        print(ctx)

        print("=== test ===")
        print(ctx.getTokens())
        #print("Statement is: %s" % ctx.toString())
    '''
    def exitStatement(self, node):
        value = str(node.getText())
        #print(f"node.children: {node.children}")
        #print(f"node.children[0].getText(): {node.children[0].getText()}")
        print(f"get Statement: {value}")

    def exitIdentifier(self, node):
        value = str(node.getText())
        print(f"get exitIdentifier: {value}")
        self.stack.append(value)

    def run(self, node):
        self.stack = []
        self.vars = {}
        ParseTreeWalker().walk(self, node)
        #result = self.stack[0]
        print(self.stack)


def main():
    # from Stdin
    lexer = pocketsLexer(StdinStream())
    stream = CommonTokenStream(lexer)
    parser = pocketsParser(stream)
    # use pocket grammar (check pockets.g4 file)
    tree = parser.pocket()
    PocketsPrintListener().run(tree)
    #printer = PocketsPrintListener()
    #walker = ParseTreeWalker()
    #walker.walk(printer, tree)

if __name__ == '__main__':
    #input_str = sys.argv[1]
    #main(input_str)
    main()
