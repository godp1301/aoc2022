from treelib import Tree

rfs = Tree()
rfs.create_node('/', '/')
current_folder = None
current_path = []


def get_initial_rfs():
    return rfs


def change_directory(location):
    global current_folder, current_path

    if location == '..':
        current_path.pop()
        current_path.pop()

        if not current_path:
            current_path.append('/')
    else:
        if len(current_path) > 1 and len(current_path) % 2 == 0:
            current_path.append('/')
        current_path.append(location)

    current_folder = rfs.get_node("".join(p for p in current_path))


def get_current_node():
    global current_folder
    return current_folder.identifier


def make_dir(dirname):
    global current_folder, current_path
    absolute_path = ''.join(p for p in current_path)

    if absolute_path == "/":
        rfs.create_node(dirname, f'{absolute_path}{dirname}', parent=current_folder)
    else:
        rfs.create_node(dirname, f'{absolute_path}/{dirname}', parent=current_folder)


def touch_file(file_info):
    global current_folder
    size, name = file_info.split(' ')
    absolute_path = ''.join(p for p in current_path)
    rfs.create_node(name, f'{absolute_path}/{name}', data=int(size), parent=current_folder)


def process_terminal_history(history):
    for line in history:
        if line.startswith('$ cd'):
            change_directory(line.split(' ')[2])
        elif line.startswith('$ ls'):
            continue
        elif line.startswith('dir'):
            make_dir(line.split(' ')[1])
        else:
            touch_file(line)

    return rfs.to_json(with_data=True)


def get_usage(location):
    size = 0
    for f in rfs.expand_tree(location):
        n = rfs.get_node(f)
        size += n.data if n.data else 0
    return size


def get_total_usage_for_directories_smaller_than_100k():
    current_folder_size, total_size = 0, 0
    for f in rfs.expand_tree('/'):
        n = rfs.get_node(f)
        if n.fpointer:
            current_folder_size = get_usage(n.identifier)
            if current_folder_size < 100000:
                total_size += current_folder_size

    return total_size


if __name__ == '__main__':
    with open('input.txt', 'r') as file:
        puzzle = [line[:-1] for line in file.readlines()]

    process_terminal_history(puzzle)
    print(get_total_usage_for_directories_smaller_than_100k())
