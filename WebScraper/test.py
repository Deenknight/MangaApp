
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

    # get  absolute path
    path = os.path.dirname(__file__)
    option = Options()
    option.headless = False
    driver = webdriver.Firefox(options=option, service=Service(path + "\geckodriver.exe")) # make firefox browser
    
    #FIXME make it so the path is in the r'' format
    adblockPath = path+"\\ublock_origin-1.44.4.xpi" 

    #FIXME change to fit your path manually :(
    driver.install_addon(r'C:\Users\Deenk\source\repos\Python\HackEdBeta\MangaApp\WebScraper\ublock_origin-1.44.4.xpi')
    #driver.install_addon(r"Python/Comic Reader/adblock.xpi", temporary=True)

    # load the site
    driver.get(url)

    # custom save screenshots
    save_screenshot(driver=driver, path=path+"\\manga\\img")

    # close browser
    print("done")
    driver.close()

def save_screenshot(driver: webdriver.Firefox, path: str = '/tmp/screenshot.png'):
    
    original_size = driver.get_window_size()
    
    # run js scripts to get the width and height of the page
    required_width = driver.execute_script('return document.body.parentNode.scrollWidth')

    # this can be changed 
    # essentially, it is getting the div with id "chapter__content", and finding the length of that
    # that way, we can ignore the comments at the bottom of the page and standardize the cbottom crop
    maxHeight = driver.execute_script('return document.getElementById("chapter__content").clientHeight')

    # obvious
    scrollIncrement = 10000

    # set the size of the browser
    driver.set_window_size(required_width, scrollIncrement)


    multiplier = 0
    scrollHeight = 0

    #TODO fix dogshit code:
    while True:
        
        scrollHeight = scrollIncrement*multiplier

        # if the next scroll will go over, do some more work
        # not sure if necessary, could just change the loop condition
        if scrollHeight+scrollIncrement > maxHeight:
             
            driver.execute_script(f"window.scrollTo(0, {scrollHeight})")
            driver.save_screenshot(f"{path}{multiplier}.png")
            break
        
        driver.execute_script(f"window.scrollTo(0, {scrollHeight})")
        driver.save_screenshot(f"{path}{multiplier}.png")
        multiplier += 1
        time.sleep(5)
    
    # reset browser size
    driver.set_window_size(original_size['width'], original_size['height'])


        
def scrollDown(driver, height):
    
    driver.execute_script(f"window.scrollTo(0, {height})") 


if __name__ == "__main__":
    url = "https://mangabuddy.com/youkoso-jitsuryoku-shijou-shugi-no-kyoushitsu-e/chapter-43"
    openUrl(url)

