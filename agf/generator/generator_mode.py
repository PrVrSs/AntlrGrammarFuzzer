import random

from agf.antlr4_parser import Ast
from agf.rule import RuleTree
from agf.checker.checkgrammar import AntlrTree
from agf.utils.decor import logging, timeout

trace_enabled = False
drop_time = 10


class GeneratorMode(object):

    __slots__ = (
        '_mutate_mode',
        '_rule_dictionary',
        '_multiplication_scale',
        '_random_scale',
        '_mutate_chance',
        '_combined_mutate_rule',
        '_exception_rule',
        '_count_to_generate',
    )

    def __init__(self, **kwargs):
        self._mutate_mode = kwargs['_mutate_mode']
        self._rule_dictionary = kwargs['_rule_dictionary']
        self._multiplication_scale = kwargs['_multiplication_scale']
        self._random_scale = kwargs['_random_scale']
        self._mutate_chance = kwargs['_mutate_chance']
        self._combined_mutate_rule = kwargs['_combined_mutate_rule']
        self._exception_rule = kwargs['_access_rule_in_lexer_file']
        self._count_to_generate = kwargs['_count_to_generate']

    @timeout(drop_time)
    def _build_tree(self, tree, node_count) -> bool:
        while True:
            if node_count == len(tree.rule_node):
                break
            sub_rule_list = self._get_sub_rule_list(tree.rule_node[node_count].name)
            if self._mutate_mode:
                sub_rule_list = self._mutate(sub_rule_list)
            tree.insert_nodes(tree.rule_node[node_count], sub_rule_list)
            node_count += 1

        return True

    @logging(trace_enabled)
    def _get_sub_rule_list(self, rule_name: str) -> list:
        try:
            ast = Ast(self._rule_dictionary[rule_name], self._multiplication_scale, self._random_scale)
            ast.get_ast()
        except KeyError:
            return []
        return ast.return_rule()

    def _mutate(self, sub_rule_list: list) -> list:
        random.seed()
        rand_ = random.randint(0, len(sub_rule_list))
        if len(sub_rule_list) == rand_:
            sub_rule_list += self._get_random_rule()
        else:
            sub_rule_list[:rand_] += self._get_random_rule()
        return sub_rule_list

    def _get_random_rule(self):
        random.seed()
        if self._mutate_chance > random.randint(0, 100):
            while 1:
                rule = [random.choice(list(self._rule_dictionary))]
                if rule[0] not in self._exception_rule:
                    break
        else:
            rule = []
        return rule


class RandomQuery(GeneratorMode):

    __slots__ = ['_start_rule']

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._start_rule = kwargs['start_rule']

    def _create_tree(self, ) -> list:
        tree = RuleTree()
        tree.add_root_node(self._start_rule)
        return tree.get_leaf(tree.rule_node[0]) if self._build_tree(tree, 0) else []

    def generate(self):
        count = 0
        while self._count_to_generate != count:
            sentence = self._create_tree()
            if not sentence:
                continue
            yield sentence
            count += 1


class SqlForms(GeneratorMode):

    __slots__ = ['_start_position', '_end_position', '_query', '_parent_node', '_check']

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._start_position = kwargs['_start_position']
        self._end_position = kwargs['_end_position']
        self._query = kwargs['query']
        self._parent_node = kwargs['parent_node']
        self._check = kwargs['check']

    def generate(self):
        for rule in list(self._rule_dictionary):
            if rule in self._exception_rule:
                continue
            for _ in range(self._count_to_generate):
                for position in range(self._start_position, self._end_position):
                    sentence = self._create_tree(rule_name=rule, position=position)
                    if not sentence:
                        continue
                    # while 1:
                    #    sentence = self._create_tree(query=query, parent_node=parent_node, rule_name=rule, position=position)
                    #    if sentence:
                    #        break
                    if self._check:
                        print(rule, sentence)
                    yield sentence

    def _create_tree(self, rule_name: str, position: int) -> list:
        tree = RuleTree()
        dict_query = AntlrTree(self._query).get_tree()
        tree.add_root_node(dict_query[list(dict_query.keys())[0]])
        tree.dict_2_tree(tree.rule_node[0], [dict_query[list(dict_query.keys())[1]][0]])
        node_count = len(tree.rule_node)
        tree.insert_node(parent_name_node=self._parent_node, name=rule_name, position=position)
        return tree.get_leaf(tree.rule_node[0]) if self._build_tree(tree, node_count) else []
