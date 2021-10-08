import csv 
import requests
from bs4 import BeautifulSoup as BS


def get_html(url):
    response = requests.get(url)
    return response.text


def get_data(html):
    soup = BS(html, 'lxml')
    catalog =  soup.find('div', class_ = 'search-results-table' )
    motorcycles = catalog.find_all('div', class_ = 'list-item list-label new-line' )
    # print(motorcycles)

    for motorcycle in motorcycles:
        try:
            title = motorcycle.find('h2', class_ = 'name').text.strip().strip()
            print(title)
        except:
            title = ''
        try:
            price = motorcycle.find('p', class_ = 'price').find('strong').text
            print(price)
        except:
            price = ''
        try:
            img = motorcycle.find('div', class_ = 'thumb-item-carousel').find('img').get('data-src')
            print(img)
        except:
            img = ''
        try:
            year = motorcycle.find('p', class_ = 'year-miles').text.strip()
            print(year)
        except:
            year = ''
        try:
            type_of_car = motorcycle.find('p', class_ = 'body-type').text.strip()
        except:
            type_of_car = ''
        try:
            city = motorcycle.find('p', class_ = 'city').text.strip()
        except:
            city = ''
        try:
            speed = motorcycle.find('p', class_ = 'volume').text.strip()
        except:
            speed = ''

        data = {
            'title': title,
            'price': price,
            'img': img,
            'year': year,
            'type_of_car': type_of_car,
            'city': city,
            'speed': speed

        }

        write_csv(data)
        
def write_csv(data):
    with open('motorcycles.csv', 'a') as csv_file:
        writer = csv.writer(csv_file, delimiter='\n')
        writer.writerow((data['title'], data['price'], data['img'], data['year'], data['type_of_car'], data['city'], data['speed']+'\n'))

def main():
    for page in range(1, 6):
        url = f'https://www.mashina.kg/motosearch/all/?type=20&page={page}'
        html = get_html(url)
        data = get_data(html)


main()

        







