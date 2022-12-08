from day8.tree_house import survey, bottom_neighbors, is_visible, \
    left_neighbors, right_neighbors, top_neighbors, walk

forest = [[3, 0, 3, 7, 3], [2, 5, 5, 1, 2],  [6, 5, 3, 3, 2], [3, 3, 5, 4, 9], [3, 5, 3, 9, 0]]


def test_survey():
    with open('example.txt', 'r') as file:
        assert survey([line[:-1] for line in file.readlines()]) == forest


def test_top_neighbors():
    assert top_neighbors(forest, 0, 0) == []
    assert top_neighbors(forest, 1, 0) == [3]
    assert top_neighbors(forest, 4, 0) == [3, 2, 6, 3]


def test_bottom_neighbor():
    assert bottom_neighbors(forest, 0, 0) == [2, 6, 3, 3]
    assert bottom_neighbors(forest, 1, 0) == [6, 3, 3]
    assert bottom_neighbors(forest, 4, 0) == []


def test_left_neighbors():
    assert left_neighbors(forest, 0, 0) == []
    assert left_neighbors(forest, 0, 1) == [3]
    assert left_neighbors(forest, 0, 4) == [3, 0, 3, 7]


def test_right_neighbor():
    assert right_neighbors(forest, 0, 4) == []
    assert right_neighbors(forest, 0, 3) == [3]
    assert right_neighbors(forest, 0, 0) == [0, 3, 7, 3]


def test_tree_is_visible_when_tree_is_located_at_forest_boundary():
    assert is_visible(forest, 0, 0) is True


def test_tree_is_visible_when_tree_is_in_the_forest():
    assert is_visible(forest, 1, 1) is True


def test_tree_is_visible_when_all_neighbors_are_traversed():
    assert is_visible(forest, 1, 2) is True


def test_tree_is_not_visible():
    # assert is_visible(forest, 1, 3) is False
    assert is_visible(forest, 2, 2) is False


def test_example():
    assert walk(forest) == 21
