import pytest

from ds_practice.stacks.stack import Stack


def test_new_stack_is_empty() -> None:
    stack = Stack()
    assert stack.is_empty()
    assert len(stack) == 0


def test_push_pop_lifo() -> None:
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    assert len(stack) == 3
    assert stack.pop() == 3
    assert stack.pop() == 2
    assert stack.pop() == 1
    assert stack.is_empty()


def test_peek_does_not_remove() -> None:
    stack = Stack()
    stack.push("a")
    stack.push("b")
    assert stack.peek() == "b"
    assert len(stack) == 2
    assert stack.pop() == "b"


def test_pop_empty_raises() -> None:
    stack = Stack()
    with pytest.raises(IndexError):
        stack.pop()


def test_peek_empty_raises() -> None:
    stack = Stack()
    with pytest.raises(IndexError):
        stack.peek()


def test_is_empty_after_operations() -> None:
    stack = Stack()
    assert stack.is_empty()
    stack.push(42)
    assert not stack.is_empty()
    stack.pop()
    assert stack.is_empty()
