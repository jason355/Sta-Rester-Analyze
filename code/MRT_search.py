import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import pandas as pd


def carry(number):
    if number[2] == 10:
        number[2] = 0
        number[1] += 1
    if number[1] == 10:
        number[1] = 0
        number[0] += 1
    if number[0] == 10:
        print("Out of range")
        number[0] = 9


def write_to_file(filename, text, mode):
    file = open(filename, mode, encoding="utf-8")
    file.writelines(str(text)+"\n")
    file.close()


def get_web_data(url):
    driver = webdriver.Chrome()
    driver.get(url)
    html = driver.page_source
    driver.quit()
    return html


def find_name(data_store, count, soup):
    name_tag = soup.find('td', class_="station__img")
    name_tag = name_tag.find('img')
    data_store.loc[count, 'name'] = name_tag['title']
    print(data_store.loc[count, 'name'])


def find_latlon(data_store, count, soup, j):
    exit_tag_link = soup.find('a', target='blank')
    exit_link = exit_tag_link['href']
    link_char = list(exit_link)

    while "L" != link_char[j]:
        if j > len(link_char):
            break
        j += 1
    if str(link_char[j]+link_char[j+1]+link_char[j+2]+link_char[j+3]+link_char[j+4]+link_char[j+5]) == "Longit":
        latlon = exit_link[j:len(link_char)]
    # print(latlon)
    data_store.loc[count, 'latlon'] = latlon
    print(data_store.loc[count, 'latlon'])


def url_generate(number, link):
    for i in range(1000):
        url = "https://web.metro.taipei/pages/tw/station/" + \
            str(number[0]) + str(number[1]) + str(number[2])
        # print(url)
        link.append(url)
        number[2] += 1
        carry(number)


url_test = "https://web.metro.taipei/pages/tw/station/007"
number = [0] * 3
j = 0
links = []
count = 0

sdf = pd.DataFrame(columns=['name', 'latlon'])

url_generate(number, links)
total_url = len(links)
Now = 0


for url in links:
    Now += 1
    Now_schedule = (Now / total_url) * 100
    print(f"Current process {Now_schedule}%", end='\r')
    html = get_web_data(url)
    soup = BeautifulSoup(html, "html.parser")
    try:
        find_name(sdf, count, soup=soup)
        find_latlon(sdf, count, soup=soup, j=j)
        text = [sdf.loc[count, 'name'], sdf.loc[count, 'latlon']]
        write_to_file("MRT_data.txt", text, mode="a")
    except KeyError:
        pass
    except AttributeError:
        pass
