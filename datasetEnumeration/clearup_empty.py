from classes import *

f_false = open("train_shit.csv", 'w')
f_true = open("train_clear.csv", 'w')

begin = open("train.csv").readline()
f_false.write(begin)
f_true.write(begin)

for row_text, DLine in dataset_parser_iterator("train.csv"):
    if DLine.urls_hashed.keys() and DLine.tokens.keys():
        f_true.write(row_text)
    else:
        f_false.write(row_text)

f_false.close()
f_true.close()