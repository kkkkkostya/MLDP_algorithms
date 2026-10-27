"""Трассировка синхронных функций с сохранением их результата и метаданных."""

from collections.abc import Callable
from contextvars import ContextVar
from functools import wraps
from typing import ParamSpec, TypeVar


P = ParamSpec("P")
R = TypeVar("R")
_depth: ContextVar[int] = ContextVar("trace_depth", default=0)


def tracer(function: Callable[P, R]) -> Callable[P, R]:
    """Печатает вход, выход и исключение; один уровень равен двум пробелам."""
    @wraps(function)
    def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
        indent = "  " * _depth.get()
        arguments = [repr(arg) for arg in args]
        arguments.extend(f"{key}={value!r}" for key, value in kwargs.items())
        print(f"{indent}-> {function.__name__}({', '.join(arguments)})")
        token = _depth.set(_depth.get() + 1)
        try:
            result = function(*args, **kwargs)
        except BaseException as error:
            print(f"{indent}!! {function.__name__} raises {error!r}")
            raise
        else:
            print(f"{indent}<- {function.__name__} = {result!r}")
            return result
        finally:
            _depth.reset(token)

    return wrapper


@tracer
def factorial(n: int) -> int:
    """Пример рекурсивной функции; аргумент — неотрицательное целое."""
    if n < 0:
        raise ValueError("n must be non-negative")
    return 1 if n == 0 else n * factorial(n - 1)


if __name__ == "__main__":
    factorial(3)
