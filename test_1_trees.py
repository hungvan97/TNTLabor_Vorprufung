from exercise_1_trees import merge_tree_nodes


def test_one_empty_tree():
    t = {}

    assert merge_tree_nodes(t) == {}


def test_two_empty_trees():
    t1, t2 = {}, {}

    assert merge_tree_nodes(t1, t2) == {}


def test_one_flat_tree():
    t = {'a': 3, 'b': 4}

    assert merge_tree_nodes(t) == {'a': (3,), 'b': (4,)}


def test_one_deep_tree():
    t = {'a': 3, 'b': {'c': 1, 'd': 2}}

    assert merge_tree_nodes(t) == {'a': (3,), 'b': {'c': (1,), 'd': (2,)}}


def test_two_deep_trees():
    t1 = {'a': 3, 'b': {'c': 1, 'd': 2}}
    t2 = {'a': 4, 'b': {'c': 7, 'd': 8}}

    assert merge_tree_nodes(t1, t2) == {'a': (3, 4), 'b': {'c': (1, 7), 'd': (2, 8)}}


def test_three_deep_trees():
    t1 = {'a': 3, 'b': {'c': 1, 'd': 2}}
    t2 = {'a': 4, 'b': {'c': 7, 'd': 8}}
    t3 = {'a': 8, 'b': {'c': 0, 'd': 12}}

    assert merge_tree_nodes(t1, t2, t3) == {'a': (3, 4, 8), 'b': {'c': (1, 7, 0), 'd': (2, 8, 12)}}


def test_ten_deep_trees():
    t0 = {'a': 3, 'b': {'c': 1, 'd': 2}}
    t1 = {'a': 5, 'b': {'c': 1, 'd': 2}}
    t2 = {'a': 9, 'b': {'c': 7, 'd': 8}}
    t3 = {'a': 0, 'b': {'c': 0, 'd': 12}}
    t4 = {'a': 1, 'b': {'c': 0, 'd': 3}}
    t5 = {'a': 3, 'b': {'c': 3, 'd': -56}}
    t6 = {'a': 4, 'b': {'c': 2, 'd': 2}}
    t7 = {'a': 3, 'b': {'c': 0, 'd': 12}}
    t8 = {'a': 2, 'b': {'c': 0, 'd': 4}}
    t9 = {'a': 3, 'b': {'c': 8, 'd': 8}}

    result = {'a': (3, 5, 9, 0, 1, 3, 4, 3, 2, 3), 'b': {'c': (1, 1, 7, 0, 0, 3, 2, 0, 0, 8),
                                                         'd': (2, 2, 8, 12, 3, -56, 2, 12, 4, 8)}}

    assert merge_tree_nodes(t0, t1, t2, t3, t4, t5, t6, t7, t8, t9) == result
