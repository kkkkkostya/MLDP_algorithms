"""Решение задачи Two Sum."""


def two_sum(arr: list[int], k: int) -> tuple[int, int]:
    """Возвращает два возрастающих индекса элементов с суммой k"""
    seen = {}

    for index, value in enumerate(arr):
        needed = k - value
        if needed in seen:
            return seen[needed], index
        seen[value] = index

    raise ValueError("A pair with the sum of K does not exist")


if __name__ == "__main__":
    arr = list(map(int, input("arr: ").split()))
    k = int(input("k: "))
    first, second = two_sum(arr, k)
    print(first, second)
