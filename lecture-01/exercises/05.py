feet = int(input("Input distance in feet: ")) # вводимо фути, перетворюємо рядок на ціле число

inches = feet * 12
yards = feet * 0.333333333
miles = feet * 0.000189393939

print("The distance in inches is", inches, "inches.")
print("The distance in yards is", round(yards, 9), "yards.") # round(число, n) округлює число до n цифр після коми
print("The distance in miles is", round(miles, 3), "miles.")