from generator import ScannerAntl, Parser, Ast
from generator.scanner.antlrexpr import *


def test_simple_rule():
    rule_string = """SELECT 1"""
    scanner = ScannerAntl(rule_string)
    tokens = scanner.scan_tokens()
    parser = Parser(tokens)
    tree = parser.parse()
    ast = Ast(tree)
    list_antlr4_expr = ast.get_ast()
    antlr4_expr = list_antlr4_expr[0]
    assert isinstance(antlr4_expr, Literal)
    assert antlr4_expr.value == 'SELECT'
    antlr4_expr = list_antlr4_expr[1]
    assert isinstance(antlr4_expr, Literal)
    assert antlr4_expr.value == '1'


def test_rule_with_parenthesis():
    rule_string = """
                (
                STARTS start=timestampValue
                )
                """
    scanner = ScannerAntl(rule_string)
    tokens = scanner.scan_tokens()
    parser = Parser(tokens)
    tree = parser.parse()
    ast = Ast(tree)
    list_antlr4_expr = ast.get_ast()
    antlr4_expr = list_antlr4_expr[0]
    assert isinstance(antlr4_expr, Literal)
    assert antlr4_expr.value == 'STARTS'
    antlr4_expr = list_antlr4_expr[1]
    assert isinstance(antlr4_expr, Literal)
    assert antlr4_expr.value == 'timestampValue'


def test_rule_with_plus():
    rule_string = """querySpecificationNointo unionStatement+"""
    scanner = ScannerAntl(rule_string)
    tokens = scanner.scan_tokens()
    parser = Parser(tokens)
    tree = parser.parse()
    ast = Ast(tree)
    ast._default_min_one = 2
    ast._multiplication_scale = 2
    list_antlr4_expr = ast.get_ast()

    antlr4_expr = list_antlr4_expr[0]
    assert isinstance(antlr4_expr, Literal)
    assert antlr4_expr.value == 'querySpecificationNointo'

    antlr4_expr = list_antlr4_expr[1]
    assert isinstance(antlr4_expr, Literal)
    assert antlr4_expr.value == 'unionStatement'

    antlr4_expr = list_antlr4_expr[2]
    assert isinstance(antlr4_expr, Literal)
    assert antlr4_expr.value == 'unionStatement'


def test_rule_with_or():
    rule_string = """
        expr NEWLINE
        | ID '=' expr NEWLINE
        | NEWLINE
    """
    scanner = ScannerAntl(rule_string)
    tokens = scanner.scan_tokens()
    parser = Parser(tokens)
    tree = parser.parse()
    ast = Ast(tree)
    ast._default_min_or = 1
    list_antlr4_expr = ast.get_ast()
    antlr4_expr = list_antlr4_expr[0]
    assert isinstance(antlr4_expr, Literal)
    assert antlr4_expr.value == 'expr'

    antlr4_expr = list_antlr4_expr[1]
    assert isinstance(antlr4_expr, Literal)
    assert antlr4_expr.value == 'NEWLINE'

    ast = Ast(tree)
    ast._default_max_or = 0
    list_antlr4_expr = ast.get_ast()
    antlr4_expr = list_antlr4_expr[0]
    assert isinstance(antlr4_expr, Literal)
    assert antlr4_expr.value == 'NEWLINE'


def test_rule_with_question():
    rule_string = """
    fullId '.' '*'                   #selectStarElement
    | fullColumnName (AS? uid)?      #selectColumnElement
    """
    scanner = ScannerAntl(rule_string)
    tokens = scanner.scan_tokens()
    parser = Parser(tokens)
    tree = parser.parse()
    ast = Ast(tree)
    ast._default_max_or = 0
    ast._default_min_zero = 1
    list_antlr4_expr = ast.get_ast()

    antlr4_expr = list_antlr4_expr[0]
    assert isinstance(antlr4_expr, Literal)
    assert antlr4_expr.value == 'fullColumnName'

    antlr4_expr = list_antlr4_expr[1]
    assert isinstance(antlr4_expr, Literal)
    assert antlr4_expr.value == 'AS'

    antlr4_expr = list_antlr4_expr[2]
    assert isinstance(antlr4_expr, Literal)
    assert antlr4_expr.value == 'uid'
