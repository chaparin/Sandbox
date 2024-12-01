# Sergei Chaparin
# Write a program that creates a list of 20 numbers input by the user and prints
# the average (mean) of the list.

import statistics

numbers = []
for i in range(20):
    numbers.append(eval(input("Enter a number: ")))
print(numbers)
print(statistics.mean(numbers))
