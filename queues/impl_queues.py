from collections import deque

class Queue:
    def __init__(self):
        self.queue = deque()

    def enqueue(self,item):
        self.queue.append(item)

    def dequeue(self):
        return self.queue.popleft()

    def peek(self):
        return self.queue[0]

    def is_empty(self):
        return len(self.queue) == 0

    def __len__(self):
        return len(self.queue)

    
