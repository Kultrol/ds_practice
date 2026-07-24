from typing import Any


class MaxHeap:
    """Binary max-heap. Parent is always >= children."""

    def __init__(self) -> None:
        """Initialize empty structure storage here."""
        pass

    def insert(self, value: Any) -> None:
        """Insert value and restore the max-heap property."""
        raise NotImplementedError

    def extract_max(self) -> Any:
        """Remove and return the maximum value. Raise IndexError if empty."""
        raise NotImplementedError

    def peek(self) -> Any:
        """Return the maximum value without removing it. Raise IndexError if empty."""
        raise NotImplementedError

    def is_empty(self) -> bool:
        """Return True if the heap has no elements."""
        raise NotImplementedError

    def __len__(self) -> int:
        """Return the number of elements."""
        raise NotImplementedError
