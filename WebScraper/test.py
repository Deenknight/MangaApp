
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By 
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.action_chains import ActionChains


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
    
    adblockPath = path+"\\ublock_origin-1.44.4.xpi" 
    driver.install_addon(adblockPath)


    # load the site
    driver.get(url)

    # remove the two popups
    removePopups(driver)

    # custom save screenshots
    save_screenshot(driver=driver, path=path+"\\manga\\")

    # close browser
    print("done")
    driver.close()

def removePopups(driver: webdriver.Firefox):
    # remove the cookies tab at the bottom
    driver.execute_script("acceptCookies()")

    # remove the google thingy that took me 3 hours to implement
    body = driver.find_element(By.XPATH, "/html/body")
    action = ActionChains(driver)
    action.move_to_element_with_offset(body, 591, -288)
    action.click()
    action.perform()



    


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
    delay = 0.5

    
    while True:
        
        scrollHeight = scrollIncrement*multiplier

        # if the next scroll will go over, do some more work
        # not sure if necessary, could just change the loop condition
        if scrollHeight+scrollIncrement > maxHeight:
            
            driver.set_window_size(required_width, maxHeight-scrollHeight)
            driver.execute_script(f"window.scrollTo(0, {scrollHeight})")
            time.sleep(delay)
            driver.save_screenshot(f"{path}{multiplier}.png")
            break
        
        driver.execute_script(f"window.scrollTo(0, {scrollHeight})")
        time.sleep(delay)
        driver.save_screenshot(f"{path}{multiplier}.png")
        
        multiplier += 1
        
    
    # reset browser size
    driver.set_window_size(original_size['width'], original_size['height'])


        
def scrollDown(driver, height):
    
    driver.execute_script(f"window.scrollTo(0, {height})") 


if __name__ == "__main__":
    url = "https://mangabuddy.com/youkoso-jitsuryoku-shijou-shugi-no-kyoushitsu-e/chapter-43"
    openUrl(url)

