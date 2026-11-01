import sys
import os

def main():
    # Отримуємо ім'я поточного файлу скрипта для рядка usage
    script_name = os.path.basename(sys.argv[0])
    
    # Текст підказки, який повністю відповідає вашому запиту
    help_message = f"""usage: {script_name} number [-h]

positional arguments:
  number         display a square of a given number

options:
  -h | --help  show this help message and exit"""

    # Перевіряємо, чи передано аргумент і чи є він запитом допомоги
    if len(sys.argv) < 2 or sys.argv[1] in ('-h', '--help'):
        print(help_message)
        sys.exit(0)

    # Намагаємося обчислити квадрат числа
    try:
        # Визначаємо, чи це ціле число, чи число з плаваючою комою
        arg = sys.argv[1]
        number = float(arg) if '.' in arg else int(arg)
        
        # Виводимо результат (квадрат числа)
        print(number ** 2)
        
    except ValueError:
        print(f"Error: argument 'number': invalid float/int value: '{sys.argv[1]}'")
        print(f"Try '{script_name} --help' for more information.")
        sys.exit(1)

if __name__ == '__main__':
    main()