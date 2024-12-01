import turtle


def rectangle(len):
    turtle.penup()
    turtle.forward(len / 8 * 3)
    turtle.pendown()
    turtle.forward(len / 5)
    turtle.right(90)
    turtle.forward(len * 2)
    turtle.right(90)
    turtle.forward(len / 5)
    turtle.right(90)
    turtle.forward(len * 2)
    turtle.right(90)


def octagon(len):
    for i in range(8):
        turtle.forward(len)
        turtle.left(45)


def stopsign(len):
    octagon(len)
    rectangle(len)


def main():
    turtle.speed(0)
    turtle.color("blue")
    stopsign(100)
    turtle.penup()
    turtle.back(250)
    turtle.pendown()
    turtle.color("red")
    stopsign(50)


main()
turtle.Screen().exitonclick()
