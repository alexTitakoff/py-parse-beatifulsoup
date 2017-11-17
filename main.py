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

    pages = soup.find('div', class_='pagination-pages').find_all('a', class_='pagination-page')[-1].get('href')
    total_pages = pages.split('=')
    return int(total_pages[1].split('&')[0])


def main():
    # https://www.avito.ru/ryazan?p=1&s=101&sgtd=1&view=gallery&q=iphone+6
    url = 'https://www.avito.ru/ryazan?p=1&s=101&sgtd=1&view=gallery&q=iphone+6'
    base_url = 'https://www.avito.ru/ryazan?'
    page_part = 'p='
    middle_part = '&s=101&sgtd=1&view=gallery&' # промежуточные параметры
    query_part = '&q=iphone+6'

    total_pages = get_total_pages(get_html(url))

    for i in range(1,total_pages):
        url_gen = base_url + page_part + str(i) + middle_part + query_part
        print(url_gen)




if __name__ == '__main__':
    main()