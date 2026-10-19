str1 = "khokho"
symmetrical = True # припускаємо, що рядок симетричний

if len(str1) % 2 == 0:
    mid = len(str1) // 2 # знаходимо середину рядка
    i = 0 # починаємо з першого символу

    while i < mid:
        if str1[i] != str1[mid + i]: # порівнюємо символи двох половин
            symmetrical = False # якщо символи різні, симетрії немає
            break # завершуємо цикл
        i = i + 1 # переходимо до наступного символу
else:
    symmetrical = False # довжина непарна, половини не можуть бути однаковими

if symmetrical:
    print("The entered string is symmetrical")
else:
    print("The entered string is not symmetrical")