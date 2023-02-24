import requests
from bs4 import BeautifulSoup
import csv

url = "https://www.fbi.gov/wanted/fugitives"
headers = {
  'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36'
}

page = requests.get(url, headers=headers)
soup = BeautifulSoup(page.content, 'html.parser')
# a_tags = soup.find_all("a")[1:].prettify()
# print(a_tags)
people = soup.find_all(class_="portal-type-person castle-grid-block-item")

for item in people:
  block = item.find('a', class_='focuportal-type-person castle-grid-block-itemspoint').div
  name = block.contents[1].text
  print(name)

# csv_headers = []

# with open('amazon_books.csv', 'w', encoding = 'utf-8', newline='') as file:
#   writer = csv.writer(file)
#   writer.writerow(csv_headers)

# for item in books:
#   children = item.find('div', class_='zg-grid-general-faceout').div

#   rank = item.find('span', class_='zg-bdg-text').text[1:]
#   title = children.contents[1].text
#   author = children.contents[2].text
#   # rating = children.contents[3].text
#   price = children.contents[-1].text

#   with open('amazon_books.csv', 'a', encoding = 'utf-8', newline='') as file:
#     writer = csv.writer(file)
#     writer.writerow([rank, title, author, price])