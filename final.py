#https://www.google.com/search?q=site%3Ayoutube.com+openinapp.co&oq=site&aqs=chrome.1.69i57j69i59l3j0i512j69i60j69i61j69i60.7822j0j7&sourceid=chrome&ie=UTF-8

from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import csv
driver = webdriver.Chrome()


with open('links.csv', 'w', newline='') as file:
    line_count = 0
    page = 1
    while line_count<10000:
        url = f"https://www.google.com/search?q=site%3Ayoutube.com+openinapp.co?page={page}"
        driver.get(url)
        elements = driver.find_elements(By.TAG_NAME, 'a')
        writer = csv.writer(file)
        for e in elements:
            try:
                href = e.get_attribute("href")
                if href.startswith('https://www.youtube.com/'):
                    writer.writerow([href])
                    line_count = line_count + 1
                    print(href)
            except:
                continue
        time.sleep(5)
        page = page + 1



driver.close()