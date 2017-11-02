import re
from enum import Enum

CONST_FOR_REPLACE = {'.': '\x39', 'A-Z_$0-9': 'AZ_$9', 'A-Z_$': 'AZ_$',
                     '0-9A-F': '9F', '0-9': '99', '01': '01', 'A-Z0-9._$': 'AZ9.', 'SEMI': ';'
                     }


def concatenate_expr(tree_: list) -> list:
    pop_list = []
    for index, expr in enumerate(tree_):
        try:
            if expr == '(':
                if index != 0:
                    tree_[index - 1] = tree_[index - 1] + expr
                    pop_list.append(index)
        except IndexError:
            pass
    count_pop = 0
    for i in pop_list:
        tree_.pop(i - count_pop)
        count_pop += 1
    return tree_


class Action(Enum):
    found_key = 1
    found_node = 2
    insert_key = 3
    insert_node = 4


class RuleNode(object):

    __slots__ = ["child", "name", "parent_pointer", ]

    def __init__(self, name: str,):
        self.name = name
        self.child = []
        self.parent_pointer = None

    def add_child(self, list_child: list):
        self.child = list_child

    def get_child(self)->list:
        return self.child

    def set_pointer(self, pointer) -> None:
        self.parent_pointer = pointer


class RuleTree(object):

    __slots__ = ["rule_node", "list_leaf", ]

    def __init__(self):
        self.rule_node = []
        self.list_leaf = []

    def add_root_node(self, name: str)-> None:
        self.rule_node.append(RuleNode(name=name))

    def _search_node(self, key: str='', node: RuleNode=None, find_type: Action=None, find_node: RuleNode=None):
        node_its = None
        if node is None:
            node_its = self._search_node(key=key, node=self.rule_node[0], find_type=find_type, find_node=find_node)
        else:
            if find_type is Action.found_key:
                if key.lower() == node.name.lower():
                    return node
            elif find_type is Action.found_node:
                if find_node is node:
                    return find_node
            for child in node.get_child():
                node_its = self._search_node(key=key, node=child, find_type=find_type, find_node=find_node)
        return node_its

    def insert_node(self, position: int=0, parent_name_node: str='', name: str='', insert_type: Action=Action.insert_key, parent_node: RuleNode=None):
        new_child_rule = RuleNode(name=name)
        if insert_type is Action.insert_key:
            parent_node = self._search_node(key=parent_name_node, find_type=Action.found_key)
            if parent_node:
                try:
                    parent_node.child.insert(position % len(parent_node.child), new_child_rule)
                except ZeroDivisionError:
                    parent_node.child.insert(position % (len(parent_node.child) + 1), new_child_rule)
                new_child_rule.set_pointer(parent_node)
                self.rule_node.append(new_child_rule)
        elif insert_type is Action.insert_node:
            parent_node = self._search_node(find_node=parent_node, find_type=Action.found_node)
            parent_node.child.append(new_child_rule)
            new_child_rule.set_pointer(parent_node)
            self.rule_node.append(new_child_rule)
            return new_child_rule

    def insert_nodes(self, node: RuleNode, list_child: list) -> None:
        list_node = [RuleNode(child) for child in list_child]
        node.add_child(list_node)
        [r.set_pointer(node) for r in node.get_child()]
        self.rule_node += list_node

    def dict_2_tree(self, parent_node: RuleNode, query_list: list):
        parent_node = parent_node
        if query_list:
            for index in query_list:
                new_child_rule = self.insert_node(parent_node=parent_node, name=index[list(index.keys())[0]], insert_type=Action.insert_node)
                self.dict_2_tree(new_child_rule, index[list(index.keys())[1]])

    def get_leaf(self, rule_node):
        self._visit_tree(rule_node)
        return " ".join(concatenate_expr(self.list_leaf)) + ";"

    def _visit_tree(self, rule_node):
        concatenation_flag = False
        count = 0
        if rule_node is not None:
            if not rule_node.child:
                self.list_leaf.append(self._string_handling(rule_node.name))
            for index_rule, rule in enumerate(rule_node.child):
                self._visit_tree(rule)
                if rule.name[0] == "'" and rule.name[-1] == "'" and len(rule.name) > 1:
                    concatenation_flag = True
                    count = 0
                if concatenation_flag is True and index_rule != 0:
                    if count != 2:
                        self.list_leaf[-2] = self.list_leaf[-2] + self.list_leaf[-1]
                        self.list_leaf.pop()
                        count += 1
                    else:
                        concatenation_flag = False
                        count = 0
                if concatenation_flag is True and index_rule == 0:
                    count = 1

    @staticmethod
    def _string_handling(rule_name: str='') -> str:
        # rule_name = ''.join(list(map(lambda word: re.sub(r'\'\\\'\'', '\'', word), rule_name)))
        # rule_name = ''.join(list(map(lambda word: re.sub(r'\'"\'', r'"', word), rule_name)))
        # rule_name = ''.join(list(map(lambda word: re.sub(r'\'""\'', r'""', word), rule_name)))
        # rule_name = ''.join(list(map(lambda word: re.sub("'\''", r"'", word), rule_name)))
        # rule_name = ''.join(list(map(lambda word: re.sub(r'\\\\', '\\\\', word), rule_name)))
        rule_name = CONST_FOR_REPLACE[rule_name] if rule_name in list(CONST_FOR_REPLACE.keys()) else rule_name
        rule_name = ''.join([s.strip("'") if s != "'" and s != "''" else s for s in [rule_name]])
        rule_name = ''.join(list(map(lambda word: re.sub(r'\\', r"'", word), rule_name)))
        return rule_name
