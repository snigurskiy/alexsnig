price = float(input()) # Зчитуємо ціну товару
discount = float(input()) # Зчитуємо частку знижки: наприклад, 0.3 означає 30%
final_price = price - price * discount # Від початкової ціни віднімаємо суму знижки
print(final_price) # Виводимо кінцеву ціну