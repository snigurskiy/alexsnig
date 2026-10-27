"""Розбір навчального телефонного довідника українською.

Це пояснений оригінал, а не виправлена версія застосунку.
Позначки «ПРОБЛЕМА» пояснюють помилки; початкова логіка збережена.
Для match/case потрібен Python 3.10 або новіший.

Основні проблеми:
1. Старі функції створюють/очікують кортеж із 4 елементів, нові — словник.
2. Пошук використовує c[0], c[1], але реальні контакти мають текстові ключі.
3. Редагування розпаковує словник із 6 ключів у 4 змінні.
4. Порожнє введення адреси через split дає [''], а не порожній список.
5. save_contact зберігає дані лише в пам’яті, попри текст документації.
6. Друге визначення view_contacts замінює перше під тим самим ім’ям.

У файлі є словники dict, zip і списковий вираз. Це окремі конструкції:
їх не слід вважати вже опанованими лише тому, що вони є у прикладі.
"""

from datetime import datetime  # Імпортуємо клас datetime з однойменного модуля.
# Після такого імпорту викликаємо datetime.now(), не datetime.datetime.now().

# Закоментовані рядки не виконуються. Це старий приклад структури даних:
# contacts — список; кожен контакт — кортеж із 4 елементів:
# (ім’я, телефон, дата додавання, список частин адреси).
# contacts = [
#     ("Alice", "123-456-7890", datetime.now().strftime("%Y-%m-%d %H:%M:%S"), ["Some City", "Some State", "Some Country"]),
#     ("Bob", "987-654-3210", datetime.now().strftime("%Y-%m-%d %H:%M:%S"), ["Another City", "Another State", "Another Country"]),
#     ("Charlie", "555-555-5555", datetime.now().strftime("%Y-%m-%d %H:%M:%S"), ["Yet Another City", "Yet Another State", "Yet Another Country"])
# ]
# Оскільки цей блок закоментований, він НЕ створює змінну contacts.
# Реальний порожній список contacts створюється нижче, до викликів функцій.

def add_contact_old():  # Визначаємо стару функцію додавання, ще не запускаємо.
    name = input("Enter name: ").strip()  # Зчитуємо ім’я без крайніх пробілів.
    phone = input("Enter phone number: ").strip()  # Телефон лишаємо рядком.
    # Це зберігає +, дефіси та початкові нулі в телефонному номері.
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    # now() отримує поточну локальну дату/час комп’ютера.
    # strftime() перетворює їх на текст за шаблоном:
    # %Y — рік, %m — місяць, %d — день, %H — години, %M — хвилини, %S — секунди.
    address = input("Enter address (City, State, Country): ").strip().split(", ")
    # Методи виконуються зліва направо: input → strip → split.
    # split(", ") розділяє за ТОЧНИМ роздільником «кома та пробіл».
    # "Kyiv, Kyiv, Ukraine" → ['Kyiv', 'Kyiv', 'Ukraine'].
    # "Kyiv,Kyiv,Ukraine" не буде розділено цим роздільником.
    contacts.append((name, phone, timestamp, address))  # Додаємо один кортеж.
    # ПРОБЛЕМА: нові функції нижче очікують словники, а не такі кортежі.
    print(f"✅ Contact '{name}' added successfully.")  # Підставляємо ім’я.

def view_contacts():  # Перша, стара версія перегляду.
    if not contacts:  # Порожній список має хибне логічне значення.
        print("📭 No contacts found.")  # Повідомляємо, що список порожній.
        return  # Виходимо з функції; без значення return повертає None.
    print("\n📇 Contacts List:")  # \n додає перенесення перед заголовком.
    for idx, (name, phone, timestamp, address) in enumerate(contacts, start=1):
        # enumerate дає пару: номер від 1 і поточний контакт.
        # idx отримує номер, а контакт розпаковуємо в 4 змінні.
        # ПРОБЛЕМА: це підходить кортежам вище, а не словникам нижче.
        print(f"{idx}. Name: {name}, Phone: {phone}, Added: {timestamp}, Address: {', '.join(address)}")
        # ', '.join(address) об’єднує частини адреси через кому та пробіл.
        # f перед лапками дозволяє обчислювати вирази всередині {}.

