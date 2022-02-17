import turtle as t
import random

tim = t.Turtle()
t.colormode(255)
########### Challenge 4 - Random Walk ########
#colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    ran_color = (r, g, b)
    return ran_color


def random_walk():
    angels = [0, 90, 270, 180]
    tim.pensize(8)
    tim.speed(0)

    while 300 > tim.xcor() > -300 and 300 > tim.ycor() > -300:
        tim.pencolor(random_color())
        tim.setheading(random.choice(angels))
        tim.forward(20)


    screen = t.Screen()
    screen.exitonclick()


random_walk()