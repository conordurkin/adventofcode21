import pandas as pd
import numpy as np
pd.options.mode.chained_assignment = None  # default='warn'

data = pd.read_csv('data/day4.csv', header = None)

# I hate the way this code looks, but it seems like the easiest way to read in the numbers and the boards given how the input file is set up.
bingo_numbers = data.iloc[0]
bingo_numbers = [int(i) for i in bingo_numbers]

boards = data[0][1:].str.split(expand = True)
boards = boards.apply(pd.to_numeric)

# convert the bingo inputs from one long entry into individual 5x5 boards.
boardlist = []
for i in (range(int(len(boards)/5))):
    boardlist.append(boards[((i+1)*5 - 5):((i+1)*5)])


# Read bingo numbers one by one. Mark them off each board.
# When any board wins (if the column or row sum to -5000), call it the winner. 
# Print off the winning board and the score.
for number in bingo_numbers:

    for board in boardlist:
        board.replace(number, -1000, inplace = True)

        for entry in range(5):
            if board.iloc[entry].sum() == -5000:
                # print("We have a winner horizontally!")
                # print("The last bingo number is: " + str(number))
                board.replace(-1000, 0, inplace = True)
                score = board.sum().sum() * number
                print("The score of the winning board is: " + str(score))
                # print(board)
                break

            elif board[entry].sum() == -5000:
                # print("We have a winner vertically!")
                # print("The last bingo number is: " + str(number))
                board.replace(-1000, 0, inplace = True)
                score = board.sum().sum() * number
                print("The score of the winning board is: " + str(score))
                # print(board)
                break

            else:
                continue
        else:
            continue
        break
    else:
        continue
    break