def search_contact(query):  # query — пошуковий текст, переданий із меню.
    results = [c for c in contacts if query.lower() in c[0].lower() or query in c[1]]
    # Це списковий вираз: створюємо новий список із контактів, які підходять.
    # c по черзі отримує кожен контакт; if вирішує, чи додати його в results.
    # lower() переводить текст у нижній регістр для пошуку без урахування регістру.
    # Для рядків in перевіряє наявність підрядка, наприклад 'ali' in 'alice'.
    # or означає: збіг у імені АБО в номері телефону.
    # ПРОБЛЕМА: у словнику немає ключів 0 і 1, тому c[0] дасть KeyError: 0.
    # Для нової структури потрібні c['name'] та c['phone'].
    # Саме створення results зупиниться з помилкою, до наступного if.
    # Порожній query збігається з будь-яким рядком: це ще одна особливість пошуку.
    if not results:  # Якщо список результатів порожній.
        print(f"🔍 No contacts found for '{query}'.")
        return  # Немає сенсу виконувати подальше виведення.
    print(f"\n🔍 Search Results for '{query}':")
    for idx, (name, phone, timestamp, address) in enumerate(results, start=1):
        # ПРОБЛЕМА: виведення теж очікує старі кортежі з 4 елементів.
        # У новому форматі результати зручно передавати до data_table().
        print(f"{idx}. Name: {name}, Phone: {phone}, Added: {timestamp}, Address: {', '.join(address)}")

def edit_contact():  # Функція редагування за номером у списку.
    view_contacts()  # На момент виклику використовується ОСТАННЯ версія цієї функції.
    id_str = input("Enter ID to edit: ").strip()  # Зчитуємо номер як текст.
    try:  # Пробуємо виконати код, який може спричинити ValueError.
        idx = int(id_str) - 1  # Людський номер 1 перетворюємо на індекс 0.
        if idx < 0 or idx >= len(contacts):  # Відсікаємо недопустимі індекси.
            print("❌ Invalid ID.")
            return  # Не намагаємося звертатися до відсутнього елемента.
        name, phone, timestamp, address = contacts[idx]
        # ПРОБЛЕМА: поточний контакт — словник із 6 ключів.
        # Під час розпакування словника перебираються КЛЮЧІ, а не значення.
        # 6 ключів не поміщаються в 4 змінні: виникне ValueError.
        # except нижче його перехопить, але повідомлення про «номер» буде неточним.
        new_name = input(f"Enter new name (or press Enter to keep '{name}'): ").strip() or name
        # Вираз X or name повертає X, якщо X непорожній; інакше — старе ім’я.
        # Тут or повертає одне зі значень, не обов’язково True/False.
        new_phone = input(f"Enter new phone (or press Enter to keep '{phone}'): ").strip() or phone
        # Порожнє введення після strip дає '', тому зберігається старий телефон.
        new_address = input(f"Enter new address (or press Enter to keep '{', '.join(address)}'): ").strip().split(", ") or address
        # ПРОБЛЕМА навіть для старого формату: ''.split(', ') повертає [''].
        # Це НЕ порожній список, тому or address не обере стару адресу.
        # Для виправлення слід спочатку перевірити введений текст,
        # і лише якщо він непорожній — розділяти його на частини.
        contacts[idx] = (new_name, new_phone, timestamp, new_address)
        # Замінюємо контакт за індексом; первинна дата додавання лишається.
        # ПРОБЛЕМА: тут знову записується кортеж замість нового словника.
        print(f"✅ Contact ID {id_str} updated successfully.")
    except ValueError:  # Перехоплює ValueError з будь-якого рядка всередині try.
        print("❌ Invalid input. Please enter a valid number.")
        # Це не означає, що помилка неодмінно виникла саме в int(id_str).

# Попередня, закоментована версія видалення працювала з кортежами:
# def delete_contact(id_str):
#     try:
#         idx = int(id_str) - 1
#         if idx < 0 or idx >= len(contacts):
#             print("❌ Invalid ID.")
#             return
#         deleted_contact = contacts.pop(idx)
#         print(f"🗑️ Contact '{deleted_contact[0]}' deleted successfully.")
#     except ValueError:
#         print("❌ Invalid input. Please enter a valid number.")
# pop(idx) і видаляє елемент, і повертає його. [0] отримувало ім’я з кортежу.

