import os

from day4.assignments import count_pairs_overlapping_others, overlaps


def test_not_overlapping():
    assert overlaps('2-4,6-8') is False


def test_first_part_overlaps():
    assert overlaps('5-7,7-9') is True


def test_overlaps():
    assert overlaps('6-6,4-6') is True


def test_second_part_overlaps():
    assert overlaps('7-9,5-7') is True


def test_example():
    with open(f'{os.getcwd()}/day4/example.txt', 'r') as file:
        puzzle = [line[:-1] for line in file.readlines()]

    assert count_pairs_overlapping_others(puzzle) == 4
