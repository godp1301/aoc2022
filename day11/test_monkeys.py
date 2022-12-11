from day11.monkey import Monkey
from day11.monkeys import play

example_monkeys = [
    Monkey([79, 98], lambda w: w * 19, 23, 2, 3),
    Monkey([54, 65, 75, 74], lambda w: w + 6, 19, 2, 0),
    Monkey([79, 60, 97], lambda w: w * w, 13, 1, 3),
    Monkey([74], lambda w: w + 3, 17, 0, 1)
]


def test_example_round_1():
    play(example_monkeys, 1)
    assert example_monkeys[0].items == [20, 23, 27, 26]
    assert example_monkeys[1].items == [2080, 25, 167, 207, 401, 1046]
    assert example_monkeys[2].items == []
    assert example_monkeys[3].items == []


def test_example_round_10():
    play(example_monkeys, 10)
    assert example_monkeys[0].items == [91, 16, 20, 98]
    assert example_monkeys[1].items == [481, 245, 22, 26, 1092, 30]
    assert example_monkeys[2].items == []
    assert example_monkeys[3].items == []


def test_example_round_20():
    play(example_monkeys, 20)
    assert example_monkeys[0].items == [10, 12, 14, 26, 34]
    assert example_monkeys[1].items == [245, 93, 53, 199, 115]
    assert example_monkeys[2].items == []
    assert example_monkeys[3].items == []

    example_monkeys.sort(key=lambda m: m.inspection_count)
    assert example_monkeys[-1].inspection_count * example_monkeys[-2].inspection_count == 10605


def test_example_round_10000():
    play(example_monkeys, 10000)

    example_monkeys.sort(key=lambda m: m.inspection_count)
    assert example_monkeys[-1].inspection_count * example_monkeys[-2].inspection_count == 2713310158
