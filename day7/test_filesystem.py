import treelib

from day7.filesystem import get_initial_rfs, process_terminal_history, get_usage, \
    get_total_usage_for_directories_smaller_than_100k, get_current_node, get_needed_space, get_deletion_candidates, \
    get_folder_size_to_be_deleted


def test_get_initial_rfs():
    rfs = get_initial_rfs()
    assert type(rfs) is treelib.tree.Tree
    assert rfs.root == "/"


def test_process_cd_and_ls_root():
    assert process_terminal_history(['$ cd /', '$ ls']) == '"/"'


def test_node_id_is_the_absolute_path_to_node():
    process_terminal_history(['$ cd /', '$ ls', 'dir a', '$ cd a', '$ ls', 'dir b', '$ cd b'])
    assert get_current_node() == '/a/b'


def test_node_id_is_the_absolute_path_to_node_when_moving_up():
    process_terminal_history(['$ cd /', '$ ls', 'dir a', '$ cd a', '$ ls', 'dir b', '$ cd b', '$ cd ..'])
    assert get_current_node() == '/a'


def test_process_root_content():
    assert process_terminal_history(['$ cd /', '$ ls', 'dir a', '12345 file.txt']) \
           == '{"/": {"children": ["a", "file.txt"]}}'


def test_assert_file_size_at_root():
    assert process_terminal_history(['$ cd /', '$ ls', '12345 file.txt']) == '{"/": {"children": ["file.txt"]}}'
    assert get_usage('/') == 12345


def test_assert_file_size_at_root_using_multiple_files():
    process_terminal_history(['$ cd /', '$ ls', '12345 file.txt', '12345 file2'])
    assert get_usage('/') == 24690


def test_can_move_one_level_up():
    assert process_terminal_history(['$ cd /', '$ ls', 'dir a', '$ cd a', '$ ls', '12345 file2', '$ cd ..']) \
           == '{"/": {"children": [{"a": {"children": ["file2"]}}]}}'


def test_example():
    with open('example.txt', 'r') as file:
        puzzle = [line[:-1] for line in file.readlines()]

    print(process_terminal_history(puzzle))
    assert get_usage('/') == 48381165
    assert get_total_usage_for_directories_smaller_than_100k() == 95437


def test_example_space_needed():
    with open('example.txt', 'r') as file:
        puzzle = [line[:-1] for line in file.readlines()]

    print(process_terminal_history(puzzle))
    needed_space = get_needed_space()
    assert needed_space == 8381165
    candidates = get_deletion_candidates(needed_space)
    assert '/' in candidates
    assert '/d' in candidates

    assert get_folder_size_to_be_deleted(candidates, needed_space) == 24933642
