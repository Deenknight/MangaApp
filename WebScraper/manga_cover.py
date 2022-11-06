from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
import os

def open_website(url):
    path = os.path.dirname(__file__)
    option = Options()
    option.headless = False
    driver = webdriver.Firefox(options=option, service=Service(path + "\geckodriver.exe")) # make firefox browser
    adblockPath = path+"\\ublock_origin-1.44.4.xpi" 

    driver.install_addon(adblockPath)
    driver.get(url)

    take_screenshots(driver=driver, path=path+"\manga_covers\\cover_img")

    print("cum stain")
    driver.close()

def take_screenshots(driver: webdriver.Firefox, path: str = '/tmp/screenshot.png'):
    body = driver.find_element(by=By.XPATH, value='//*[@id="cover"]/div[1]/img')
    body.screenshot(f"{path}.png")
    

if __name__ == "__main__":
    url = "https://mangabuddy.com/youkoso-jitsuryoku-shijou-shugi-no-kyoushitsu-e"
    open_website(url)