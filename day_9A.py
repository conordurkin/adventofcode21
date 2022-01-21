# Fun one - working with dataframe math to get local minimums

import pandas as pd
import numpy as np

# Took some work to make the data look nice - a 100x100 grid, one digit per cell, indexed 0 to 99 both ways
data = pd.read_csv('data/day9.csv', header = None)
data = data[0].astype('str').str.split('', expand = True)
data = data.apply(pd.to_numeric)
data = data.drop([0, 101], axis = 1)
data.columns = np.arange(100)

# Function to find local mins. Pass a series of integers, checks if a given cell is lower than before/after
# Note: I need the Try/Except for the edges. If you are in the first cell, you can't check the last one
# because there is no last one. So then you just check the next one. Vice versa for the final cell.
# This returns a series of 0s and 1s equal in length to the input series.
def local_min_finder(series):
    series_tracker = []
    for i in range(len(series)):
        try:
            if series[i] < series[i-1]:
                try:
                    if series[i] < series[i+1]:
                        out = 1
                    else:
                        out = 0
                except:
                    out = 1
            else:
                out = 0
        except:
            if series[i] < series[i+1]:
                out = 1
            else:
                out = 0
        series_tracker.append(out)
    return series_tracker

# Apply the local_min_finder to the 100x100 twice - once columnwise and once rowwise.
# This gives us local min based on row and based on column and returns two 100x100 grids of 1s and 0s.
# Then multiply both grids together to get local min by both column AND row.
row_minimums = data.apply(local_min_finder, axis = 1, result_type = 'expand')
column_minimums = data.apply(local_min_finder, axis = 0, result_type = 'expand')
local_minimum = row_minimums * column_minimums

# Create a new grid with risk level for each box (Height + 1), and multiply that grid by the local_minimums.
risk_level_all = data + 1
risk_level_minimums = risk_level_all * local_minimum

# Return the sum of the entire grid.
print(risk_level_minimums.sum().sum())
