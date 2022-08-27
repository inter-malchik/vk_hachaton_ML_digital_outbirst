import numpy as np
import pandas as pd

from utils import *

df = pd.read_csv("lies.csv", delimiter='\t')

# clear df
count = 0
for index, row in enumerate(df.itertuples()):
    if not is_correct_row(row):
        df.drop(index)
        count += 1
    else:
        ClientParser


print(count)