from bubble_sort2 import bubble_sort2

def test_sorted():
    assert bubble_sort2([1, 2, 3]) == [1, 2, 3]

def test_reverse():
    assert bubble_sort2([3, 2, 1]) == [1, 2, 3]

def test_duplicates():
    assert bubble_sort2([4, 5, 3, 4]) == [3, 4, 4, 5]
