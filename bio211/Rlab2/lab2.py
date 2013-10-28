import matplotlib.pyplot as plt
import numpy as np
import pprint as pp

import csv
from data import raw_ph_data, raw_temp_data, raw_con_data

high = lambda x: x/4 + x  # 1/4th of the max plus the max
low = lambda x: x/2  # Choose value half way between value and 0


def normalize(raw_data):
    """
    Go through data and parse a number value.
        If there was a '>' in the raw value, apply high().
        If there was a '<' in the value apply low().
    """
    numeric_data = {}
    for cond, values in raw_data.iteritems():
        numeric_values = []
        for raw_value in values:
            if '>' in raw_value:
                num = high(float(raw_value.replace('>', '')))
            elif '<' in raw_value:
                num = low(float(raw_value.replace('<', '')))
            else:
                num = float(raw_value)
            numeric_values.append(num)
        numeric_data[cond] = numeric_values
    return numeric_data


def avg(l):
    return sum(l) / float(len(l))


def average_data(data):
    """
    Each list is the data of all the groups. Take the average of the all of
    each group's data.
    """
    average_data = {}
    for cond, values in data.iteritems():
        average_data[cond] = avg(values)
    return average_data


avg_ph_data = average_data(normalize(raw_ph_data))
avg_temp_data = average_data(normalize(raw_temp_data))
avg_con_data = average_data(normalize(raw_con_data))


def gen_csv(file_name, raw_data):
    with open(file_name, 'w+') as fd:
        csvfile = csv.writer(fd)
        data = normalize(raw_data)
        keys = sorted(data.keys())
        csvfile.writerow(keys)
        stop = False
        while True:
            row = []
            for key in sorted(keys):
                if not data[key]:
                    stop = True
                    break
                row.append(data[key].pop())

            csvfile.writerow(row)
            if stop:
                break


def print_files():
    gen_csv('ph_data.csv', raw_ph_data)
    gen_csv('temperature_data.csv', raw_temp_data)
    gen_csv('consentration_data.csv', raw_con_data)

if __name__ == '__main__':
    print_files()
