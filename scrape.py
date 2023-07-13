from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains, Keys
import time

# Driver instanciado; é o principal objeto do Selenium
def scrape(arg, time_to_run):
    driver = webdriver.Firefox()
    driver.get(f'https://www.linkedin.com/jobs/search?keywords={arg.replace("_","+")}&location=Brazil&geoId=&position=1&pageNum=0c')
     
    # Lógica de scrolling. O script irá ativar o scroll infinito X vezes, clicando no botão "ver mais" se necessário

    start = time.time()
    initialScroll = 0
    finalScroll = 1000
     
    while True:
        driver.execute_script(f'window.scrollTo({initialScroll},{finalScroll})')
        initialScroll = finalScroll
        finalScroll += 1000

        # Tempo para carregar os dados em cada scroll 
        time.sleep(3)

        # Definir um tempo para ele scrollar até chegar no botão
        if round(time.time() - start) > time_to_run:
            break

        # Checa se o botão está visível e, se positivo, clica nele
        show_more = driver.find_element(By.CLASS_NAME, 'infinite-scroller__show-more-button')
        if show_more.is_displayed():
            show_more.click()

    ActionChains(driver).send_keys(Keys.HOME).perform()
    cards = driver.find_elements(By.CLASS_NAME, 'base-card')

    jobs = []
    for card in cards:
        card.click()
        time.sleep(3)

        title = card.find_element(By.CLASS_NAME, 'base-search-card__title').text.strip()
        publisher = card.find_element(By.CLASS_NAME, 'base-search-card__subtitle').text.strip()
        location = card.find_element(By.CLASS_NAME, 'job-search-card__location').text.strip()
        time_posted = card.find_element(By.TAG_NAME, 'time').text.strip()
        description = driver.find_element(By.CLASS_NAME, 'show-more-less-html__markup').text.strip()
        
        jobs.append((title, publisher, location, time_posted, description))
    driver.close()

    with open(f'{arg}.csv', "w") as results:
        results.write('Title,Publisher,Location,Time_Posted,Description\n')
        for job in jobs:
            results.write(f'"{job[0]}","{job[1]}","{job[2]}","{job[3]}","{job[4]}"\n')
