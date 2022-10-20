# from the Drawing package

from turtle import *

class no_delay:
    "A context manager which causes drawing code to run instantly"

    def __enter__(self):
        self.n = tracer()
        self.delay = delay()
        tracer(0, 0)

    def __exit__(self, exc_type, exc_value, traceback):
        update()
        tracer(self.n, self.delay)

