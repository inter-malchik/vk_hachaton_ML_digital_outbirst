from datetime import datetime, date
from typing import List

def is_correct_row(row):
    if row:
        if len(row) != 5:
            return False
        if not (row['CLIENT_ID'].is_digit() and row['RETRO_DT'].is_digit() and row['DEF'].is_digit()):
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


class User:

    #     favorite_title = ''
    #     favorite_url = ''
    #     max_cnt_title_click = 0
    #     max_cnt_url_click = 0

    #     worst_title = ''
    #     worst_url = ''

    #     min_cnt_title_click = 0
    #     min_cnt_url_click = 0

    #     mid_cnt_title_click = 0
    #     mid_cnt_url_click = 0

    def __init__(self, row: List):
        self.user_ID = int(row['CLIENT_ID'])
        self.retro_dt = row['RETRO_DT']
        titles = row['tokens']
        self.DEF = int(row['DEF'])
        urls = row['urls']
        self.titles_dict = self.to_dict(titles)
        self.urls_dict = self.to_dict(urls)

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