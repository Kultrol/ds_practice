from typing import Any

from ds_practice.partition import partition


def quicksort(arr: list[Any], low: int, high: int) -> list[Any]:
    if low < high:
        pivot_index = partition(arr, low, high)
        quicksort(arr, low, pivot_index - 1)
        quicksort(arr, pivot_index + 1, high)

    return arr
