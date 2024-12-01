import turtle

# Set the screen size to 800 pixels wide and 600 pixels high
screen = turtle.Screen()
screen.setup(width = 800, height = 600)

length = 300
angle = 123
outer_length = 75
outer_angle = 120

for a in range(120):
    turtle.speed(10)
    for n in range(3):
        turtle.forward(length)
        turtle.right(angle)
    for i in range(3):
        turtle.back(outer_length)
        turtle.left(outer_angle)

turtle.done()