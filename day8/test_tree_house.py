from day8.tree_house import survey, bottom_neighbors, \
    left_neighbors, right_neighbors, top_neighbors, scenic_score

forest = [[3, 0, 3, 7, 3], [2, 5, 5, 1, 2],  [6, 5, 3, 3, 2], [3, 3, 5, 4, 9], [3, 5, 3, 9, 0]]


def test_survey():
    with open('example.txt', 'r') as file:
        assert survey([line[:-1] for line in file.readlines()]) == forest


def test_top_neighbors():
    assert top_neighbors(forest, 2, 2) == [5]
    assert top_neighbors(forest, 4, 4) == [9]
    assert top_neighbors(forest, 3, 2) == [3, 5]


def test_bottom_neighbors():
    assert bottom_neighbors(forest, 1, 2) == [3, 5]
    assert bottom_neighbors(forest, 3, 2) == [3]
    assert bottom_neighbors(forest, 0, 1) == [5]
    assert bottom_neighbors(forest, 2, 2) == [5]


def test_left_neighbors():
    assert left_neighbors(forest, 1, 2) == [5]
    assert left_neighbors(forest, 3, 2) == [3, 3]
    assert left_neighbors(forest, 0, 4) == [7]


def test_right_neighbors():
    assert right_neighbors(forest, 1, 2) == [1, 2]
    assert right_neighbors(forest, 3, 2) == [4, 9]
    assert right_neighbors(forest, 4, 2) == [9]


def test_calculate_scenic_score():
    assert scenic_score(forest, 0, 0) == 0
    assert scenic_score(forest, 0, 1) == 0
    assert scenic_score(forest, 0, 2) == 0
    assert scenic_score(forest, 0, 3) == 0
    assert scenic_score(forest, 0, 4) == 0
    assert scenic_score(forest, 1, 0) == 0
    assert scenic_score(forest, 1, 1) == 1
    assert scenic_score(forest, 1, 2) == 4
    assert scenic_score(forest, 1, 3) == 1
    assert scenic_score(forest, 1, 4) == 0
    assert scenic_score(forest, 2, 0) == 0
    assert scenic_score(forest, 2, 1) == 6
    assert scenic_score(forest, 2, 2) == 1
    assert scenic_score(forest, 2, 3) == 2
    assert scenic_score(forest, 2, 4) == 0
    assert scenic_score(forest, 3, 0) == 0
    assert scenic_score(forest, 3, 1) == 1
    assert scenic_score(forest, 3, 2) == 8
    assert scenic_score(forest, 3, 3) == 3
    assert scenic_score(forest, 3, 4) == 0
    assert scenic_score(forest, 4, 0) == 0
    assert scenic_score(forest, 4, 1) == 0
    assert scenic_score(forest, 4, 2) == 0
    assert scenic_score(forest, 4, 3) == 0
    assert scenic_score(forest, 4, 4) == 0
