# Transparency: This takes a couple functions from here:
# https://github.com/CJX3M/AdventOfCode/blob/2cacc6117d4e27d1b6f08f93a73814f249e35bf5/2021/day9.py

# I got stuck on this one. Idea is to start at low points, check surrounding cells to see if they're in the basin.
# If yes -> add to "size" and zero them out. If no -> zero them out and continue searching.

import pandas as pd
import numpy as np

# Took some work to make the data look nice - a 100x100 grid, one digit per cell, indexed 0 to 99 both ways
data = pd.read_csv('data/day9.csv', header = None)
data = data[0].astype('str').str.split('', expand = True)
data = data.apply(pd.to_numeric)
data = data.drop([0, 101], axis = 1)
data.columns = np.arange(100)

# Get a list of the low points to start basin-searching at.
low_points = []
for i in range(len(risk_level_minimums)):
    for j in range(len(risk_level_minimums[i])):
        if risk_level_minimums[i][j] == 0:
            pass
        else:
            low_points.append([i, j])


# This function checks a given point to see how large its basin is (recursive - checks surrounding points too, etc)
def checkPoint(x, y, matrix):
    size = 0
    rightBound = len(matrix[0])
    bottomBound = len(matrix)
    if matrix[x][y] == '.' or matrix[x][y] == 9:
        return size
    matrix[x][y] = '.'
    size += 1
    if y+1 < rightBound:
        size += checkPoint(x, y+1, matrix)
    if y-1 >= 0:
        size += checkPoint(x, y-1, matrix)
    if x+1 < bottomBound:
        size += checkPoint(x+1, y, matrix)
    if x-1 >= 0:
        size += checkPoint(x-1, y, matrix)
    return size

# This maps the basins based on the lowest points
def findBasin(lowest, matrix):
    sizes = []
    for low in lowest:
        sizes.append(checkPoint(low[0], low[1], matrix))
    return sizes

# Now we run the actual functions and get largest basins
sizes = sorted(findBasin(low_points, data))[::-1]

# And we multiply the top 3
print(sizes[0]*sizes[1]*sizes[2])
