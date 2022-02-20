# Day 13B - gotta find some capital letters
# Playing around with arrays/matrices and flipping them across some axis.
# The final output requires slightly more work than normal - rather than a copy/paste
# To the 'submit answer here' field, you have to interpret the output and type in the answer.

import pandas as pd
import numpy as np

pd.options.mode.chained_assignment = None  # default='warn'
pd.set_option('display.max_columns', None)

# Load in data file, split the coordinates part out from the folds part
data = pd.read_csv('data/day13.csv', header = None)
coordinates = data.loc[0:1003]
coordinates.columns = ['x', 'y']
coordinates['x'] = pd.to_numeric(coordinates['x'])
folds = data.loc[1004:][0].reset_index(drop = True)

# Clean up the folds part
folds_parsed = folds.str.replace('fold along ', '')
folds_parsed = folds_parsed.str.split('=', expand = True)
folds_parsed.columns = ['dimension', 'line']
folds_parsed['line'] = pd.to_numeric(folds_parsed['line'])

# Okay, set up a giant grid of zeros - how big? 2x the biggest folds needed.
grid_width = 2 * folds_parsed.groupby('dimension').max().loc['x']['line'] + 1
grid_length = 2 * folds_parsed.groupby('dimension').max().loc['y']['line'] + 1
grid = np.zeros([grid_length, grid_width])

# Replace the 0s with 1s based on the starting coordinates
for i in range(len(coordinates)):
    x = coordinates.iloc[i]['x'].astype('int')
    y = coordinates.iloc[i]['y'].astype('int')
    grid[y][x] = 1

# Function to perform a 'fold' and then combine the resulting grids.
def fold(input_grid, fold_axis, fold_line):
    if fold_axis == 'x':
        new_grid = input_grid[:, :fold_line]
        extra_grid = np.flipud(np.flip(input_grid[:, (fold_line+1):]))
        output_grid = new_grid + extra_grid

    elif fold_axis == 'y':
        new_grid = input_grid[:fold_line, :]
        extra_grid = np.flipud(input_grid[(fold_line+1):, ])
        output_grid = new_grid + extra_grid

    return output_grid

# Function to perform multiple folds, inputting the output grid of one fold as the input of the next.
def fold_loop(start_grid, list_of_folds):
    grid_list = list()
    grid_list.append(start_grid)

    for i in range(len(list_of_folds)):
        grid_list.append(fold(grid_list.pop(), list_of_folds.iloc[i]['dimension'], list_of_folds.iloc[i]['line']))

    return grid_list.pop()

final_output = fold_loop(grid, folds_parsed)

# Let's clean up the visual - make it a DF instead of Array,
# replace zeros with blanks and replace non-zeros with a black square (easier to interpret)
visual = pd.DataFrame(np.where(final_output > 0, u"\u2588", ''))

# Print out the final visual 'paper' - hopefully you can interpret letters! 
print(visual)
