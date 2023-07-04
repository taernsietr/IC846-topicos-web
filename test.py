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

    # Tempo para carregar os dados do scroll
    time.sleep(3)

    end = time.time()
    print(f'start: {start}, end: {end}')

    #Definir um tempo para ele scrollar até chegar no botão
    if round(end - start) > 5:
        break

    #Checa se o botão está visível e, se positivo, clica nele
    if driver.find_element(By.CLASS_NAME, 'infinite-scroller__show-more-button').is_displayed():
        driver.find_element(By.CLASS_NAME, 'infinite-scroller__show-more-button').click()

src = driver.page_source
soup = BeautifulSoup(src, 'lxml')

jobs_info = soup.find_all('div', {'class': 'base-search-card__info'}) 
jobs = []
for job in jobs_info:
    publisher = job.find('a', {'class' : 'hidden-nested-link'}).text.strip()
    if not publisher:
        publisher = job.find('h4').text.strip() 

    # Adicionar localização e tempo de postagem. (Achar um jeito de pegar o texto dentro de uma span)
    jobs.append((job.find('h3').text.strip(), job.find('h4').text.strip()))

print(jobs)
driver.close()