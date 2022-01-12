import pandas as pd
import numpy as np
pd.options.mode.chained_assignment = None  # default='warn'

data = pd.read_csv('data/day4.csv', header = None)

# I hate the way this code looks, but it seems like the easiest way to read in the numbers and the boards given how the input file is set up.
bingo_numbers = data.iloc[0]
bingo_numbers = [int(i) for i in bingo_numbers]

boards = data[0][1:].str.split(expand = True)
boards = boards.apply(pd.to_numeric)

boardlist = []
for i in (range(int(len(boards)/5))):
    boardlist.append(boards[((i+1)*5 - 5):((i+1)*5)])

lastboard = []

for i in range(len(boardlist)):
    board_number = i
    board = boardlist[i]
    for j in range(len(bingo_numbers)):
        number = bingo_numbers[j]
        board.replace(number, -1000, inplace = True)

        for entry in range(5):
            if board.iloc[entry].sum() == -5000:
                board.replace(-1000, 0, inplace = True)
                score = board.sum().sum() * number
                lastboard.append([board_number, j, number, score])
                break

            elif board[entry].sum() == -5000:
                board.replace(-1000, 0, inplace = True)
                score = board.sum().sum() * number
                lastboard.append([board_number, j, number, score])
                break

            else:
                pass

df = pd.DataFrame(lastboard)
df.columns = ['board_number', 'iteration', 'last_bingo_number', 'score']
df = df.drop_duplicates('board_number')
score = df.loc[df.iteration == df.iteration.max()].reset_index().score[0]

print(score)
