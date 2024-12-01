# Sergei Chaparin
# Optional JoC sum 1 to N recursion
N = 0


def sum1(N):
    if N <= 1:
        return 1
    else:
        return N + sum1(N - 1)


print('Your N recursive sum equals: ', sum1(20))
