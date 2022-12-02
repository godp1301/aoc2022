def parse_food_list(filename):
    food_list = []
    with open(filename, 'r') as file:
        puzzle = [line[:-1] for line in file.readlines()]
        individual_elf_food_list = []
        for entry in puzzle:
            if entry:
                individual_elf_food_list.append(int(entry))
            else:
                food_list.append(individual_elf_food_list.copy())
                individual_elf_food_list.clear()
        food_list.append(individual_elf_food_list.copy())
    return food_list


def get_highest_calories(calories_list):
    all_elves = []
    for item in calories_list:
        all_elves.append(sum(item))

    return max(all_elves)


if __name__ == '__main__':
    print(get_highest_calories(parse_food_list('input.txt')))