def delete_contact(contact_id):  # Нова версія працює зі словниками.
    """Видаляє контакт за номером у поточному списку."""
    if not contacts:  # Передусім перевіряємо, чи є що видаляти.
        print(f"{chr(10060)} No contacts to delete.")  # chr(10060) — символ ❌.
        return  # Завершуємо функцію без видалення.
    try:
        contact_id = int(contact_id)  # Перетворюємо отриманий текст на число.
        if contact_id < 1 or contact_id > len(contacts):  # Номери від 1 до довжини.
            print(f"{chr(10060)} Invalid contact ID.")
            return
    except ValueError:  # Якщо текст не є записом цілого числа.
        print(f"{chr(10060)} Please enter a valid number.")
        return  # Без return функція пішла б далі з неправильним значенням.
    deleted_contact = contacts.pop(contact_id - 1)  # Видаляємо й отримуємо словник.
    print(f"🗑 Contact '{deleted_contact['name']}' deleted successfully!")
    # ['name'] отримує значення за ключем name, а не за числовим індексом.
    # Номери тут не постійні ID: після видалення наступні контакти зсуваються.

menu_items = [  # Список рядків із пунктами меню.
    "Add Contact",
    "View Contacts",
    "Search Contact",
    "Edit Contact",
    "Delete Contact",
    "Exit"
]
# Старий закоментований блок меню в оригіналі виконував один вибір без циклу.
# Він не запускався. Його діючий варіант з while True розміщений наприкінці.

keys = ["name", "phone", "email", "address", "notes", "added"]  # Ключі контакту.
# Словник dict зберігає пари «ключ: значення»:
# {'name': 'Alice', 'phone': '456730', ...}.
# На відміну від кортежу, потрібне поле знаходимо за ім’ям ключа.
# Закоментований експеримент contact.from_keys = lambda ... не виконується.
# lambda — інший спосіб створення функції; для розбору цього застосунку не потрібний.
# Як звичайне присвоєння атрибута словнику contact.from_keys він не працював би.
contact = dict.fromkeys(keys, "")  # Створюємо словник: кожен ключ має значення ''.
# fromkeys() — метод dict, а не from_keys.
# Початковий результат:
# {'name': '', 'phone': '', 'email': '', 'address': '', 'notes': '', 'added': ''}
print("📞 Welcome to Phone Book CLI")  # Вітання.
print("Please choose an option:")  # Підказка меню.
for idx, item in enumerate(menu_items, start=1):  # Номер і назва пункту.
    print(f"{idx}. {item}")  # Друкуємо 1. Add Contact тощо.
# Тут лише показуємо меню — вибір ще не зчитуємо.
# Воно повторно друкується в основному циклі нижче: це зайве дублювання виводу.
# print(contact) — у початковому коді закоментований перегляд словника.

print(hash(contact['name']))  # Обчислюємо й друкуємо хеш порожнього рядка ''.
# hash() повертає ціле число для хешованого об’єкта; це не шифрування і не ID.
# На цьому етапі ім’я ще порожнє, John Doe записується тільки нижче.
# Різні значення можуть мати однаковий хеш. Хеші непорожніх рядків зазвичай
# можуть відрізнятися між запусками Python; сталий ID контакту так не створюють.

i = 1  # Демонстраційний порядковий номер.
contact['name'] = "John Doe"  # Записуємо значення за ключем name.
contact['phone'] = "123-456-7890"  # Телефон як текст.
contact['email'] = "john.doe@example.com"  # Електронна адреса.
contact['address'] = "123 Main St, Anytown, USA"  # Адреса тепер один рядок.
contact['notes'] = "Friend from college"  # Примітка.
added = datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # Окрема змінна з датою.
# ПРОБЛЕМА: це не присвоєння contact['added']; у словнику added лишається ''.
# Демонстраційний John Doe не додається в contacts і в меню не з’явиться.
print(f"{i:<2} {contact['name']:<8} {contact['phone']:<10} {contact['email']:<15} {contact['address']:<20} {contact['notes']:<20} {added}")
# :<20 — вирівняти ліворуч у полі мінімальної ширини 20 символів.
# < — напрямок вирівнювання, число — мінімальна ширина.
# Довший текст не обрізається: John Doe не обмежується жорстко 8 символами.

