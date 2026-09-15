import pytest

from .solution import max_even_sum


@pytest.mark.parametrize(
    ("numbers", "expected"),
    [
        ([5, 7, 13, 2, 14], 36),
        ([3], 0),
        ([2], 2),
        ([2, 4, 6], 12),
        ([1, 3, 5, 7], 16),
        ([1, 2, 3], 6),
        ([1, 4], 4),
        ([10, 1, 1], 12),
        ([7, 8, 9, 10, 11], 38),
    ],
)
def test_max_even_sum(numbers: list[int], expected: int) -> None:
    assert max_even_sum(numbers) == expected


def test_empty_iterable() -> None:
    assert max_even_sum([]) == 0


def test_generator_input() -> None:
    assert max_even_sum(x for x in [5, 2, 7]) == 14


def test_non_positive_number_is_invalid() -> None:
    with pytest.raises(TypeError):
        max_even_sum([2, 0, 4])


def test_non_integer_is_invalid() -> None:
    with pytest.raises(TypeError):
        max_even_sum([2, 4.0])
