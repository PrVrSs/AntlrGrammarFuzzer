from generator.scanner.antlrexpr import *
from generator.scanner.tokentype import TokenType


class Parser(object):

    def __init__(self, token_list):
        self._current = 0
        self.token_list = token_list

    def parse(self):
        return self._choice()

    def _choice(self):
        expr = Grouping(self._expression())
        while not self._is_at_end():
            if self._is_at_right_paren() or self._is_at_right_square():
                break
            operator = self._previous()
            right = Grouping(self._expression())
            expr = Choice(left=expr, operator=operator, right=right)
        return [expr]

    def _expression(self):
        tree = []
        while not self._match(TokenType.SLASH):
            if self._is_at_right_paren() or self._is_at_right_square():
                break
            if self._is_at_end():
                break
            expr = self._equal()
            tree.append(expr)
        return tree

    def _equal(self):
        expr = self._multiplication()
        if self._match(TokenType.EQUAL, TokenType.PLUS_EQUAL):    # need fix TokenType.PLUS_EQUAL
            expr = self._multiplication()
            expr = Equal(value=expr)
        return expr

    def _multiplication(self):
        expr = self._tilde()
        if self._match(TokenType.STAR):
            expr = StarMultiplication(expr)
        elif self._match(TokenType.PLUS):
            expr = PlusMultiplication(expr)
        return expr

    def _tilde(self):
        if self._match(TokenType.TILDE):
            expr = self._primary()
            expr = Tilde(expr)
        else:
            expr = self._primary()
        return expr

    def _primary(self):
        if self._match(TokenType.DOT):
            if self._match(TokenType.STAR):
                return RandomLiteral(StarMultiplication(Literal(self.token_list[self._current - 2].lexeme))) if self._match(TokenType.QUESTION) else StarMultiplication(Literal(self._previous().lexeme))
            elif self._match(TokenType.PLUS):
                return RandomLiteral(PlusMultiplication(Literal(self.token_list[self._current - 2].lexeme))) if self._match(TokenType.QUESTION) else PlusMultiplication(Literal(self._previous().lexeme))
            elif self._match(TokenType.QUESTION):
                return RandomLiteral(Literal(self.token_list[self._current - 2].lexeme))
            return Literal(self._previous().lexeme)
        if self._match(TokenType.NONTERMINAL, TokenType.TERMINAL):

            if self._match(TokenType.QUESTION):
                return RandomLiteral(Literal(self.token_list[self._current - 2].lexeme))  # check!
            return Literal(self._previous().lexeme)
        if self._match(TokenType.LEFT_PAREN, TokenType.LEFT_SQUARE):
            expr = []
            while not self._match(TokenType.RIGHT_PAREN, TokenType.RIGHT_SQUARE):
                expr = self._choice()
            if self._match(TokenType.STAR):
                return RandomGrouping(StarMultiplicationGrouping(expr)) if self._match(TokenType.QUESTION) else StarMultiplicationGrouping(expr)
            elif self._match(TokenType.PLUS):
                return RandomGrouping(PlusMultiplicationGrouping(expr)) if self._match(TokenType.QUESTION) else PlusMultiplicationGrouping(expr)
            elif self._match(TokenType.QUESTION):
                return RandomGrouping(expr)
            return Grouping(expr)

    def _match(self, *token_types):
        for token in token_types:
            if self._check(token):
                self._advance()
                return True
        return False

    def _check(self, token_type):
        if self._is_at_end():
            return False
        return self._peek().token_type == token_type

    def _advance(self):
        if not self._is_at_end():
            self._current += 1
        return self._previous()

    def _is_at_end(self):
        return self._peek().token_type == TokenType.EOF

    def _is_at_right_paren(self):
        return self._peek().token_type == TokenType.RIGHT_PAREN

    def _is_at_right_square(self):
        return self._peek().token_type == TokenType.RIGHT_SQUARE

    def _is_at_right_slash(self):
        return self._peek().token_type == TokenType.SLASH

    def _peek(self):
        return self.token_list[self._current]

    def _previous(self):
        return self.token_list[self._current - 1]
