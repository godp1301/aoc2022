from day1.calories import get_highest_calories, parse_food_list


def test_parse():
    parsed = parse_food_list('example.txt')
    assert len(parsed) == 5
    assert type(parsed[0][0]) == int


def test_single_elf_single_snack():
    assert get_highest_calories([[1000]]) == 1000


def test_single_elf_double_snacks():
    assert get_highest_calories([[1000, 2000]]) == 3000


def test_double_elves_single_snack():
    assert get_highest_calories([[1000], [2000]]) == 2000


def test_double_elves_multiple_snacks():
    assert get_highest_calories([[1000], [2000], [1000, 2000]]) == 3000


def test_example():
    assert get_highest_calories(parse_food_list('example.txt')) == 24000
