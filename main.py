import turtle as t
import random

tom = t.Turtle()
tom.shape("turtle")

colours = [
    "red", "blue", "green", "yellow", "orange", "purple", "pink", "brown",
    "black", "white", "gray", "cyan", "magenta", "gold", "silver",
    "navy", "lime", "teal", "maroon", "violet", "turquoise", "indigo",
    "beige", "salmon", "coral", "orchid", "plum", "tan", "olive"
]
directions = [0, 90, 180, 270]
tom.pensize(10)
# tom.speed("fast")

for _ in range(100):
    tom.color(random.choice(colours))
    tom.forward(30)
    tom.setheading(random.choice(directions))

