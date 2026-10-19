str = "amaama"
polyndrome = True
for i in range(len(str) // 2):
    if str[i] != str[len(str) - 1 - i]:
        polyndrome = False
        break
    while i < len(str) // 2:
        if str[i] != str[len(str) - 1 - i]:
            polyndrome = False
            break
        i += 1
else:
    polyndrome = False
if polyndrome:
    print("The entered string is a polyndrome")
else:
    print("The entered string is not a polyndrome")