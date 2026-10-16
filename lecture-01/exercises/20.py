# Описуємо функцію перетворення секунд
def show_time(total_seconds):
    # Виділяємо повні дні.
    days = total_seconds // 86400
    remaining_seconds = total_seconds % 86400

    # Із залишку виділяємо повні години
    hours = remaining_seconds // 3600
    remaining_seconds = remaining_seconds % 3600

    # Виділяємо повні хвилини та решту секунд
    minutes = remaining_seconds // 60
    seconds = remaining_seconds % 60

    # Виводимо результат для одного числа
    print(days, "day(s),", hours, "hour(s),",
          minutes, "minute(s),", seconds, "second(s).")


# Зчитуємо всі три значення
a = int(input())
b = int(input())
c = int(input())

# Виконуємо перетворення для кожного значення
show_time(a)
show_time(b)
show_time(c)