from functools import cmp_to_key


def compare(l, r):
    if type(l) == int and type(r) == int:
        if l < r:
            return -1
        elif l == r:
            return 0
        else:
            return 1
    elif type(l) == list and type(r) == list:
        i = 0
        while i < len(l) and i < len(r):
            comparison = compare(l[i], r[i])
            if comparison == 1:
                return 1
            if comparison == -1:
                return -1
            i += 1
        if i == len(l) and i < len(r):
            return -1
        elif i == len(r) and i < len(l):
            return 1
        else:
            return 0
    elif type(l) == list and type(r) == int:
        return compare(l, [r])
    elif type(l) == int and type(r) == list:
        return compare([l], r)


if __name__ == '__main__':
    is_right_ordered_packets = []
    with open('input.txt', 'r') as file:
        transmission = [eval(line[:-1]) for line in file.readlines() if line != '\n']

    transmission.append([[2]])
    transmission.append([[6]])

    decoder_key = 1
    transmission = sorted(transmission, key=cmp_to_key(lambda l, r: compare(l, r)))
    for i, p in enumerate(transmission):
        if p == [[2]] or p == [[6]]:
            decoder_key *= i + 1
    print(decoder_key)
