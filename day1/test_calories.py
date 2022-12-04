import os

from day1.calories import get_highest_calories, parse_food_list


def test_parse():
    parsed = parse_food_list(f'{os.getcwd()}/day1/example.txt')
    assert len(parsed) == 5
    assert type(parsed[0][0]) == int


def test_example():
    assert get_highest_calories(parse_food_list(f'{os.getcwd()}/day1/example.txt')) == 45000
