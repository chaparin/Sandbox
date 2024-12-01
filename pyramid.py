# Sergei Chaparin
# Write a function, pyramid, that takes a single character and a number as parameters
# and displays an ASCII art pyramid to the screen with number rows

def pyramid(n, character):
    for i in range(n):
        print(character * (i + 1))
        i += 1


def main():
    pyramid(2, "*")
    pyramid(5, "+")
    pyramid(10, "x")
    pyramid(100, "◊")


main()
