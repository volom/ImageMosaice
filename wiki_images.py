#Download all images from wiki page
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options
import requests
import time

chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--ignore-certificate-errors')
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome() #options=chrome_options

#Wiki
wiki_page = '' #put here link to wiki page
driver.get(wiki_page)

# XPATH of main image
WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="mw-content-text"]/div[1]/div[1]/div/a/img'))).click()

images_count = 1000
index = 0
output_dir = '' # put here dir to download images
request = 'wiki_russian_army'
while index <= images_count:
    # XPATH of selected image     
    image_link = driver.find_elements_by_xpath('/html/body/div[7]/div/div[2]/div/div[1]/img')[0].get_attribute("src")
    response = requests.get(image_link)
    image_file_name = f"{output_dir}/{request}_{index}.jpeg" 
    file = open(image_file_name, "wb")
    file.write(response.content)
    file.close()
    
    driver.find_element_by_tag_name('body').send_keys(Keys.ARROW_RIGHT)
    
    time.sleep(3)
    print(f"Load image - {image_file_name}")
    index += 1
    
