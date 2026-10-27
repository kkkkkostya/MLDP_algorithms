from itertools import permutations
from random import Random

import pytest

from .solution import AVL


def assert_avl(tree, expected):
    """Независимо пересчитывает высоты, проверяет границы BST и баланс."""
    seen = set()

    def check(node, lower=None, upper=None):
        if node is None:
            return 0
        assert id(node) not in seen
        seen.add(id(node))
        assert lower is None or lower < node.value
        assert upper is None or node.value < upper
        left = check(node.left, lower, node.value)
        right = check(node.right, node.value, upper)
        assert abs(left - right) <= 1
        assert node.height == 1 + max(left, right)
        return node.height

    check(tree.root)
    assert tree.inorder() == sorted(expected)
    assert len(seen) == len(expected)


def test_empty_and_missing_values():
    tree = AVL()
    assert not tree.search(1)
    assert not tree.delete(1)
    assert tree.visualize() == "(empty)"
    assert_avl(tree, set())


def test_single_node_and_duplicates():
    tree = AVL([0, 0, 0])
    assert tree.search(0) is True
    assert_avl(tree, {0})
    assert tree.delete(0) is True
    assert tree.root is None
    assert tree.delete(0) is False
    assert_avl(tree, set())


@pytest.mark.parametrize("values", [
    [30, 20, 10],  # LL
    [10, 20, 30],  # RR
    [30, 10, 20],  # LR
    [10, 30, 20],  # RL
])
def test_all_insertion_rotations(values):
    tree = AVL()
    expected = set()
    for value in values:
        tree.insert(value)
        expected.add(value)
        assert_avl(tree, expected)
    assert tree.root.value == 20
    assert tree.root.left.value == 10
    assert tree.root.right.value == 30


@pytest.mark.parametrize("values, deleted, new_root", [
    ([3, 2, 4, 1], 4, 2),             # LL
    ([2, 1, 3, 4], 1, 3),             # RR
    ([5, 2, 6, 3], 6, 3),             # LR
    ([2, 1, 5, 4], 1, 4),             # RL
    ([4, 2, 5, 1, 3], 5, 2),          # баланс левого ребёнка 0
    ([2, 1, 4, 3, 5], 1, 4),          # баланс правого ребёнка 0
])
def test_deletion_rotations(values, deleted, new_root):
    tree = AVL(values)
    assert tree.delete(deleted)
    assert tree.root.value == new_root
    assert_avl(tree, set(values) - {deleted})


@pytest.mark.parametrize("values, deleted", [
    ([2, 1, 3], 1),                  # лист
    ([2, 1], 2),                     # корень с одним ребёнком
    ([4, 2, 6, 1], 2),               # внутренний узел с одним ребёнком
    ([2, 1, 3], 2),                  # два ребёнка, преемник — правый ребёнок
    ([20, 10, 40, 5, 15, 30, 50, 35], 20),  # у преемника есть правый ребёнок
])
def test_deletion_shapes(values, deleted):
    tree = AVL(values)
    assert tree.delete(deleted)
    assert not tree.search(deleted)
    assert_avl(tree, set(values) - {deleted})


def test_negative_and_large_values():
    values = [-10**100, -3, 0, 2, 10**100]
    tree = AVL(iter(values))
    assert_avl(tree, set(values))
    for value in values:
        assert tree.search(value)
    assert not tree.search(1)


def test_all_small_insertion_and_deletion_orders():
    values = range(4)
    for insertion in permutations(values):
        for deletion in permutations(values):
            tree = AVL(insertion)
            expected = set(values)
            assert_avl(tree, expected)
            for value in deletion:
                assert tree.delete(value)
                expected.remove(value)
                assert_avl(tree, expected)


def test_sorted_input_and_full_deletion():
    tree = AVL()
    expected = set()
    for value in range(1000):
        tree.insert(value)
        expected.add(value)
    assert_avl(tree, expected)
    assert tree.root.height <= 2 * len(expected).bit_length()
    for value in range(1000):
        assert tree.delete(value)
        expected.remove(value)
        assert_avl(tree, expected)


def test_random_operations_against_set():
    random = Random(2026)
    tree = AVL()
    expected = set()
    for _ in range(2000):
        value = random.randrange(-100, 101)
        operation = random.choice(["insert", "delete", "search"])
        if operation == "insert":
            tree.insert(value)
            expected.add(value)
        elif operation == "delete":
            assert tree.delete(value) is (value in expected)
            expected.discard(value)
        else:
            assert tree.search(value) is (value in expected)
        assert_avl(tree, expected)


def test_visualization_and_documented_sequence():
    tree = AVL([30, 10, 20, 40, 50])
    assert tree.visualize() == (
        "20 (h=3, b=-1)\n"
        "  L: 10 (h=1, b=0)\n"
        "  R: 40 (h=2, b=0)\n"
        "    L: 30 (h=1, b=0)\n"
        "    R: 50 (h=1, b=0)"
    )
    assert tree.delete(10)
    assert tree.visualize() == (
        "40 (h=3, b=1)\n"
        "  L: 20 (h=2, b=-1)\n"
        "    R: 30 (h=1, b=0)\n"
        "  R: 50 (h=1, b=0)"
    )
    assert_avl(tree, {20, 30, 40, 50})
