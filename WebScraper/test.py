
from selenium import webdriver
from selenium.webdriver.firefox.service import Service

from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.action_chains import ActionChains
import os
import json
import time



def openUrl(url):
    abs_path = os.path.dirname(__file__)
    option = Options()
    option.headless = False
    driver = webdriver.Firefox(options=option, service=Service(abs_path + "\geckodriver.exe"))
    #driver.install_addon(r"Python/Comic Reader/adblock.xpi", temporary=True)



    driver.get(url)

    time.sleep(5)
    driver.save_screenshot('ss.png')

    save_screenshot(driver=driver, path="bob.png")

    print("done")

def save_screenshot(driver: webdriver.Firefox, path: str = '/tmp/screenshot.png') -> None:
    # Ref: https://stackoverflow.com/a/52572919/
    original_size = driver.get_window_size()
    required_width = driver.execute_script('return document.body.parentNode.scrollWidth')
    required_height = driver.execute_script('return document.body.parentNode.scrollHeight')
    driver.set_window_size(required_width, required_height + 74)
    # driver.save_screenshot(path)  # has scrollbar
    driver.save_screenshot(path)  # avoids scrollbar
    driver.set_window_size(original_size['width'], original_size['height'])




if __name__ == "__main__":
    url = "https://mangabuddy.com/youkoso-jitsuryoku-shijou-shugi-no-kyoushitsu-e/chapter-43"
    openUrl(url)

