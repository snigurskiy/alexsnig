from decimal import Decimal, getcontext

# задаємо точність обчислень
getcontext().prec = 28


def EMI(P, r, n):
    # перетворюємо початкову суму на Decimal
    P = Decimal(P)

    # переводимо річну ставку у відсотках на місячну частку
    r = Decimal(r) / 100 / 12

    # перетворюємо кількість платежів на Decimal
    n = Decimal(n)

    # обчислюємо щомісячний платіж
    payment = P * (r * (1 + r) ** n) / ((1 + r) ** n - 1)

    return payment


# обчислюємо платіж для прикладу з умови
result = EMI(500000, 8, 24)

# виводимо результат без округлення до сотих
print("EMI for 24 months:", result)