from .solution import HashTable


class SameHash:
    """Разные ключи, которые намеренно попадают в одну корзину."""

    def __init__(self, value: str) -> None:
        self.value = value

    def __hash__(self) -> int:
        return 1

    def __eq__(self, other: object) -> bool:
        return isinstance(other, SameHash) and self.value == other.value


def test_set_get_and_update() -> None:
    table = HashTable()
    table.set("name", "Ada")
    table.set(7, "seven")
    table.set("name", "Grace")

    assert len(table) == 2
    assert table.get("name") == "Grace"
    assert table.get(7) == "seven"


def test_collision_chain_keeps_all_values() -> None:
    table = HashTable()
    first = SameHash("first")
    second = SameHash("second")
    third = SameHash("third")

    table.set(first, 10)
    table.set(second, 20)
    table.set(third, 30)

    assert table.get(first) == 10
    assert table.get(second) == 20
    assert table.get(third) == 30


def test_remove_from_middle_of_collision_chain() -> None:
    table = HashTable()
    first = SameHash("first")
    second = SameHash("second")
    third = SameHash("third")
    for key, value in [(first, 1), (second, 2), (third, 3)]:
        table.set(key, value)

    assert table.remove(second)
    assert not table.contains(second)
    assert table.get(second, "missing") == "missing"
    assert table.get(first) == 1
    assert table.get(third) == 3
    assert len(table) == 2
    assert not table.remove(second)


def test_resize_preserves_all_entries() -> None:
    table = HashTable()
    for number in range(100):
        table.set(number, number * number)

    assert len(table) == 100
    for number in range(100):
        assert table.get(number) == number * number


def test_none_value_is_distinguished_from_missing_key() -> None:
    table = HashTable()
    table.set("known", None)

    assert table.contains("known")
    assert table.get("known", "fallback") is None
    assert not table.contains("unknown")
    assert table.get("unknown", "fallback") == "fallback"
