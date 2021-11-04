from turtle import *
import settings
import random

def draw_kite(length,angle,color, outline_color):
    """Takes length, angle, color, and outline color as arguments and
    draws a kite shape. length determines how long the kite shape is
    angle determines how sharp the kite is. small angles will make the kite
    appear like an arrow  """
    for i in range(2):
        bottom = pos()
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
        goto(bottom)
        end_fill()
        setheading(direction)

def draw_cluster(length):
    """Takes length as an argument and then calls draw_kite in a loop
    so that the kites create a 3-dimensional cluster. It is also
    determines the color of the cluster. If the color setting is random,
    it randomizes the color """

    if settings.FILLCOLOR == "random":
        #Create a random color
        random_element_red = random.random()/2 +0.25
        random_element_blue = random.random()/2 +0.5
        random_element_green = random.random()/2 +0.5
        my_color = (random_element_red,random_element_green, random_element_blue)
    else:
        #use the color from settings
        my_color = settings.FILLCOLOR
    if settings.OUTLINECOLOR == "random":
        #create a random color
        random_element_red = random.random()/2 +0.25
        random_element_blue = random.random()/2 +0.5
        random_element_green = random.random()/2 +0.5
        outline_color = (random_element_red,random_element_green, random_element_blue)
    else:
        #use the color from settings
        outline_color = settings.OUTLINECOLOR

    #draw 9 kites with angles that are evenly spaced
    for i in range(10,171,20):
        draw_kite(length,i,my_color,outline_color)

def draw_circle(length):
    """Draws a bunch of clusters radiating out from the center.
    The length of the clusters determines how many are drawn."""
    number = length//10
    for i in range(number):
        draw_cluster(length)
        right(360//number)
