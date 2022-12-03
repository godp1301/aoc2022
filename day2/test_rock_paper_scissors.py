from day2.rock_paper_scissors import game, calculate


def test_opponent_has_to_win():
    assert calculate('A X') == 3
    assert calculate('B X') == 1
    assert calculate('C X') == 2


def test_opponent_has_to_loose():
    assert calculate('A Z') == 8
    assert calculate('B Z') == 9
    assert calculate('C Z') == 7


def test_draws():
    assert calculate('A Y') == 4
    assert calculate('B Y') == 5
    assert calculate('C Y') == 6


def test_example():
    assert game('example.txt') == 12
