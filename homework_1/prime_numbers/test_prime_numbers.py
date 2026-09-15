import pytest

from .solution import count_primes_less_than


@pytest.mark.parametrize(
    ("n", "expected"),
    [
        (0, 0),
        (1, 0),
        (2, 0),
        (3, 1),
        (4, 2),
        (10, 4),
        (11, 4),
        (20, 8),
        (30, 10),
        (100, 25),
    ],
)
def test_count_primes_less_than(n: int, expected: int) -> None:
    assert count_primes_less_than(n) == expected


def test_only_prime_2_before_3() -> None:
    assert count_primes_less_than(4) == 2


def test_non_integer_is_invalid() -> None:
    with pytest.raises(TypeError):
        count_primes_less_than(10.0)