contacts = []  # Створюємо реальний список контактів у пам’яті програми.
values = ['Alice', '456730', 'test@my.com', 'My city', 'My note', datetime.now().isoformat()]
# Значення стоять у тому самому порядку, що й keys.
# isoformat() повертає дату/час на кшталт 2026-10-26T14:30:12.123456.
# Без часової зони now() дає локальний час без позначення зони у цьому рядку.

def save_contact(keys, values):  # Отримуємо список ключів і список значень.
    """Add a new contact to memory and disk"""
    # ПРОБЛЕМА документації: жодного запису на диск нижче немає!
    # Дані залишаються лише в оперативній пам’яті до завершення програми.
    contact = {}  # Новий локальний порожній словник для одного контакту.
    # Він відрізняється від демонстраційного contact із John Doe зовні функції.
    for k, v in zip(keys, values):  # Перебираємо попарно ключі та значення.
        # zip дає ('name', 'Alice'), потім ('phone', '456730') тощо.
        # k отримує ключ, v отримує відповідне значення.
        # Якщо довжини списків різні, zip зупиниться на коротшому.
        contact[k] = v  # Додаємо пару до словника, наприклад name: Alice.
    contacts.append(contact)  # Додаємо сформований словник у спільний список.
    # global не потрібний: змінюємо сам список, а не переприсвоюємо contacts.
    print(f"✅ Contact '{contact['name'].title()}' added successfully!")
    # title() змінює регістр лише для цього повідомлення, не значення в словнику.
    print(f"📇 Total contacts: {len(contacts)}")  # Кількість усіх контактів.
    # print(contacts[0]) можна використати для перегляду першого словника.
    # Функція не має явного return, отже повертає None.

save_contact(keys, values)  # Уже зараз додаємо Alice, ще до запуску меню.

def get_field(field):  # field — назва обов’язкового поля для підказки.
    """Зчитує обов’язкове непорожнє поле."""
    while True:  # Повторюємо, поки користувач не введе непорожній текст.
        result = input(f"Enter {field}: ").strip()  # Зчитуємо й чистимо краї.
        if result:  # Непорожній рядок у логічній умові означає істину.
            return result  # Повертаємо текст; завершуємо і цикл, і функцію.
        print(f"{chr(10060)} {field.title()} cannot be empty.")
        # Якщо введено лише пробіли, strip дає '', тому просимо ще раз.
    # Функція перевіряє лише непорожність, не коректність email чи телефону.

def get_optional_field(field):  # Функція для необов’язкового поля.
    """Зчитує текст або повертає None для порожнього введення."""
    return input(f"Enter {field} (optional): ").strip() or None
    # Непорожній рядок лишається рядком, а '' замінюється на None.
    # None — спеціальне значення «даних немає», а не рядок 'None'.

# Демонстраційні виклики нижче були закоментовані й не виконуються:
# name = get_field("name")
# phone = get_field("phone")
# address = get_optional_field("address")
# Закоментоване старе add_contact() в оригіналі дублювало add_contact_old().
# Воно формувало кортеж із 4 полів і теж несумісне з новим форматом.

def add_contact():  # Це діюча функція, яку викликає пункт 1 меню.
    """Додає контакт після перевірки обов’язкових полів."""
    print("\n➕ ADD NEW CONTACT")  # Заголовок додавання.
    name = get_field('name')  # Отримуємо непорожнє ім’я.
    phone = get_field('phone number')  # Отримуємо непорожній номер.
    email = get_field('email')  # Email у цій версії також обов’язковий.
    address = get_optional_field('address')  # Текст адреси або None.
    notes = get_optional_field('notes')  # Текст примітки або None.
    save_contact(keys, [name, phone, email, address, notes, datetime.now().isoformat()])
    # Формуємо список із 6 значень і передаємо його разом із keys.
    # Позиції значень мають відповідати позиціям ключів у keys.

# add_contact() — прямий тестовий виклик у початковому коді закоментований.

