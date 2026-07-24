from ds_practice.partition.partition import partition


def _assert_lomuto(arr: list[int], low: int, high: int, pivot_index: int) -> None:
    pivot = arr[pivot_index]
    assert low <= pivot_index <= high
    for i in range(low, pivot_index):
        assert arr[i] < pivot
    for i in range(pivot_index + 1, high + 1):
        assert arr[i] >= pivot


def test_partition_basic() -> None:
    arr = [3, 1, 4, 1, 5, 9, 2, 6]
    high = len(arr) - 1
    pivot_index = partition(arr, 0, high)
    _assert_lomuto(arr, 0, high, pivot_index)
    # original pivot was last element (6)
    assert arr[pivot_index] == 6


def test_partition_single_element() -> None:
    arr = [42]
    assert partition(arr, 0, 0) == 0
    assert arr == [42]


def test_partition_two_elements() -> None:
    arr = [2, 1]
    pivot_index = partition(arr, 0, 1)
    _assert_lomuto(arr, 0, 1, pivot_index)
    assert arr[pivot_index] == 1


def test_partition_already_ordered() -> None:
    arr = [1, 2, 3, 4]
    pivot_index = partition(arr, 0, 3)
    _assert_lomuto(arr, 0, 3, pivot_index)
    assert arr[pivot_index] == 4


def test_partition_subarray_bounds() -> None:
    """Only the subarray [low, high] is partitioned; outside stays put."""
    arr = [99, 3, 1, 4, 2, 88]
    low, high = 1, 4
    outer_left, outer_right = arr[0], arr[5]
    pivot_index = partition(arr, low, high)
    assert arr[0] == outer_left
    assert arr[5] == outer_right
    _assert_lomuto(arr, low, high, pivot_index)
    assert arr[pivot_index] == 2


def test_partition_all_equal() -> None:
    arr = [5, 5, 5, 5]
    pivot_index = partition(arr, 0, 3)
    _assert_lomuto(arr, 0, 3, pivot_index)
    assert arr[pivot_index] == 5
