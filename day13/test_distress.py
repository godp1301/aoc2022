from day13.distress import compare


def test_compare_integers_only():
    assert compare(1, 1) == 0
    assert compare(1, 2) == -1
    assert compare(2, 1) == 1


def test_compare_same_size_simple_lists():
    assert compare([1, 1, 3, 1, 1], [1, 1, 5, 1, 1]) == -1
    assert compare([1, 1, 5, 1, 1], [1, 1, 3, 1, 1]) == 1


def test_compare_mixed_type_left():
    assert compare([[1], [2, 3, 4]], [[1], 4]) == -1


def test_compare_mixed_type_right():
    assert compare([9], [[8, 7, 6]]) == 1


def test_left_is_running_out_of_items():
    assert compare([[4, 4], 4, 4], [[4, 4], 4, 4, 4]) == -1
    assert compare([], [3]) == -1


def test_right_is_running_out_of_items():
    assert compare([7, 7, 7, 7], [7, 7, 7]) == 1
    assert compare([[[]]], [[]]) == 1


def test_a_more_complex_example():
    assert compare([1, [2, [3, [4, [5, 6, 7]]]], 8, 9], [1, [2, [3, [4, [5, 6, 0]]]], 8, 9]) == 1


def test_example():
    is_right_ordered_packets = []
    packets = '[1,1,3,1,1]\n' + \
              '[1,1,5,1,1]\n' + \
              '\n' + \
              '[[1],[2,3,4]]\n' + \
              '[[1],4]\n' + \
              '\n' + \
              '[9]\n' + \
              '[[8,7,6]]\n' + \
              '\n' + \
              '[[4,4],4,4]\n' + \
              '[[4,4],4,4,4]\n' + \
              '\n' + \
              '[7,7,7,7]\n' + \
              '[7,7,7]\n' + \
              '\n' + \
              '[]\n' + \
              '[3]\n' + \
              '\n' + \
              '[[[]]]\n' + \
              '[[]]\n' + \
              '\n' + \
              '[1,[2,[3,[4,[5,6,7]]]],8,9]\n' + \
              '[1,[2,[3,[4,[5,6,0]]]],8,9]\n'

    transmission = packets.split('\n')
    for i in range(0, len(transmission), 3):
        is_right_ordered_packets.append(compare(eval(transmission[i]), eval(transmission[i + 1])))

    sum = 0
    for i, v in enumerate(is_right_ordered_packets):
        if v == -1:
            sum += i + 1
    print(sum)
