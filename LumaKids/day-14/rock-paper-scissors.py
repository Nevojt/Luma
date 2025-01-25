
import pyfiglet
from random import choice

hello = "ROCK\nPAPER\nSCISSORS"
print(pyfiglet.figlet_format(hello))

list_choose = ["rock", "paper", "scissors"]
choose_comp = choice(list_choose)
# print(choose_comp)

user_input = input("Your choose from game\nROCK\nPAPER\nSCISSORS: ").lower()
# print(user_input)

try:
    if user_input == choose_comp:
        print("It's a draw!")
        print(f"User chose: {user_input}")
        print(f"Computer chose: {choose_comp}")
        print(pyfiglet.figlet_format("Draw"))

    elif user_input == "rock" and choose_comp == "paper":
        print("You loose!")
        print(f"User chose: {user_input}")
        print(f"Computer chose: {choose_comp}")
        print(pyfiglet.figlet_format("You Lose"))

    elif user_input == "rock" and choose_comp == "scissors":
        print("You win")
        print(f"User chose: {user_input}")
        print(f"Computer chose: {choose_comp}")
        print(pyfiglet.figlet_format("You win"))

    elif user_input == "paper" and choose_comp == "scissors":
        print("You loose!")
        print(f"User chose: {user_input}")
        print(f"Computer chose: {choose_comp}")
        print(pyfiglet.figlet_format("You Lose"))

    elif user_input == "paper" and choose_comp == "rock":
        print("You win")
        print(f"User chose: {user_input}")
        print(f"Computer chose: {choose_comp}")
        print(pyfiglet.figlet_format("You win"))

    elif user_input == "scissors" and choose_comp == "rock":
        print("You loose!")
        print(f"User chose: {user_input}")
        print(f"Computer chose: {choose_comp}")
        print(pyfiglet.figlet_format("You Lose"))

    elif user_input == "scissors" and choose_comp == "paper":
        print("You win")
        print(f"User chose: {user_input}")
        print(f"Computer chose: {choose_comp}")
        print(pyfiglet.figlet_format("You win"))


except Exception:
    print("Your choice is bad!")


