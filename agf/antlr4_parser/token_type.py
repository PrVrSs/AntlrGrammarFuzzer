"""Token Type"""
from enum import Enum, auto


class TokenType(Enum):

    LEFT_PAREN = auto()
    RIGHT_PAREN = auto()
    LEFT_SQUARE = auto()
    RIGHT_SQUARE = auto()
    PLUS = auto()
    SEMICOLON = auto()
    DOT = auto()
    STAR = auto()
    SLASH = auto()
    QUESTION = auto()
    EQUAL = auto()
    PLUS_EQUAL = auto()
    TILDE = auto()
    NEW_LINE = auto()
    # literals
    TERMINAL = auto()
    NONTERMINAL = auto()

    EOF = auto()
