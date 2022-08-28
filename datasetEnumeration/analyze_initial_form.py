from datasetEnumeration.classes import *
import pymorphy2
from transliterate import translit

morph = pymorphy2.MorphAnalyzer(lang='ru')

def get_normal_form(word):
    return morph.parse(translit(word, 'ru'))[0].normal_form

counter_all_items = dict() # сумма тайтлов за все время

for row_text, DLine in dataset_parser_iterator("train_clear.csv"):
    for item in DLine.tokens.items():
        key = get_normal_form(item[0])
        counter_all_items[key] = counter_all_items.get(item[0], 0) + item[1]


with open("items_statistics_all_lines_initial_foem.csv") as out_file:
    out_file.write(sorted(counter_all_items.items(), key=lambda item: item[1]).__repr__())