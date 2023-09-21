import requests
from bs4 import BeautifulSoup
import numpy as np
import csv


def write_to_file(filename, text):
    file = open(filename, "w", encoding="utf-8")
    file.writelines(str(text))
    file.close()


def find_target(output_data):
    global count
    stores_name = soup.find_all("td", class_="store-name")
    stores_loc = soup.find_all("td", class_="store-where")
    for store_name, store_loc in zip(stores_name, stores_loc):
        name = store_name.text.strip()
        location = store_loc.text.strip()
        output_data[count][0] = name
        output_data[count][1] = location
        count += 1


def find_print_target():
    stores_name = soup.find_all("td", class_="store-name")
    stores_loc = soup.find_all("td", class_="store-where")
    for store_name, store_loc in zip(stores_name, stores_loc):
        name = store_name.text.strip()
        location = store_loc.text.strip()
        print(f"name: {name} address: {location}")


def add_url(page_num, link):
    for i in range(page_num):
        page = i
        url = f"https://subway.com.tw/GoWeb2/include/index.php?pageNum_content01={page}&totalRows_content01=44&select=index.php%3FPage%3D2&address=%E5%8F%B0%E5%8C%97%E5%B8%82&Page=2&Cate01=&Cate02=&Cate03="
        link.append(url)


count = 0
page = 0
url = f"https://subway.com.tw/GoWeb2/include/index.php?pageNum_content01={page}&totalRows_content01=44&select=index.php%3FPage%3D2&address=%E5%8F%B0%E5%8C%97%E5%B8%82&Page=2&Cate01=&Cate02=&Cate03="
link = []

response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

NoS = soup.find("p", class_="store-sum")
NoS = NoS.find("span")
NoS = int(NoS.text.strip())
if (NoS % 10) != 0:
    page_num = (NoS // 10) + 1
else:
    page_num = NoS // 10


result_data = [[0, 0] for i in range(NoS)]

add_url(page_num, link)

# for address in link:
#     del soup
#     response = requests.get(address)
#     soup = BeautifulSoup(response.text, "html.parser")
#     find_target(result_data)
for i in range(page_num):
    response = requests.get(link[i])
    soup = BeautifulSoup(response.text, "html.parser")
    find_target(result_data)
print(len(result_data))

with open("subway_data.csv", 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    for row, column in result_data:
        writer.writerow([row, column])
print("mission accomplish.")
