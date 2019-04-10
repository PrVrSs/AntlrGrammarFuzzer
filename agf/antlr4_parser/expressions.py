"""Expressions"""
import abc
import attr
from typing import Any


class Expression(metaclass=abc.ABCMeta):
    """Abstract Expression"""
    type: Any = None
    value: Any = None

    @abc.abstractmethod
    def accept(self, visitor):
        raise NotImplementedError()


@attr.s(slots=True)
class Choice(Expression):
    """Choice expression"""
    left = attr.ib(type=Expression)
    operator = attr.ib(type=Any)
    right = attr.ib(type=Expression)
    type: str = 'Choice'

    def accept(self, visitor):
        return visitor.visit_choice(self)


@attr.s(slots=True)
class Equal(Expression):
    """Equal expression"""
    value = attr.ib(type=Any)
    type: str = 'Equal'

    def accept(self, visitor):
        return visitor.visit_equal(self)


@attr.s(slots=True)
class Literal(Expression):
    """Literal expression"""
    value = attr.ib(type=Any)
    type: str = 'Literal'

    def accept(self, visitor):
        return visitor.visit_literal(self)


@attr.s(slots=True)
class RandomLiteral(Expression):
    """RandomLiteral expression"""
    value = attr.ib(type=Any)
    type: str = 'RandomLiteral'

    def accept(self, visitor):
        return visitor.visit_random_literal(self)


@attr.s(slots=True)
class StarMultiplication(Expression):
    """StarMultiplication expression"""
    value = attr.ib(type=Any)
    type: str = 'Multiplication'

    def accept(self, visitor):
        return visitor.visit_star_multiplication(self)


@attr.s(slots=True)
class PlusMultiplication(Expression):
    """PlusMultiplication expression"""
    value = attr.ib(type=Any)
    type: str = 'Multiplication'

    def accept(self, visitor):
        return visitor.visit_plus_multiplication(self)


@attr.s(slots=True)
class Grouping(Expression):
    """Grouping expression"""
    value = attr.ib(type=Any)
    type: str = 'Grouping'

    def accept(self, visitor):
        return visitor.visit_grouping(self)


@attr.s(slots=True)
class StarMultiplicationGrouping(Expression):
    """StarMultiplicationGrouping expression"""
    value = attr.ib(type=Any)
    type: str = 'MultiplicationGrouping'

    def accept(self, visitor):
        return visitor.visit_star_multiplication_grouping(self)


@attr.s(slots=True)
class PlusMultiplicationGrouping(Expression):
    """PlusMultiplicationGrouping expression"""
    value = attr.ib(type=Any)
    type: str = 'PlusMultiplicationGrouping'

    def accept(self, visitor):
        return visitor.visit_plus_multiplication_grouping(self)


@attr.s(slots=True)
class RandomGrouping(Expression):
    """RandomGrouping expression"""
    value = attr.ib(type=Any)
    type: str = 'RandomGrouping'

    def accept(self, visitor):
        return visitor.visit_random_grouping(self)


@attr.s(slots=True)
class Tilde(Expression):
    """Tilde expression"""
    value = attr.ib(type=Any)
    type: str = 'Tilde'

    def accept(self, visitor):
        return visitor.visit_tilde(self)
