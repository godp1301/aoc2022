from day11.monkey import Monkey


def play(monkeys, rounds):
    magic = 1
    for m in monkeys:
        magic = magic * m.test

    for r in range(rounds):
        for m in monkeys:
            for item in m.items:
                m.inspection_count += 1
                m.worry = m.operation(item)
                m.worry %= magic

                if m.worry % m.test == 0:
                    monkeys[m.true].items.append(m.worry)
                else:
                    monkeys[m.false].items.append(m.worry)

            m.items.clear()


if __name__ == '__main__':
    monkeys = [
        Monkey([84, 66, 62, 69, 88, 91, 91], lambda w: w * 11, 2, 4, 7),
        Monkey([98, 50, 76, 99], lambda w: w * w, 7, 3, 6),
        Monkey([72, 56, 94], lambda w: w + 1, 13, 4, 0),
        Monkey([55, 88, 90, 77, 60, 67], lambda w: w + 2, 3, 6, 5),
        Monkey([69, 72, 63, 60, 72, 52, 63, 78], lambda w: w * 13, 19, 1, 7),
        Monkey([89, 73], lambda w: w + 5, 17, 2, 0),
        Monkey([78, 68, 98, 88, 66], lambda w: w + 6, 11, 2, 5),
        Monkey([70], lambda w: w + 7, 5, 1, 3)
    ]
    play(monkeys, 10000)
    monkeys.sort(key=lambda m: m.inspection_count)
    print(monkeys[-1].inspection_count * monkeys[-2].inspection_count)
