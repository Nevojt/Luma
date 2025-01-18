import pyfiglet
from colorama import Fore, Back, Style

hello = "This is calculater!!!"
# Back.GREEN

print(Fore.LIGHTMAGENTA_EX + Back.RED +Style.BRIGHT + pyfiglet.figlet_format(hello))

num1 = float(input("Enter first number: "))
option = input("Enter operator (+, -, *, /): ")
num2 = float(input("Enter second number: "))


if option == "+":
    result = num1 + num2
    print(pyfiglet.figlet_format(f"{num1} + {num2} = {result}"))

elif option == "-":
    result = num1 - num2
    print(pyfiglet.figlet_format(f"{num1} - {num2} = {result}"))

elif option == "/":
    result = num1 / num2
    print(pyfiglet.figlet_format(f"{num1} / {num2} = {result}"))

elif option == "*":
    result = num1 * num2
    print(pyfiglet.figlet_format(f"{num1} * {num2} = {result}"))