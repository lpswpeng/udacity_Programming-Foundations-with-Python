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

    i = 0
    while i < 4:
        brad.forward(100)
        brad.right(90)
        i += 1
    # draw a circle
    anna = turtle.Turtle()
    anna.shape('arrow')
    anna.color('blue')
    anna.circle(80)

    # draw a triangle
    mary = turtle.Turtle()
    mary.shape('triangle')
    mary.color('green')

    j = 0
    while j < 3:
        mary.forward(150)
        mary.lt(120)
        j += 1

    window.exitonclick()


draw_art()
