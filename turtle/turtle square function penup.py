import turtle
turtle.color("green")

# Set the screen size to 800 pixels wide and 600 pixels high
screen = turtle.Screen()
screen.setup(width = 800, height = 600)

def back(len):
    turtle.penup()
    turtle.backward(len)
    turtle.pendown()

def square(size):
    for n in range(4):
        angle = 90
        turtle.speed(10)
        turtle.forward(size)
        turtle.left(angle)
        
square(300)
back(200)
square(150)
back(100)
square(75)

turtle.exitonclick()