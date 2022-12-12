
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.action_chains import ActionChains
import os
import json
import time


def openUrl(url, savingDir=None, headless=False, title = "the-eminence-in-shadow", chapter = 46):

    # get  absolute path
    path = os.path.dirname(__file__)
    option = Options()
    option.headless = headless
    #option.binary_location = r"C:\Program Files\Mozilla Firefox\firefox.exe"
    driver = webdriver.Firefox(options=option, service=FirefoxService(
        GeckoDriverManager().install()))  # make firefox browser

    adblockPath = path+"\\ublock_origin-1.44.4.xpi"
    driver.install_addon(adblockPath)

    # load the site
    driver.get(url)

    if option.headless:
        time.sleep(2)
    # remove the two popups

    chapter_img_container = driver.find_element(By.XPATH, '//*[@id="chapter-images"]')
    chapter_images = chapter_img_container.find_elements(By.CLASS_NAME, "chapter-image")

    download_images(f"{path}\\manga\\{title}\\{chapter}", chapter_images)

    # custom save screenshots

    # close browser
    print("done")
    driver.close()

    return


def download_images(chapter_folder, images):
    if not os.path.exists(chapter_folder):
        os.makedirs(chapter_folder)

    index = 0
    for image in images:
        image_file = open(f"{chapter_folder}\\{index}.png", 'wb')
        image_file.write(image.screenshot_as_png)
        image_file.close()
        index += 1
    
    


if __name__ == "__main__":
    url = "https://mangabuddy.com/the-eminence-in-shadow/chapter-46"
    path = os.path.dirname(__file__)
    openUrl(url, path+"\\manga", False)
