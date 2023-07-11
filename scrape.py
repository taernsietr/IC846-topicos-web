from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
import sys

TIME_TO_RUN = 5 

if len(sys.argv) == 1: 
    print("É necessário informar pelo menos uma palavra para que a busca seja feita. O script será encerrado agora.")
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

    # Tempo para carregar os dados do scroll
    time.sleep(3)

    end = time.time()
    print(f'start: {start}, end: {end}')

    # Definir um tempo para ele scrollar até chegar no botão
    if round(end - start) > TIME_TO_RUN:
        break

    # Checa se o botão está visível e, se positivo, clica nele
    show_more = driver.find_element(By.CLASS_NAME, 'infinite-scroller__show-more-button')
    if show_more.is_displayed():
        show_more.click()

src = driver.page_source
soup = BeautifulSoup(src, 'lxml')

jobs_info = soup.find_all('div', {'class': 'base-search-card__info'}) 
jobs = []
for job in jobs_info:
    publisher = job.find('a', {'class': 'hidden-nested-link'})
    if not publisher:
        publisher = job.find('h4') 
    publisher = publisher.text.strip()

    jobs.append((
        job.find('h3').text.strip(),
        publisher,
        job.find('span', {'class': 'job-search-card__location'}).text.strip(),
        job.find('time').text.strip()
    ))
driver.close()

with open("results.csv", "w") as results:
    results.write('Title,Publisher,Location,Time Posted\n')
    for job in jobs:
        results.write(f'"{job[0]}","{job[1]}","{job[2]}","{job[3]}"\n')

