def min_n(lst, n):
    return sorted(lst)[:n] # сортуємо список і повертаємо перші n елементів

print(min_n([1, 2, 3], 1)) # [1]
print(min_n([1, 2, 3], 2)) # [1, 2]