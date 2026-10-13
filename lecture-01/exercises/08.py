a = int(input("Days: "))
b = int(input("Hours: "))
c = int(input("Minutes: "))
d = int(input("Seconds: "))
# 1 день = 86400 с, 1 година = 3600 с, 1 хвилина = 60 с
total = a * 86400 + b * 3600 + c * 60 + d

print("The amounts of seconds:", total, end=".\n")