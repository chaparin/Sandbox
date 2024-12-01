# Module 3 - Problem 3
# Sergei Chaparin
summ = 0  # aggregator variables must be initialized before the loop
for i in range(10):
    num = float(input("Enter a real number: "))
    summ += num

print("Average is ", summ / 10)
