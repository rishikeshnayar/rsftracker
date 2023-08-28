from bs4 import BeautifulSoup
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

option = webdriver.ChromeOptions()
# I use the following options as my machine is a window subsystem linux. 
# I recommend to use the headless option at least, out of the 3
option.add_argument('--headless')
option.add_argument('--no-sandbox')
option.add_argument('--disable-dev-sh-usage')
# Replace YOUR-PATH-TO-CHROMEDRIVER with your chromedriver location
driver = webdriver.Chrome(ChromeDriverManager().install(), options=option) # Updating Chromedriver

def scrape(driver):
    driver.get('https://safe.density.io/#/displays/dsp_956223069054042646?token=shr_o69HxjQ0BYrY2FPD9HxdirhJYcFDCeRolEd744Uj88e') # Getting page HTML through request
    time.sleep(5)
    soup = BeautifulSoup(driver.page_source, 'html.parser') # Parsing content using beautifulsoup. Notice driver.page_source instead of page.content
    
    # Selecting the span with the percentage
    links = soup.select("div div div div div div span") 
    text = links[-1].text

    # Returning percentage as int
    if len(text) == 7:
        return int(text[:1])
    if len(text) == 8:
        return int(text[:2])
    else:
        return int(text[:3])
