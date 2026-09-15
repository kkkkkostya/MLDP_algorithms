from math import isqrt


def count_primes_less_than(n: int) -> int:
    """Возвращает количество простых чисел p, для которых p < N."""
    if not isinstance(n, int):
        raise TypeError("N must be an integer")
    if n <= 2:
        return 0

    is_prime = [True] * n
    is_prime[0] = False
    is_prime[1] = False

    for p in range(2, int(n ** 0.5) + 1):
        if is_prime[p]:
            for multiple in range(p * p, n, p):
                is_prime[multiple] = False

    return sum(is_prime)


if __name__ == "__main__":
    value = int(input().strip())
    print(count_primes_less_than(value))
