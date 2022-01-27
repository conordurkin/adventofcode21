# Syntax Scoring - this one was pretty fun too.
# Basic approach: Find only the incomplete rows. Find the 'ends' to those rows.
# Score those ends, then find the median.

import pandas as pd
data = pd.read_csv('data/day10.csv', header = None)

# First, reduce the rows (eliminate complete chunks), then keep only incomplete rows.
def reduce_row(row):
    i = 1
    while i == 1:
        if row.find('()') != -1:
            row = row.replace('()','')
        elif row.find('[]') != -1:
            row = row.replace('[]', '')
        elif row.find('<>') != -1:
            row = row.replace('<>', '')
        elif row.find('{}') != -1:
            row = row.replace('{}', '')
        else:
            i = 0
    return row

def incomplete_flag(row):
    bad_paren = row.find(')')
    bad_brack = row.find(']')
    bad_brace = row.find('}')
    bad_arrow = row.find('>')
    bad_list = [bad_paren, bad_brack, bad_brace, bad_arrow]
    if sum(bad_list) == -4:
        out = 1
    else:
        out = 0
    return out

data_reduced = pd.DataFrame(data[0].apply(reduce_row))
data_reduced['incomplete'] = data_reduced[0].apply(incomplete_flag)
data_reduced = data_reduced.loc[data_reduced.incomplete == 1].drop('incomplete', axis = 1).reset_index(drop = True)
data_reduced.columns = ['input']


# Dictionary to map the characters to their scores. Cleaner than a for loop.
character_scores = {')': 1,
                    ']': 2,
                    '}': 3,
                    '>': 4}


# Function to return a list of the 'completing characters' in proper order.
def series_completer(input_series):
    output = []
    for character in reversed(input_series):
        if character == '(':
            output.append(')')
        elif character == '{':
            output.append('}')
        elif character == '[':
            output.append(']')
        elif character == '<':
            output.append('>')
        else:
            pass
    return output


# Function to calculate the score for a given list of completing characters.
def score_calculator(completer_list):
    completer_list_scored = [character_scores.get(character) for character in completer_list]
    score = 0
    for value in completer_list_scored:
        score = score * 5
        score += value
    return score


# Function combining the two above to return the proper score for a given input row.
def score_from_data(input):
    series_completer_output = series_completer(input)
    final_score = score_calculator(series_completer_output)
    return final_score


# Now get my column of scores and return the median (rounded to remove a decimal ".0")
data_scored = data_reduced['input'].apply(score_from_data)
print(round(data_scored.median()))
