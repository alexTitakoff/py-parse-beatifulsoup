# coding=utf-8
import requests
from bs4 import BeautifulSoup
import csv

import sys
reload(sys)
sys.setdefaultencoding('utf8')



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


def write_csv(data):
    with open('avito.csv', 'a') as f:
        writer = csv.writer(f)

        writer.writerow((
            data['title'],
            data['url'],
            data['price'],
            data['date'],
        ))
    # pass



def get_page_data(html):
    soup = BeautifulSoup(html, 'lxml')
    ads = soup.find('div', class_='catalog-list').find_all('div', class_='item_gallery')

    for ad in ads:
        # recieve title price url date
        print(ad.find('div', class_='created-date').text.strip())
        try:
            title = ad.find('h3').text.strip()
        except:
            title = ''
        try:
            url = 'https://www.avito.ru' + ad.find('h3').find('a').get('href')
        except:
            url = ''
        try:
            price = ad.find('span', class_='option price').text.strip()
        except:
            price = ''
        try:
            date = ad.find('div', class_='created-date').text.strip()
        except:
            date = ''

        data = {
            'title': title,
            'url': url,
            'price': price,
            'date': date,
        }

        print data
        write_csv(data)



def main():
    # https://www.avito.ru/ryazan?p=1&s=101&sgtd=1&view=gallery&q=iphone+6
    url = 'https://www.avito.ru/ryazan?p=1&s=101&sgtd=1&view=gallery&q=iphone+6'
    base_url = 'https://www.avito.ru/ryazan?'
    page_part = 'p='
    middle_part = '&s=101&sgtd=1&view=gallery&' # промежуточные параметры
    query_part = '&q=iphone+6'

    total_pages = get_total_pages(get_html(url))
    # total_pagesExample = 3   # тестовые две страницы

    for i in range(1,total_pages):
        url_gen = base_url + page_part + str(i) + middle_part + query_part
        print('Cтраница' + str(i))
        print(url_gen)
        html = get_html(url_gen)
        get_page_data(html)




if __name__ == '__main__':
    main()