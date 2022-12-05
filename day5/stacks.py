import re


def move(stacks, quantity, source, destination):
    boxes = []
    for _ in range(quantity):
        boxes.append(stacks[source].pop())

    boxes.reverse()
    for b in boxes:
        stacks[destination].append(b)
    return stacks


def process(stacks, moves):
    for m in moves:
        parsed = re.search('move (?P<quantity>[0-9]*) from (?P<source>[0-9]*) to (?P<destination>[0-9]*)', m)
        move(stacks, int(parsed.group('quantity')), int(parsed.group('source')) - 1,
             int(parsed.group('destination')) - 1)

    return ''.join([s.pop() for s in stacks])


if __name__ == '__main__':
    with open('input.txt', 'r') as file:
        moves = file.readlines()

    stacks = [
        ['S', 'Z', 'P', 'D', 'L', 'B', 'F', 'C'],
        ['N', 'V', 'G', 'P', 'H', 'W', 'B'],
        ['F', 'W', 'B', 'J', 'G'],
        ['G', 'J', 'N', 'F', 'L', 'W', 'C', 'S'],
        ['W', 'J', 'L', 'T', 'P', 'M', 'S', 'H'],
        ['B', 'C', 'W', 'G', 'F', 'S'],
        ['H', 'T', 'P', 'M', 'Q', 'B', 'W'],
        ['F', 'S', 'W', 'T'],
        ['N', 'C', 'R']
    ]
    print(process(stacks, moves))
