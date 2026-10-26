# Домашнее задание №4

## Запуск

Linux/macOS, из `homework_4`:

```bash
bash setup.sh
bash run_tests.sh
```

Windows PowerShell, из корня репозитория:

```powershell
python -m venv homework_4/.venv
homework_4/.venv/Scripts/python.exe -m pip install -r homework_4/requirements.txt
homework_4/.venv/Scripts/python.exe -m pytest homework_4/Binary_Tree -q
```

Если `pytest` уже установлен: `python -m pytest homework_4/Binary_Tree -q`.
