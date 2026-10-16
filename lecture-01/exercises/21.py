# Описуємо функцію для годин і хвилин
def show_clock(hours, minutes):
    # Виділяємо повні години
    hours = total_minutes // 24
    # Із залишку виділяємо повні хвилини
    minutes = total_minutes % 60
    # Виводимо результат для одного числа
    print(hours, minutes)

# Зчитуємо всі три значення
a = 150
b = 25
c = 440

# Виконуємо перетворення для кожного значення
show_clock(a)
show_clock(b)
show_clock(c)