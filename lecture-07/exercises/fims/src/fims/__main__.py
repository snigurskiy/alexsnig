from . import helpers, monit
from . import TITLE, monitor, DATABASE
import hashlib
import shelve
import time

def main():
    helpers.hello(TITLE)

    # Відкриваємо базу та зчитуємо збережені хеші у словник.
    with shelve.open(DATABASE) as database:
        files = dict(database)

    while True:
        # Отримуємо список файлів, які потрібно перевірити.
        for file_path in monit.getFiles(monitor):
            try:
                # Створюємо новий об'єкт SHA-256 для кожного файлу.
                file_hash = hashlib.sha256()

                # Відкриваємо файл у двійковому режимі.
                with open(file_path, 'rb') as file:
                    while True:
                        chunk = file.read(2048) # читаємо частину файлу

                        if not chunk: # порожнє значення означає кінець файлу
                            break

                        file_hash.update(chunk) # додаємо частину до обчислення

                # Отримуємо хеш лише після читання ВСЬОГО файлу.
                sha256 = file_hash.hexdigest()

                # Порівнюємо його з попереднім хешем у пам’яті.
                if file_path in files and sha256 != files[file_path]:
                    print(
                        f'{file_path} has been changed! '
                        f'{time.strftime("%Y-%m-%d %H:%M:%S")}'
                    )

                # Зберігаємо останній хеш у пам’яті.
                files[file_path] = sha256

                # Також записуємо хеш у базу shelve.
                with shelve.open(DATABASE) as database:
                    database[file_path] = sha256

            except OSError as error:
                # Наприклад, файл могли видалити під час перевірки.
                print(f"Cannot read '{file_path}': {error}")

        # Чекаємо одну секунду перед наступною перевіркою всіх файлів.
        time.sleep(1)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        # Виконується, коли користувач натискає Ctrl + C.
        helpers.bye(TITLE)