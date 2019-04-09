from agf.antlr4_parser.scanner import ScannerAntl
from agf.antlr4_parser.parser import Parser
from agf.antlr4_parser.expressions import *


def test_simple_rule():
    rule_string = """SELECT 1"""
    scanner = ScannerAntl(rule_string)
    tokens = scanner.scan_tokens()
    parser = Parser(tokens)
    tree = parser.parse()
    assert isinstance(tree[0], Grouping)
    value = tree[0].value[0]
    assert isinstance(value, Literal)
    assert value.value == 'SELECT'
    value = tree[0].value[1]
    assert isinstance(value, Literal)
    assert value.value == '1'
