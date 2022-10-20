from turtle import *

def draw_shape(length, angle, color, outline_color):
    # Takes length, angle, color, and outline color as arguments.
        # length determines how long the shape is
        # angle determines how sharp the kite is 
            # small angles will make the shape appear like an arrow

    for i in range(2):
        position = pos()
        direction = heading()

        pencolor(outline_color)
        fillcolor(color)
        begin_fill()

        forward(length)

        if i == 0:
            left(angle)
        else:
            right(angle)

        forward(30)
        goto(position)
        end_fill()

        setheading(direction)

def draw_design(length, fill, outline):
    # Draws a custom design

    angle = 35
    
    draw_shape(length, angle, fill , outline)
    angle = angle + 30

    draw_shape(length, angle, fill , outline)
    angle = angle + 30

    draw_shape(length, angle, fill , outline)


def draw_circle(num, length, fill, outline):
    # Draws multiple of the design
  
    for i in range(num):
        draw_design(length, fill, outline)
        right(360//num)
