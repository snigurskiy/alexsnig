from decimal import Decimal, getcontext

# задаємо точність обчислень: 28 значущих цифр
getcontext().prec = 28

def emi(P, r, n):
    # перетворюємо передані значення на Decimal
    P = Decimal(P)
    r = Decimal(r)
    n = Decimal(n)

    # обчислюємо щомісячний платіж за формулою EMI
    EMI = P * ((r * (1 + r) ** n) / ((1 + r) ** n - 1))
    return EMI

# зчитуємо дані як рядки, без перетворення на float
principal = input("Princiapal amount borrowed: ")
rate = input("Periodic monthly interest rate: ")
numbers = input("Total number of monthly payments: ")

# передаємо три значення у функцію
result = emi(principal, rate, numbers)

# виводимо отриману суму та округлюємо до сотих
print(
    "EMI for", numbers, "months:",
    result.quantize(Decimal("0.01"))
)