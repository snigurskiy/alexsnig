def search_str(file_path, word):
    # Відкриваємо файл для читання.
    with open(file_path, 'r') as file:
        # Зчитуємо всі рядки файлу у список.
        lines = file.readlines()

        # Перебираємо рядки та нумеруємо їх, починаючи з 1.
        for number, line in enumerate(lines, start=1):
            # Перевіряємо, чи є шуканий текст у поточному рядку.
            if word in line:
                # Виводимо номер і текст рядка.
                print(number, line, end='')

# Шукаємо текст "laptop" у файлі sales.txt.
search_str('sales.txt', 'laptop')