def data_table(contacts, title):  # Отримуємо список для показу та заголовок.
    """Друкує контакти у вигляді текстової таблиці."""
    # contacts тут — параметр: можна передати весь список або результати пошуку.
    print("\n" + "=" * 80)  # Новий рядок та 80 знаків =.
    print(f"📱 {title.upper()}")  # Заголовок великими літерами.
    print("=" * 80)  # Верхня лінія таблиці.
    print(f"{'No.':<3} {'Name':<20} {'Phone':<15} {'Email':<20} {'Added':<10}")
    # Форматуємо назви колонок так само, як значення в рядках нижче.
    print("-" * 80)  # Розділювач заголовка та даних.
    for i, contact in enumerate(contacts, 1):  # Порядковий номер і словник.
        email = contact.get('email', 'N/A')  # Значення або N/A, якщо ключа немає.
        address = contact.get('address', 'N/A')  # Отримуємо адресу.
        # Особливість: address далі не виводиться й тут фактично не потрібна.
        added = contact.get('added', 'N/A')  # Отримуємо дату або запасний текст.
        # get(key, default) обирає default лише якщо КЛЮЧА немає.
        # Якщо ключ є зі значенням None або '', get поверне саме None або ''.
        # None у email не підтримує формат :<20; None у added не можна нарізати.
        # Діючий add_contact забезпечує текст для email і added, але для
        # довільних зовнішніх контактів потрібна додаткова обробка цих випадків.
        print(f"{i:<3} {contact['name']:<20} {contact['phone']:<15} {email:<20} {added[:10]}")
        # added[:10] бере перші 10 символів, наприклад 2026-10-26, без часу.
        # ['name'] та ['phone'] вимагають наявності цих ключів, інакше KeyError.
        # Ширина колонок мінімальна: довгі значення можуть зсувати таблицю.

# У закоментованому варіанті друку оригіналу було:
# contact['address'] or 'N/A' та contact['notes'] or 'N/A'.
# Так можна заміняти порожній рядок або None на N/A під час показу.

def view_contacts():  # ДРУГЕ визначення під тією самою назвою.
    """Показує всі контакти у новому форматі словників."""
    # Ім’я view_contacts тепер посилається на цю функцію, а не на стару вище.
    if not contacts:  # Якщо спільний список порожній.
        print("📭 No contacts found.")
        return  # Завершуємо без побудови таблиці.
    data_table(contacts, 'contact list')  # Передаємо список і заголовок.

# ОСНОВНИЙ ЦИКЛ: до цього моменту визначені всі потрібні функції.
while True:  # Показуємо меню повторно до виконання break.
    print("\nPlease choose an option:")
    for idx, item in enumerate(menu_items, start=1):  # Нумеруємо пункти від 1.
        print(f"{idx}. {item}")
    choice = input(f"Enter your choice (1-{len(menu_items)}): ").strip()
    # len(menu_items) = 6. choice — рядок, тому case також містять рядки.
    match choice:  # Зіставляємо введене значення з варіантами.
        case "1": add_contact()  # Запускаємо додавання нового словника.
        case "2": view_contacts()  # Показуємо актуальну таблицю.
        case "3":
            query = input("Enter term for search: ").strip()  # Запит пошуку.
            search_contact(query)  # ПРОБЛЕМА: старий пошук несумісний зі словниками.
        case "4": edit_contact()  # ПРОБЛЕМА: старе редагування теж несумісне.
        case "5":
            view_contacts()  # Спочатку показуємо номери доступних контактів.
            id_str = input("Enter ID to delete: ").strip()  # Просимо номер.
            delete_contact(id_str)  # Перевіряємо та видаляємо за номером.
        case "6":
            print("👋 Thank you for using Phone Book CLI. Goodbye!")
            break  # Виходимо з while; оскільки коду нижче немає, програма завершується.
        case _: print("❌ Invalid choice. Please try again.")
        # _ — запасний зразок: сюди потрапляє будь-який інший вибір.
    # Після виконання пунктів 1–5 або неправильного вибору повертаємося до меню.

# ПОРЯДОК РОБОТИ ПРОГРАМИ
# 1. Імпортує datetime і визначає функції — тіла функцій ще не виконуються.
# 2. Створює меню та демонстраційний словник, друкує приклади.
# 3. Створює contacts і додає Alice через save_contact().
# 4. Визначає решту функцій та замінює старий view_contacts новим.
# 5. Запускає нескінченний цикл меню; пункт 6 завершує його.
# Усе виконується згори вниз. Функції звертаються до глобальних імен
# у момент свого виклику, тому contacts може бути визначено нижче за def,
# але обов’язково до виклику, який використовує цей список.
# Після виходу контакти не зберігаються: файлів або бази даних у коді немає.
