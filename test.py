from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
import sys

if len(sys.argv) == 1: 
        sys.exit() 
arg = sys.argv[1].replace(" ","+")

driver = webdriver.Firefox()
driver.get(f'https://www.linkedin.com/jobs/search?keywords={arg}&location=Brazil&geoId=&position=1&pageNum=0c')
 
start = time.time()
initialScroll = 0
finalScroll = 1000
 
while True:
    driver.execute_script(f'window.scrollTo({initialScroll},{finalScroll})')
    initialScroll = finalScroll
    finalScroll += 1000

    # Tempo para carregar os dados
    time.sleep(3)

    end = time.time()
    # print(f'start: {start}, end: {end}')
    if round(end - start) > 10:
        break

src = driver.page_source
soup = BeautifulSoup(src, 'lxml')
intro = soup.find('div', {'class': 'jobs-search__results-list'})
print(intro)
    