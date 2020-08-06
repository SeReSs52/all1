import random
import turtle

Display = turtle.Screen()
steve = turtle.Turtle()

rainbow = [
    "green",
    "yellow",
    "pink",
    "orange",
    "blue",
    "purple"
]

steve.width(4)
steve.speed(0)

def draw_slinky(count, angle):
    for i in range(count):
        color = random.choice(rainbow)
        steve.color(color)
        steve.left(angle)
        steve.circle(i)

def draw_stars(count, angle):
    for i in range(count):
        color = random.choice(rainbow)
        steve.color(color)
        steve.left(angle)
        steve.forward(i)

a = random.randint(0, 10)

if a > 5:
    draw_stars(1000, 89)
else:
    draw_slinky(1000, 8)