# What does this program do?
def double(x):
    return x * 2


def quad(x):
    return double(double(x))


def hello(name):
    print("Hello,", name + "! How are you today?")


def repeat(string, n):
    return string * n


def square(string, n):
    for i in range(n):
        print(repeat(string, n))


print(double(5))
print(quad(4))
hello("Joe")
print(repeat("hi", 10))
square("*", 4)
