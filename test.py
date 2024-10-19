from selenium import webdriver
import time

driver = webdriver.Chrome()

driver.get("https://ved.rocks/")

with open('src/responsiveWiz/data/disableAnimations.js', 'r') as file:
    js_code = file.read()
    
driver.execute_script(js_code)

time.sleep(5)
