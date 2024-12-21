from random import randint

# Super Punk 2076

print("Hello new Loser!")
print("Welcome to the world of Super Punk 2076!")

name = input("What is name your hero?\n")

characters = ["British", "Puchnastiks", "Lysiashysh", "Luker", "Choinker"]

print("Characters: ", characters)
char_input = int(input("What is character number 1-5?\n"))

if char_input < 1 or char_input > 5:
    print("Invalid character number!")
    char_input = randint(1, 5)


loser_character = characters[char_input - 1]

print("Your name: " + name + " your character " + loser_character)

full_name = name + " " + loser_character

print()
# TODO: Implement the game logic
print("Кіт потрапив до печери з драконом!")
print(full_name, " Бачить 3 двері, в які двері він піде?")


door_input = int(input("Введіть номер двері (1-3):\n"))
if door_input < 1 or door_input > 3:
    print("Invalid character number!")
    door_input = randint(1, 3)

    if door_input == 1:
        print("Za dveryma  1 sydiv Stary Did, i kazaw sp****!!!")
    elif door_input == 2:
        print("Za dveryma 2 na kota " + full_name + " vyskochyla krysa rozmirom z kamaz")
        print("Kit nawalyw welyku kupu!!!")
    else:
        print("Za dveryma 3 sydiw " + characters[-1] + " I lyzaw choinku...")
