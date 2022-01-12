import pandas as pd
import numpy as np

data = pd.read_csv('data/day3.csv', header = None, dtype = 'str')
data.columns = ['inputs']

# Split the binary code into individual columns so I can go column by column and find the right ones.
individual = data['inputs'].str.split('', expand = True)
individual = individual.iloc[:, 1:-1]
individual = individual.apply(pd.to_numeric)

gamma_data = individual.mean().round()
gamma = 0
for i in range(1,13):
    gamma += (gamma_data[i] * (2 ** (12-i)))  # This is a clever(ish? maybe?) way of converting from binary into base-10

epsilon_data = 1- individual.mean().round()
epsilon = 0
for i in range(1,13):
    epsilon += (epsilon_data[i] * (2 ** (12-i)))

print(gamma * epsilon)
