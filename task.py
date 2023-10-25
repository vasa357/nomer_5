# Словник для зберігання інформації про користувачів
users = {}

# Початковий ID користувача
current_user_id = 1

while True:
    print("Меню:")
    print("1 - Карта читача")
    print("2 - Взяти книгу")
    print("3 - Повернути книгу")
    print("0 - Вихід")
    choice = input("Виберіть опцію: ")

    if choice == '0':
        break
    elif choice == '1':
        user_id = int(input("Введіть ID користувача: "))
        user = users.get(user_id)
        if user:
            print("КАРТА ЧИТАЧА")
            for key, value in user.items():
                print(f"{key}: {value}")
        else:
            print("Користувача з таким ID не знайдено.")
    elif choice == '2':
        user_id = int(input("Введіть ID користувача: "))
        book_name = input("Введіть назву книги, яку ви берете в борг: ")
        user = users.get(user_id, {'ID': user_id, 'Книги': [], 'Статистика книг': []})
        user['Книги'].append(book_name)
        users[user_id] = user
        print(f"Книга '{book_name}' додана до боргу користувача.")
    elif choice == '3':
        user_id = int(input("Введіть ID користувача: "))
        user = users.get(user_id)
        if user:
            if user['Книги']:
                print("Список книг у боргу:")
                for i, book in enumerate(user['Книги']):
                    print(f"{i+1}. {book}")
                book_to_return = int(input("Введіть номер книги, яку ви хочете повернути: ")) - 1
                if 0 <= book_to_return < len(user['Книги']):
                    returned_book = user['Книги'].pop(book_to_return)
                    user['Статистика книг'].append(returned_book)
                    print(f"Книгу '{returned_book}' повернуто.")
                else:
                    print("Неправильний номер книги.")
            else:
                print("Список книг у боргу порожній.")
        else:
            print("Користувача з таким ID не знайдено.")
    else:
        print("Неправильний вибір. Спробуйте ще раз.")
