"""Два варианта слияния отсортированных односвязных списков."""

from __future__ import annotations

from collections.abc import Iterable


class ListNode:
    """Узел односвязного списка целых чисел."""

    def __init__(self, value: int, next_node: ListNode | None = None) -> None:
        self.value = value
        self.next = next_node


def merge_with_dummy(list1: ListNode | None, list2: ListNode | None) -> ListNode | None:
    """Сливает списки, используя фиктивный начальный узел."""
    dummy = ListNode(0)
    tail = dummy

    while list1 is not None and list2 is not None:
        if list1.value <= list2.value:
            tail.next = list1
            list1 = list1.next
        else:
            tail.next = list2
            list2 = list2.next
        tail = tail.next

    tail.next = list1 if list1 is not None else list2
    return dummy.next


def merge_without_dummy(list1: ListNode | None, list2: ListNode | None) -> ListNode | None:
    """Сливает списки без нового фиктивного узла, переиспользуя их узлы."""
    if list1 is None:
        return list2
    if list2 is None:
        return list1

    if list1.value <= list2.value:
        head = tail = list1
        list1 = list1.next
    else:
        head = tail = list2
        list2 = list2.next

    while list1 is not None and list2 is not None:
        if list1.value <= list2.value:
            tail.next = list1
            list1 = list1.next
        else:
            tail.next = list2
            list2 = list2.next
        tail = tail.next

    tail.next = list1 if list1 is not None else list2
    return head


def from_values(values: Iterable[int]) -> ListNode | None:
    """Строит список."""
    head: ListNode | None = None
    tail: ListNode | None = None
    for value in values:
        node = ListNode(value)
        if head is None:
            head = node
        else:
            tail.next = node
        tail = node
    return head


def to_values(head: ListNode | None) -> list[int]:
    """Преобразует список в обычный список."""
    result: list[int] = []
    while head is not None:
        result.append(head.value)
        head = head.next
    return result
