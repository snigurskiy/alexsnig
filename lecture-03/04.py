def includes_any(lst, values):
    for x in values: # перебираємо значення, які потрібно знайти
        if x in lst: # перевіряємо наявність поточного значення у lst
            return True # знайшли хоча б один збіг — завершуємо функцію
    return False # усі значення перевірено, збігів немає

print(includes_any([1, 2, 3, 4], [2, 9])) # True
print(includes_any([1, 2, 3, 4], [8, 9])) # False