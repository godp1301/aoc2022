from day9.rope import get_head_position, get_tail_position, move, number_of_unique_location_visited, is_tail_too_far

example = ['R 4', 'U 4', 'L 3', 'D 1', 'R 4', 'D 1', 'L 5', 'R 2']


def test_start_position():
    assert get_head_position() == [0, 0]
    assert get_tail_position() == [0, 0]


def test_move_head_movements():
    assert move('R 2')[0] == [2, 0]
    assert move('L 1')[0] == [1, 0]
    assert move('U 4')[0] == [1, 4]
    assert move('D 2')[0] == [1, 2]


def test_tail_distance_from_head():
    assert is_tail_too_far([2, 2], [2, 2]) is False
    assert is_tail_too_far([1, 2], [2, 2]) is False
    assert is_tail_too_far([0, 2], [2, 2]) is True

    assert is_tail_too_far([3, 2], [2, 2]) is False
    assert is_tail_too_far([4, 2], [2, 2]) is True

    assert is_tail_too_far([2, 3], [2, 2]) is False
    assert is_tail_too_far([2, 4], [2, 2]) is True

    assert is_tail_too_far([2, 1], [2, 2]) is False
    assert is_tail_too_far([2, 0], [2, 2]) is True

    assert is_tail_too_far([3, 3], [2, 2]) is False
    assert is_tail_too_far([3, 4], [2, 2]) is True

    assert is_tail_too_far([1, 3], [2, 2]) is False
    assert is_tail_too_far([1, 4], [2, 2]) is True

    assert is_tail_too_far([1, 1], [2, 2]) is False
    assert is_tail_too_far([1, 0], [2, 2]) is True

    assert is_tail_too_far([3, 1], [2, 2]) is False
    assert is_tail_too_far([3, 0], [2, 2]) is True


def test_example_movements():
    first_move = move(example[0])
    assert first_move[0] == [4, 0]
    assert first_move[1] == [3, 0]
    assert number_of_unique_location_visited() == 4

    second_move = move(example[1])
    assert second_move[0] == [4, 4]
    assert second_move[1] == [4, 3]
    assert number_of_unique_location_visited() == 7

    third_move = move(example[2])
    assert third_move[0] == [1, 4]
    assert third_move[1] == [2, 4]
    assert number_of_unique_location_visited() == 9

    fourth_move = move(example[3])
    assert fourth_move[0] == [1, 3]
    assert fourth_move[1] == [2, 4]
    assert number_of_unique_location_visited() == 9

    fifth_move = move(example[4])
    assert fifth_move[0] == [5, 3]
    assert fifth_move[1] == [4, 3]
    assert number_of_unique_location_visited() == 10

    sixth_move = move(example[5])
    assert sixth_move[0] == [5, 2]
    assert sixth_move[1] == [4, 3]
    assert number_of_unique_location_visited() == 10

    seventh_move = move(example[6])
    assert seventh_move[0] == [0, 2]
    assert seventh_move[1] == [1, 2]
    assert number_of_unique_location_visited() == 13

    eighth_move = move(example[7])
    assert eighth_move[0] == [2, 2]
    assert eighth_move[1] == [1, 2]
    assert number_of_unique_location_visited() == 13


def test_example():
    for m in example:
        move(m)

    assert number_of_unique_location_visited() == 13
