# Some of this code is a bit ugly but it works.
# Lot of functions and got to use a "return two things" here which is new-ish for me.

import pandas as pd
import numpy as np
import itertools

# Clean the data into a 10x10 matrix
data = pd.read_csv('data/day11.csv', header = None)
data = data[0].astype('str').str.split('', expand = True)
data = data.apply(pd.to_numeric)
data = data.drop([0, 11], axis = 1)
data.columns = np.arange(10)



# I don't like how this looks with the Try/Excepts, but it is what it is.
# Basically I need that to deal with literal 'edge' cases - where the cell is the edge of the matrix.
def flash_surrounding(x, y, df):
    def flash_cell(cell):
        if cell == 0:
            pass
        else:
            cell += 1
        return cell
    try:
        df[x-1][y-1] = flash_cell(df[x-1][y-1])
    except:
        pass
    try:
        df[x][y-1] = flash_cell(df[x][y-1])
    except:
        pass
    try:
        df[x+1][y-1] = flash_cell(df[x+1][y-1])
    except:
        pass
    try:
        df[x-1][y] = flash_cell(df[x-1][y])
    except:
        pass
    try:
        df[x+1][y] = flash_cell(df[x+1][y])
    except:
        pass
    try:
        df[x-1][y+1] = flash_cell(df[x-1][y+1])
    except:
        pass
    try:
        df[x][y+1] = flash_cell(df[x][y+1])
    except:
        pass
    try:
        df[x+1][y+1] = flash_cell(df[x+1][y+1])
    except:
        pass
    return df


# Now go through the matrix, cell by cell, and flash when appropriate.
# Only stop going through the matrix when there are no 'New Flashes' in a given loop.
# Return both the New DF and the total flashes in that loop.
def flash_step(df):
    height = len(df)
    width = len(df[0])
    df_step = df + 1
    total_flashes = 0
    new_flashes = 1 # Arbitrarily set this to 1 to make the 'While' work
    while new_flashes > 0:
        flashes_on_this_loop = 0
        for x,y in itertools.product(range(height), range(width)):
            new_flashes = 0
            if df_step[x][y] > 9:
                df_step = flash_surrounding(x, y, df_step)
                df_step[x][y] = 0
                flashes_on_this_loop += 1
            else:
                continue
        new_flashes = flashes_on_this_loop
        total_flashes += flashes_on_this_loop

    return df_step, total_flashes

# The Flash_Step function runs one Step. This Runs as many steps as you want.
# It returns two things - the final DF AND the total flash count.
def flash_loop(df, steps):
    running_flash_count = 0
    for i in range(1, steps + 1):
        df, flashes = flash_step(df)
        running_flash_count += flashes
    return df, running_flash_count

# Now we run the data for 100 steps and see the total flash count. Voila! 
print(flash_loop(data, 100)[1])
