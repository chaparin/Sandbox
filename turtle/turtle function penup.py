import turtle
turtle.color("green")

# Set the screen size to 800 pixels wide and 600 pixels high
screen = turtle.Screen()
screen.setup(width = 800, height = 600)

def back(len):
    turtle.penup()
    turtle.backward(len)
    turtle.pendown()

def triangle(size):
    for n in range(3):
        angle = 120
        turtle.speed(10)
        turtle.forward(size)
        turtle.left(angle)
triangle(300)
back(200)
triangle(150)
back(100)
triangle(75)

turtle.exitonclick()