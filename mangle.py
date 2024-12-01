# Sergei Chaparin
# Write a function mangle that takes a string as a parameter and returns the
# string after performing the following operations:
# i. Converting the string to all upper case letters
# ii. Removing the third character
# iii. Removing the third to last character
# Test that your function works.

def mangle(string):
    string = string.upper()  # 2.i Converting the string to all upper case letters
    string = string[0:2] + string[3:-3] + string[-2:]
    return string


def main():
    print(mangle("Hellothere"))
    test_input = ["hellothere", "42 degrees Celsius", "eeeeeee"]
    test_output = ["HELOTHRE", "42DEGREES CELSUS", "EEEEE"]
    for i in range(len(test_input)):
        print("Mangle", test_input[i] + ":", mangle(test_input[i]) == test_output[i])


main()
