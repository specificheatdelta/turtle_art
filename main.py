# Multiple ways to import modules.
# from turtle import *
# from turtle import Turtle, Screen
#import turtle
import turtle as t
import random
from color_list import COLORS
import heroes

tim_turt = t.Turtle()
tim_color = tim_turt.color("red")
# timmy_the_turtle.forward(100)
# TK color speficiation string. TK is short for tkinter which is tk interface. Can be used to create a GUI

# for n in range(4):
#     tim_turt.forward(100)
#     tim_turt.left(90)
#
# for n in range(4):
#     tim_turt.forward(100)
#     tim_turt.right(90)


# print(heroes.gen())

# for n in range(15):
#     tim_turt.forward(10)
#     tim_turt.penup()
#     tim_turt.forward(10)
#     tim_turt.pendown()

tim_turt.speed(1)
tim_turt.hideturtle()
tim_turt.penup()
tim_turt.goto(-50, 150)
tim_turt.pendown()
tim_turt.showturtle()
n = 3
while n <= 10:
    m = n + 1
    for _ in range(1, m):
        angle = 360 / n
        tim_turt.forward(100)
        tim_turt.right(angle)
    tim_turt.color(random.choice(COLORS))
    n += 1

screen = t.Screen()
screen.exitonclick()
