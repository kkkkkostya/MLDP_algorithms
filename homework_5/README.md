# Домашнее задание №5

Решения оформлены по аналогии с предыдущими работами. Каждая папка содержит
`solution.py`, тесты и README с идеей алгоритма, обоснованием корректности,
оценкой сложности и пошаговой визуализацией.

| Задача | Папка | Реализация |
| --- | --- | --- |
| Tracer | [tracer/](tracer/README.md) | декоратор стека вызовов |
| Permutations | [permutations/](permutations/README.md) | поиск с возвратом и Tracer |
| AVL | [AVL/](AVL/README.md) | вставка, удаление, поиск, схема дерева |

Требуется Python 3.10+. Решения используют стандартную библиотеку, тесты — `pytest`.

## Запуск тестов

Из корня репозитория, если `pytest` уже установлен:

```bash
python -m pytest homework_5 -q
```

Linux/macOS, из `homework_5`:

```bash
bash setup.sh
bash run_tests.sh
```

Windows PowerShell, из корня репозитория:

```powershell
python -m venv homework_5/.venv
homework_5/.venv/Scripts/python.exe -m pip install -r homework_5/requirements.txt
homework_5/.venv/Scripts/python.exe -m pytest homework_5 -q
```
