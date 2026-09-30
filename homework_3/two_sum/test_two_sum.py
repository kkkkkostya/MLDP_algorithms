import pytest

from .solution import two_sum


@pytest.mark.parametrize(
    ("arr", "k", "expected"),
    [
        ([1, 3, 4, 10], 7, (1, 2)),
        ([5, 5, 1, 4], 10, (0, 1)),
        ([-3, 4, 3, 90], 0, (0, 2)),
        ([0, 4, 9, 12], 4, (0, 1)),
        ([8, -2], 6, (0, 1)),
        ([100, 1, 50, 49], 99, (2, 3)),
    ],
)
def test_two_sum(arr: list[int], k: int, expected: tuple[int, int]) -> None:
    assert two_sum(arr, k) == expected


def test_two_sum_raises_when_pair_does_not_exist() -> None:
    with pytest.raises(ValueError):
        two_sum([1, 2, 3], 100)
