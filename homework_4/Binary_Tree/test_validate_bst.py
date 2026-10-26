import pytest

from .solution import BST, TreeNode, is_valid_bst


@pytest.mark.parametrize("root, expected", [
    (None, True),
    (TreeNode(0), True),
    (TreeNode(2, TreeNode(1), TreeNode(3)), True),
    (TreeNode(0, TreeNode(-10), TreeNode(10)), True),
    (TreeNode(2, TreeNode(3)), False),
    (TreeNode(2, None, TreeNode(1)), False),
    (TreeNode(2, TreeNode(2)), False),
    (TreeNode(2, None, TreeNode(2)), False),
    # Локальные сравнения с родителями верны, но нарушена граница предка.
    (TreeNode(10, TreeNode(5, None, TreeNode(12)), TreeNode(15)), False),
    (TreeNode(10, TreeNode(5), TreeNode(15, TreeNode(6))), False),
    (TreeNode(10, TreeNode(5, None, TreeNode(10))), False),
    (TreeNode(0, TreeNode(-(10**100)), TreeNode(10**100)), True),
])
def test_validation_cases(root, expected):
    assert is_valid_bst(root) is expected


def test_documented_examples():
    tree = BST([8, 3, 10, 1, 6, 14, 4, 7, 13])
    assert is_valid_bst(tree.root) is True
    tree.root.left.right.right.value = 9
    assert is_valid_bst(tree.root) is False


def test_deep_violation_of_root_bound():
    root = TreeNode(0)
    tail = root
    for value in range(1, 2500):
        tail.right = TreeNode(value)
        tail = tail.right
    assert is_valid_bst(root) is True
    tail.left = TreeNode(-1)
    assert is_valid_bst(root) is False
