import pandas as pd
import numpy as np

data = pd.read_csv('data/day2.csv', header = None)
data.columns = ['command']
data = data['command'].str.split(expand = True)

data.columns = ['command', 'amount']
data.amount = data.amount.astype('int')

aim = 0
horizontal = 0
vertical = 0

for i in range(len(data)):
    instruction = data.iloc[i]

    if instruction.command == 'forward':
        horizontal += instruction.amount
        vertical += (instruction.amount * aim)

    elif instruction.command == 'down':
        aim += instruction.amount

    elif instruction.command == 'up':
        aim -= instruction.amount

    else:
        pass

print(horizontal * vertical)
