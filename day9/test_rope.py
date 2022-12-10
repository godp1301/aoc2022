from day9.rope import get_head_position, get_tail_position, move, number_of_unique_location_visited, is_following_knot_too_far, \
    get_rope_position

example = ['R 4', 'U 4', 'L 3', 'D 1', 'R 4', 'D 1', 'L 5', 'R 2']
second_example = ['R 5', 'U 8', 'L 8', 'D 3', 'R 17', 'D 10', 'L 25', 'U 20']


def test_start_position():
    assert get_head_position() == [0, 0]
    assert get_tail_position() == [0, 0]
    assert get_rope_position() == [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]


def test_example_movements():
    first_move = move(example[0])
    assert first_move[0] == [4, 0]
    assert first_move[1] == [3, 0]
    assert first_move[2] == [2, 0]
    assert first_move[3] == [1, 0]
    assert first_move[4] == [0, 0]
    assert first_move[5] == [0, 0]
    assert first_move[6] == [0, 0]
    assert first_move[7] == [0, 0]
    assert first_move[8] == [0, 0]
    assert first_move[9] == [0, 0]
    assert number_of_unique_location_visited() == 1

    second_move = move(example[1])
    assert second_move[0] == [4, 4]
    assert second_move[1] == [4, 3]
    assert second_move[2] == [4, 2]
    assert second_move[3] == [3, 2]
    assert second_move[4] == [2, 2]
    assert second_move[5] == [1, 1]
    assert second_move[6] == [0, 0]
    assert second_move[7] == [0, 0]
    assert second_move[8] == [0, 0]
    assert second_move[9] == [0, 0]
    assert number_of_unique_location_visited() == 1

    third_move = move(example[2])
    assert third_move[0] == [1, 4]
    assert third_move[1] == [2, 4]
    assert third_move[2] == [3, 3]
    assert third_move[3] == [3, 2]
    assert third_move[4] == [2, 2]
    assert third_move[5] == [1, 1]
    assert third_move[6] == [0, 0]
    assert third_move[7] == [0, 0]
    assert third_move[8] == [0, 0]
    assert third_move[9] == [0, 0]
    assert number_of_unique_location_visited() == 1

    fourth_move = move(example[3])
    assert fourth_move[0] == [1, 3]
    assert fourth_move[1] == [2, 4]
    assert fourth_move[2] == [3, 3]
    assert fourth_move[3] == [3, 2]
    assert fourth_move[4] == [2, 2]
    assert fourth_move[5] == [1, 1]
    assert fourth_move[6] == [0, 0]
    assert fourth_move[7] == [0, 0]
    assert fourth_move[8] == [0, 0]
    assert fourth_move[9] == [0, 0]
    assert number_of_unique_location_visited() == 1

    fifth_move = move(example[4])
    assert fifth_move[0] == [5, 3]
    assert fifth_move[1] == [4, 3]
    assert fifth_move[2] == [3, 3]
    assert fifth_move[3] == [3, 2]
    assert fifth_move[4] == [2, 2]
    assert fifth_move[5] == [1, 1]
    assert fifth_move[6] == [0, 0]
    assert fifth_move[7] == [0, 0]
    assert fifth_move[8] == [0, 0]
    assert fifth_move[9] == [0, 0]
    assert number_of_unique_location_visited() == 1

    sixth_move = move(example[5])
    assert sixth_move[0] == [5, 2]
    assert sixth_move[1] == [4, 3]
    assert sixth_move[2] == [3, 3]
    assert sixth_move[3] == [3, 2]
    assert sixth_move[4] == [2, 2]
    assert sixth_move[5] == [1, 1]
    assert sixth_move[6] == [0, 0]
    assert sixth_move[7] == [0, 0]
    assert sixth_move[8] == [0, 0]
    assert sixth_move[9] == [0, 0]
    assert number_of_unique_location_visited() == 1

    seventh_move = move(example[6])
    assert seventh_move[0] == [0, 2]
    assert seventh_move[1] == [1, 2]
    assert seventh_move[2] == [2, 2]
    assert seventh_move[3] == [3, 2]
    assert seventh_move[4] == [2, 2]
    assert seventh_move[5] == [1, 1]
    assert seventh_move[6] == [0, 0]
    assert seventh_move[7] == [0, 0]
    assert seventh_move[8] == [0, 0]
    assert seventh_move[9] == [0, 0]
    assert number_of_unique_location_visited() == 1

    eighth_move = move(example[7])
    assert eighth_move[0] == [2, 2]
    assert eighth_move[1] == [1, 2]
    assert eighth_move[2] == [2, 2]
    assert eighth_move[3] == [3, 2]
    assert eighth_move[4] == [2, 2]
    assert eighth_move[5] == [1, 1]
    assert eighth_move[6] == [0, 0]
    assert eighth_move[7] == [0, 0]
    assert eighth_move[8] == [0, 0]
    assert eighth_move[9] == [0, 0]
    assert number_of_unique_location_visited() == 1


def test_second_example():
    for m in second_example:
        move(m)

    assert number_of_unique_location_visited() == 36
