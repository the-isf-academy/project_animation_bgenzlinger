from turtle import *
from helpers import draw_circle
from movement import no_delay
import time
import settings

def draw_animation(num_frames,sleeptime):
    """Takes num_frames and sleeptime as arguments and draws the animation.
    Draws 3 circles on top of eachother. With each frame, the innermost and outermost
    circles rotate clockwise and the middle circle rotates anti-clockwise"""
    hideturtle()

    for i in range(num_frames):
        with no_delay():
            clear()
            setheading(360-i)
            draw_circle(300)
            setheading(i)
            draw_circle(200)
            setheading(360-i)
            draw_circle(100)

    time.sleep(5)
    clear()

def main():
    for i in range(settings.NUMREPEATS):
        draw_animation(settings.NUMFRAMES, settings.SLEEPTIME)
    input("Press enter...")

if __name__ == '__main__':
    screen = Screen()
    screen.setup(settings.SCREENWIDTH,settings.SCREENHEIGHT)
    main()
