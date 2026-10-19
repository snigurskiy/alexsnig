str1 = "amaama"
palindrome = True # припускаємо, що рядок є паліндромом
i = 0 # починаємо з першого символу

while i < len(str1) // 2:
    if str1[i] != str1[len(str1) - 1 - i]:
        palindrome = False # знайшли різні символи
        break # завершуємо перевірку
    i += 1 # переходимо до наступної пари

if palindrome:
    print("The entered string is a palindrome")
else:
    print("The entered string is not a palindrome")