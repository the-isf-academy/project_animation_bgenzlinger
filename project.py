from turtle import *
import settings

def draw_animation(num_frames, sleeptime):
    for i in range(num_frames):
        # YOUR CODE GOES HERE#

        screen.update()
        time.sleep(sleeptime)
    clear()

def main():
    for i in range(settings.NUMREPEATS):
        draw_animation(settings.NUMFRAMES, settings.SLEEPTIME)
    input("Press enter...")

if __name__ == '__main__':
    screen = Screen()
    screen.setup(settings.SCREENWIDTH,settings.SCREENHEIGHT)
    main()
