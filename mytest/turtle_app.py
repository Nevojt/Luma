import turtle
from random import choice, random

t = turtle.Turtle()
# t.speed(0)
t.speed(5)

screen = turtle.Screen()
screen.setup(width=600, height=600)

# t.forward(100)
# t.left(90)
# t.forward(100)

list_color = ['black', 'red', 'green', 'yellow', 'orange', 'purple']
FORWARD = 300
LEFT = 170
for i in range(100):
    t.forward(FORWARD)
    t.color(choice(list_color))
    t.left(LEFT)




# for i in range(100):
#     steps = int(random() * 100)
#     angle = int(random() * 360)
#     t.right(angle)
#     t.fd(steps)











screen.exitonclick()


