"""Телефонна книга: навчальний приклад із контактами-словниками.

Кожен контакт зберігається у списку contacts як словник із ключами
name, phone, email, address, notes, added. Python 3.10+ потрібен для match.
Контакти зберігаються в оперативній пам'яті й після виходу зникають.
"""

from datetime import datetime  # Імпортуємо клас для отримання дати й часу.

# Список містить контакти лише під час роботи програми.
contacts = []

# Назви полів. Порядок ключів відповідає порядку значень під час додавання.
keys = ["name", "phone", "email", "address", "notes", "added"]
menu_items = ["Add Contact", "View Contacts", "Search Contact",
              "Edit Contact", "Delete Contact", "Clear All Contacts", "Exit"]

def get_field(field):
    """Запитує обов'язкове поле, доки воно не стане непорожнім."""
    while True:
        result = input(f"Enter {field}: ").strip()  # Прибираємо крайні пробіли.
        if result:  # Непорожній рядок — істина.
            return result  # Повертаємо текст і завершуємо функцію.
        print(f"❌ {field.title()} cannot be empty.")

def get_name(current_index=None):
    """Зчитує непорожнє унікальне повне ім'я; Enter зберігає його при редагуванні."""
    while True:
        if current_index is None:  # Під час додавання ім'я обов'язкове.
            name = get_field("full name")
        else:  # Під час редагування Enter залишає вже збережене ім'я.
            old_name = contacts[current_index]["name"]
            name = input(f"Enter full name (Enter to keep '{old_name}'): ").strip()
            if not name:
                return old_name
        # При порівнянні ігноруємо регістр і зайві пробіли між словами.
        normalized_name = " ".join(name.split()).casefold()
        duplicate = False
        for index, contact in enumerate(contacts):
            # Не порівнюємо контакт із самим собою під час редагування.
            if index != current_index:
                existing_name = " ".join(contact["name"].split()).casefold()
                if normalized_name == existing_name:
                    duplicate = True
                    break
        if not duplicate:
            return name
        print("❌ This full name already exists. Enter another name.")

def get_phone(current_index=None):
    """Зчитує унікальний телефон із 12 цифр; Enter при редагуванні зберігає його."""
    while True:
        if current_index is None:
            phone = get_field("phone number (12 digits)")
        else:
            old_phone = contacts[current_index]["phone"]
            phone = input(f"Enter phone (Enter to keep '{old_phone}'): ").strip()
            if not phone:
                return old_phone
        # Номер — рядок із 12 цифр: int() прибрав би початкові нулі.
        if len(phone) != 12 or not phone.isascii() or not phone.isdecimal():
            print("❌ Phone number must contain exactly 12 digits (0-9).")
            continue
        duplicate = False
        for index, contact in enumerate(contacts):
            if index != current_index and contact["phone"] == phone:
                duplicate = True
                break
        if not duplicate:
            return phone
        print("❌ This phone number already exists. Enter another number.")

def save_contact(keys, values):
    """Створює словник із полів і додає його до списку в пам'яті."""
    contact = {}  # Для кожного контакту створюємо окремий порожній словник.
    for key, value in zip(keys, values):  # Беремо по одному ключу й значенню.
        contact[key] = value  # Наприклад, contact['name'] = 'Alice'.
    contacts.append(contact)  # Додаємо заповнений словник у спільний список.
    print(f"✅ Contact '{contact['name']}' added successfully!")
    print(f"📇 Total contacts: {len(contacts)}")

def add_contact():
    """Зчитує дані та додає новий контакт."""
    print("\n➕ ADD NEW CONTACT")
    name = get_name()  # Перевіряємо, що ім'я непорожнє й унікальне.
    phone = get_phone()  # Перевіряємо 12 цифр і відсутність дублів.
    email = get_field("email")
    address = get_field("address")  # Адреса тепер обов'язкова.
    notes = get_field("notes")  # Примітки також обов'язкові.
    added = datetime.now().isoformat()  # Дата й час додавання як рядок.
    save_contact(keys, [name, phone, email, address, notes, added])

def data_table(items, title):
    """Друкує передані контакти разом із їхніми номерами в загальному списку."""
    print("\n" + "=" * 80)
    print(f"📱 {title.upper()}")
    print("=" * 80)
    print(f"{'No.':<4} {'Name':<20} {'Phone':<15} {'Email':<20} {'Added':<10}")
    print("-" * 80)
    for number, contact in items:  # Кожен елемент — пара (номер, словник).
        email = contact.get("email") or "N/A"  # None або '' замінюємо для показу.
        added = contact.get("added") or "N/A"
        print(f"{number:<4} {contact['name']:<20} {contact['phone']:<15} "
              f"{email:<20} {added[:10]}")  # Перші 10 символів — дата.

