user = { id: 1,
        'прізвище': "Кравчук",
        "ім'я": "Василь",
        'група': "ІПЗс-23-2",
        'курс': 1,
        'книги борг': {},
        'статистика книг': {} }
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
        user = user.get(user_id)
        if user:
            print("КАРТА ЧИТАЧА")
            for key, value in user.items():
                print(f"{key}: {value}")
        else:  
            print("Користувача з таким ID не знайдено.")