from typing import Any


class MinHeap:
    """Binary min-heap. Parent is always <= children."""

    def __init__(self) -> None:
        """Initialize empty structure storage here."""
        pass

    def insert(self, value: Any) -> None:
        """Insert value and restore the min-heap property."""
        raise NotImplementedError

    def extract_min(self) -> Any:
        """Remove and return the minimum value. Raise IndexError if empty."""
        raise NotImplementedError

    def peek(self) -> Any:
        """Return the minimum value without removing it. Raise IndexError if empty."""
        raise NotImplementedError

    def is_empty(self) -> bool:
        """Return True if the heap has no elements."""
        raise NotImplementedError

    def __len__(self) -> int:
        """Return the number of elements."""
        raise NotImplementedError
