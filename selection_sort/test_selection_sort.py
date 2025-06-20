from selection_sort2 import selection_sort2

def test_sorted():
    assert selection_sort([1, 2, 3]) == [1, 2, 3]

def test_reverse():
    assert selection_sort([3, 2, 1]) == [1, 2, 3]

def test_duplicates():
    assert selection_sort([29, 10, 14, 37, 14]) == [10, 14, 14, 29, 37]
