# Sergei Chaparin
# Write a function average_neg_evens that takes a list of numbers as a parameter,
# and adds all the negative even numbers (less than 0 and divisible by 2) together and returns their average.

def average_neg_evens(source_list):
    accumulator = 0
    count = 0
    # for num in source_list:
    i = 0  # initializing the loop index variable
    while i < len(source_list):  # loop condition
        num = source_list[i]  # how we go from index -> value in list
        if num % 2 == 0 and num < 0:
            accumulator += num
            count += 1
        i += 1  # loop variable increment
    return accumulator / count  # avg


def main():
    print(average_neg_evens([0, 1, 2, -2, -3, -4, 3, 4]))
    print(average_neg_evens([-6, 1, 2, -2, -3, -4, 3, 4, -4, -88, -34, -6]))


main()
