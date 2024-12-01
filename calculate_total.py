# Sergei Chaparin
# Write a function calculate_total that takes 3 parameters:
#   a. meal: the cost of the meal
#   b. tax_rate: the percent tax (e.g., NJ tax would be 0.07)
#   c. tip_rate: the percent tip (e.g., a 20% tip rate is 0.20)

def calculate_total(meal):
    total = meal + (meal * 0.18) + (meal * 0.07)
    return total


def main():
    print(calculate_total(53.48))


main()
