import pytest

from .solution import factorial, tracer


def test_recursive_trace_exact_output(capsys):
    assert factorial(3) == 6
    assert capsys.readouterr().out == (
        "-> factorial(3)\n"
        "  -> factorial(2)\n"
        "    -> factorial(1)\n"
        "      -> factorial(0)\n"
        "      <- factorial = 1\n"
        "    <- factorial = 1\n"
        "  <- factorial = 2\n"
        "<- factorial = 6\n"
    )


def test_base_case_and_independent_calls(capsys):
    assert factorial(0) == 1
    assert factorial(1) == 1
    lines = capsys.readouterr().out.splitlines()
    assert lines[0] == "-> factorial(0)"
    assert lines[2] == "-> factorial(1)"


def test_arguments_result_identity_and_metadata(capsys):
    @tracer
    def collect(first, *rest, flag=False, **extra):
        """Сохраняемый docstring."""
        return first

    value = [1, 2]
    assert collect(value, "x", flag=True, key=3) is value
    assert collect.__name__ == "collect"
    assert collect.__doc__ == "Сохраняемый docstring."
    assert collect.__wrapped__(value) is value
    assert capsys.readouterr().out == (
        "-> collect([1, 2], 'x', flag=True, key=3)\n"
        "<- collect = [1, 2]\n"
    )


def test_no_arguments_and_none_result(capsys):
    @tracer
    def nothing():
        pass

    assert nothing() is None
    assert capsys.readouterr().out == "-> nothing()\n<- nothing = None\n"


def test_exception_identity_and_depth_reset(capsys):
    error = ValueError("stop")

    @tracer
    def fail(n):
        if n:
            return fail(n - 1)
        raise error

    with pytest.raises(ValueError) as caught:
        fail(2)
    assert caught.value is error
    assert capsys.readouterr().out == (
        "-> fail(2)\n  -> fail(1)\n    -> fail(0)\n"
        "    !! fail raises ValueError('stop')\n"
        "  !! fail raises ValueError('stop')\n"
        "!! fail raises ValueError('stop')\n"
    )
    assert factorial(0) == 1
    assert capsys.readouterr().out.startswith("-> factorial(0)\n")


def test_shared_depth_and_caught_exception(capsys):
    @tracer
    def inner():
        raise RuntimeError("inner")

    @tracer
    def outer():
        try:
            inner()
        except RuntimeError:
            return factorial(0)

    assert outer() == 1
    assert capsys.readouterr().out == (
        "-> outer()\n"
        "  -> inner()\n"
        "  !! inner raises RuntimeError('inner')\n"
        "  -> factorial(0)\n"
        "  <- factorial = 1\n"
        "<- outer = 1\n"
    )


def test_mutual_recursion(capsys):
    @tracer
    def even(n):
        return True if n == 0 else odd(n - 1)

    @tracer
    def odd(n):
        return False if n == 0 else even(n - 1)

    assert even(3) is False
    assert capsys.readouterr().out == (
        "-> even(3)\n  -> odd(2)\n    -> even(1)\n      -> odd(0)\n"
        "      <- odd = False\n    <- even = False\n"
        "  <- odd = False\n<- even = False\n"
    )


def test_negative_factorial():
    with pytest.raises(ValueError, match="non-negative"):
        factorial(-1)
