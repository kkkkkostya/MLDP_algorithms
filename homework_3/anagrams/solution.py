"""Решение задачи группировки анаграмм."""


def group_anagrams(words: list[str]) -> list[list[str]]:
    """Возвращает детерминированно отсортированные группы анаграмм"""
    groups_by_key: dict[str, list[str]] = {}

    for word in words:
        key = "".join(sorted(word))
        if key not in groups_by_key:
            groups_by_key[key] = []
        groups_by_key[key].append(word)

    groups = list(groups_by_key.values())
    for group in groups:
        group.sort()
    groups.sort(key=lambda group: group[0])
    return groups
