from turtle import *
from movement import *
import settings
import random

def draw(length,angle,color, outline_color):
    bottom = pos()
    direction = heading()
    pencolor(outline_color)
    fillcolor(color)
    begin_fill()
    forward(length)
    right(angle)
    forward(30)
    goto(bottom)
    end_fill()
    setheading(direction)

    bottom = pos()
    direction = heading()
    pencolor(outline_color)
    fillcolor(color)
    begin_fill()
    forward(length)
    left(angle)
    forward(30)
    goto(bottom)
    end_fill()
    setheading(direction)

def draw_0(length):
    for i in range(10,171,20):
        random_element1 = random.random()/2 +0.5
        random_element2 = random.random()/2 +0.5
        random_element3 = random.random()/2 +0.25

        my_color = (random_element3,random_element1, random_element2)
        outline_color = my_color
        draw(length,i,my_color,outline_color)

def draw_1():
    for i in range(30):
        draw_0(300)
        right(12)

def draw_2():
    for i in range(20):
        draw_0(200)
        right(18)

def draw_3():
    for i in range(10):
        draw_0(100)
        right(36)
