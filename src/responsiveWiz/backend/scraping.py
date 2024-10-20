import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

from responsiveWiz.utils import print
from dataLoader import getJsonData

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

import time
import json
import argparse
import shutil
from tqdm import tqdm

print("Scraping the website for screenshots", "green")

class ResponsiveWiz:
    def __init__(self, args):
        self.chrome_options = Options()
        if args.hide_output:
            self.chrome_options.add_argument("--headless")
            self.chrome_options.add_argument("--no-sandbox")
            self.chrome_options.add_argument("--disable-dev-shm-usage")
            print("Hiding output", "yellow")
        
        assert int(args.level) in [0, 1, 2], "Level should be 0, 1 or 2"
        self.level = args.level
                    
        dir_path = f'src/responsiveWiz/uploads/{args.url.replace("https://", "").replace("/", "")}'
        if os.path.exists(dir_path):
            shutil.rmtree(dir_path)

        os.makedirs(dir_path)
            
        
        self.dataPath = "src/responsiveWiz/data"
        self.driver = webdriver.Chrome(options=self.chrome_options)
        
        if args.animation_experimental:
            print("Disabling Animations/Transistions in the webpage for cleaner screenshots", "yellow")
            with open('src/responsiveWiz/data/disableAnimations.js', 'r') as file:
                self.jsCode = file.read()
        else:
            self.jsCode = None
            
        self.url = args.url
        
        print("\n")
    
    def save_screenshots(self):
        dimensions = self.__get_json_data(level=self.level)

        len_dimensions = len(dimensions)
        
        for index, (width, height) in enumerate(dimensions):
            self.driver.set_window_size(width, height)
            self.driver.get(self.url)

            if self.jsCode is not None:
                self.driver.execute_script(self.jsCode)

            base_dir = f'src/responsiveWiz/uploads/{self.url.replace("https://", "").replace("/", "")}/{width}x{height}'
            os.makedirs(base_dir, exist_ok=True)

            total_height = self.driver.execute_script("return document.body.scrollHeight")
            viewport_height = self.driver.execute_script("return window.innerHeight")
            scroll_position = self.driver.execute_script("return window.pageYOffset")

            scroll = 0
            
            self.driver.execute_script(f"window.scrollTo(0, {scroll});")
            scroll_position = self.driver.execute_script("return window.pageYOffset")
            
            total_scrolls = (total_height // viewport_height)
            
            parts = 0
            
            with tqdm(total=total_scrolls, desc=f'{width}x{height} | {index + 1}/{len_dimensions}', unit='scroll') as pbar:
                while scroll_position + viewport_height < total_height:
                    parts += 1
                    
                    scroll += viewport_height
                    self.driver.execute_script(f"window.scrollTo(0, {scroll});")
                    
                    time.sleep(0.005)
                    
                    total_height = self.driver.execute_script("return document.body.scrollHeight")
                    viewport_height = self.driver.execute_script("return window.innerHeight")
                    scroll_position = self.driver.execute_script("return window.pageYOffset")
                    
                    screenshot_path_update = f"{base_dir}/{parts}.png"
                    self.driver.save_screenshot(screenshot_path_update)

                    pbar.update(1)
        
        base_dir.split('/')
        base_dir = '/'.join(base_dir.split('/')[:-1])
        print(f"Saved screenshots at {base_dir}", "green") 
    
    def quit(self):
        self.driver.quit()
    
    def __get_json_data(self, level: int = 0):
        jsonPath = self.dataPath + '/responsiveOptions.json'
        jsonData = getJsonData(jsonPath)
        
        level = str(level)
        
        assert level in jsonData, f"Level {level} not found in JSON"
        
        dimensions = []
        
        for key in jsonData[level]['dimensions']:
            width, height = map(int, key.split('x'))
            dimensions.append((width, height))
            
        return dimensions
        
def main() -> None:
    parser = argparse.ArgumentParser(description='Runs the ResponsiveWiz tool')
    parser.add_argument('--animation-experimental', action='store_true', help='Disables Animations/Transistions in the webpage for cleaner screenshots')
    parser.add_argument('--url', type=str, required=True, help='The URL of the website to take screenshots of')
    parser.add_argument('--hide-output', action='store_true', help='Hides the live preview of the screenshots being taken')
    parser.add_argument('--level', type=str, required=True, help='How many types of screens to select? (0, 1, 2)')
    
    args = parser.parse_args()
    
    wiz = ResponsiveWiz(args)
    wiz.save_screenshots()

if __name__ == '__main__':
    main()