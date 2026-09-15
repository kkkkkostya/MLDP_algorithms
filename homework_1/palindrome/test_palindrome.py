import pytest

from .solution import is_palindrome


@pytest.mark.parametrize(
    ("number", "expected"),
    [
        (1, True),
        (7, True),
        (11, True),
        (121, True),
        (1221, True),
        (12321, True),
        (567765, True),
        (1001, True),
        (10, False),
        (31, False),
        (123, False),
        (1223, False),
        (123456789, False),
        (567465, False),
        (100, False),
    ],
)
def test_is_palindrome(number: int, expected: bool) -> None:
    assert is_palindrome(number) is expected


def test_zero_is_invalid() -> None:
    with pytest.raises(ValueError):
        is_palindrome(0)


def test_negative_number_is_invalid() -> None:
    with pytest.raises(ValueError):
        is_palindrome(-121)


def test_non_integer_is_invalid() -> None:
    with pytest.raises(TypeError):
        is_palindrome(121.0)
