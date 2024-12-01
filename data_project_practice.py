# Sergei Chaparin
# Data Project Practice
import statistics
import pandas as pd  # use of pandas
from tabulate import tabulate  # use of tabulate
import matplotlib.pyplot as plt
import seaborn as sns


def data_presentation_tabulate(spring_list, fall_list):
    data = [
        ["Mean", round(statistics.mean(spring_list), 2), round(statistics.mean(fall_list), 2)],
        ["Median", statistics.median(spring_list), statistics.median(fall_list)],
        ["Standard Deviation", round(statistics.stdev(spring_list), 2), round(statistics.stdev(fall_list), 2)]
    ]
    print(tabulate(data, headers=["2016", "Spring", "Fall"], tablefmt="grid"))


def data_presentation_pandas(spring_list, fall_list):
    data = {
        "Spring": [round(statistics.mean(spring_list), 2),
                   statistics.median(spring_list),
                   round(statistics.stdev(spring_list), 2)],
        "Fall": [round(statistics.mean(fall_list), 2),
                 statistics.median(fall_list),
                 round(statistics.stdev(fall_list), 2)]
    }
    df = pd.DataFrame(data, index=["Mean", "Median", "Standard Deviation"])
    print(df)


def data_presentation_matplotlib_seaborn(spring_list, fall_list):
    data = {
        "Semester": ["Spring", "Fall"],
        "Mean": [statistics.mean(spring_list), statistics.mean(fall_list)],
        "Median": [statistics.median(spring_list), statistics.median(fall_list)],
        "Standard Deviation": [statistics.stdev(spring_list), statistics.stdev(fall_list)]
    }
    plt.figure(figsize=(5, 6))
    sns.barplot(x="Semester", y="Mean", data=data)
    plt.title("Comparison of Mean Grades")
    plt.show()


# Read in the file:
file = "sample_grades.csv"

open_file = open(file, "r")

spring = []
fall = []

for line in open_file:
    list1 = line.rstrip().split(",")
    if list1[1] == 'Spring 2016':
        spring.append(eval(list1[2]))
    else:
        fall.append(eval(list1[2]))

open_file.close()

data_presentation_tabulate(spring, fall)
data_presentation_pandas(spring, fall)
data_presentation_matplotlib_seaborn(spring, fall)
