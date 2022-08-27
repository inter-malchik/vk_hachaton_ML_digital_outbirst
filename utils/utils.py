from datetime import datetime, date
from typing import List

import pymorphy2
from transliterate import translit

from ..reformate_data import *

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


def parse_date(date_str):
    try:
        date = datetime.strptime(date_str, "%Y%m%d").date()
    except Exception:
        raise ValueError
    return date


def check_word(word, view=False):
    morph = pymorphy2.MorphAnalyzer(lang='ru')
    result = morph.word_is_known(translit(word, 'ru'))
    if view and not result:
        print(word)
    return result


class ClientParser:

    max_url_click = 0
    min_url_click = float('inf')
    url_click_counter = 0

    max_title_click = 0
    min_title_click = float('inf')
    title_click_counter = 0

    def __init__(self, row: List):

        self.user_ID = int(row['CLIENT_ID'])
        self.retro_dt = row['RETRO_DT']
        self.DEF = int(row['DEF'])
        urls = row['urls']
        titles = row['tokens']
        self.titles_dict = self.to_dict(titles)
        self.urls_dict = self.to_dict(urls)
        self.ready_urls = waste_digits(self.urls_dict)
        self.ready_titles = waste_digits(self.titles_dict)

        self.url_average = sum(self.urls_dict.values()) / len(self.urls_dict)
        self.title_average = sum(self.urls_dict.values()) / len(self.urls_dict)

        ClientParser.update_class_fields(self)

    @classmethod
    def update_class_fields(cls, instance):

        cls.min_url_click = min(min(instance.urls_dict.values()), cls.min_url_click)
        cls.max_url_click = max(max(instance.urls_dict.values()), cls.max_url_click)
        cls.url_click_counter += sum(instance.urls_dict.values())

        cls.min_title_click = min(min(instance.titles_dict.values()), cls.min_title_click)
        cls.max_title_click = max(max(instance.titles_dict.values()), cls.max_title_click)
        cls.title_click_counter += sum(instance.titles_dict.values())

    @staticmethod
    def to_dict(string):
        dictionary = {}
        for i, str_obj in enumerate(string.split()):
            if i % 2 == 0:
                key = str_obj
            else:
                value = str_obj
                dictionary[key] = int(value)
        return dictionary

