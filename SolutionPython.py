import turtle as t
from itertools import cycle

colors = cycle(["violet", "indigo", "blue", "green", "yellow", "orange", "red"])

def circle(size, angle, shift):
    t.hideturtle()
    t.pencolor(next(colors))
    t.circle(size)
    t.right(angle)
    t.forward(shift)
    circle(size + 2, angle + 1, shift + 1)

t.bgcolor("black")
t.speed(50)
t.pensize(4)
circle(40, 0, 1)
