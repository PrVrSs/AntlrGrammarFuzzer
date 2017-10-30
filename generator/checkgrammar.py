from antlr4 import CommonTokenStream, BailErrorStrategy
from antlr4.atn.PredictionMode import PredictionMode
from antlr4.error.Errors import ParseCancellationException, InputStream
from grammar.antlr4.mysql.mysqlParser import mysqlParser
from grammar.antlr4.mysql.mysqlLexer import mysqlLexer
from antlr4.Utils import escapeWhitespace
from antlr4.tree.Trees import Trees
from grammar.antlr4.tsql.TSqlLexer import TSqlLexer
from grammar.antlr4.tsql.TSqlParser import TSqlParser


class TreePrinter(Trees):
    """
    It is used to print a parse tree.
    """
    @classmethod
    def toDictionaryTree(cls, t, rule_names=None, recog=None):
        """ Converts  a parse tree to a dictionary. """
        tree = {"name": "", "children": []}
        if recog is not None:
            rule_names = recog.ruleNames
        s = escapeWhitespace(cls.getNodeText(t, rule_names), False)
        tree["name"] = s
        if t.getChildCount() == 0:
            return tree
        for i in range(0, t.getChildCount()):
            a = cls.toDictionaryTree(t.getChild(i), rule_names)
            tree["children"].append(a)
        return tree


class CheckMySQLAntlr(object):
    def __init__(self):
        self.lexer = mysqlLexer(None)
        self.parser = mysqlParser(None)
        self.parser._errHandler = BailErrorStrategy()
        self.parser.removeErrorListeners()

    def parse(self, text):
        char_stream = InputStream(text)
        self.lexer.inputStream = char_stream
        token_stream = CommonTokenStream(self.lexer)
        self.parser.setInputStream(token_stream)
        self.parser._interp.predictionMode = PredictionMode.SLL
        try:
            tree = self.parser.root()
        except ParseCancellationException:
            pass
        else:
            return tree
        token_stream.reset()
        self.parser.reset()
        self.parser._interp.predictionMode = PredictionMode.LL
        try:
            tree = self.parser.root()
        except ParseCancellationException:
            tree = None
        return tree

    def check_syntax(self, input_data: str=''):
        is_valid = False
        tree = self.parse(input_data)
        if tree:
            is_valid = True
        return is_valid

    def parse_lines(self, query):
        is_valid = self.check_syntax(query)
        print("Code is valid: " + str(is_valid))


class AntlrTree(object):

    def __init__(self, query: str):
        input_data = query
        input_ = InputStream(input_data)
        lexer = mysqlLexer(input_)
        self.stream = CommonTokenStream(lexer)
        self.parser = mysqlParser(self.stream)
        self.tree = self.parser.root()

    def get_tree(self):
        return TreePrinter.toDictionaryTree(self.tree, None, self.parser)


class CheckTSQLAntlr(object):
    def __init__(self):
        self.lexer = TSqlLexer(None)
        self.parser = TSqlParser(None)

        self.parser._errHandler = BailErrorStrategy()
        self.parser.removeErrorListeners()

    def parse(self, text):
        # errListener = ErrorListener()
        # self.lexer.removeErrorListeners()
        # self.lexer.addErrorListener(errListener)
        char_stream = InputStream(text)
        self.lexer.inputStream = char_stream
        token_stream = CommonTokenStream(self.lexer)
        self.parser.setInputStream(token_stream)
        self.parser._interp.predictionMode = PredictionMode.SLL

        try:
            tree = self.parser.tsql_file()

        except ParseCancellationException:
            pass
        else:
            return tree
        token_stream.reset()
        self.parser.reset()
        self.parser._interp.predictionMode = PredictionMode.LL
        try:
            tree = self.parser.tsql_file()
        except ParseCancellationException:
            tree = None
        return tree

    def check_syntax(self, input_data: str=''):
        is_valid = False
        tree = self.parse(input_data)
        if tree:
            is_valid = True
        return is_valid

    def parse_lines(self, query):
        is_valid = self.check_syntax(query)
        print("Code is valid: " + str(is_valid))


def main():
    a = CheckMySQLAntlr()
    query = '''DESC ` UTF8 ` select * from t'''
    a.parse_lines(query)
    # Parser()


if __name__ == "__main__":
    main()
