# For python 3,
# Download the Swampy modules
# you can either work in the directory that contains the Swampy files,
# or add that directory to Python’s
# search path. Then you can import TurtleWorld like this:
# from TurtleWorld import *

from TurtleWorld import *
world = TurtleWorld()
bob = Turtle()

def square(t, length):
    """Draws n line segments with the given length and
    angle (in degrees) between them. t is a turtle.
    """
    for i in range(4):
        fd(t, 100)
        lt(t)

def polygon(t, n, length):
    angle = 360.0 / n
    for i in range(n):
    fd(t, length)
    lt(t, angle)

def circle(t, r):
    circumference = 2 * math.pi * r
    n = int(circumference / 3) + 1
    length = circumference / n
    polygon(t, n, length)

square(bob, 100)
wait_for_user()
