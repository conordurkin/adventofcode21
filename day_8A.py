import pandas as pd
import numpy as np

data = pd.read_csv('data/day8.csv', header = None, sep = " ")
output = data[[11, 12, 13, 14]]   # Limit to only the 'output columns'

# Now make one long list of those four columns
output_list = []
for column in output.columns:
    output_list.append(output[column])
flat_list = [item for sublist in output_list for item in sublist]

# Turn the strings into integers representing string length
lengths = [len(entry) for entry in flat_list]

# Get a count of each string length, and keep the lengths associated with 1, 4, 7, 8
# Please note that those are string of length 2, 4, 3, and 7, respectively.
summary = pd.Series(lengths).value_counts()
uniques = summary.loc[2] + summary.loc[4] + summary.loc[3] + summary.loc[7]

print(uniques)
