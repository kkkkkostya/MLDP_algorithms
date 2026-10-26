"""Итеративные алгоритмы для бинарных деревьев целых чисел."""

from __future__ import annotations

from collections.abc import Iterable
from dataclasses import dataclass


@dataclass
class TreeNode:
    """Узел произвольного бинарного дерева."""

    value: int
    left: TreeNode | None = None
    right: TreeNode | None = None


def _traverse(root: TreeNode | None, order: str) -> list[int]:
    """Выполняет действия N (узел), L (левое), R (правое) через стек."""
    result: list[int] = []
    stack = [(root, False)]
    while stack:
        node, visit = stack.pop()
        if node is None:
            continue
        if visit:
            result.append(node.value)
            continue
        # LIFO: действия кладутся в обратном порядке выполнения.
        for action in reversed(order):
            if action == "N":
                stack.append((node, True))
            elif action == "L":
                stack.append((node.left, False))
            else:
                stack.append((node.right, False))
    return result


def preorder(root: TreeNode | None) -> list[int]:
    """Узел → левое поддерево → правое поддерево (NLR)."""
    return _traverse(root, "NLR")


def inorder(root: TreeNode | None) -> list[int]:
    """Левое поддерево → узел → правое поддерево (LNR)."""
    return _traverse(root, "LNR")


def postorder(root: TreeNode | None) -> list[int]:
    """Левое поддерево → правое поддерево → узел (LRN)."""
    return _traverse(root, "LRN")


def reverse_preorder(root: TreeNode | None) -> list[int]:
    """Узел → правое поддерево → левое поддерево (NRL)."""
    return _traverse(root, "NRL")


def reverse_inorder(root: TreeNode | None) -> list[int]:
    """Правое поддерево → узел → левое поддерево (RNL)."""
    return _traverse(root, "RNL")


def reverse_postorder(root: TreeNode | None) -> list[int]:
    """Правое поддерево → левое поддерево → узел (RLN)."""
    return _traverse(root, "RLN")


class BST:
    """Строгое BST: повторные значения игнорируются, балансировки нет."""

    def __init__(self, values: Iterable[int] = ()) -> None:
        self.root: TreeNode | None = None
        for value in values:
            self.insert(value)

    def insert(self, value: int) -> None:
        """Вставляет значение в подходящую свободную позицию."""
        if self.root is None:
            self.root = TreeNode(value)
            return
        node = self.root
        while True:
            if value == node.value:
                return
            if value < node.value:
                if node.left is None:
                    node.left = TreeNode(value)
                    return
                node = node.left
            else:
                if node.right is None:
                    node.right = TreeNode(value)
                    return
                node = node.right


def is_valid_bst(root: TreeNode | None) -> bool:
    """Проверяет строгие границы, заданные всеми предками узла."""
    stack: list[tuple[TreeNode | None, int | None, int | None]] = [
        (root, None, None)
    ]
    while stack:
        node, lower, upper = stack.pop()
        if node is None:
            continue
        if lower is not None and node.value <= lower:
            return False
        if upper is not None and node.value >= upper:
            return False
        stack.append((node.right, node.value, upper))
        stack.append((node.left, lower, node.value))
    return True


def is_balanced(root: TreeNode | None) -> bool:
    """Проверяет баланс снизу вверх; высота пустого дерева равна нулю."""
    stack = [(root, False)]
    heights: list[int] = []
    while stack:
        node, visited = stack.pop()
        if node is None:
            heights.append(0)
        elif not visited:
            # Сначала вычисляем обе высоты, затем обрабатываем сам узел.
            stack.append((node, True))
            stack.append((node.right, False))
            stack.append((node.left, False))
        else:
            right_height = heights.pop()
            left_height = heights.pop()
            if abs(left_height - right_height) > 1:
                return False
            heights.append(1 + max(left_height, right_height))
    return True
