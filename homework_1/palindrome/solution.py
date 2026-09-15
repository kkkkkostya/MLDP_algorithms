def is_palindrome(number: int) -> bool:
    """Возвращает True, если число является палиндомом."""

    if not isinstance(number, int):
        raise TypeError("Number must be an integer")
    if number <= 0:
        raise ValueError("Number must be a positive integer")

    if number < 10:
        return True

    if number % 10 == 0:
        return False

    reversed_half = 0
    while number > reversed_half:
        reversed_half = reversed_half * 10 + number % 10
        number //= 10

    return number == reversed_half or number == reversed_half // 10


if __name__ == "__main__":
    value = int(input().strip())
    print(is_palindrome(value))