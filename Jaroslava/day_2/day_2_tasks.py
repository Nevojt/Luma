
#  TODO: Завдання 1: Персональне привітання
"""
1. Запитай ім'я користувача за допомогою input().
2. Створи привітання за допомогою змінної, наприклад: greeting = "Привіт, " + name.
3. Виведи привітання на екран.
"""

name = input("What is your name? ")
greeting = "Hello, " + name + "!"
print(greeting)



# TODO: Завдання 2: Рахуємо вік
"""
1. Запитай рік народження користувача за допомогою input() і збережи його як ціле число, використовуючи int().
2. Обчисли вік користувача, віднявши рік народження від поточного року.
3. Виведи повідомлення, наприклад: 'Тобі приблизно X років'
"""

age = int(input("What year were yuo born? "))
current_year = 2024
your_age = current_year - age
print("You are approximately " + str(your_age) +" years old.")

# TODO: Завдання 3: Обчислюємо площу круга
"""
1. Запитай у користувача радіус кола в сантиметрах
   за допомогою input() і збережи його як число з плаваючою точкою, використовуючи float().
2. Обчисли площу кола за формулою: area = 3.14 * radius * radius.
3. Використай round() для округлення результату до 2 знаків після коми.
4. Виведи результат у вигляді: "Площа круга з радіусом X дорівнює Y".
"""

radius = float(input("What is the radius of the circle in centimeters? "))
area = 3.14 * radius * radius
rounded_area = round(area, 2)
print("The area of the circle with radius " + str(radius) + "cm" + " equals " + str(rounded_area) + "cm.")

# TODO: Завдання 4: Перетворення типів
"""
1. Запитай у користувача два числа за допомогою input().
2. Перетвори їх у числа з плаваючою точкою (float()) та знайди їх середнє значення.
3. Використай round() для округлення результату до цілого числа.
4. Виведи результат як ціле число, використовуючи int().
"""

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
average = round((num1 + num2) / 2)
print("The average of " + str(num1) + " and " + str(num2) + " is " + str(average) + ".")


#  TODO: Завдання 5: Конвертація одиниць
"""
Запитай у користувача значення в кілограмах (число), використовуючи input() та float().
Перетвори це значення в грами за формулою: grams = kg * 1000.
Використай str() для перетворення числового значення у рядок і склади результат у повідомленні.
Виведи результат у вигляді: "X кг = Y грамів".
"""

kilograms = float(input("Kilograms: "))
grams = kilograms * 1000
result = str(kilograms) + " kg = " + str(grams) + " grams."
# print(str(kilograms) + " kg = " + str(grams) + " grams.")
print(result)