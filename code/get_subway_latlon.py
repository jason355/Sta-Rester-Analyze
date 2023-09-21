import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import re
import time



def init_subway_data(file):
    global count
    count = 0
    with open(file, "r", encoding="utf-8") as csvfile:
        counter = csv.reader(csvfile)
        for i in counter:
            count += 1
        global subway_data
        subway_data = [[None, None, None] for i in range(count)]




def read_csv_data(file, subway_data):
    j = 0
    with open(file, "r", encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            subway_data[j][0] = row[0]
            # print(row[0])
            subway_data[j][1] = row[1]
            # print(row[1])
            j += 1



def trans_addr(subway_data):
    k = 0
    for i in range(count-1):
        while subway_data[i+1][1][k:k+1] != "號":
            k += 1
            if k >= len(subway_data[i+1][1]):
                break
        subway_data[i+1][2] = subway_data[i+1][1][0:k+1]
        print(subway_data[i+1][2])
        k = 0



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


# def find_latlon(soup, store):
#     temp = []
#     tag = soup.find('div', id="rc_model_list")
#     a_tag = tag.find_all('a', href='#')
#     for i in a_tag:
#         temp.append(str(i))
#     pattern = re.compile(r"\d+\.\d+")
#     for j in temp:
#         result = pattern.finditer(j)
#         for k in result:
#             store.append(k.group())

def find_lattlon(get_url, store):
    parrser = re.compile(r"\d+\.\d+,")
    result = parrser.finditer(get_url)
    for i in result:
        store.append(i.group()[0:len(i.group())-2])
    print(store)
        
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




file = "./get_data/subway_data.csv"
url = "https://maps.nlsc.gov.tw/T09/mapshow.action?language=ZH" 
url_google_maps = "https://maps.google.com/maps/search/"



store = ['25.03921', '121.57698', '25.013002', '121.536706', '25.027221', '121.525783', '25.079184', '121.569329', '25.070023', '121.612030', '25.062624', '121.542741', '25.019380', '121.5299', '25.02532', '121.54825', '25.07548', '121.57679', '25.033753', '121.534349', '25.065305', '121.52252', '25.138131', '121.502568', '25.124742', '121.468078', '25.035073', '121.507804', '25.032894', '121.544792', '25.040139', '121.531793', '25.000425', '121.555874', '25.049200', '121.517309', '25.027526', '121.562512', '24.988730', '121.576555', '25.06378', '121.550926', '25.048322', '121.534528', '25.057120', '121.553117', '25.03687', '121.555346', '25.02524', '121.542381', '25.027775', '121.53010', '25.042438', '121.512909', '25.051111', '121.563970', '25.095511', '121.525136', '25.083856', '121.524060', '25.118223', '121.532017', '25.11528', '121.528068', '25.082384', '121.546275', '25.051854', '121.530226', '25.052234', '121.53566', '25.052158', '121.542374', '25.072169', '121.518962', '25.0460', '121.58547', '25.062682', '121.575944', '25.083202', '121.594071', '25.042381', '121.54355', '25.049306', '121.579186', '25.052441', '121.603552', '25.056445', '121.617951']
j = 0
k=0
# init_subway_data(file)
# read_csv_data(file, subway_data)
# trans_addr(subway_data)



with open(file, "r", newline='', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    data = list(reader)
    # for i in range(count-1):
    #     get_url = get_lattlon_google_maps(str(url_google_maps+subway_data[i+1][2]))
    #     find_lattlon(get_url,store)
    
    for row in data:
        if "name" not in row:
            row.append(store[j])
            row.append(store[j+1])
            j +=2
with open(file, "w", newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    for row in data:
        writer.writerow(row)
