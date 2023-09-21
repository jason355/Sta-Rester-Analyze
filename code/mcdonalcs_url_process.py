import requests
from bs4 import BeautifulSoup
import csv
import re

file = './get_data/Mcdonalcs_taipei_addr.csv'
data = []

with open(file, 'r', newline='', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    data = list(reader)
len_data = 0
for row in data:
    if '' not in row:
        len_data += 1
print(len_data)

patter = re.compile(r"\d+\.\d+")
temp = []
m = 0
n = 0

for i in range(len_data):
    request = requests.get(data[i][2])
    soup = BeautifulSoup(request.text, "html.parser")
    a_tag = soup.find("div", class_="cmp-restaurant-detail__main-details")
    result = patter.finditer(a_tag['data-restaurant-details-resp'])
    for row in result:
        # print(row.group())
        temp.append(row.group())


print(data)
for j in range(0, len(temp), 2):
    data[m].append(temp[j])
    data[m].append(temp[j+1])
    print(data[m])
    m += 1


with open(file, "w", newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    for k in data:
        writer.writerow(k)
