def find_marker(signal):
    for i, _ in enumerate(signal):
        if len(set(signal[i:i + 4])) == 4:
            return i + 4


def find_som_marker(signal):
    for i, _ in enumerate(signal):
        if len(set(signal[i:i + 14])) == 14:
            return i + 14


if __name__ == '__main__':
    with open('input.txt', 'r') as file:
        puzzle = file.readlines()

    print(find_marker(puzzle[0]))
    print(find_som_marker(puzzle[0]))
