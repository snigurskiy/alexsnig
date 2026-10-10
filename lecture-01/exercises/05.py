feet = int(input("Input distance in feet: "))

inches = feet * 12
yards = feet * 0.333333333
miles = feet * 0.000189393939

print("The distance in inches is", inches, "inches.")
print("The distance in yards is", round(yards, 9), "yards.")
print("The distance in miles is", round(miles, 3), "miles.")