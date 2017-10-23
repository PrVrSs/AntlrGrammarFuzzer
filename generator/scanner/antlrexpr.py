class Expr(object):
    pass


class Choice(Expr):
    def __init__(self, left, operator, right):
        self.type = 'Choice'
        self.left = left
        self.operator = operator
        self.right = right

    def accept(self, visitor):
        return visitor.visit_choice(self)


class Equal(Expr):
    def __init__(self, value):
        self.type = 'Equal'
        self.value = value

    def accept(self, visitor):
        return visitor.visit_equal(self)


class Literal(Expr):

    def __init__(self, value):
        self.type = 'Literal'
        self.value = value

    def accept(self, visitor):
        return visitor.visit_literal(self)


class RandomLiteral(Expr):

    def __init__(self, value):
        self.type = 'RandomLiteral'
        self.value = value

    def accept(self, visitor):
        return visitor.visit_random_literal(self)


class StarMultiplication(Expr):
    def __init__(self, value):
        self.type = 'Multiplication'
        self.value = value

    def accept(self, visitor):
        return visitor.visit_star_multiplication(self)


class PlusMultiplication(Expr):
    def __init__(self, value):
        self.type = 'Multiplication'
        self.value = value

    def accept(self, visitor):
        return visitor.visit_plus_multiplication(self)


class Grouping(Expr):
    def __init__(self, value):
        self.type = 'Grouping'
        self.value = value

    def accept(self, visitor):
        return visitor.visit_grouping(self)


class StarMultiplicationGrouping(Expr):
    def __init__(self, value):
        self.type = 'MultiplicationGrouping'
        self.value = value

    def accept(self, visitor):
        return visitor.visit_star_multiplication_grouping(self)


class PlusMultiplicationGrouping(Expr):
    def __init__(self, value):
        self.type = 'PlusMultiplicationGrouping'
        self.value = value

    def accept(self, visitor):
        return visitor.visit_plus_multiplication_grouping(self)


class RandomGrouping(Expr):
    def __init__(self, value):
        self.type = 'RandomGrouping'
        self.value = value

    def accept(self, visitor):
        return visitor.visit_random_grouping(self)


class Tilde(Expr):
    def __init__(self, value):
        self.type = 'Tilde'
        self.value = value

    def accept(self, visitor):
        return visitor.visit_tilde(self)
