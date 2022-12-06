from day6.device import find_marker


def test_first_example():
    assert find_marker('mjqjpqmgbljsphdztnvjfqwrcgsmlb') == 7


def test_second_example():
    assert find_marker('bvwbjplbgvbhsrlpgdmjqwftvncz') == 5


def test_third_example():
    assert find_marker('nppdvjthqldpwncqszvftbrmjlhg') == 6
