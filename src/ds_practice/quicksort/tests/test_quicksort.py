import pytest

from ds_practice.quicksort.quicksort import quicksort


@pytest.mark.parametrize(
    "arr",
    [
        [],
        [1],
        [1, 2, 3, 4, 5],
        [5, 4, 3, 2, 1],
        [3, 1, 4, 1, 5, 9, 2, 6],
        [2, 2, 2, 2],
        [-3, 0, 5, -1, 2],
        [0],
    ],
)
def test_quicksort_sorts(arr: list[int]) -> None:
    original = list(arr)
    result = quicksort(arr, 0, len(arr) - 1)
    assert result == sorted(original)
    assert len(result) == len(original)


def test_quicksort_returns_list() -> None:
    arr = [3, 1, 2]
    result = quicksort(arr, 0, len(arr) - 1)
    assert isinstance(result, list)
    assert result == [1, 2, 3]
