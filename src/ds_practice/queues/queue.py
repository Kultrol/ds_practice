from collections import deque
from typing import Any


class Queue:
    """FIFO queue."""

    def __init__(self) -> None:
        """Initialize empty structure storage here."""
        self.queue = deque()
        pass

    def enqueue(self, item: Any) -> None:
        """Add item to the back of the queue."""
        self.queue.append(item)
        return None

    def dequeue(self) -> Any:
        """Remove and return the front item. Raise IndexError if empty."""
        if self.is_empty is True:
            raise IndexError
        else:
            return self.queue.popleft()

    def peek(self) -> Any:
        """Return the front item without removing it. Raise IndexError if empty."""
        if self.is_empty is True:
            raise IndexError
        else:
            return self.queue[0]

    def is_empty(self) -> bool:
        """Return True if the queue has no elements."""
        if len(self.queue) == 0:
            return True
        else:
            return False

    def __len__(self) -> int:
        """Return the number of elements in the queue."""
        return len(self.queue)
