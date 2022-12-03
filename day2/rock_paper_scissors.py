score_map = {'A X': 3, 'A Y': 4, 'A Z': 8, 'B X': 1, 'B Y': 5, 'B Z': 9, 'C X': 2, 'C Y': 6, 'C Z': 7}


def calculate(round):
    return score_map.get(round)


def game(filename):
    with open(filename, 'r') as file:
        puzzle = [line[:-1] for line in file.readlines()]

    score = 0
    for round in puzzle:
        score += calculate(round)

    return score


if __name__ == '__main__':
    print(game('input.txt'))
