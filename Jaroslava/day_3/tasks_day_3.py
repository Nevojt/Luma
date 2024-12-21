# TODO Завдання 1: Створення списку списку

"""
1. Створити порожній список з назвою my_list
2. Створити список з назвою my_list_2 який буде містити строку Hello There, 125, True, False
3. Вставити в список my_list дві стрічки тексту: "Hello, World!" та "Привіт, Мир!" використати
        a) один метод append()
            1) Роздрукувати my_list
        b) один метод extend()
            1) Роздрукувати my_list
        ctrl + lcm --> синтаксис https://www.w3schools.com/python/python_lists_add.asp
3. Роздрукувати весь список my_list
4. Використати len(my_list) для підрахунку елементів в списку
5. Роздрукувати результат

ctrl + lcm --> синтаксисhttps://www.w3schools.com/python/python_lists_remove.asp
6. Видалити за допомогою pop() перший елемент списку
    Роздрукувати результат
7. Видалити за допомогою remove()  елемент списку True
    Роздрукувати результат

"""

my_list = []
my_list.append("Hello, World!")
my_list.append("Привіт, Мир!")
print(my_list) # Output: ['Hello, World!', 'Привіт, Мир!']

my_list_2 = ["Hello There", 125, True, False]
my_list.extend(my_list_2)
print(my_list) # Output: ['Hello, World!', 'Привіт, Мир!', 'Hello There']

print(len(my_list)) # Output: 6

my_list.pop(0)
print(my_list) # Output: ['Привіт, Мир!', 'Hello There', 125, True, False]

my_list.remove(True)
print(my_list) # Output: ['Привіт, Мир!', 'Hello There', 125, False]


# TODO Завдання 2: Спілкування з користувачем

"""
1. Створити порожній список з назвою user_list
    a. Запитати у користувача його ім'я
    b. Додати ім'я до списку user_list
    c. Повторити 3 рази
2. Роздрукувати список (повинно бути 3 імені)
3. За допомогою insert() додати 4-те ім'я на позицію 1
    a. Роздрукувати список
    b. Змінити 3-ий елемент --- список[індекс] = нове ім'я
     https://www.w3schools.com/python/python_lists_change.asp
4. Роздрукувати список
"""

user_list = []
user_name_1 = input("Enter your first name: ")
user_list.append(user_name_1)
user_name_2 = input("Enter your second name: ")
user_list.append(user_name_2)
user_name_3 = input("Enter your tree name: ")
user_list.append(user_name_3)

print(user_list)

user_list.insert(1, "Fourth Name")
print(user_list)