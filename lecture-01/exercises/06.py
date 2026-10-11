a = int(input())
b = int(input())
a = a + b # a отримало суму двох чисел
b = a - b # b отримало старе значення a
a = a - b # a тепер із старим значенням b
print(a)
print(b)