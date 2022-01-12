import pandas as pd
import numpy as np

data = pd.read_csv('data/day1.csv', header = None)
data.columns = ['Day']

three_day = []
new_counter = 0

for i in range(1998):
    three_day.append(data.Day[i] + data.Day[i+1] + data.Day[i+2])

for i in range(1997):
    if three_day[i] < three_day[i+1]:
        new_counter += 1
    else:
        pass

print(new_counter)
