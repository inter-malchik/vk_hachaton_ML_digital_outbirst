from classes import *


f_false = open("train_DEF_0.csv", 'w')
f_true = open("train_DEF_1.csv", 'w')

begin = open("train.csv").readline()
f_false.write(begin)
f_true.write(begin)

for row_text, DLine in dataset_parser_iterator("train.csv"):
    if DLine.DEF == 1:
        f_true.write(row_text)
    else:
        f_false.write(row_text)

f_false.close()
f_true.close()