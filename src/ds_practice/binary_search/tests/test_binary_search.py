import pytest

from ds_practice.binary_search.binary_search import binary_search


@pytest.mark.parametrize(
    ("arr", "target", "expected"),
    [
        ([], 1, -1),
        ([5], 5, 0),
        ([5], 4, -1),
        ([1, 3, 5, 7, 9], 1, 0),
        ([1, 3, 5, 7, 9], 5, 2),
        ([1, 3, 5, 7, 9], 9, 4),
        ([1, 3, 5, 7, 9], 4, -1),
        ([1, 3, 5, 7, 9], 0, -1),
        ([1, 3, 5, 7, 9], 10, -1),
        ([-5, -2, 0, 4], -2, 1),
        ([-5, -2, 0, 4], 3, -1),
    ],
)
def test_binary_search(arr: list[int], target: int, expected: int) -> None:
    assert binary_search(arr, target) == expected
