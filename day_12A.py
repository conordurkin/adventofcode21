# This has to do with "Graphs" and paths between nodes - I've never done this before!
# Given that, I had to explore some guides on how to deal with this, and ended up borrowing
# code from here, for the most part: https://github.com/mebeim/aoc/tree/master/2021#day-12---passage-pathing

# Basic idea is to create a dictionary of each Node and its neighbors, and then find all paths from start/end

import pandas as pd
import numpy as np
from collections import defaultdict, deque

data = pd.read_csv('data/day12.csv', header = None)
data_series = data[0]

# This givs me a list of nodes mapped to their neighbors in a dictionary
nodes = defaultdict(list)
for entry in data_series:
    i,j = entry.split('-')
    if j != 'start':
        nodes[i].append(j)
    if i != 'start':
        nodes[j].append(i)

# This finds all valid paths from src to dst
def find_all_paths(mapping, src, dst):
    stack = deque([(src, {src})])
    total = 0
    while stack:
        node, visited = stack.pop()
        if node == dst:
            total += 1
            continue

        for n in mapping[node]:
            if n in visited and n.islower():
                continue

            stack.append((n, visited | {n}))
    return total

# This solves it
print(find_all_paths(nodes, 'start', 'end'))
