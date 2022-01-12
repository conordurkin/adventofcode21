import pandas as pd
import numpy as np

data = pd.read_csv('data/day3.csv', header = None, dtype = 'str')
data.columns = ['inputs']

individual = data['inputs'].str.split('', expand = True)
individual = individual.iloc[:, 1:-1]
individual = individual.apply(pd.to_numeric)

oxygen_data = individual.copy()
oxygen = 0
for i in range(1, 13):
    if len(oxygen_data) == 1:
        break
    elif len(oxygen_data) == 2:
        oxygen_data = oxygen_data.loc[oxygen_data[i] == 1]
    else:
        oxygen_data = oxygen_data.loc[oxygen_data[i] == round(oxygen_data[i].mean())]
for i in range(1,13):
    oxygen += (oxygen_data[i] * (2 ** (12-i)))
oxygen = oxygen.values[0]


co_data = individual.copy()
co = 0
for i in range(1, 13):
    if len(co_data) == 1:
        break
    elif len(co_data) == 2:
        if co_data[i].mean() == 1:
            pass
        else:
            co_data = co_data.loc[co_data[i] == 0]
    else:
        if co_data[i].mean() == 0.5:
            co_data = co_data.loc[co_data[i] == 0]
        else:
            co_data = co_data.loc[co_data[i] == (1 - round(co_data[i].mean()))]
for i in range(1,13):
    co += (co_data[i] * (2 ** (12-i)))
co = co.values[0]

print(co * oxygen)
