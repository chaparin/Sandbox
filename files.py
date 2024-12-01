# Sergei Chaparin
# Practice with files and dictionaries
# Count the number of letter grades in a file using a dictionary

letters = ["A", "B", "C", "D", "F"]

counts = {}  # initializing a dictionary

file = "letter_grades.txt"

# loop through all lines in the file

for line in open(file):
    letter = line.replace("\n", "")
    # if commas are used, use split function
    # print(line)
    # gets a count of letter if it exists, 0 otherwise
    counts.get(letter, 0)
    counts[letter] = counts.get(letter, 0) + 1  # store count

# Print out counts
print("Letter counts: ")
for l in letters:
    print(l + ":", counts.get(l, 0))

# Print Dictionary
print("file grade counts: ")
for item in counts.keys():
    print(item, counts.get(item))