from itertools import permutations as reference
from math import factorial

import pytest

from .solution import permutations


@pytest.mark.parametrize("nums, expected", [
    ([1, 2, 3], [[1, 2, 3], [1, 3, 2], [2, 1, 3],
                 [2, 3, 1], [3, 1, 2], [3, 2, 1]]),
    ([0, 1], [[0, 1], [1, 0]]),
    ([1], [[1]]),
    ([], [[]]),
    ([1, 1, 2], [[1, 1, 2], [1, 2, 1], [2, 1, 1]]),
    ([5, 5, 5], [[5, 5, 5]]),
    ([2, -1, 0], [[2, -1, 0], [2, 0, -1], [-1, 2, 0],
                  [-1, 0, 2], [0, 2, -1], [0, -1, 2]]),
])
def test_examples_and_boundaries(nums, expected):
    before = nums.copy()
    assert permutations(nums, trace=False) == expected
    assert nums == before


def test_trace_enabled_by_default(capsys):
    assert permutations([0, 1]) == [[0, 1], [1, 0]]
    assert capsys.readouterr().out == (
        "-> backtrack([])\n"
        "  -> backtrack([0])\n"
        "    -> backtrack([0, 1])\n"
        "    <- backtrack = None\n"
        "  <- backtrack = None\n"
        "  -> backtrack([1])\n"
        "    -> backtrack([1, 0])\n"
        "    <- backtrack = None\n"
        "  <- backtrack = None\n"
        "<- backtrack = None\n"
    )


def test_trace_switch_does_not_change_result(capsys):
    expected = permutations([1, 1, 2], trace=False)
    assert capsys.readouterr().out == ""
    assert permutations([1, 1, 2]) == expected
    assert capsys.readouterr().out.startswith("-> backtrack([])\n")


def test_results_are_independent_copies():
    nums = [1, 2, 3]
    result = permutations(nums, trace=False)
    result[0][0] = 100
    assert nums == [1, 2, 3]
    assert all(100 not in row for row in result[1:])
    assert permutations([], trace=False) == [[]]


@pytest.mark.parametrize("size", range(8))
def test_against_standard_library(size):
    nums = list(range(size))
    result = permutations(nums, trace=False)
    assert len(result) == factorial(size)
    assert {tuple(row) for row in result} == set(reference(nums))


@pytest.mark.parametrize("nums", [[2, 1, 2, 1], [0, 0, -1], [7] * 6])
def test_repeated_values_against_standard_library(nums):
    result = permutations(nums, trace=False)
    actual = [tuple(row) for row in result]
    assert len(actual) == len(set(actual))
    assert set(actual) == set(reference(nums))
