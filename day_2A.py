import pandas as pd
import numpy as np

data = pd.read_csv('data/day2.csv', header = None)
data.columns = ['command']
data = data['command'].str.split(expand = True)

data.columns = ['command', 'amount']
data.amount = data.amount.astype('int')

summary = data.groupby('command').agg({'amount': 'sum'})

depth = summary.loc['down'].amount - summary.loc['up'].amount

horizontal = summary.loc['forward'].amount

print(horizontal * depth)
