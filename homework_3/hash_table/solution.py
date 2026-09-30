"""Хеш-таблица с цепочками коллизий и автоматическим расширением"""


class HashTable:
    """Отображение hashable-ключей в значения.

    Коллизии разрешаются методом цепочек: записи с одним индексом хранятся в
    одной корзине-списке. Когда коэффициент заполнения превысит 0.75, число
    корзин удваивается, а все записи раскладываются заново.
    """

    _INITIAL_CAPACITY = 8
    _MAX_LOAD_FACTOR = 0.75

    def __init__(self) -> None:
        self._buckets: list[list[list[object]]] = [[] for _ in range(self._INITIAL_CAPACITY)]
        self._size = 0

    def _index(self, key: object) -> int:
        return hash(key) % len(self._buckets)

    def _find_entry(self, key: object) -> list[object] | None:
        for entry in self._buckets[self._index(key)]:
            if entry[0] == key:
                return entry
        return None

    def _insert_entry(self, key: object, value: object) -> None:
        """Добавляет новую запись, предполагая, что ключа ещё нет."""
        self._buckets[self._index(key)].append([key, value])
        self._size += 1

    def _resize(self) -> None:
        old_buckets = self._buckets
        self._buckets = [[] for _ in range(len(old_buckets) * 2)]
        self._size = 0

        for bucket in old_buckets:
            for entry in bucket:
                self._insert_entry(entry[0], entry[1])

    def set(self, key: object, value: object) -> None:
        """Вставляет пару или заменяет значение уже существующего ключа."""
        entry = self._find_entry(key)
        if entry is not None:
            entry[1] = value
            return

        if (self._size + 1) / len(self._buckets) > self._MAX_LOAD_FACTOR:
            self._resize()
        self._insert_entry(key, value)

    def get(self, key: object, default: object = None) -> object:
        """Возвращает значение ключа или ``default``, когда ключ не найден."""
        entry = self._find_entry(key)
        return default if entry is None else entry[1]

    def remove(self, key: object) -> bool:
        """Удаляет ключ; возвращает ``True`` только если он существовал."""
        bucket = self._buckets[self._index(key)]
        for index, entry in enumerate(bucket):
            if entry[0] == key:
                bucket.pop(index)
                self._size -= 1
                return True
        return False

    def contains(self, key: object) -> bool:
        """Проверяет наличие ключа, в том числе если его значение равно None."""
        return self._find_entry(key) is not None

    def __len__(self) -> int:
        return self._size
