from .solution import group_anagrams


def test_groups_anagrams_from_task() -> None:
    words = ["eat", "tea", "tan", "ate", "nat", "bat"]
    assert group_anagrams(words) == [["ate", "eat", "tea"], ["bat"], ["nat", "tan"]]


def test_groups_repeated_and_empty_words() -> None:
    assert group_anagrams(["", "", "a", "a", "ab", "ba"]) == [
        ["", ""],
        ["a", "a"],
        ["ab", "ba"],
    ]


def test_groups_are_case_sensitive() -> None:
    assert group_anagrams(["Cat", "tac", "act", "cat"]) == [
        ["Cat"],
        ["act", "cat", "tac"],
    ]


def test_empty_input() -> None:
    assert group_anagrams([]) == []


def test_does_not_change_input() -> None:
    words = ["tea", "eat", "bat"]
    group_anagrams(words)
    assert words == ["tea", "eat", "bat"]
