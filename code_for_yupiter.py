# файл train очищенный от пропусков и проверенный на шумы
file = open('train_clear.csv', 'r', encoding='utf-8')
frames = file.readline()
# массив с информацией о каждом пользователе
users = []

# класс пользователя
class ID:

    def __init__(self, user_ID, user_date, title_dict, url_dict):

        self.user_ID = user_ID
        self.user_date = user_date

        # словарь ключ-title : значение-clicks
        # clicks - количество посещений
        self.titles = title_dict
        # словарь ключ-url : значение-clicks
        self.urls = url_dict

        # словарь ключ-title : значение-clicks
        # в нем содержатся titles входящие в топ самых популярных за всеря среди всех юзеров
        self.top_most_popular_titles = {}

        # самый частопосещаемый тайтл/ы
        self.most_popular_title = []
        # самый частопосещаемый url/ы
        self.most_popular_url = []
        # количество посещений самого популярного тайтла
        self.max_cnt_title_click = 0
        # количество посещений самого популярного url
        self.max_cnt_url_click = 0

        # самый нечастопосещаемый тайтл/ы
        self.less_popular_title = []
        # самый нечастопосещаемый url/ы
        self.less_popular_url = []
        # количество посещений самого непопулярного тайтла
        self.min_cnt_title_click = 0
        # количество посещений самого непопулярного url
        self.min_cnt_url_click = 0

        # среднее количество посещений тайтлов
        self.mid_cnt_title_click = 0
        # среднее количество посещений url
        self.mid_cnt_url_click = 0

        # общее количево посещений всех тайтлов
        self.total_cnt_title_click = 0
        # общее количево посещений всех url
        self.total_cnt_url_click = 0

    def find_most_popular_data(self):
        self.max_cnt_title_click = max(self.titles.values())
        self.most_popular_title = [title for title in self.titles if self.titles[title] == self.max_cnt_title_click]

        self.max_cnt_url_click = max(self.urls.values())
        self.most_popular_url = [url for url in self.urls if self.urls[url] == self.max_cnt_url_click]

    def find_less_popular_data(self):
        self.min_cnt_title_click = min(self.titles.values())
        self.less_popular_title = [title for title in self.titles if self.titles[title] == self.min_cnt_title_click]

        self.min_cnt_url_click = min(self.urls.values())
        self.less_popular_url = [url for url in self.urls if self.urls[url] == self.min_cnt_url_click]

    def find_mid_cnt_clicks(self):
        self.total_cnt_title_click = sum(self.titles.values())
        self.mid_cnt_title_click = self.total_cnt_title_click / len(self.titles)

        self.total_cnt_url_click = sum(self.urls.values())
        self.mid_cnt_url_click = self.total_cnt_url_click / len(self.urls)

    # вычисление всех данных
    def find_class_data(self):
        self.find_most_popular_data()
        self.find_less_popular_data()
        self.find_mid_cnt_clicks()

    # обработка + сокращение данных данных
    def filter_popular_title(self, filter_set):
        # print('user ID', self.user_ID)
        # print('before', len(self.titles))
        for title in self.titles:
            if title in filter_set:
                self.top_most_popular_titles[title] = self.titles[title]
        # print('after', len(self.top_most_popular_titles))

    def print_class_data(self):
        print('self.user_ID', self.user_ID)
        print('self.user_date', self.user_date)

        print('self.titles', self.titles)
        print('self.urls', self.urls)

        print('self.top_most_popular_titles', self.top_most_popular_titles)

        print('self.most_popular_title', self.most_popular_title)
        print('self.most_popular_url', self.most_popular_url)
        print('self.max_cnt_title_click', self.max_cnt_title_click)
        print('self.max_cnt_url_click', self.max_cnt_url_click)

        print('self.less_popular_title', self.less_popular_title)
        print('self.less_popular_url', self.less_popular_url)
        print('self.min_cnt_title_click', self.min_cnt_title_click)
        print('self.min_cnt_url_click', self.min_cnt_url_click)

        print('self.mid_cnt_title_click', self.mid_cnt_title_click)
        print('self.mid_cnt_url_click', self.mid_cnt_url_click)

        print('self.total_cnt_title_click', self.total_cnt_title_click)
        print('self.total_cnt_url_click', self.total_cnt_url_click)

