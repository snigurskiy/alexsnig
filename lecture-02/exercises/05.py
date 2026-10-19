from decimal import Decimal, getcontext

# задаємо точність обчислень: 28 значущих цифр
getcontext().prec = 28

def complex_interest(P, r, n, t):
    # перетворюємо передані значення на Decimal
    P = Decimal(P)
    r = Decimal(r)
    n = Decimal(n)
    t = Decimal(t)

    # обчислюємо кінцеву суму зі складними відсотками
    A = P * (1 + r / n) ** (n * t)

    # повертаємо результат
    return A

# зчитуємо дані як рядки, без перетворення на float
principal = input("Введіть початкову суму: ")
rate = input("Введіть річну ставку часткою (0.15 означає 15%): ")
periods = input("Введіть кількість нарахувань за рік: ")
years = input("Введіть кількість років: ")

# передаємо чотири значення у функцію
result = complex_interest(principal, rate, periods, years)

# виводимо отриману суму та округлюємо до сотих
print(result.quantize(Decimal("0.01")))