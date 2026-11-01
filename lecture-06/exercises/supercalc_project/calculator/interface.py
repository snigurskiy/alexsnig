title = "Super Calc"

def menu():
    print(f"{title}".title().center(40, '='), '\n')
    print("_"*40)
    str1 = 'Select operation:'
    print('|' + str1 + ' ' * (38 - len(str1)) + '|')
    print('|' + "_"*38 + '|')
    print("| c : Calculate".ljust(39, ' ') + '|')
    print("| h : Help".ljust(39, ' ') + '|')
    print("| q : Quit".ljust(39, ' ') + '|')
    print("="*40)

    choice = input("| Enter choice (h|c|q): ".title()).lower()
    return choice if choice in ('h', 'c', 'q') else 'h'

def calc_help(e=''):
    if e:
        print(f"\n{e}")
    print("""        Usage operation:            h                        Display this usage message            2 + 2                    Add            3 - 1                    Subtract            2 * 2                    Multiply            4 / 2                    Divide            5 // 2                   Int Divide            7 % 3                    Modulo Divide            2 ** 3                   Exponentiation            q                        Quit        """)