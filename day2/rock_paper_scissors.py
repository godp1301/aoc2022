score_map = {'A X': 4, 'A Y': 8, 'A Z': 3, 'B X': 1, 'B Y': 5, 'B Z': 9, 'C X': 7, 'C Y': 2, 'C Z': 6}


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
