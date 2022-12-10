from collections import deque

register = []


def get_strength():
    return 1


def compute(program):
    global register
    stack = deque()
    ticks = program.count('noop') + 2 * (len(program) - program.count('noop'))

    instruction = deque(program)
    for t in range(ticks):
        try:
            i = instruction.popleft()
            if i == 'noop':
                stack.append(0)
            elif i.startswith('addx'):
                value = int(i.split(' ')[1])
                stack.append(0)
                stack.append(value)
        except IndexError:
            pass

        if stack:
            value = stack.popleft()
            if value == 0:
                register.append(register[-1] if register else 1)
            else:
                register.append(register[-1] + value)

    return register


def get_signal_strength():
    global register
    return register[19] * 20 + register[59] * 60 + register[99] * 100 + register[139] * 140 + register[179] * 180 + register[219] * 220
