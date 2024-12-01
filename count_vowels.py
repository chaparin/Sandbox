# Sergei Chaparin
# Needed a little leg up from Gemini, as I was missing the inner for loop.

def count_vowels(strings):
    char_count = 0
    vowels = ['a', 'e', 'i', 'o', 'u']
    for string in strings:  # Iterate over each string in the list
        for char in string.lower():  # Iterate over each character in the lowercase string
            if char in vowels:
                char_count += 1  # Increment the count if the character is a vowel
    return char_count


print(count_vowels(['desk', 'Echo', 'vendor', 'I', 'be', 'quiet', 'please', 'circle']))
