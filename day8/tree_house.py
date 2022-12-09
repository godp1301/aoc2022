def survey(forest):
    return [[int(c) for c in r] for r in forest]


def top_neighbors(forest, x, y):
    visible = []
    for t in reversed([forest[i][y] for i in range(0, x)]):
        if t >= forest[x][y]:
            visible.append(t)
            break
        else:
            visible.append(t)
    return visible


def bottom_neighbors(forest, x, y):
    visible = []
    for t in [forest[i][y] for i in range(x + 1, len(forest[y]))]:
        if t >= forest[x][y]:
            visible.append(t)
            break
        else:
            visible.append(t)
    return visible


def left_neighbors(forest, x, y):
    left = []
    for t in reversed(forest[x][0:y]):
        if t >= forest[x][y]:
            left.append(t)
            break
        else:
            left.append(t)
    return left


def right_neighbors(forest, x, y):
    right = []
    for t in forest[x][y + 1: len(forest[x])]:
        if t >= forest[x][y]:
            right.append(t)
            break
        else:
            right.append(t)
    return right


def scenic_score(forest, x, y):
    return len(top_neighbors(forest, x, y)) * len(bottom_neighbors(forest, x, y)) * \
        len(left_neighbors(forest, x, y)) * len(right_neighbors(forest, x, y))


def walk(forest):
    score = 0
    for i, r in enumerate(forest):
        for j, c in enumerate(r):
            x = scenic_score(forest, i, j)
            if x > score:
                score = x
    return score


if __name__ == '__main__':
    with open('input.txt', 'r') as file:
        puzzle = [line[:-1] for line in file]

    forest = survey(puzzle)
    print(walk(forest))
