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
    soup = BeautifulSoup(html, 'lxml')

    pages = soup.find('div', class_='pagination-pages').find_all('a', class_='pagination-page')[-1]

def main():
    # https://www.avito.ru/ryazan?s=101&sgtd=1&view=gallery&q=iphone+6
    pass

if __name__ == '__main__':
    main()