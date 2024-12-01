# Sergei Chaparin
# Write a function count_letter that takes a list of strings and a string letter as parameters and returns the number
# of times this letter occurs, both upper- & lower-cased.

def count_letter(list, letter):
    count = 0
    letter = letter.lower()
    # for string in list:
    i = 0
    while i < len(list):
        string = list[i]
        count += string.lower().count(letter)
        i += 1
    return count


def main():
    list = ['HELLO', 'goodbye', '1234 Oooh!']
    print(count_letter(list, "o"))


main()
