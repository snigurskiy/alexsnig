str1 = "JhonDipPeta"
str2 = "JaSonAy"
mid1 = len(str1) // 2 # Знаходимо індекс середнього символу
mid2 = len(str2) // 2
fin1 = str1[mid1 - 1:mid1 + 2] # Створюємо рядки з трьох середніх символів
fin2 = str2[mid2 - 1:mid2 + 2]
print(fin1)
print(fin2)