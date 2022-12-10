head = [0, 0]
tail = [0, 0]
visited_location = [[0, 0]]


def get_head_position():
    global head
    return head


def get_tail_position():
    global head
    return tail


def is_tail_too_far(head, tail):
    return abs(head[0] - tail[0]) >= 2 or abs(head[1] - tail[1]) >= 2


def move(movement):
    print(movement)
    global head, visited_location
    direction, distance = movement.split(' ')

    if direction == 'R':
        for _ in range(int(distance)):
            head[0] += 1
            if is_tail_too_far(head, tail):
                move_tail()
            show_movement()
    if direction == 'L':
        for _ in range(int(distance)):
            head[0] -= 1
            if is_tail_too_far(head, tail):
                move_tail()
            show_movement()
    if direction == 'U':
        for _ in range(int(distance)):
            head[1] += 1
            if is_tail_too_far(head, tail):
                move_tail()
            show_movement()
    if direction == 'D':
        for _ in range(int(distance)):
            head[1] -= 1
            if is_tail_too_far(head, tail):
                move_tail()
            show_movement()

    return head, tail


def move_tail():
    global head, tail
    if head[0] > tail[0] and head[1] == tail[1]:  # head is right of tail
        tail[0] += 1
    elif head[0] < tail[0] and head[1] == tail[1]:  # head is right of tail
        tail[0] -= 1
    elif head[1] > tail[1] and head[0] == tail[0]:  # head is top of tail
        tail[1] += 1
    elif head[1] < tail[1] and head[0] == tail[0]:  # head is down of tail
        tail[1] -= 1
    elif head[1] > tail[1] and head[0] > tail[0]:  # head is top right up of tail
        tail[0] += 1
        tail[1] += 1
    elif head[1] > tail[1] and head[0] < tail[0]:  # head is top left up of tail
        tail[0] -= 1
        tail[1] += 1
    elif head[1] < tail[1] and head[0] > tail[0]:  # head is bottom right down of tail
        tail[0] += 1
        tail[1] -= 1
    elif head[1] < tail[1] and head[0] < tail[0]:  # head is bottom left down of tail
        tail[0] -= 1
        tail[1] -= 1

    if [tail[0], tail[1]] not in visited_location:
        visited_location.append([tail[0], tail[1]])


def number_of_unique_location_visited():
    global visited_location
    return len(visited_location)


def show_movement():
    print(f'H: {head[0]},{head[1]} T: {tail[0]},{tail[1]}')


if __name__ == '__main__':
    with open('input.txt') as file:
        puzzle = [line[:-1] for line in file.readlines()]

    for m in puzzle:
        move(m)
    print(number_of_unique_location_visited())
