from __future__ import annotations

from typing import Any


class Node:
    """Binary tree node."""

    def __init__(
        self,
        value: Any,
        left: Node | None = None,
        right: Node | None = None,
    ) -> None:
        self.value = value
        self.left = left
        self.right = right


class BinarySearchTree:
    def __init__(self) -> None:
        """Initialize empty structure storage here."""
        pass

    def insert(self, value: Any) -> None:
        """Insert value into the BST."""
        raise NotImplementedError

    def search(self, value: Any) -> bool:
        """Return True if value is in the tree."""
        raise NotImplementedError

    def inorder(self) -> list[Any]:
        """Return values in inorder (left, root, right) — sorted for a BST."""
        raise NotImplementedError

    def preorder(self) -> list[Any]:
        """Return values in preorder (root, left, right)."""
        raise NotImplementedError

    def postorder(self) -> list[Any]:
        """Return values in postorder (left, right, root)."""
        raise NotImplementedError

    def level_order(self) -> list[Any]:
        """Return values in level-order (breadth-first, left to right)."""
        raise NotImplementedError

    def is_empty(self) -> bool:
        """Return True if the tree has no nodes."""
        raise NotImplementedError

    def __len__(self) -> int:
        """Return the number of nodes."""
        raise NotImplementedError
