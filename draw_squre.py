"""

"""

import turtle

def draw_art():
    window = turtle.Screen()
    window.bgcolor('red')

    # draw a square
    brad = turtle.Turtle()
    brad.shape('turtle')
    brad.color('yellow')
    brad.speed(2)

    n = 0
    while n <360:
        brad.right(10)
        n += 10
        i = 0
        while i < 4:
            brad.forward(100)
            brad.right(90)
            i += 1

    window.exitonclick()
draw_art()
