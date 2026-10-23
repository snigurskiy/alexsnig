def every_nth(lst, n):
    return lst[n-1::n]

i = [1, 2, 3, 4, 5, 6]
n = 2
print(every_nth(i, n))
