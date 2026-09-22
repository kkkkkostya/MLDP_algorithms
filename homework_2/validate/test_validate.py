import pytest

from .solution import validate_stack_sequences


@pytest.mark.parametrize(
    ("pushed", "popped", "expected"),
    [
        ([1, 2, 3, 4, 5], [1, 3, 5, 4, 2], True),
        ([1, 2, 3], [3, 1, 2], False),
        ([1], [1], True),
        ([1, 2, 3], [3, 2, 1], True),
        ([1, 2, 3, 4], [2, 4, 3, 1], True),
        ([1, 2, 3, 4], [3, 4, 1, 2], False),
        ([1, 2], [2], False),
        ([1, 2], [2, 3], False),
        ([], [], True),
    ],
)
def test_validate_stack_sequences(
    pushed: list[int], popped: list[int], expected: bool
) -> None:
    assert validate_stack_sequences(pushed, popped) is expected


def test_large_valid_sequence() -> None:
    pushed = list(range(100_000))
    assert validate_stack_sequences(pushed, list(reversed(pushed)))
