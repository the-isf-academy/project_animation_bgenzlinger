from turtle import *
from helpers import *
import time
import settings

def draw_animation(num_frames, sleeptime):
    hideturtle()

    for i in range(num_frames):
        # # YOUR CODE GOES HERE#
        with no_delay():
            clear()
            setheading(360-i)
            draw_1()
            setheading(i)
            draw_2()
            setheading(360-i)
            draw_3()

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
