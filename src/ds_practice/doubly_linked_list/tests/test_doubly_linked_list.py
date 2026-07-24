from ds_practice.doubly_linked_list.doubly_linked_list import DoublyLinkedList


def test_new_list_is_empty() -> None:
    dll = DoublyLinkedList()
    assert dll.is_empty()
    assert len(dll) == 0
    assert list(dll) == []


def test_append_order() -> None:
    dll = DoublyLinkedList()
    dll.append(1)
    dll.append(2)
    dll.append(3)
    assert list(dll) == [1, 2, 3]
    assert len(dll) == 3


def test_prepend_order() -> None:
    dll = DoublyLinkedList()
    dll.prepend(1)
    dll.prepend(2)
    dll.prepend(3)
    assert list(dll) == [3, 2, 1]


def test_find_present_and_missing() -> None:
    dll = DoublyLinkedList()
    dll.append("a")
    dll.append("b")
    node = dll.find("b")
    assert node is not None
    assert node.value == "b"
    assert dll.find("z") is None


def test_delete_head_middle_tail_missing() -> None:
    dll = DoublyLinkedList()
    for v in (1, 2, 3, 4):
        dll.append(v)

    assert dll.delete(1) is True
    assert list(dll) == [2, 3, 4]

    assert dll.delete(3) is True
    assert list(dll) == [2, 4]

    assert dll.delete(4) is True
    assert list(dll) == [2]

    assert dll.delete(99) is False
    assert list(dll) == [2]

    assert dll.delete(2) is True
    assert dll.is_empty()


def test_prev_links_after_append() -> None:
    """Nodes should maintain prev pointers after appends."""
    dll = DoublyLinkedList()
    dll.append(10)
    dll.append(20)
    dll.append(30)
    middle = dll.find(20)
    assert middle is not None
    assert middle.prev is not None and middle.prev.value == 10
    assert middle.next is not None and middle.next.value == 30
    assert middle.prev.prev is None
    assert middle.next.next is None
