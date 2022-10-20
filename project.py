from turtle import *
from designs import draw_circle
from helpers import no_delay
import time
import settings
from random import randint 

def draw_animation(num_frames, sleeptime,outline):
    # Draws a moving circle

    for i in range(num_frames):
        val1 = randint(0,255)
        val2 = randint(0,255)
        val3 = randint(0,255)

        fill_color = (val1, val2, val3)

        with no_delay():
            clear()

            draw_circle(8, 250, fill_color, outline)
            right(10)

        time.sleep(sleeptime)

def main():
    screen = Screen()
    screen.setup(settings.SCREENWIDTH,settings.SCREENHEIGHT)
 
    hideturtle()
    colormode(255)
  
    for i in range(settings.NUMREPEATS):
        draw_animation(
            settings.NUMFRAMES, 
            settings.SLEEPTIME,  
            settings.OUTLINECOLOR)

main()




