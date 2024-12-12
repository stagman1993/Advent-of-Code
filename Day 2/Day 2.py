from pickle import FALSE

import pandas as pd
import numpy as np

file = "Day 2 input.txt"

def parse_file(filename):
    count = 0
    with open(filename) as f:
        for line in f:
            raw_list = line.split()
            int_list = []
            for i in raw_list:
                value = int(i)
                int_list.append(value)

            test = check_reactor(int_list)
            if test == True:
                count += 1
        print(count)

def check_reactor(report: list):
    reactor_safe = False
    np_report = np.array(report)
    diff = np.diff(np_report)
    if np.all((diff > 0) & (diff <= 3)) or np.all((diff >= -3) & (diff < 0)):
        reactor_safe = True
    else:
        for i in range(len(np_report)):
            new_report = report[:i] + report[i +1 :]
            diff = np.diff(new_report)
            if np.all((diff > 0) & (diff <= 3)) or np.all((diff >= -3) & (diff < 0)):
                reactor_safe = True

    return reactor_safe



test_1 = [7, 6, 4, 2, 1]
test_2 = [1, 2, 7, 8, 9]
test_3 = [9, 7, 6, 2, 1]
test_4 = [1, 3, 2, 4, 5]
test_5 = [8, 6, 4, 4, 1]
test_6 = [1, 3, 6, 7, 9]

list_of_test = [test_1, test_2, test_3, test_4, test_5, test_6]

parse_file(file)
