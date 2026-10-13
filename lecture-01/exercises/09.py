f = float(input("Enter the desired future value: ")) # бажана майбутня сума
r = float(input("Enter the annual interest rate: ")) # річна відсоткова ставка
n = int(input("Enter the number of years the money will grow: ")) # кількість років
p = f / (1 + r) ** n # сума, яку потрібно внести сьогодні
print("You will need to deposit this amount:", round(p, 2), end=".\n") # виводимо суму з крапкою в кінці