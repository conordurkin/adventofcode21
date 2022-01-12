import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings("ignore") # otherwise your output gives you a warning about the parser using "->" as a sep

data = pd.read_csv('data/day5.csv', header = None, sep = "->")

starts = data[0].str.split(',', expand = True)
ends = data[1].str.split(',', expand = True)
combo = pd.concat([starts, ends], axis = 1)
combo.columns = ['start_x', 'start_y', 'end_x', 'end_y']
combo = combo.apply(pd.to_numeric)


# If it's vertical or horizontal, the loops are same as before.
# If diagonal, this iterates by (1,1) every time instead of (1,0) or (0,1)
# I'm not wild about the aesthetics but it gets the job done.

points = []

for row in range(len(combo)):
    entry = combo.loc[row]

    if entry.start_x == entry.end_x:

        if entry.start_y < entry.end_y:
            for i in range(entry.start_y, (entry.end_y+1), 1):
                points.append((entry.start_x, i))

        else:
            for i in range(entry.start_y, (entry.end_y-1), -1):
                points.append((entry.start_x, i))

    elif entry.start_y == entry.end_y:

        if entry.start_x < entry.end_x:
            for i in range(entry.start_x, (entry.end_x+1), 1):
                points.append((i, entry.start_y))

        else:
            for i in range(entry.start_x, (entry.end_x-1), -1):
                points.append((i, entry.start_y))

    else:
        if entry.start_x < entry.end_x:
            if entry.start_y < entry.end_y:
                for i in range((1 + entry.end_x - entry.start_x)):
                    points.append((entry.start_x + i, entry.start_y + i))

            else:
                for i in range((1 + entry.end_x - entry.start_x)):
                    points.append((entry.start_x + i, entry.start_y - i))

        else:
            if entry.start_y < entry.end_y:
                for i in range((1 + entry.start_x - entry.end_x)):
                    points.append((entry.end_x + i, entry.end_y - i))

            else:
                for i in range((1 + entry.start_x - entry.end_x)):
                    points.append((entry.end_x + i, entry.end_y + i))


points_series = pd.Series(points)
summary = pd.DataFrame(points_series.value_counts())
print(len(summary.loc[summary[0] > 1]))
