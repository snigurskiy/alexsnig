import os # модуль для роботи з файлами та папками

def getFiles(monitor):
    filesList = [] # створюємо порожній список знайдених файлів

    for x in monitor: # перебираємо налаштування для кожного шляху
        path = x['path'] # отримуємо шлях
        recursive = x['recursive'] # отримуємо значення True або False

        if os.path.isdir(path): # перевіряємо, чи шлях є папкою
            if recursive:
                # os.walk() перебирає папку та всі її підпапки
                for root, dirs, files in os.walk(path):
                    for name in files:
                        full_path = os.path.join(root, name)
                        filesList.append(full_path)
            else:
                # os.listdir() повертає назви елементів без шляху
                for name in os.listdir(path):
                    full_path = os.path.join(path, name)

                    # Додаємо тільки файли, не папки
                    if os.path.isfile(full_path):
                        filesList.append(full_path)

        elif os.path.isfile(path): # якщо шлях веде до окремого файлу
            filesList.append(path)

    return filesList # повертаємо список знайдених файлів