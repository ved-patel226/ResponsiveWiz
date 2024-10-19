from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import json


class ResponsiveWiz:
    def __init__(self, url):
        self.url = url
        self.chrome_options = Options()
        # self.chrome_options.add_argument("--headless")
        # self.chrome_options.add_argument("--no-sandbox")
        # self.chrome_options.add_argument("--disable-dev-shm-usage")
        
        self.dataPath = "src/responsiveWiz/data"
        self.driver = webdriver.Chrome(options=self.chrome_options)
    
    def get_screenshot(self):
        self.__get_json_data()
        
        self.driver.get(self.url)
        self.driver.save_screenshot('screenshot.png')
        self.driver.quit()
        
    def __get_json_data(self):
        jsonPath = self.dataPath + '/responsiveOptions.json'
        print(jsonPath)

def main() -> None:
    responsive = ResponsiveWiz('https://www.google.com')
    responsive.get_screenshot()

if __name__ == '__main__':
    main()