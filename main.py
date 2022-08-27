import numpy as np
import pandas as pd

df = pd.read_csv("lies.csv", delimiter='\t')


def is_correct_row(row):
    if row:
        if len(row)!=5:
            return False
        if not(row['CLIENT_ID'].is_digit() and row['RETRO_DT'].is_digit() and row['DEF'].is_digit()):
            return False
        if not all(row):
            return False
        return True
    else:
        return False


count = 0
for index, row in enumerate(df.itertuples()):
    if not is_correct_row(row):
        df.drop(index)
        count += 1

print(count)