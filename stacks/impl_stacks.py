from collections import deque

class Stack:

    def __init__(self):
        self.stack = deque()

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        try:
            self.stack.pop()
        except IndexError:
            print("Stack is empty")
            return None

    def peek(self):
        return self.stack[-1]

    def is_empty(self):
        return len(self.stack) == 0

    def __len__(self):
        return len(self.stack)