def view_contacts():
    """Показує список контактів із номерами від 1."""
    if not contacts:
        print("📭 No contacts found.")
        return  # Якщо список порожній, завершуємо функцію.
    data_table(enumerate(contacts, start=1), "contact list")

def search_contact(query):
    """Шукає частину імені або номера телефону."""
    query = query.strip()  # Прибираємо зайві пробіли на краях пошукового тексту.
    if not query:
        print("❌ Search term cannot be empty.")
        return
    results = []  # Тут зберемо пари (номер у загальному списку, контакт).
    for number, contact in enumerate(contacts, start=1):
        # lower() робить пошук за іменем нечутливим до регістру.
        if query.lower() in contact["name"].lower() or query in contact["phone"]:
            results.append((number, contact))
    if not results:
        print(f"🔍 No contacts found for '{query}'.")
        return
    # Номери збігів — їхні початкові номери, а не нова нумерація результатів.
    data_table(results, f"Search results for '{query}'")

def get_contact_index(action):
    """Повертає індекс контакту для редагування/видалення або None."""
    if not contacts:
        print("📭 No contacts found.")
        return None
    view_contacts()  # Показуємо номери перед вибором.
    id_str = input(f"Enter ID to {action}: ").strip()
    # isdecimal() приймає десяткові цифри; порожній рядок і слова відхиляються.
    if not id_str.isdecimal():
        print("❌ Please enter a valid number.")
        return None
    index = int(id_str) - 1  # Номер 1 відповідає індексу 0.
    if index < 0 or index >= len(contacts):
        print("❌ Invalid contact ID.")
        return None
    return index

def edit_contact():
    """Змінює поля словника; Enter залишає поточне значення."""
    index = get_contact_index("edit")
    if index is None:  # 0 — правильний індекс, тому перевіряємо саме на None.
        return
    contact = contacts[index]  # Отримуємо словник потрібного контакту.
    # Перевіряємо нове ім'я та телефон за тими ж правилами, що і при додаванні.
    # Enter зберігає попереднє значення; поточний контакт не вважаємо дублем.
    contact["name"] = get_name(index)
    contact["phone"] = get_phone(index)
    # Решту полів теж не можна зробити порожніми: Enter зберігає старі дані.
    for key in ("email", "address", "notes"):
        current = contact.get(key) or "N/A"
        new_value = input(f"Enter new {key} (Enter to keep '{current}'): ").strip()
        if new_value:  # Порожній ввід залишає старе значення.
            contact[key] = new_value  # Змінюємо поле безпосередньо у словнику.
    print(f"✅ Contact ID {index + 1} updated successfully.")

def delete_contact():
    """Видаляє вибраний словник зі списку."""
    index = get_contact_index("delete")
    if index is None:
        return
    deleted_contact = contacts.pop(index)  # pop видаляє й повертає елемент.
    print(f"🗑 Contact '{deleted_contact['name']}' deleted successfully!")

def clear_contacts():
    """Очищує весь список після підтвердження користувача."""
    if not contacts:
        print("📭 No contacts to clear.")
        return
    answer = input("Delete ALL contacts? Enter yes to confirm: ").strip().lower()
    if answer == "yes":
        contacts.clear()  # clear() видаляє всі словники зі списку contacts.
        print("🗑 All contacts cleared.")
    else:
        print("Clear cancelled.")  # Будь-яка інша відповідь скасовує очищення.

def main():
    """Показує меню, доки користувач не вибере вихід."""
    print("📞 Welcome to Phone Book CLI")
    while True:
        print("\nPlease choose an option:")
        for number, item in enumerate(menu_items, start=1):
            print(f"{number}. {item}")
        choice = input(f"Enter your choice (1-{len(menu_items)}): ").strip()
        match choice:  # input повертає рядок, тому порівнюємо з '1', '2' тощо.
            case "1": add_contact()
            case "2": view_contacts()
            case "3":
                query = input("Enter term for search: ")
                search_contact(query)
            case "4": edit_contact()
            case "5": delete_contact()
            case "6": clear_contacts()
            case "7":
                print("👋 Thank you for using Phone Book CLI. Goodbye!")
                break  # Завершуємо цикл меню.
            case _: print("❌ Invalid choice. Please try again.")

if __name__ == "__main__":
    # Запускаємо меню, коли цей файл виконують як програму.
    main()
