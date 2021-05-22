def sort_by_choose(param: list):
    for i in range(len(param)):
        i_min = i
        for j in range(i+1, len(param)):
            if param[j] < param[i_min]:
                i_min = j
        param[i], param[i_min] = param[i_min], param[i]
    return param


def test_sort_empty_list():
    assert sort_by_choose([]) == []


def test_sort():
    assert sort_by_choose([1, 2, 3]) == [1, 2, 3]
    assert sort_by_choose([2, 3, 4, 1, 5 ]) == [1, 2, 3, 4, 5]