"""AST"""
import random
import copy
from typing import (
    List,
    Iterator
)

from .expressions import Literal, Expression, Choice


class Ast:
    """Ast"""
    __slots__ = (
        'tree',
        '_multiplication_scale',
        '_random_scale',
        '_default_min_zero',
        '_default_min_one',
        '_default_min_or',
        '_default_max_or'
    )

    def __init__(self, tree_: List[Expression] = None, multiplication_scale: int = 1, random_scale: int = 1) -> None:
        self.tree: List[Expression] = tree_ or []

        self._multiplication_scale: int = multiplication_scale
        self._random_scale: int = random_scale
        self._default_min_zero: int = 0
        self._default_min_one: int = 1
        self._default_min_or: int = 0
        self._default_max_or: int = 4

    def get_ast(self) -> List[Expression]:
        new_tree: List[Expression] = copy.copy(self.tree)
        while True:
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

            self.tree = copy.copy(new_tree)
        return self.tree

    def return_rule(self) -> Iterator[Expression]:
        return (expr.value for expr in self.tree)

    def visit_star_multiplication_grouping(self, expr: Expression) -> List[Expression]:
        return self._unpacking_multiplication_grouping(expr=expr, min_=self._default_min_zero, max_=self._multiplication_scale)

    def visit_random_grouping(self, expr: Expression) -> List[Expression]:
        return self._unpacking_random(expr=expr)

    def visit_grouping(self, expr: Expression) -> List[Expression]:
        return self._unpacking_multiplication_grouping(expr=expr, min_=self._default_min_one, max_=self._default_min_one)

    def visit_plus_multiplication_grouping(self, expr: Expression) -> List[Expression]:
        return self._unpacking_multiplication_grouping(expr=expr, min_=self._default_min_one, max_=self._multiplication_scale)

    def visit_equal(self, expr: Expression):
        return expr.value.accept(self)

    def visit_choice(self, expr: Choice):
        return self._do_choice(expr.left, expr.right)

    def visit_random_literal(self, expr: Expression):
        return self._unpacking_random(expr)

    def visit_star_multiplication(self, expr: Expression):
        return self._unpacking_multiplication(expr, min_=self._default_min_zero, max_=self._multiplication_scale)

    def visit_plus_multiplication(self, expr: Expression):
        return self._unpacking_multiplication(expr, min_=self._default_min_one, max_=self._multiplication_scale)

    @staticmethod
    def visit_tilde(expr: Expression) -> Expression:
        return Literal(value='\x33')

    @staticmethod
    def visit_literal(expr) -> Expression:
        return expr

    def _unpacking_random(self, expr: Expression) -> List[Expression]:
        return expr.value if self._repeat(min_=self._default_min_zero, max_=self._random_scale) else []

    def _unpacking_multiplication_grouping(self, expr: Expression, min_: int = 1, max_: int = 1) -> List[Expression]:
        return [exp for _ in range(self._repeat(min_=min_, max_=max_)) for exp in expr.value]

    def _unpacking_multiplication(self, expr: Expression, min_: int = 1, max_: int = 2) -> List[Expression]:
        return [expr.value for _ in range(self._repeat(min_=min_, max_=max_))]

    def _do_choice(self, left: Expression, right: Expression) -> Expression:
        return left.accept(self) if self._repeat(min_=self._default_min_or, max_=self._default_max_or) else right.accept(self)

    @staticmethod
    def _repeat(min_: int = 1, max_: int = 1) -> int:
        random.seed()
        return random.randint(min_, max_)
