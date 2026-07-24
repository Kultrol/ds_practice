from ds_practice.linked_list.linked_list import LinkedList


def test_new_list_is_empty() -> None:
    ll = LinkedList()
    assert ll.is_empty()
    assert len(ll) == 0
    assert list(ll) == []


def test_append_order() -> None:
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    assert list(ll) == [1, 2, 3]
    assert len(ll) == 3
    assert not ll.is_empty()


def test_prepend_order() -> None:
    ll = LinkedList()
    ll.prepend(1)
    ll.prepend(2)
    ll.prepend(3)
    assert list(ll) == [3, 2, 1]


def test_find_present_and_missing() -> None:
    ll = LinkedList()
    ll.append("a")
    ll.append("b")
    node = ll.find("b")
    assert node is not None
    assert node.value == "b"
    assert ll.find("z") is None


def test_delete_head_middle_tail_missing() -> None:
    ll = LinkedList()
    for v in (1, 2, 3, 4):
        ll.append(v)

    assert ll.delete(1) is True
    assert list(ll) == [2, 3, 4]

    assert ll.delete(3) is True
    assert list(ll) == [2, 4]

    assert ll.delete(4) is True
    assert list(ll) == [2]

    assert ll.delete(99) is False
    assert list(ll) == [2]

    assert ll.delete(2) is True
    assert ll.is_empty()
