from .token import Token
from .tokentype import TokenType


class ScannerAntl(object):

    __slots__ = ['source', 'tokens', '_start', '_current']

    def __init__(self, source):
        self.source = source
        self.tokens = []
        self._start = 0
        self._current = 0

    def scan_tokens(self):
        while not self._is_at_end():
            self._start = self._current
            self.scan_token()
        self.tokens.append(Token(TokenType.EOF, '', None,))
        return self.tokens

    def scan_token(self):
        char = self._advance()
        if char == '(':
            self.add_token(TokenType.LEFT_PAREN)
        elif char == ')':
            self.add_token(TokenType.RIGHT_PAREN)
        if char == '[':
            self.add_token(TokenType.LEFT_SQUARE)
        elif char == ']':
            self.add_token(TokenType.RIGHT_SQUARE)
        elif char == '+':
            self.add_token(TokenType.PLUS_EQUAL if self._match('=') else TokenType.PLUS)
        elif char == '.':
            self.add_token(TokenType.DOT)
        elif char == '*':
            self.add_token(TokenType.STAR)
        elif char == '=':
            self.add_token(TokenType.EQUAL)
        elif char == '/':
            if self._match('/'):
                while self._peek() != '\n' and not self._is_at_end():
                    self._advance()
        elif char == '-':
            if self._match('>'):
                pass
        elif char == '~':
            self.add_token(TokenType.TILDE)
        elif char == '|':
            self.add_token(TokenType.SLASH)
        elif char == '?':
            self.add_token(TokenType.QUESTION)
        elif char in [' ', '\r', '\t', '\n']:
            pass
        elif char == '#':
            while self._peek() != '\n' and not self._is_at_end():
                self._advance()
        elif char == "'":
            self.constant()
        elif self._is_alpha(char):
            self.identifier()

    def new_line(self):
        self.tokens.append(Token(TokenType.NEW_LINE, '\\n', None))

    def identifier(self):
        while self._is_alpha(self._peek()):
            self._advance()
        token_type = TokenType.NONTERMINAL
        self.add_token(token_type)

    def constant(self):
        while (self._peek() != "'")and not self._is_at_end():
            self._advance()
        self._advance()
        while self._match('\''):
            pass
        value = self.source[self._start + 1:self._current - 1]
        self.add_token(TokenType.TERMINAL, value)

    def add_token(self, token_type, literal=None):
        text = self.source[self._start:self._current]
        self.tokens.append(Token(token_type, text, literal))

    def _peek(self):
        if self._current >= len(self.source):
            return '\0'
        return self.source[self._current]

    def _advance(self):
        self._current += 1
        return self.source[self._current - 1]

    @staticmethod
    def _is_alpha(c):
        return (97 <= ord(c) <= 122) or (65 <= ord(c) <= 90) or ord(c) == 95 or (48 <= ord(c) <= 57) or ord(c) == 45 or ord(c) == 36 or ord(c) == 46

    def _match(self, expected):
        if self._is_at_end():
            return False
        if self.source[self._current] != expected:
            return False
        self._current += 1
        return True

    def _is_at_end(self):
        return self._current >= len(self.source)
