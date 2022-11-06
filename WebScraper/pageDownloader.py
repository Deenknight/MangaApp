
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By 
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.action_chains import ActionChains


from selenium.webdriver.common.action_chains import ActionChains
import os
import json
import time



def openUrl(url, savingDir=None, headless=False):

    # get  absolute path
    path = os.path.dirname(__file__)
    option = Options()
    option.headless = headless
    driver = webdriver.Firefox(options=option, service=Service(path + "\geckodriver.exe")) # make firefox browser
    
    adblockPath = path+"\\ublock_origin-1.44.4.xpi" 
    driver.install_addon(adblockPath)


    # load the site
    driver.get(url)

    if option.headless:
        time.sleep(2)
    # remove the two popups
    

    # custom save screenshots
    startPoint, imgWidth = save_screenshot(driver=driver, path=savingDir, headless=headless)

    # close browser
    print("done")
    driver.close()

    return startPoint, imgWidth

def removePopups(driver: webdriver.Firefox, width, height):
    # remove the cookies tab at the bottom
    driver.execute_script("acceptCookies()")

    # remove the google thingy that took me 3 hours to implement
    body = driver.find_element(By.XPATH, "/html/body")
    action = ActionChains(driver)
    x_offset = int(body.size['width']/2)
    y_offset = int(body.size['width']/4)
    action.move_to_element_with_offset(body, width-41-x_offset, 56-y_offset)
    action.click()
    action.perform()



    


def save_screenshot(driver: webdriver.Firefox, path, headless):
    
    original_size = driver.get_window_size()

    removePopups(driver, original_size["width"], original_size['height'])
    
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

    imgWidth = driver.execute_script('return document.getElementById("chapter-images").firstChild.clientWidth')
    startPoint = driver.execute_script('return document.getElementById("chapter-images").firstChild.offsetLeft')


    multiplier = 0
    scrollHeight = 0
    delay = 0.5
    offset = 54.5 if headless else 0
    
    while True:
        
        scrollHeight = scrollIncrement*multiplier - (offset*multiplier)

        # if the next scroll will go over, do some more work
        # not sure if necessary, could just change the loop condition
        if scrollHeight+scrollIncrement > maxHeight:
            
            driver.set_window_size(required_width, maxHeight-scrollHeight+(offset*multiplier*2))
            driver.execute_script(f"window.scrollTo(0, {scrollHeight})")
            time.sleep(delay)
            driver.save_screenshot(f"{path}\\{multiplier}.png")
            break
        
        driver.execute_script(f"window.scrollTo(0, {scrollHeight })")
        time.sleep(delay)
        driver.save_screenshot(f"{path}\\{multiplier}.png")
        
        multiplier += 1
        
    
    # reset browser size
    driver.set_window_size(original_size['width'], original_size['height'])

    return startPoint, imgWidth
    


        
def scrollDown(driver, height):
    
    driver.execute_script(f"window.scrollTo(0, {height})") 

def saveScreen(driver):
    driver.save_screenshot(f"{path}\\test.png")

if __name__ == "__main__":
    url = "https://mangabuddy.com/the-eminence-in-shadow/chapter-46"
    path = os.path.dirname(__file__)
    openUrl(url, path+"\\manga", True)

