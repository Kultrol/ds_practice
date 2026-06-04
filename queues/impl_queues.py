from collections import deque
from typing import Any

class Queue:
    def __init__(self) -> None:
        self.queue = deque()

    def enqueue(self,item: Any) -> None:
        self.queue.append(item)

    def dequeue(self) -> Any:
        if self.is_empty():
            raise IndexError('Queue is empty')
        return self.queue.popleft()

    def peek(self) -> Any:
        if self.is_empty():
            raise IndexError('Queue is empty')
        return self.queue[0]

    def is_empty(self) -> bool:
        return len(self.queue) == 0

    def __len__(self) -> int:
        return len(self.queue)


