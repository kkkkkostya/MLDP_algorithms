from itertools import product

import pytest

from .solution import BST, TreeNode, is_balanced


@pytest.mark.parametrize("root, expected", [
    (None, True),
    (TreeNode(1), True),
    (TreeNode(1, TreeNode(2)), True),
    (TreeNode(1, None, TreeNode(2)), True),
    (TreeNode(1, TreeNode(2, TreeNode(3))), False),
    (TreeNode(1, None, TreeNode(2, None, TreeNode(3))), False),
    (TreeNode(0, TreeNode(0), TreeNode(0)), True),
    # Значения и свойство BST не влияют на баланс.
    (TreeNode(1, TreeNode(100), TreeNode(-100)), True),
])
def test_balance_cases(root, expected):
    assert is_balanced(root) is expected


def test_documented_tree_and_unbalanced_subtree():
    tree = BST([8, 3, 10, 1, 6, 14, 4, 7, 13])
    assert is_balanced(tree.root) is False
    tree.insert(9)
    assert is_balanced(tree.root) is True


def test_equal_root_heights_do_not_guarantee_balance():
    root = TreeNode(0,
                    TreeNode(1, TreeNode(2, TreeNode(3))),
                    TreeNode(4, None, TreeNode(5, None, TreeNode(6))))
    assert is_balanced(root) is False


@pytest.mark.parametrize("direction", ["left", "right"])
def test_deep_chain(direction):
    root = tail = TreeNode(0)
    for value in range(1, 2500):
        child = TreeNode(value)
        setattr(tail, direction, child)
        tail = child
    assert is_balanced(root) is False


def test_all_small_tree_shapes_against_height_definition():
    def shapes(size):
        if size == 0:
            return [None]
        return [TreeNode(0, left, right)
                for left_size in range(size)
                for left, right in product(shapes(left_size),
                                           shapes(size - 1 - left_size))]

    def height(node):
        return 0 if node is None else 1 + max(height(node.left), height(node.right))

    def definition(node):
        return node is None or (
            abs(height(node.left) - height(node.right)) <= 1
            and definition(node.left) and definition(node.right)
        )

    for size in range(8):
        for root in shapes(size):
            assert is_balanced(root) is definition(root)
