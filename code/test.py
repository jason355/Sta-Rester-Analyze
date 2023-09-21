from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import re
import time
import requests

def get_lattlon(url, addr):
    driver = webdriver.Chrome()
    driver.get(url)
    search_box = driver.find_element(By.NAME, "lucene")
    search_box.send_keys(addr)
    search_button2 = driver.find_element(By.XPATH, "//a[@id='lucene_search']")
    search_button2.click()
    time.sleep(1)
    html = driver.page_source
    driver.quit()
    soup = BeautifulSoup(html, "html.parser")
    return soup

def get_lattlon_google_maps(url):
    driver = webdriver.Chrome()
    driver.get(url)
    driver.implicitly_wait(1)
    time.sleep(5)
    #html = driver.page_source   
    get_url = driver.current_url
    driver.quit()
    #soup = BeautifulSoup(html, "html.parser")
    return get_url


def find_latlon(soup, store):
    temp = []
    tag = soup.find('div', id="rc_model_list")
    a_tag = tag.find_all('a', href='#')
    for i in a_tag:
        temp.append(str(i))
    pattern = re.compile(r"\d+\.\d+")
    for j in temp:
        result = pattern.finditer(j)
        for k in result:
            store.append(k.group())



# pattern = re.compile(r"\d+\.\d+")
url = "https://maps.google.com/maps/place/台北市大安區羅斯福路4段85號" # &lat=23.682530&lon=120.959120&zoom=8
# addr = "台北市信義區松德路28號"
result = []
# soup = get_lattlon(url, addr)
# find_latlon(soup, result)



def write_to_file(filename, text):
    file = open(filename, "w", encoding="utf-8")
    file.writelines(str(text))
    file.close()


# file = "./get_data/text.html"
# get_url = get_lattlon_google_maps(url)

# print(get_url)
# store = []
# def find_lattlon(get_url, store):
#     parrser = re.compile(r"\d+\.\d+,")
#     result = parrser.finditer(get_url)
#     for i in result:
#         store.append(i.group()[0:len(i.group())-2])
# find_lattlon(get_url, store)
# print(store)

data = ['ajd', 'da', 'ei', 'dfv;']

i = 0

del data[1]

print(data)