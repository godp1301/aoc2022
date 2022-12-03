from day3.rucksacks import get_compartments, get_common, get_value_of, get_priorities_sum


def test_get_compartments():
    a, b = get_compartments('vJrwpWtwJgWrhcsFMMfFFhFp')
    assert a == 'vJrwpWtwJgWr'
    assert b == 'hcsFMMfFFhFp'


def test_get_common_item():
    a, b = get_compartments('vJrwpWtwJgWrhcsFMMfFFhFp')
    common = get_common(a, b)
    assert common == 'p'


def test_lower_case_value():
    assert get_value_of('a') == 1
    assert get_value_of('z') == 26
    assert get_value_of('A') == 27
    assert get_value_of('Z') == 52


def test_example():
    with open('example.txt', 'r') as file:
        puzzle = [line[:-1] for line in file.readlines()]

    assert get_priorities_sum(puzzle) == 157
