from itertools import permutations

import pytest

from .solution import (
    BST, TreeNode, inorder, is_valid_bst, postorder, preorder,
    reverse_inorder, reverse_postorder, reverse_preorder,
)


TRAVERSALS = [
    (preorder, [8, 3, 1, 6, 4, 7, 10, 14, 13]),
    (inorder, [1, 3, 4, 6, 7, 8, 10, 13, 14]),
    (postorder, [1, 4, 7, 6, 3, 13, 14, 10, 8]),
    (reverse_preorder, [8, 10, 14, 13, 3, 6, 7, 4, 1]),
    (reverse_inorder, [14, 13, 10, 8, 7, 6, 4, 3, 1]),
    (reverse_postorder, [13, 14, 10, 7, 4, 6, 1, 3, 8]),
]


@pytest.mark.parametrize("traverse, expected", TRAVERSALS)
def test_documented_tree(traverse, expected):
    tree = BST([8, 3, 10, 1, 6, 14, 4, 7, 13])
    assert traverse(tree.root) == expected
    # Повторный вызов возвращает новый список и не меняет дерево.
    assert traverse(tree.root) == expected
    assert is_valid_bst(tree.root)


@pytest.mark.parametrize("traverse, _", TRAVERSALS)
def test_empty_and_single_node(traverse, _):
    assert traverse(BST().root) == []
    assert traverse(TreeNode(0)) == [0]


def test_insert_structure_and_duplicates():
    tree = BST()
    for value in [0, -5, 5, -2, 2, 0, -5, 2]:
        tree.insert(value)
        assert is_valid_bst(tree.root)
    assert tree.root == TreeNode(0, TreeNode(-5, None, TreeNode(-2)),
                                 TreeNode(5, TreeNode(2)))
    assert inorder(tree.root) == [-5, -2, 0, 2, 5]


def test_all_insertion_orders_of_five_keys():
    for values in permutations([-2, -1, 0, 1, 2]):
        tree = BST(iter(values))
        assert is_valid_bst(tree.root)
        assert inorder(tree.root) == [-2, -1, 0, 1, 2]
        assert reverse_inorder(tree.root) == [2, 1, 0, -1, -2]


@pytest.mark.parametrize("direction", ["left", "right"])
def test_deep_tree_all_traversals_and_insertion(direction):
    size = 2500
    values = list(range(size))
    if direction == "left":
        values.reverse()
    # Строим цепочку за O(n), затем проверяем вставку на полной глубине.
    tree = BST([values[0]])
    tail = tree.root
    for value in values[1:]:
        child = TreeNode(value)
        setattr(tail, direction, child)
        tail = child
    extra = -1 if direction == "left" else size
    tree.insert(extra)
    values.append(extra)
    assert preorder(tree.root) == values
    assert reverse_preorder(tree.root) == values
    assert postorder(tree.root) == values[::-1]
    assert reverse_postorder(tree.root) == values[::-1]
    assert inorder(tree.root) == sorted(values)
    assert reverse_inorder(tree.root) == sorted(values, reverse=True)
    assert is_valid_bst(tree.root)


def test_traversals_also_accept_non_bst():
    root = TreeNode(1, TreeNode(9), TreeNode(-3))
    assert preorder(root) == [1, 9, -3]
    assert inorder(root) == [9, 1, -3]
    assert postorder(root) == [9, -3, 1]
    assert reverse_preorder(root) == [1, -3, 9]
    assert reverse_inorder(root) == [-3, 1, 9]
    assert reverse_postorder(root) == [-3, 9, 1]
