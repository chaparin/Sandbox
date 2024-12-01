# Sergei Chaparin
# Used Gemini to help, but I still don't understand why a negative exponent should produce zero in the assignment,
# rather than a fractional value.
# Write a function there that takes a number n as a parameter, and returns 2n if
# n is positive, and 0 otherwise. Your function should output the following for the
# given calls:
# there_1 is a rudimentary implementation of the problem
def there_1(base, exp):
    result = 1
    for i in range(exp):
        result *= base
    return result


def there_2(base, exp):
    return base ** exp


def there_3(exp):
    if exp <= 0:
        return 0
    return 2 ** exp


def main():
    print(there_1(2, 5))
    print(there_1(2, 0))
    print(there_1(2, 3))
    print(there_1(2, -2))
    print(there_1(2, -6))
    print(there_2(2, 5))
    print(there_2(2, 0))
    print(there_2(2, 3))
    print(there_2(2, -2))
    print(there_2(2, -6))
    print(there_3(5))
    print(there_3(0))
    print(there_3(3))
    print(there_3(-2))
    print(there_3(-6))


main()
