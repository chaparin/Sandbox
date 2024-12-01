import turtle
turtle.color("green")

# Set the screen size to 800 pixels wide and 600 pixels high
screen = turtle.Screen()
screen.setup(width = 800, height = 600)

def back(len):
    turtle.penup()
    turtle.backward(len)
    turtle.pendown()

# Forward helper function
def move(len):
    back(-1 * len)

def polygon(sides, size):
    for n in range(sides):
        turtle.speed(10)
        turtle.forward(size)
        turtle.left(360 / sides)

# polygon(3, 100)
# back(125)
# polygon(4, 100)

# for n in range(3, 10):
#     move(50) #Forward
#     polygon(n, 100 / n)
#     back(50)
#     turtle.right(360 / 7)

def spiral(len, angle):
    for i in range(len, 5, -1):
        turtle.forward(i)
        turtle.right(angle)

spiral(100, 30)
move (150)
turtle.color("blue")
spiral (100, 90)

turtle.exitonclick()