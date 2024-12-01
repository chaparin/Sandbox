from math import sqrt

enteredNumber = eval(input("Please enter a number: "))
# number_int = int(enteredNumber)
print("The absolute value of the entered number is: ", abs(enteredNumber))
print("The number rounded to 0 decimal places: ", round(enteredNumber, 0))
print("The square root of the rounded number is: ", sqrt(abs(round(enteredNumber, 0))))
