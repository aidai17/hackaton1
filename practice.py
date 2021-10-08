# import requests
# from bs4 import BeautifulSoup as BS

# import csv

# def get_html(url):
#     response = requests.get(url)
#     # print(response)
#     return response.text

# def get_data(html):
#     soup = BS(html, 'lxml')
#     catalog = soup.find('div', class_='catalog-list')
#     # print(catalog)
#     cars = catalog.find_all('a', class_='catalog-list-item')
#     # print(cars)

#     for car in cars:
# # находим название
#         try:
#             title = car.find('span', class_='catalog-item-caption').text.strip()
#             # вызываем текст чтобы упорядочить заголовки
#             # strip - убирает пробелы слева и справа
#             # print(title)
#         except:
#             title = ''
# # находи цену
#         try:
#             price = car.find('span', class_='catalog-item-price').text.strip()
#             # print(price)
#         except:
#             price = ''
# # картинки:
#         try:
#             image = car.find('img', class_='catalog-item-cover-img').get('src')
#             print(image)
#         except:
#             image = ''

#         data = {
#             'title': title,
#             'price': price,
#             'image': image
#         }

#         write_csv(data)


# def write_csv(data):
#     with open('cars.csv', 'a') as csv_file:
#         writer = csv.writer(csv_file, delimiter='/')
#         writer.writerow((data['title'], data['price'], data['image']))


# def main():
#     # url = 'https://cars.kg/offers'
#     # html = get_html(url)
#     # data = get_data(html)

#     for page in range(1, 7):
#         url = f'https://cars.kg/offers/{page}'
#         html = get_html(url)
#         data = get_data(html)
    

# main()