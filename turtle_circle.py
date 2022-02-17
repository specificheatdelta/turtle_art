import turtle as t
import random

tim = t.Turtle()
tim.speed(0)
t.colormode(255)
tim.setheading(0)


########### Challenge 4 - Random Walk ########
# colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    ran_color = (r, g, b)
    return ran_color


def spirograph(size_of_gap):
    # for n in range(0, 100):
    #     tim.color(random_color())
    #     tim.circle(100)
    #     tim.left(n)

    for n in range(int(360 / size_of_gap)):
        tim.color(random_color())
        tim.circle(100)
        current_heading = tim.heading()
        tim.setheading(current_heading + size_of_gap)
        print(tim.heading())

    screen = t.Screen()
    screen.exitonclick()


spirograph(2)