# функция парсинга clear_train_data
def extract_data(line):

    id, date, titles, flag, urls = line.split('\t')
    titles = titles.split(' ')
    urls = urls.split(' ')

    # формирование словаря titles из строки
    titles_dict = {}
    for i in range(0, len(titles) - 1, 2):
        titles_dict[titles[i]] = int(titles[i + 1])

    # формирование словаря urls из строки
    url_dict = {}
    for i in range(0, len(urls) - 1, 2):
        url_dict[urls[i]] = int(urls[i + 1])

    # создание экземппляра класа для каждого юзера
    user = ID(id, date, titles_dict, url_dict)

    return user

# сохраняем и обрабатываем данные о каждом пользователе
for line in file:
    users.append(extract_data(line))
    users[-1].find_class_data()

# класс с информацией за некоторый временной промежуток(промежуток параметризируется)
class Date:

    def __init__(self):
        self.date = ''
        self.users = []

        self.all_titles_and_clicks = {}
        self.all_url_and_clicks = {}

        self.sort_list_all_titles_and_clicks = []
        self.titles_to_numbers = {}
        self.top_most_popular_titles = set()

        self.all_titles_and_uniq_users_amount = {}
        self.all_url_and_uniq_users_amount = {}

        self.most_popular_title_users = []
        self.most_popular_title_user_amount = 0
        self.most_popular_title_clicks = []
        self.most_popular_title_click_amount = 0

        self.most_popular_url_users = []
        self.most_popular_url_user_amount = 0
        self.most_popular_url_clicks = []
        self.most_popular_url_click_amount = 0

        self.less_popular_title_users = []
        self.less_popular_title_user_amount = 0
        self.less_popular_title_clicks = []
        self.less_popular_title_click_amount = 0

        self.less_popular_url_users = []
        self.less_popular_url_user_amount = 0
        self.less_popular_url_clicks = []
        self.less_popular_url_click_amount = 0

    def add_titles(self, titles):
        # titles - titles current user
        # this function will be called for every user

        for title in titles:
            if title in self.all_titles_and_clicks:
                self.all_titles_and_clicks[title] += titles[title]
            else:
                self.all_titles_and_clicks[title] = titles[title]

    def add_urls(self, urls):
        # urls - urls current user
        # this function will be called for every user

        for url in urls:
            if url in self.all_url_and_clicks:
                self.all_url_and_clicks[url] += urls[url]
            else:
                self.all_url_and_clicks[url] = urls[url]

    def add_user(self, user):
        # this function will be called for every user
        self.users.append(user.user_ID)

        self.add_titles(user.titles)
        for title in user.titles:

            if title in self.all_titles_and_uniq_users_amount:
                self.all_titles_and_uniq_users_amount[title] += 1
            else:
                self.all_titles_and_uniq_users_amount[title] = 1

        self.add_urls(user.urls)
        for url in user.urls:

            if url in self.all_url_and_uniq_users_amount:
                self.all_url_and_uniq_users_amount[url] += 1
            else:
                self.all_url_and_uniq_users_amount[url] = 1

    def find_most_popular_click_data(self):

        self.most_popular_title_click_amount = max(self.all_titles_and_clicks.values())
        self.most_popular_title_clicks = [name for name in self.all_titles_and_clicks if
                                          self.all_titles_and_clicks[name] == self.most_popular_title_click_amount]

        self.most_popular_url_click_amount = max(self.all_url_and_clicks.values())
        self.most_popular_url_clicks = [name for name in self.all_url_and_clicks if
                                        self.all_url_and_clicks[name] == self.most_popular_url_click_amount]

    def find_less_popular_click_data(self):

        self.less_popular_title_click_amount = min(self.all_titles_and_clicks.values())
        self.less_popular_title_clicks = [name for name in self.all_titles_and_clicks if
                                          self.all_titles_and_clicks[name] == self.less_popular_title_click_amount]

        self.less_popular_url_click_amount = min(self.all_url_and_clicks.values())
        self.less_popular_url_clicks = [name for name in self.all_url_and_clicks if
                                        self.all_url_and_clicks[name] == self.less_popular_url_click_amount]

    def find_most_popular_user_data(self):
        self.most_popular_title_user_amount = max(self.all_titles_and_uniq_users_amount.values())
        self.most_popular_title_users = [name for name in self.all_titles_and_uniq_users_amount if
                                         self.all_titles_and_uniq_users_amount[name] ==
                                         self.most_popular_title_user_amount]

        self.most_popular_url_user_amount = max(self.all_url_and_uniq_users_amount.values())
        self.most_popular_url_users = [name for name in self.all_url_and_uniq_users_amount if
                                       self.all_url_and_uniq_users_amount[name] == self.most_popular_url_user_amount]

    def find_less_popular_user_data(self):
        self.less_popular_title_user_amount = min(self.all_titles_and_uniq_users_amount.values())
        self.less_popular_title_users = [name for name in self.all_titles_and_uniq_users_amount if
                                         self.all_titles_and_uniq_users_amount[name] ==
                                         self.less_popular_title_user_amount]

        self.less_popular_url_user_amount = min(self.all_url_and_uniq_users_amount.values())
        self.less_popular_url_users = [name for name in self.all_url_and_uniq_users_amount if
                                       self.all_url_and_uniq_users_amount[name] == self.less_popular_url_user_amount]

    def print_class_data(self):
        # print('self.date', self.date)
        # print('self.users', len(self.users))

        # print('self.all_titles_and_clicks', len(self.all_titles_and_clicks))
        for title in self.all_titles_and_clicks:
            print(title, self.all_titles_and_clicks[title])
        # print('self.all_url_and_clicks', len(self.all_url_and_clicks))

        #
        # print('self.all_titles_and_uniq_users_amount', len(self.all_titles_and_uniq_users_amount))
        # print('self.all_url_and_uniq_users_amount', len(self.all_url_and_uniq_users_amount))
        #
        # self.most_popular_title_users = []
        # self.most_popular_title_user_amount = 0
        # self.most_popular_title_clicks = []
        # self.most_popular_title_click_amount = 0
        #
        # self.most_popular_url_users = []
        # self.most_popular_url_user_amount = 0
        # self.most_popular_url_clicks = []
        # self.most_popular_url_click_amount = 0
        #
        # self.less_popular_title_users = []
        # self.less_popular_title_user_amount = 0
        # self.less_popular_title_clicks = []
        # self.less_popular_title_click_amount = 0
        #
        # self.less_popular_url_users = []
        # self.less_popular_url_user_amount = 0
        # self.less_popular_url_clicks = []
        # self.less_popular_url_click_amount = 0

    def sorting_list_titles(self):
        number = 1
        for title in self.all_titles_and_clicks:
            self.titles_to_numbers[title] = number
            self.sort_list_all_titles_and_clicks.append((self.all_titles_and_clicks[title], title))
            number += 1

        self.sort_list_all_titles_and_clicks = sorted(self.sort_list_all_titles_and_clicks, key=lambda tup: tup[0],
                                                      reverse=True)

        self.sort_list_all_titles_and_clicks = self.sort_list_all_titles_and_clicks[0:100]

        for pair in self.sort_list_all_titles_and_clicks:
            print(pair)
            self.top_most_popular_titles.add(pair[1])
            self.top_most_popular_titles_dict[pair[1]] = pair[0]

        print(self.top_most_popular_titles)
        print(self.top_most_popular_titles_dict)

    def find_all_class_data(self):
        self.find_less_popular_click_data()
        self.find_most_popular_click_data()
        self.find_less_popular_user_data()
        self.find_most_popular_user_data()
        self.sorting_list_titles()

# переменная со статистическими данными за временной интервал от самой ранней даты до самой поздней из датасета
all_time = Date()
# сохранение и обработка данных по всем пользователям за все время
for user in users:
    all_time.add_user(user)

# вычисление самых популярных тайтлов среди всех юзеров за все время и обработка этой информации
all_time.sorting_list_titles()

# для каждого юзера создание словаря тайтлов (и количества посещений),
# которые входят в топ самых популярных за все время
for user in users:
    user.filter_popular_title(all_time.top_most_popular_titles)