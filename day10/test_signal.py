from day10.signal import compute, get_signal_strength, display


def test_simple_example():
    assert compute(['noop', 'addx 3', 'addx -5']) == [1, 1, 4, 4, -1]


def test_complex_example_display():
    with open('example.txt', 'r') as file:
        program = [line[:-1] for line in file.readlines()]

    computed = compute(program)
    display(computed)


def test_input_display():
    with open('input.txt', 'r') as file:
        program = [line[:-1] for line in file.readlines()]

    computed = compute(program)
    display(computed)


def test_input():
    with open('input.txt', 'r') as file:
        program = [line[:-1] for line in file.readlines()]

    compute(program)
    print(get_signal_strength())
