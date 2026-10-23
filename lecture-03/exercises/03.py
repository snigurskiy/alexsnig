def max_n(lst, n):
    return sorted(lst, reverse=True)[:n]

print(max_n([1, 2, 3], 1))
print(max_n([1, 2, 3], 2))