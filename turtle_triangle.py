"""

"""

import turtle , math

window = turtle.Screen()
window.bgcolor("white")

tria = turtle.Turtle()
tria.pensize(1)
tria.speed(5)
#tria.shape('turtle')
tria.color('white', 'green')

def draw_tria(length,startX, startY):
    tria.setpos(startX, startY)
    tria.pendown()
    tria.fillcolor('green')
    tria.begin_fill()
    for i in range(3):
        tria.forward(length)
        tria.left(120)
    tria.penup()
    tria.end_fill()

def draw(level, length, startX, startY):
    if level == 1:
        draw_tria(length,startX, startY)
        return
    draw(level-1, length/2, startX, startY)
    draw(level-1, length/2, startX + length/2, startY)
    draw(level-1, length/2, startX + length/4, startY + math.sqrt(3)/4 *length)

#    window.exitonclick()

draw(4, 400, -200, -200)

window.exitonclick()
