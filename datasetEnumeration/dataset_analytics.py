from classes import *


counter_all_items = dict() # сумма тайтлов за все время
counter_all_urls = dict() # сумма url'ов за все время

for row_text, DLine in dataset_parser_iterator("train_clear.csv"):
    for item in DLine.tokens.items():
        counter_all_items[item[0]] = counter_all_items.get(item[0], 0) + item[1]

    for item in DLine.urls_hashed.items():
        counter_all_urls[item[0]] = counter_all_urls.get(item[0], 0) + item[1]

with open("items_statistics_all_lines.csv") as out_file:
    out_file.write(sorted(counter_all_items.items(), key=lambda item: item[1]).__repr__())

with open("urls_statistics_all_lines.csv") as out_file:
    out_file.write(sorted(counter_all_urls.items(), key=lambda item: item[1]).__repr__())
