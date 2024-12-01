# Sergei Chaparin
# Create a program that reads in each line of the file, and prints "Hello, ..."

filename = "hello.txt"

fh = open(filename, "r")  # file handle

for line in fh:
    print("Hello, " + line.rstrip("\n"))

fh.close()  # You want to close a file if you created a variable for it. Otherwise, you'll run out of handles.
# for line in fh:
#     print(line.rstrip(), end=" ")
for line in open("hello.txt"):
    print("Hello, " + line.rstrip() + "!")
