# This has to do with "Graphs" and paths between nodes - I've never done this before!
# I again borrowed code from this guy who knows more than me: https://github.com/mebeim/aoc/tree/master/2021#day-12---passage-pathing

# Good way to learn the basic idea! You start at Start, try every path, and record


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
def find_all_paths_with_return(mapping, src, dst):
    stack = deque([(src, {src}, False)])
    total = 0
    while stack:
        node, visited, double = stack.pop()
        if node == dst:
            total += 1
            continue

        for n in mapping[node]:
            if n not in visited or n.isupper():
                stack.append((n, visited | {n}, double))
                continue

            if double:  #This means "If True"
                continue

            stack.append((n, visited, True))
    return total

# This solves it
print(find_all_paths_with_return(nodes, 'start', 'end'))
