def overlaps(assignment):
    pairs = assignment.split(',')
    fp_numbers = pairs[0].split('-')
    fp_lower_bound, fp_upper_bound = int(fp_numbers[0]), int(fp_numbers[1])
    sp_numbers = pairs[1].split('-')
    sp_lower_bound, sp_upper_bound = int(sp_numbers[0]), int(sp_numbers[1])

    if fp_lower_bound in range(sp_lower_bound, sp_upper_bound + 1) \
            or fp_upper_bound in range(sp_lower_bound, sp_upper_bound + 1):
        return True

    if sp_lower_bound in range(fp_lower_bound, fp_upper_bound + 1) \
            or sp_upper_bound in range(fp_lower_bound, fp_upper_bound + 1):
        return True

    return False


def count_pairs_overlapping_others(puzzle):
    sum = 0
    for line in puzzle:
        sum += 1 if overlaps(line) else 0

    return sum


if __name__ == '__main__':
    with open('input.txt', 'r') as file:
        puzzle = [line[:-1] for line in file.readlines()]
    print(count_pairs_overlapping_others(puzzle))
