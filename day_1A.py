import pandas as pd
import numpy as np

data = pd.read_csv('data/day1.csv', header = None)
data.columns = ['Day']

counter = 0

for i in range(1999):
    if data.Day[i] < data.Day[i+1]:
        counter +=1
    else:
        pass

print(counter)
