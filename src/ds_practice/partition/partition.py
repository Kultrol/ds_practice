from typing import Any


def partition(arr: list[Any], low: int, high: int) -> int:

    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[j], arr[i] = arr[i], arr[j]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    pivot_index = i + 1
    return pivot_index
