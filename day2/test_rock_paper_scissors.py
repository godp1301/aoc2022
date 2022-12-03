from day2.rock_paper_scissors import game, calculate


def test_rock_beats_scissors():
    assert calculate('A Z') == 3
    assert calculate('C X') == 7


def test_paper_beats_rock():
    assert calculate('B X') == 1
    assert calculate('A Y') == 8


def test_scissors_beats_paper():
    assert calculate('C Y') == 2
    assert calculate('B Z') == 9


def test_draws():
    assert calculate('A X') == 4
    assert calculate('B Y') == 5
    assert calculate('C Z') == 6


def test_example():
    assert game('example.txt') == 15
