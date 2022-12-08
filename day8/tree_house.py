def survey(forest):
    return [[int(c) for c in r] for r in forest]


def top_neighbors(forest, x, y):
    top = []
    for i in range(0, x):
        top.append(forest[i][y])
    return top


def bottom_neighbors(forest, x, y):
    bottom = []
    for i in range(x + 1, len(forest[y])):
        bottom.append(forest[i][y])
    return bottom


def left_neighbors(forest, x, y):
    return forest[x][0:y]


def right_neighbors(forest, x, y):
    return forest[x][y + 1: len(forest[x])]


def is_visible(forest, x, y):
    neighbors = [top_neighbors(forest, x, y),
                 bottom_neighbors(forest, x, y),
                 left_neighbors(forest, x, y),
                 right_neighbors(forest, x, y)]

    if [] in neighbors:
        return True
    else:
        visible = []
        for n in neighbors:
            visible.append(list(filter(lambda h: h >= forest[x][y], n)))
        return [] in visible


def walk(forest):
    sum = 0
    for i, r in enumerate(forest):
        for j, c in enumerate(r):
            sum += is_visible(forest, i, j)
    return sum


if __name__ == '__main__':
    with open('input.txt', 'r') as file:
        puzzle = [line[:-1] for line in file]

    forest = survey(puzzle)
    print(walk(forest))
