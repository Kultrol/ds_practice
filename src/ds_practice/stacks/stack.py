from collections import deque
from typing import Any


class Stack:
    """LIFO stack."""

    def __init__(self) -> None:
        """Initialize empty structure storage here."""
        self.stack = deque()
        pass

    def push(self, value: Any) -> None:
        """Add value to the top of the stack."""
        self.stack.append(value)
        return None

    def pop(self) -> Any:
        """Remove and return the top value. Raise IndexError if empty."""
        if self.is_empty is True:
            raise IndexError
        else:
            return self.stack.pop()

    def peek(self) -> Any:
        """Return the top value without removing it. Raise IndexError if empty."""
        if self.is_empty is True:
            raise IndexError
        else:
            return self.stack[-1]

    def is_empty(self) -> bool:
        """Return True if the stack has no elements."""
        if len(self.stack) == 0:
            return True
        else:
            return False

    def __len__(self) -> int:
        """Return the number of elements in the stack."""
        return len(self.stack)
