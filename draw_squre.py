"""

"""

import turtle

def draw_square(somez_turtle):
    while i < 4:
        somez_turtle.forward(100)
        somez_turtle.right(90)
        i += 1

def draw_art():
    window = turtle.Screen()
    window.bgcolor('red')

    # draw a square
    brad = turtle.Turtle()
    brad.shape('turtle')
    brad.color('yellow')
    brad.speed(2)

    n = 0
    for j in range(0,36):
        draw_square(brad)
        brad.rt(10)

    window.exitonclick()
draw_art()
