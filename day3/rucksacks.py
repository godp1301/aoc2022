items = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
values = {}
for i in items:
    values[i] = items.index(i) + 1


def get_common(elves):
    return [value for value in elves[0] if value in elves[1] and value in elves[2]][0]


def get_value_of(item):
    return values[item]


def get_priorities_sum(list_of_items):
    i, sum = 0, 0
    for _ in range(int(len(list_of_items)/3)):
        sum += get_value_of(get_common(list_of_items[i: i+3]))
        i += 3

    return sum


if __name__ == '__main__':
    with open('input.txt', 'r') as file:
        puzzle = [line[:-1] for line in file.readlines()]

    print(get_priorities_sum(puzzle))
