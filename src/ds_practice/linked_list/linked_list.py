from __future__ import annotations

from typing import Any, Iterator


class Node:
    """Singly linked list node."""

    def __init__(self, value: Any, next: Node | None = None) -> None:
        self.value = value
        self.next = next


class LinkedList:
    """Singly linked list."""

    def __init__(self) -> None:
        """Initialize empty structure storage here."""
        self.head: Node | None = None

    def append(self, value: Any) -> None:
        """Add value at the end of the list."""
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            return None

        current_node = self.head

        while current_node.next is not None:
            current_node = current_node.next

        current_node.next = new_node
        return None

    def prepend(self, value: Any) -> None:
        """Add value at the front of the list."""
        self.head = Node(value, self.head)

    def delete(self, value: Any) -> bool:
        """Remove the first node with value. Return True if removed, else False."""
        if self.head is None:
            return False

        if self.head.value == value:
            self.head = self.head.next
            return True

        previous_node = self.head
        current_node = self.head.next

        while current_node is not None:
            if current_node.value == value:
                previous_node.next = current_node.next
                return True

            previous_node = current_node
            current_node = current_node.next

        return False

    def find(self, value: Any) -> Node | None:
        """Return the first node with value, or None if not found."""
        current_node = self.head
        while current_node is not None:
            if current_node.value == value:
                return current_node

            current_node = current_node.next

        return None

    def is_empty(self) -> bool:
        """Return True if the list has no nodes."""
        if self.head is None:
            return True
        else:
            return False

    def __len__(self) -> int:
        """Return the number of nodes."""
        counter = 0
        current_node = self.head
        while current_node is not None:
            counter += 1
            current_node = current_node.next
        return counter

    def __iter__(self) -> Iterator[Any]:
        """Yield values from head to tail."""
        current_node = self.head
        while current_node is not None:
            yield current_node.value
            current_node = current_node.next
