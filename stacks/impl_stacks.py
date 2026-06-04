from collections import deque
from typing import Any


class Stack:

    def __init__(self) -> None:
        self.stack = deque()

    def push(self, value: Any):
        self.stack.append(value)

    def pop(self) -> Any:
        if self.is_empty():
            raise IndexError('Stack is empty')
        return self.stack.pop()

    def peek(self) -> Any:
        return self.stack[-1]

    def is_empty(self) -> bool:
        return len(self.stack) == 0

    def __len__(self) -> int:
        return len(self.stack)



