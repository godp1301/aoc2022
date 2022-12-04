from day4.assignments import is_contained_in, count_pairs_contained_in_others


def test_not_contained():
    assert is_contained_in('50-52,32-51') is False


def test_first_part_contained_in_second():
    assert is_contained_in('12-18,10-44') is True


def test_second_part_contained_in_first():
    assert is_contained_in('22-28,23-24') is True


def test_example():
    with open('example.txt', 'r') as file:
        puzzle = [line[:-1] for line in file.readlines()]

    assert count_pairs_contained_in_others(puzzle) == 2
