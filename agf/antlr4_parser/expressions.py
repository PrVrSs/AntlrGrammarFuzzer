"""Expressions"""


class Expression:
    """Base Expression"""
    pass


class Choice(Expression):
    """Choice expression"""
    def __init__(self, left, operator, right):
        self.type = 'Choice'
        self.left = left
        self.operator = operator
        self.right = right

    def accept(self, visitor):
        return visitor.visit_choice(self)


class Equal(Expression):
    """Equal expression"""
    def __init__(self, value):
        self.type = 'Equal'
        self.value = value

    def accept(self, visitor):
        return visitor.visit_equal(self)


class Literal(Expression):
    """Literal expression"""
    def __init__(self, value):
        self.type = 'Literal'
        self.value = value

    def accept(self, visitor):
        return visitor.visit_literal(self)


class RandomLiteral(Expression):
    """RandomLiteral expression"""
    def __init__(self, value):
        self.type = 'RandomLiteral'
        self.value = value

    def accept(self, visitor):
        return visitor.visit_random_literal(self)


class StarMultiplication(Expression):
    """StarMultiplication expression"""
    def __init__(self, value):
        self.type = 'Multiplication'
        self.value = value

    def accept(self, visitor):
        return visitor.visit_star_multiplication(self)


class PlusMultiplication(Expression):
    """PlusMultiplication expression"""
    def __init__(self, value):
        self.type = 'Multiplication'
        self.value = value

    def accept(self, visitor):
        return visitor.visit_plus_multiplication(self)


class Grouping(Expression):
    """Grouping expression"""
    def __init__(self, value):
        self.type = 'Grouping'
        self.value = value

    def accept(self, visitor):
        return visitor.visit_grouping(self)


class StarMultiplicationGrouping(Expression):
    """StarMultiplicationGrouping expression"""
    def __init__(self, value):
        self.type = 'MultiplicationGrouping'
        self.value = value

    def accept(self, visitor):
        return visitor.visit_star_multiplication_grouping(self)


class PlusMultiplicationGrouping(Expression):
    """PlusMultiplicationGrouping expression"""
    def __init__(self, value):
        self.type = 'PlusMultiplicationGrouping'
        self.value = value

    def accept(self, visitor):
        return visitor.visit_plus_multiplication_grouping(self)


class RandomGrouping(Expression):
    """RandomGrouping expression"""
    def __init__(self, value):
        self.type = 'RandomGrouping'
        self.value = value

    def accept(self, visitor):
        return visitor.visit_random_grouping(self)


class Tilde(Expression):
    """Tilde expression"""
    def __init__(self, value):
        self.type = 'Tilde'
        self.value = value

    def accept(self, visitor):
        return visitor.visit_tilde(self)
