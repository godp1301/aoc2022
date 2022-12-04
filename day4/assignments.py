def is_contained_in(assignment):
    pairs = assignment.split(',')
    fp_numbers = pairs[0].split('-')
    fp_lower_bound, fp_upper_bound = int(fp_numbers[0]), int(fp_numbers[1])
    sp_numbers = pairs[1].split('-')
    sp_lower_bound, sp_upper_bound = int(sp_numbers[0]), int(sp_numbers[1])

    if fp_lower_bound >= sp_lower_bound and fp_upper_bound <= sp_upper_bound \
            or sp_lower_bound >= fp_lower_bound and sp_upper_bound <= fp_upper_bound:
        return True

    return False


def count_pairs_contained_in_others(puzzle):
    sum = 0
    for line in puzzle:
        sum += 1 if is_contained_in(line) else 0

    return sum


if __name__ == '__main__':
    with open('input.txt', 'r') as file:
        puzzle = [line[:-1] for line in file.readlines()]
    print(count_pairs_contained_in_others(puzzle))
