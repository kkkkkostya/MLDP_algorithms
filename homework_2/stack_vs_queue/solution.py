from __future__ import annotations
from typing import Generic, TypeVar


T = TypeVar("T")


class _Node(Generic[T]):
    """Один узел односвязного списка."""

    def __init__(self, value: T, next_node: _Node[T] | None = None) -> None:
        self.value = value
        self.next: _Node[T] | None = next_node


class Stack(Generic[T]):
    """Стек LIFO на односвязном списке."""

    def __init__(self) -> None:
        self._top: _Node[T] | None = None
        self._size = 0

    def push(self, value: T) -> None:
        """Добавляет значение на вершину стека."""
        self._top = _Node(value, self._top)
        self._size += 1

    def pop(self) -> T:
        """Удаляет и возвращает значение с вершины."""
        if self._top is None:
            raise IndexError("pop from empty stack")

        node = self._top
        self._top = node.next
        self._size -= 1
        return node.value

    def peek(self) -> T:
        """Возвращает вершину, не удаляя её."""
        if self._top is None:
            raise IndexError("peek from empty stack")
        return self._top.value

    def is_empty(self) -> bool:
        return self._top is None

    def __len__(self) -> int:
        return self._size


class Queue(Generic[T]):
    """Очередь FIFO на односвязном списке."""

    def __init__(self) -> None:
        self._head: _Node[T] | None = None
        self._tail: _Node[T] | None = None
        self._size = 0

    def enqueue(self, value: T) -> None:
        """Добавляет значение в конец очереди."""
        new_node = _Node(value)
        if self._tail is None:
            self._head = new_node
        else:
            self._tail.next = new_node
        self._tail = new_node
        self._size += 1

    def dequeue(self) -> T:
        """Удаляет и возвращает значение из начала очереди."""
        if self._head is None:
            raise IndexError("dequeue from empty queue")

        node = self._head
        self._head = node.next
        if self._head is None:
            self._tail = None
        self._size -= 1
        return node.value

    def peek(self) -> T:
        """Возвращает первый элемент, не удаляя его."""
        if self._head is None:
            raise IndexError("peek from empty queue")
        return self._head.value

    def is_empty(self) -> bool:
        return self._head is None

    def __len__(self) -> int:
        return self._size
