"""Генерация уникальных перестановок целых чисел поиском с возвратом."""

from collections import Counter

from ..tracer.solution import tracer


def permutations(nums: list[int], *, trace: bool = True) -> list[list[int]]:
    """Возвращает перестановки, не меняя nums"""
    remaining = Counter(nums)
    result: list[list[int]] = []

    def backtrack(path: list[int]) -> None:
        if len(path) == len(nums):
            result.append(path.copy())
            return

        for value in remaining:
            if remaining[value] == 0:
                continue
            remaining[value] -= 1
            path.append(value)
            backtrack(path)
            path.pop()
            remaining[value] += 1

    if trace:
        backtrack = tracer(backtrack)
    backtrack([])
    return result


if __name__ == "__main__":
    print(permutations([1, 2, 3]))
