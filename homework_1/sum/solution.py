from collections.abc import Iterable


def max_even_sum(numbers: Iterable[int]) -> int:
    """Возвращает максимальную сумму элементов, кратную 2"""
    total = 0
    min_odd = None

    for number in numbers:
        if not isinstance(number, int) or number <= 0:
            raise TypeError("All numbers must be positive integers")

        total += number
        if number % 2 == 1 and (min_odd is None or number < min_odd):
            min_odd = number

    if total % 2 == 0:
        return total

    return total - min_odd


if __name__ == "__main__":
    raw = input().strip()
    numbers = list(map(int, raw.split())) if raw else []
    print(max_even_sum(numbers))
