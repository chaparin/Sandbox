# Sergei Chaparin
# Write a function are_we that takes a number of times to repeat and a phrase to
# be repeated as parameters and outputs the following for the given calls:

def are_we(number, insert):
    string = number * ("Are we " + insert + " yet? ")
    return string


def main():
    print(are_we(2, "there"))
    print(are_we(3, "50"))
    print(are_we(1, ""))
    print(are_we(0, "hey!"))


main()
