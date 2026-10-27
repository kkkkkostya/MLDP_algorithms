"""AVL-дерево целых чисел: вставка, удаление, поиск и визуализация."""

from __future__ import annotations

from collections.abc import Iterable
from dataclasses import dataclass


@dataclass
class AVLNode:
    value: int
    left: AVLNode | None = None
    right: AVLNode | None = None
    height: int = 1


def _height(node: AVLNode | None) -> int:
    return 0 if node is None else node.height


def _update(node: AVLNode) -> None:
    node.height = 1 + max(_height(node.left), _height(node.right))


def _balance(node: AVLNode) -> int:
    return _height(node.left) - _height(node.right)


def _rotate_right(root: AVLNode) -> AVLNode:
    pivot = root.left
    assert pivot is not None
    root.left = pivot.right
    pivot.right = root
    _update(root)
    _update(pivot)
    return pivot


def _rotate_left(root: AVLNode) -> AVLNode:
    pivot = root.right
    assert pivot is not None
    root.right = pivot.left
    pivot.left = root
    _update(root)
    _update(pivot)
    return pivot


def _rebalance(node: AVLNode) -> AVLNode:
    _update(node)
    if _balance(node) > 1:
        assert node.left is not None
        if _balance(node.left) < 0:
            node.left = _rotate_left(node.left)
        return _rotate_right(node)
    if _balance(node) < -1:
        assert node.right is not None
        if _balance(node.right) > 0:
            node.right = _rotate_right(node.right)
        return _rotate_left(node)
    return node


class AVL:
    """Строгое BST без дубликатов, с балансом высот в каждом узле."""

    def __init__(self, values: Iterable[int] = ()) -> None:
        self.root: AVLNode | None = None
        for value in values:
            self.insert(value)

    def search(self, value: int) -> bool:
        """Возвращает True, если значение есть в дереве."""
        node = self.root
        while node is not None:
            if value == node.value:
                return True
            node = node.left if value < node.value else node.right
        return False

    def insert(self, value: int) -> None:
        """Добавляет значение; повторная вставка не меняет дерево."""
        def add(node: AVLNode | None) -> AVLNode:
            if node is None:
                return AVLNode(value)
            if value < node.value:
                node.left = add(node.left)
            elif value > node.value:
                node.right = add(node.right)
            else:
                return node
            return _rebalance(node)

        self.root = add(self.root)

    def delete(self, value: int) -> bool:
        """Удаляет значение; возвращает False, если его не было."""
        if not self.search(value):
            return False

        def remove(node: AVLNode | None, key: int) -> AVLNode | None:
            if node is None:
                return None
            if key < node.value:
                node.left = remove(node.left, key)
            elif key > node.value:
                node.right = remove(node.right, key)
            else:
                if node.left is None:
                    return node.right
                if node.right is None:
                    return node.left
                successor = node.right
                while successor.left is not None:
                    successor = successor.left
                node.value = successor.value
                node.right = remove(node.right, successor.value)
            return _rebalance(node)

        self.root = remove(self.root, value)
        return True

    def inorder(self) -> list[int]:
        """Возвращает значения по возрастанию."""
        result: list[int] = []

        def visit(node: AVLNode | None) -> None:
            if node is not None:
                visit(node.left)
                result.append(node.value)
                visit(node.right)

        visit(self.root)
        return result

    def visualize(self) -> str:
        """Возвращает схему с высотами h и балансом b; L/R — стороны детей."""
        if self.root is None:
            return "(empty)"
        lines: list[str] = []

        def draw(node: AVLNode, prefix: str, label: str) -> None:
            lines.append(f"{prefix}{label}{node.value} "
                         f"(h={node.height}, b={_balance(node)})")
            if node.left is not None:
                draw(node.left, prefix + "  ", "L: ")
            if node.right is not None:
                draw(node.right, prefix + "  ", "R: ")

        draw(self.root, "", "")
        return "\n".join(lines)


if __name__ == "__main__":
    tree = AVL()
    for number in [30, 10, 20, 40, 50]:
        tree.insert(number)
        print(f"insert({number})\n{tree.visualize()}\n")
    tree.delete(10)
    print(f"delete(10)\n{tree.visualize()}")
