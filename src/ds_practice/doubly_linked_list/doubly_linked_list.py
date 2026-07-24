from __future__ import annotations

from typing import Any, Iterator


class Node:
    """Doubly linked list node."""

    def __init__(
        self,
        value: Any,
        prev: Node | None = None,
        next: Node | None = None,
    ) -> None:
        self.value = value
        self.prev = prev
        self.next = next


class DoublyLinkedList:
    """Doubly linked list."""

    def __init__(self) -> None:
        """Initialize empty structure storage here."""
        self.head: Node | None = None

    def append(self, value: Any) -> None:
        """Add value at the end of the list."""
        if self.head is None:
            self.head = Node(value, prev=None, next=None)

        current_node = self.head
        while current_node.next is not None:
            current_node = current_node.next

        current_node.next = Node(value, prev=current_node, next=None)

    def prepend(self, value: Any) -> None:
        """Add value at the front of the list."""
        if self.head is None:
            self.head = Node(value, None, None)

        self.head.prev = Node(value, None, self.head)
        self.head = Node(value, None, self.head)

    def delete(self, value: Any) -> bool:
        """Remove the first node with value. Return True if removed, else False."""
        # If the list is empty

        raise NotImplementedError

    def find(self, value: Any) -> Node | None:
        """Return the first node with value, or None if not found."""
        raise NotImplementedError

    def is_empty(self) -> bool:
        """Return True if the list has no nodes."""
        raise NotImplementedError

    def __len__(self) -> int:
        """Return the number of nodes."""
        raise NotImplementedError

    def __iter__(self) -> Iterator[Any]:
        """Yield values from head to tail."""
        raise NotImplementedError
