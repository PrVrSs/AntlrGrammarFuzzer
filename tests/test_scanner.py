from generator import ScannerAntl, TokenType


# Test lexical analyzer

def test_simple_rule():
    rule_string = """SELECT 1"""
    scanner = ScannerAntl(rule_string)
    tokens = scanner.scan_tokens()
    token = tokens[0]
    assert token.token_type is TokenType.NONTERMINAL
    assert token.lexeme == "SELECT"
    token = tokens[1]
    assert token.token_type is TokenType.NONTERMINAL
    assert token.lexeme == "1"


def test_rule_with_parenthesis():
    rule_string = """
        (
          STARTS start=timestampValue 
        )
        """
    scanner = ScannerAntl(rule_string)
    tokens = scanner.scan_tokens()
    token = tokens[0]
    assert token.token_type is TokenType.LEFT_PAREN
    assert token.lexeme == "("

    token = tokens[1]
    assert token.token_type is TokenType.NONTERMINAL
    assert token.lexeme == "STARTS"

    token = tokens[2]
    assert token.token_type is TokenType.NONTERMINAL
    assert token.lexeme == "start"

    token = tokens[3]
    assert token.token_type is TokenType.EQUAL
    assert token.lexeme == "="

    token = tokens[4]
    assert token.token_type is TokenType.NONTERMINAL
    assert token.lexeme == "timestampValue"


def test_rule_with_question():
    rule_string = """KEY_BLOCK_SIZE '='? fileSizeLiteral"""
    scanner = ScannerAntl(rule_string)
    tokens = scanner.scan_tokens()
    token = tokens[0]
    assert token.token_type is TokenType.NONTERMINAL
    assert token.lexeme == "KEY_BLOCK_SIZE"

    token = tokens[1]
    assert token.token_type is TokenType.TERMINAL
    assert token.lexeme == "'='"

    token = tokens[2]
    assert token.token_type is TokenType.QUESTION
    assert token.lexeme == "?"

    token = tokens[3]
    assert token.token_type is TokenType.NONTERMINAL
    assert token.lexeme == "fileSizeLiteral"


def test_rule_with_star():
    rule_string = """SUBPARTITION uid partitionOption*"""
    scanner = ScannerAntl(rule_string)
    tokens = scanner.scan_tokens()
    token = tokens[0]
    assert token.token_type is TokenType.NONTERMINAL
    assert token.lexeme == "SUBPARTITION"

    token = tokens[1]
    assert token.token_type is TokenType.NONTERMINAL
    assert token.lexeme == "uid"

    token = tokens[2]
    assert token.token_type is TokenType.NONTERMINAL
    assert token.lexeme == "partitionOption"

    token = tokens[3]
    assert token.token_type is TokenType.STAR
    assert token.lexeme == "*"


def test_rule_with_plus_and_slash():
    rule_string = """ALTER dbFormat=(DATABASE | SCHEMA) uid? createDatabaseOption+"""
    scanner = ScannerAntl(rule_string)
    tokens = scanner.scan_tokens()
    token = tokens[0]
    assert token.token_type is TokenType.NONTERMINAL
    assert token.lexeme == "ALTER"

    token = tokens[1]
    assert token.token_type is TokenType.NONTERMINAL
    assert token.lexeme == "dbFormat"

    token = tokens[2]
    assert token.token_type is TokenType.EQUAL
    assert token.lexeme == "="

    token = tokens[3]
    assert token.token_type is TokenType.LEFT_PAREN
    assert token.lexeme == "("

    token = tokens[4]
    assert token.token_type is TokenType.NONTERMINAL
    assert token.lexeme == "DATABASE"

    token = tokens[5]
    assert token.token_type is TokenType.SLASH
    assert token.lexeme == "|"

    token = tokens[6]
    assert token.token_type is TokenType.NONTERMINAL
    assert token.lexeme == "SCHEMA"

    token = tokens[7]
    assert token.token_type is TokenType.RIGHT_PAREN
    assert token.lexeme == ")"

    token = tokens[8]
    assert token.token_type is TokenType.NONTERMINAL
    assert token.lexeme == "uid"

    token = tokens[9]
    assert token.token_type is TokenType.QUESTION
    assert token.lexeme == "?"

    token = tokens[10]
    assert token.token_type is TokenType.NONTERMINAL
    assert token.lexeme == "createDatabaseOption"

    token = tokens[11]
    assert token.token_type is TokenType.PLUS
    assert token.lexeme == "+"
