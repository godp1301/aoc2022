items = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
values = {}
for i in items:
    values[i] = items.index(i) + 1


def get_compartments(items):
    half = int(len(items) / 2)
    return items[0:half], items[half:len(items)]


def get_common(first_compartment, second_compartment):
    return [value for value in first_compartment if value in second_compartment][0]


def get_value_of(item):
    return values[item]


def get_priorities_sum(list_of_items):
    sum = 0
    for items in list_of_items:
        a, b = get_compartments(items)
        sum += get_value_of(get_common(a, b))

    return sum


if __name__ == '__main__':
    with open('input.txt', 'r') as file:
        puzzle = [line[:-1] for line in file.readlines()]

    print(get_priorities_sum(puzzle))
