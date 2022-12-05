from day5.stacks import move, process


def test_move_one_from_a_to_b():
    stacks = [['X'], ['Z']]
    new_arrangement = move(stacks, 1, 0, 1)
    assert new_arrangement[0] == []
    assert new_arrangement[1] == ['Z', 'X']


def test_move_two_from_a_to_b():
    stacks = [['X', 'Y'], ['Z']]
    new_arrangement = move(stacks, 2, 0, 1)
    assert new_arrangement[0] == []
    assert new_arrangement[1] == ['Z', 'Y', 'X']


def test_example():
    stacks = [
        ['Z', 'N'],
        ['M', 'C', 'D'],
        ['P']
    ]

    assert process(stacks, ['move 1 from 2 to 1\n', 'move 3 from 1 to 3\n', 'move 2 from 2 to 1\n', 'move 1 from 1 to 2\n']) == 'CMZ'
