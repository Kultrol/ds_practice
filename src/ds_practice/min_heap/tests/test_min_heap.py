import pytest

from ds_practice.min_heap.min_heap import MinHeap


def test_new_heap_is_empty() -> None:
    heap = MinHeap()
    assert heap.is_empty()
    assert len(heap) == 0


def test_insert_and_peek() -> None:
    heap = MinHeap()
    heap.insert(3)
    heap.insert(10)
    heap.insert(7)
    assert heap.peek() == 3
    assert len(heap) == 3


def test_extract_min_order() -> None:
    heap = MinHeap()
    for v in (3, 1, 4, 1, 5, 9, 2, 6):
        heap.insert(v)
    extracted = [heap.extract_min() for _ in range(8)]
    assert extracted == sorted([3, 1, 4, 1, 5, 9, 2, 6])
    assert heap.is_empty()


def test_extract_min_empty_raises() -> None:
    heap = MinHeap()
    with pytest.raises(IndexError):
        heap.extract_min()


def test_peek_empty_raises() -> None:
    heap = MinHeap()
    with pytest.raises(IndexError):
        heap.peek()


def test_single_element() -> None:
    heap = MinHeap()
    heap.insert(42)
    assert heap.peek() == 42
    assert heap.extract_min() == 42
    assert heap.is_empty()
