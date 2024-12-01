# Writing Functions 1
# Sergei Chaparin
def add_numbers(a, b):
    add = a + b
    return add


def multiply_numbers(a, b):
    multiply = a * b
    return multiply


def main():
    x = int(input("Enter first number: "))
    y = int(input("Enter second number: "))
    print("The sum of the entered numbers is: ", add_numbers(x, y))
    print("The multiply of the entered numbers is: ", multiply_numbers(x, y))


main()
