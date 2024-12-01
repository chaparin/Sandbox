import turtle

# Set the screen size to 800 pixels wide and 600 pixels high
screen = turtle.Screen()
screen.setup(width = 800, height = 600)

length = 300
angle = 123
for n in range(120):
    turtle.speed(0)
    turtle.forward(length)
    turtle.right(angle)

turtle.done()