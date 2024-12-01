def count_e(strings):
    char_count = 0
    for char in strings:
        char_count += char.upper().count("E")
    return char_count


print(count_e(["desk", "Echo", "vendor"]))
