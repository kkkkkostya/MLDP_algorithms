import pytest

from .solution import ListNode, from_values, merge_with_dummy, merge_without_dummy, to_values


@pytest.mark.parametrize("merge", [merge_with_dummy, merge_without_dummy])
@pytest.mark.parametrize(
    ("first", "second", "expected"),
    [
        ([1, 2, 4], [1, 3, 4], [1, 1, 2, 3, 4, 4]),
        ([], [], []),
        ([], [1, 2], [1, 2]),
        ([1, 2], [], [1, 2]),
        ([1, 1, 5], [1, 1, 1, 6], [1, 1, 1, 1, 1, 5, 6]),
        ([-3, 0, 7], [-2, 0, 8], [-3, -2, 0, 0, 7, 8]),
    ],
)
def test_merge_sorted_lists(merge, first: list[int], second: list[int], expected: list[int]) -> None:
    assert to_values(merge(from_values(first), from_values(second))) == expected


@pytest.mark.parametrize("merge", [merge_with_dummy, merge_without_dummy])
def test_merge_reuses_original_nodes(merge) -> None:
    first = ListNode(1, ListNode(4))
    second = ListNode(2, ListNode(3))
    original_nodes = {id(first), id(first.next), id(second), id(second.next)}

    merged = merge(first, second)
    merged_nodes = set()
    while merged is not None:
        merged_nodes.add(id(merged))
        merged = merged.next

    assert merged_nodes == original_nodes
