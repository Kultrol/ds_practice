import pytest

from ds_practice.queues.queue import Queue


def test_new_queue_is_empty() -> None:
    queue = Queue()
    assert queue.is_empty()
    assert len(queue) == 0


def test_enqueue_dequeue_fifo() -> None:
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    assert len(queue) == 3
    assert queue.dequeue() == 1
    assert queue.dequeue() == 2
    assert queue.dequeue() == 3
    assert queue.is_empty()


def test_peek_does_not_remove() -> None:
    queue = Queue()
    queue.enqueue("a")
    queue.enqueue("b")
    assert queue.peek() == "a"
    assert len(queue) == 2
    assert queue.dequeue() == "a"


def test_dequeue_empty_raises() -> None:
    queue = Queue()
    with pytest.raises(IndexError):
        queue.dequeue()


def test_peek_empty_raises() -> None:
    queue = Queue()
    with pytest.raises(IndexError):
        queue.peek()


def test_is_empty_after_operations() -> None:
    queue = Queue()
    assert queue.is_empty()
    queue.enqueue(42)
    assert not queue.is_empty()
    queue.dequeue()
    assert queue.is_empty()
