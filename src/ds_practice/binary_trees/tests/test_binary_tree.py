from ds_practice.binary_trees.binary_tree import BinarySearchTree


def test_new_tree_is_empty() -> None:
    tree = BinarySearchTree()
    assert tree.is_empty()
    assert len(tree) == 0
    assert tree.inorder() == []
    assert tree.preorder() == []
    assert tree.postorder() == []
    assert tree.level_order() == []


def test_insert_and_search() -> None:
    tree = BinarySearchTree()
    for v in (5, 3, 7, 2, 4, 6, 8):
        tree.insert(v)
    assert len(tree) == 7
    assert not tree.is_empty()
    assert tree.search(5) is True
    assert tree.search(4) is True
    assert tree.search(8) is True
    assert tree.search(1) is False
    assert tree.search(9) is False


def test_traversals() -> None:
    """
    Build:
            5
           / \\
          3   7
         / \\ / \\
        2  4 6  8
    """
    tree = BinarySearchTree()
    for v in (5, 3, 7, 2, 4, 6, 8):
        tree.insert(v)

    assert tree.inorder() == [2, 3, 4, 5, 6, 7, 8]
    assert tree.preorder() == [5, 3, 2, 4, 7, 6, 8]
    assert tree.postorder() == [2, 4, 3, 6, 8, 7, 5]
    assert tree.level_order() == [5, 3, 7, 2, 4, 6, 8]


def test_single_node() -> None:
    tree = BinarySearchTree()
    tree.insert(42)
    assert len(tree) == 1
    assert tree.search(42) is True
    assert tree.inorder() == [42]
    assert tree.preorder() == [42]
    assert tree.postorder() == [42]
    assert tree.level_order() == [42]
