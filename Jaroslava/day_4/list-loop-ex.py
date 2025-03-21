# TODO:Завдання 1: Використання зрізів
"""
Завдання: Маючи список numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90], виконайте наступні дії:

1. Виведіть перші три числа списку використовуючи зріз.
2. Виведіть останні чотири числа списку використовуючи зріз.
3. Виведіть кожне друге число з повного списку.
4. Виведіть список у зворотному порядку.
"""
# numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90]
#
# print(numbers[:3])
# print(numbers[-4:])
# print(numbers[::2])
# print(numbers[::-1])



# TODO: Завдання 2: Заміна елементів у списку
"""
Завдання: Маючи список fruits = ["apple", "banana", "cherry", "date", "elderberry"], виконайте наступні дії:

1. Замініть "banana" на "blueberry" і виведіть весь оновлений список.
2. Замініть перші два елементи списку на "kiwi" і "mango", потім виведіть весь список.
3. Вставте "orange" між "cherry" та "date" (замість "date", яке потім повинно слідувати за "orange").
"""
# fruits = ["apple", "banana", "cherry", "date", "elderberry"]
# fruits[1] = "blueberry"
# print(fruits)
# fruits[0], fruits[1] = "kiwi", "mango"
# print(fruits)
# fruits.insert(3, "orange")
# print(fruits)



# TODO: Завдання 3: Завдання з використанням циклів та умовних конструкцій:
"""
Фільтрація елементів списку:
Для списку [10, 20, 33, 46, 55, 68, 79, 123] виведіть слово "Парне",
якщо число парне, і слово "Непарне", якщо число непарне.
"""
# my_list = [10, 20, 33, 46, 55, 68, 79, 123]
#
# for i in my_list:
#     if i % 2 == 0:
#         print(f"{i} - Парне")
#     else:
#         print(f"{i} - Непарне")



# TODO: Завдання 4: Виведення елементів за умовою:
"""Напишіть скрипт, який ітерує список [3, 5, 7, 10, 12, 13, 18, 21, 22] і виводить:
"Ділиться на 3" для чисел, що діляться на 3 без залишку,
"Ділиться на 2" для чисел, що діляться на 2 без залишку,
"Не ділиться на 2 або 3" для інших чисел.
"""
# my_list = [3, 5, 7, 10, 12, 13, 18, 21, 22]
# for i in my_list:
#     if i % 3 == 0:
#         print(f"{i} - Ділиться на 3")
#     elif i % 2 == 0:
#         print(f"{i} - Ділиться на 2")
#     else:
#         print(f"{i} - Не ділиться на 2 або 3")


# TODO: Завдання 5: Аналіз чисел у списку
"""
Завдання: Даний список чисел: [1, 2, 3, 4, 5, 6, 7, 8, 9].
Виконайте наступні підзавдання використовуючи цикл for та умовні оператори if, elif i else :

1. Створіть змінну count і надайте їй нульове значення
2. Виведіть всі парні числа зі списку.
3. Підрахуйте суму всіх парних чисел і виведіть їх
4. Виведіть всі числа, що є кратними 3.
5. Підрахуйте середнє значення всіх чисел
6. Виведіть кількість ітерацій
"""

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]


count = 0
pare_count = 0
not_pare_count = 0
average_value = 0
for i in my_list:
    count += 1
    average_value += i
    if i % 2 == 0:
        print(i)
        pare_count += i
    elif i % 3 == 0:
        not_pare_count += i
        print(i)

print(f"Сума парних чисел: {pare_count}")
print(f"Сума не парних чисел: {not_pare_count}")

print(f"Кількість ітерацій: {count}")
print(f"Середнє значення всіх чисел: {average_value / count}")