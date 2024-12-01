# Module 3 Learning Exercise
# Sergei Chaparin

# 1
for i in range(10, 26, 5):
    print(i, end=" ")
print()
# 2
for i in range(-3, 22, 3):
    if i == 21:
        print(i, end="")
    else:
        print(i, end=", ")
print()
# 2 Version 2
for i in range(-3, 21, 3):
    print(i, end=", ")
print(21)
