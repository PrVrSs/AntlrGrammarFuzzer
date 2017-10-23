from generator.scanner.antlrexpr import Literal
import random


class Ast(object):

    __slots__ = ['tree', '_multiplication_scale', '_random_scale', '_default_min_zero', '_default_min_one', '_default_min_or', '_default_max_or']

    def __init__(self, tree_: list=None, multiplication_scale: int = 1, random_scale: int = 1):
        self.tree = tree_
        self._multiplication_scale = multiplication_scale
        self._random_scale = random_scale
        self._default_min_zero = 0
        self._default_min_one = 1
        self._default_min_or = 0
        self._default_max_or = 4

    def get_ast(self) -> list:
        new_tree = self.tree[:]
        while 1:
            for expr in self.tree:
                value = expr.accept(self)
                if expr.type != 'Literal' and not isinstance(value, list):
                    value = [value]
                if isinstance(value, list):
                    index = new_tree.index(expr)
                    new_tree.pop(index)
                    new_tree = new_tree[:index] + value + new_tree[index:]
                    break
            else:
                break
            self.tree = new_tree[:]
        return self.tree

    def return_rule(self) -> list:
        rule = []
        for expr in self.tree:
            rule.append(expr.value)
        return rule

    def visit_star_multiplication_grouping(self, expr) -> list:
        return self._unpacking_multiplication_grouping(expr=expr, min_=self._default_min_zero, max_=self._multiplication_scale)

    def visit_random_grouping(self, expr) -> list:
        return self._unpacking_random(expr=expr)

    def visit_grouping(self, expr) -> list:
        return self._unpacking_multiplication_grouping(expr=expr, min_=self._default_min_one, max_=self._default_min_one)

    def visit_plus_multiplication_grouping(self, expr) -> list:
        return self._unpacking_multiplication_grouping(expr=expr, min_=self._default_min_one, max_=self._multiplication_scale)

    def _unpacking_random(self, expr):
        random.seed()
        result = expr.value if random.randint(self._default_min_zero, self._random_scale) else []
        return result

    @staticmethod
    def _unpacking_multiplication_grouping(expr, min_: int = 1, max_: int = 1) -> list:
        grouping_value = []
        random.seed()
        repeat = random.randint(min_, max_)
        for index in range(repeat):
            grouping_value += expr.value
        return grouping_value

    @staticmethod
    def visit_tilde(expr):
        return Literal('\x33')

    def visit_equal(self, expr):
        return expr.value.accept(self)

    def visit_choice(self, expr):
        return self._do_choice(expr.left, expr.right)

    def _do_choice(self, left, right):
        random.seed()
        check_left = random.randint(self._default_min_or, self._default_max_or)
        return left.accept(self) if check_left else right.accept(self)

    @staticmethod
    def visit_literal(expr):
        return expr

    def visit_random_literal(self, expr):
        return self._unpacking_random(expr)

    def visit_star_multiplication(self, expr):
        return self._unpacking_multiplication(expr, min_=self._default_min_zero, max_=self._multiplication_scale)

    def visit_plus_multiplication(self, expr):
        return self._unpacking_multiplication(expr, min_=self._default_min_one, max_=self._multiplication_scale)

    @staticmethod
    def _unpacking_multiplication(expr, min_: int = 1, max_: int = 2):
        literal_value = []
        random.seed()
        repeat = random.randint(min_, max_)
        for index in range(repeat):
            literal_value.append(expr.value)
        return literal_value
