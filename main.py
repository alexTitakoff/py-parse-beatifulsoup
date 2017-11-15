import requests
from bs4 import BeautifulSoup




# План
# 1. Выяснить количество страниц
# 2. Сформировать список урлов на страницы выдачи
# 3. Собрать данные


def get_html(url):
    r = requests.get(url)
    return r.text


def get_total_pages(html):
    soup = BeautifulSoup


def main():
    # https: // www.avito.ru / ryazan / noutbuki?q = macbook & sgtd = 2
    pass

if __name__ == '__main__':
    main()