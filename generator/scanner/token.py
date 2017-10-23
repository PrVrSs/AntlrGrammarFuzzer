class Token(object):

    __slots__ = ["token_type", "lexeme", "literal"]

    def __init__(self, token_type, lexeme, literal):
        self.token_type = token_type
        self.lexeme = lexeme
        self.literal = literal

    def __str__(self):
        return "{} {} {}".format(self.token_type, self.lexeme, self.literal)
