from generator.rule import RuleTree
from generator.checkgrammar import AntlrTree


def test_simple_rule():
    tree = RuleTree()
    tree.add_root_node('select')
    tree.insert_nodes(tree.rule_node[0], ['node2', 'node3'])
    tree.insert_nodes(tree.rule_node[1], ['node5'])
    tree.insert_node(position=0, parent_name_node='select', name='node4')
    tree.get_leaf(tree.rule_node[0])
    leaf = tree.list_leaf[0]
    assert leaf == 'node4'
    leaf = tree.list_leaf[1]
    assert leaf == 'node5'
    leaf = tree.list_leaf[2]
    assert leaf == 'node3'


def test_dict_2_tree():
    query = 'select 1'
    tree = RuleTree()
    dict_query = AntlrTree(query).get_tree()
    tree.add_root_node(dict_query[list(dict_query.keys())[0]])
    tree.dict_2_tree(tree.rule_node[0], [dict_query[list(dict_query.keys())[1]][0]])
    node_count = len(tree.rule_node)
    assert node_count == 15
    tree.get_leaf(tree.rule_node[0])
    leaf = tree.list_leaf[0]
    assert leaf == 'select'
    leaf = tree.list_leaf[1]
    assert leaf == '1'


def test_dict_2_tree_insert():
    query = 'select 1'
    tree = RuleTree()
    dict_query = AntlrTree(query).get_tree()
    tree.add_root_node(dict_query[list(dict_query.keys())[0]])
    tree.dict_2_tree(tree.rule_node[0], [dict_query[list(dict_query.keys())[1]][0]])
    tree.insert_node(parent_name_node='querySpecification', name='Test', position=1)
    node_count = len(tree.rule_node)
    assert node_count == 16
    tree.get_leaf(tree.rule_node[0])
    leaf = tree.list_leaf[0]
    assert leaf == 'select'
    leaf = tree.list_leaf[1]
    assert leaf == 'Test'
    leaf = tree.list_leaf[2]
    assert leaf == '1'
