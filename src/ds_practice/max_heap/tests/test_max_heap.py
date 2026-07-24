import pytest

from ds_practice.max_heap.max_heap import MaxHeap


def test_new_heap_is_empty() -> None:
    heap = MaxHeap()
    assert heap.is_empty()
    assert len(heap) == 0


def test_insert_and_peek() -> None:
    heap = MaxHeap()
    heap.insert(3)
    heap.insert(10)
    heap.insert(7)
    assert heap.peek() == 10
    assert len(heap) == 3


def test_extract_max_order() -> None:
    heap = MaxHeap()
    for v in (3, 1, 4, 1, 5, 9, 2, 6):
        heap.insert(v)
    extracted = [heap.extract_max() for _ in range(8)]
    assert extracted == sorted([3, 1, 4, 1, 5, 9, 2, 6], reverse=True)
    assert heap.is_empty()


def test_extract_max_empty_raises() -> None:
    heap = MaxHeap()
    with pytest.raises(IndexError):
        heap.extract_max()


def test_peek_empty_raises() -> None:
    heap = MaxHeap()
    with pytest.raises(IndexError):
        heap.peek()


def test_single_element() -> None:
    heap = MaxHeap()
    heap.insert(42)
    assert heap.peek() == 42
    assert heap.extract_max() == 42
    assert heap.is_empty()
