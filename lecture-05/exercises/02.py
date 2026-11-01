# Читаємо вміст з вхідного файлу
with open('02_py_text.txt', 'r', encoding='utf-8') as file:
    text = file.read()

# Розбиваємо текст на список рядків за допомогою splitlines()
lines = text.splitlines()

# Вносимо зміни - нове речення після другого рядка (індекс 2)
new_sentence = "If Peter Piper picked a peck of pickled peppers."
lines.insert(2, new_sentence)

# Записуємо оновлений список рядків у новий файл
with open('new_02_py_text.txt', 'w', encoding='utf-8') as file:
    file.write('\n'.join(lines) + '\n')