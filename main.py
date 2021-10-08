import requests
from bs4 import BeautifulSoup as BS


import csv


def get_html(url):
    response = requests.get(url)
    print(response)
    return response.text

def get_data(html):
    soup = BS(html, 'lxml')
    # print(soup)
    catalog = soup.find('div', class_='catalog-list')
    cars = catalog.find_all('a', class_='catalog-list-item')
    # print(cars)
    for car in cars:
        try:
            title = car.find('span', class_='catalog-item-caption').text.strip()
            print(title)
        except:
            title = ''
        try:
            price = car.find('span', class_='catalog-item-price').text.strip()
            print(price)
        except:
            price = ''
        try:
            img = car.find('img', class_='catalog-item-cover-img').get('src')
            print(img)
        except:
            img = ''

        data = {
            'title': title,
            'price': price,
            'img': img
        }

        write_csv(data)

def write_csv(data):
    with open('cars.csv', 'a') as csv_file:
        writer = csv.writer(csv_file, delimiter='/')
        writer.writerow((data['title'], data['price'], data['img']))

def main():
    for page in range(1, 7):
        url = f'https://cars.kg/offers/{page}'
        html = get_html(url)
        data = get_data(html)







main()

