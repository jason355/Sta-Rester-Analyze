from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import re
from selenium.webdriver.common.action_chains import ActionChains
import time
import csv


def action_on_web(url):
    global combine
    v = 0
    w = 0
    top = 0
    driver = webdriver.Chrome()
    driver.get(url)
    search_box = driver.find_element(By.CLASS_NAME, "cmp-form-text__text")
    search_box.send_keys("台北市")
    search_button = driver.find_element(By.ID, "button-93a5672f18")
    search_button.click()
    time.sleep(1)
    more_res = driver.find_element(By.XPATH, "//button[@aria-controls='mcdFilterMenu']")
    #print(more_res)
    more_res.click()
    time.sleep(1)
    range_button = driver.find_elements(By.XPATH, "//input[@class='cmp-form-options__field cmp-form-options__field--radio']")
    # print(len(range_button))
    actions = ActionChains(driver)
    actions.move_to_element_with_offset(range_button[1], 2, 2).click().perform()
    time.sleep(1)
    if range_button[1].is_selected():
        print("Input is selected.")
    else:
        print("Input is not selected.")
    
    len_item = driver.find_element(By.CLASS_NAME, "cmp-restaurant-locator__info")
    pattern = re.compile(r"\d+")
    #print(type(len_item.text))
    result = pattern.finditer(len_item.text)
    for row in result:
        # print(row.group())
        len_item = int(row.group())
        page = int(int(row.group()) / 10)
        for i in range(page):    
            more_item = driver.find_element(By.ID, "button-93a5672f17")
            more_item.click()
            time.sleep(1)
    items = driver.find_elements(By.CLASS_NAME, "cmp-restaurant-locator__restaurant-list-item-details-al2")
    # for addr in items:
    #     #print(addr.text)
    item_urls = driver.find_elements(By.CLASS_NAME, "cmp-restaurant-locator__restaurant-list-item-details-al1")

    provi = [[None, None] for i in range(len_item)]
    combine = [[None, None, None] for i in range(len_item)]
    for row in item_urls:
        a_tag = row.find_element(By.TAG_NAME, "a")
        href = a_tag.get_attribute("href")
        text = row.text
        provi[v][0] = href
        provi[v][1] = text
        v += 1
    # 篩選出台北市內的店家
    while True:
        if "新北市" in items[w].text or "宜蘭" in items[w].text:
            w += 1
        else:
            combine[top][0] = provi[w][1]
            combine[top][1] = items[w].text
            combine[top][2] = provi[w][0]
            top += 1
            w += 1
        if w >= len_item:
            break
        
        
    #html = driver.page_source
    driver.quit()
    
    #soup = BeautifulSoup(html, "html.parser")
    return top


url = "https://www.mcdonalds.com/tw/zh-tw/restaurant-locator.html"

final_total = action_on_web(url)


print(final_total)

with open("Mcdonalcs_taipei_addr.csv", 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    for i in combine:
        print(i)
        writer.writerow(i)

