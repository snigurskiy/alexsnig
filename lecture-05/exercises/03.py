from pathlib import Path

# Вказуємо шлях до файлу.
file_path = Path('new_02_py_text.txt')

# Перевіряємо, чи існує файл.
if file_path.is_file():
    # Читаємо весь текст із файлу один раз.
    content = file_path.read_text(encoding='utf-8')

    # Ділимо текст на рядки та рахуємо їх.
    num_lines = len(content.splitlines())

    # Ділимо текст за пробільними символами та рахуємо слова.
    num_words = len(content.split())

    # Рахуємо всі символи, включно з пробілами й переносами.
    num_chars = len(content)

    # Виводимо результати.
    print(f"Файл: {file_path}")
    print(f"Кількість рядків: {num_lines}")
    print(f"Кількість слів: {num_words}")
    print(f"Кількість символів: {num_chars}")
else:
    print(f"Помилка: файл '{file_path}' не знайдено.")