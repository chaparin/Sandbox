# Sergei Chaparin
# Wrote myself entirely from scratch, except had to get Gemini help with the 'end' parameter

def while_loops(n):
    while n < 6:
        print(n)
        n += 1
    print('------------------')


def while_by_three(n):
    while n < 12:
        print(n)
        n += 3
    print('------------------')


def while_in_line_six(n):
    while n < 1:
        # n = '' #builder/accumulator
        print(n, end=' ')
        n += 2
    print('\n------------------')


def while_four_stars(n):
    while n < 5:
        print('****')
        n += 1
    print('------------------')


def main():
    while_loops(1)
    while_by_three(2)
    while_in_line_six(-10)
    while_four_stars(1)


main()
