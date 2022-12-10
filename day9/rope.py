previous_knot = [0, 0]
current_knot = [0, 0]
rope = [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]
visited_location = [[0, 0]]


def get_head_position():
    global rope
    return rope[0]


def get_tail_position():
    global rope
    return rope[-1]


def get_rope_position():
    global rope
    return rope


def is_following_knot_too_far(head, tail):
    return abs(head[0] - tail[0]) >= 2 or abs(head[1] - tail[1]) >= 2


def move(movement):
    global rope, visited_location
    direction, distance = movement.split(' ')

    if direction == 'R':
        for _ in range(int(distance)):
            rope[0][0] += 1
            move_all_knots(rope)
    if direction == 'L':
        for _ in range(int(distance)):
            rope[0][0] -= 1
            move_all_knots(rope)
    if direction == 'U':
        for _ in range(int(distance)):
            rope[0][1] += 1
            move_all_knots(rope)
    if direction == 'D':
        for _ in range(int(distance)):
            rope[0][1] -= 1
            move_all_knots(rope)

    return rope


def move_all_knots(rope):
    for index in range(1, len(rope)):
        if is_following_knot_too_far(rope[index - 1], rope[index]):
            move_knot(rope[index - 1], rope[index], index == len(rope) - 1)
    show_movement()


def move_knot(previous_knot, current_knot, is_tail):
    if previous_knot[0] > current_knot[0] and previous_knot[1] == current_knot[1]:  # head is right of tail
        current_knot[0] += 1
    elif previous_knot[0] < current_knot[0] and previous_knot[1] == current_knot[1]:  # head is right of tail
        current_knot[0] -= 1
    elif previous_knot[1] > current_knot[1] and previous_knot[0] == current_knot[0]:  # head is top of tail
        current_knot[1] += 1
    elif previous_knot[1] < current_knot[1] and previous_knot[0] == current_knot[0]:  # head is down of tail
        current_knot[1] -= 1
    elif previous_knot[1] > current_knot[1] and previous_knot[0] > current_knot[0]:  # head is top right up of tail
        current_knot[0] += 1
        current_knot[1] += 1
    elif previous_knot[1] > current_knot[1] and previous_knot[0] < current_knot[0]:  # head is top left up of tail
        current_knot[0] -= 1
        current_knot[1] += 1
    elif previous_knot[1] < current_knot[1] and previous_knot[0] > current_knot[0]:  # head is bottom right down of tail
        current_knot[0] += 1
        current_knot[1] -= 1
    elif previous_knot[1] < current_knot[1] and previous_knot[0] < current_knot[0]:  # head is bottom left down of tail
        current_knot[0] -= 1
        current_knot[1] -= 1

    if is_tail:
        if [current_knot[0], current_knot[1]] not in visited_location:
            visited_location.append([current_knot[0], current_knot[1]])


def number_of_unique_location_visited():
    global visited_location
    return len(visited_location)


def show_movement():
    print(f'H: {previous_knot[0]},{previous_knot[1]} T: {current_knot[0]},{current_knot[1]}')


if __name__ == '__main__':
    with open('input.txt') as file:
        puzzle = [line[:-1] for line in file.readlines()]

    for m in puzzle:
        move(m)
    print(number_of_unique_location_visited())
