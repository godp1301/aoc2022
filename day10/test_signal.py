from day10.signal import get_strength, compute, get_signal_strength


def test_initial_signal_strength():
    assert get_strength() == 1


def test_simple_example():
    assert compute(['noop', 'addx 3', 'addx -5']) == [1, 1, 4, 4, -1]


def test_input():
    with open('input.txt', 'r') as file:
        program = [line[:-1] for line in file.readlines()]

    compute(program)
    print(get_signal_strength())
