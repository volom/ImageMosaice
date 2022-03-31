# Search and download images from https://duckduckgo.com/?q=&t=h_&iar=images
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

list_reqs = [] # put here your requests key words
images_count = 10 # put here images yu want to donwload
output_dir = '' # put here output dir for downloaded images

for request in list_reqs:
    search_str = f'https://duckduckgo.com/?q={request}&t=h_&iax=images&ia=images'
    driver.get(search_str)

    WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="zci-images"]/div/div[2]/div/div[1]/div[1]/span/img'))).click()

    for index in range(images_count):
        image_link = driver.find_elements_by_xpath('//*[@id="zci-images"]/div[2]/div/div[1]/div[1]/div/div[1]/div/a/img[2]')[0].get_attribute("src")
        response = requests.get(image_link)
        image_file_name = f"{output_dir}/{request}_{index}.jpeg"
        file = open(image_file_name, "wb")
        file.write(response.content)
        file.close()

        driver.find_element_by_tag_name('body').send_keys(Keys.ARROW_RIGHT)

        time.sleep(3)
        print(f"Load image - {image_file_name}")
    
    
