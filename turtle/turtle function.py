import turtle
turtle.color("green")

# Set the screen size to 800 pixels wide and 600 pixels high
screen = turtle.Screen()
screen.setup(width = 800, height = 600)

def triangle(size):
    for n in range(3):
        angle = 120
        turtle.speed(10)
        turtle.forward(size)
        turtle.left(angle)
triangle(300)

turtle.exitonclick()