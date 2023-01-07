'''--------------------------------------------------------------------------------------------------------------------------------
Search Functionality 

Uses selenium to gather information from exernal websites through firefox
--------------------------------------------------------------------------------------------------------------------------------'''

import sys
import os

#pyqt5 
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QVBoxLayout, QListWidget

#selenium
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class Search(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(1200,900)

        #PyQt5 list of Manga Titles
        self.manga_list = QListWidget()
        #dict of manga titles (key) and their urls (value)
        self.manga_dict = {}
        #input from user to be sent to the website
        self.mangas = 0

        mainLayout = QVBoxLayout()

        #search bar in the window
        self.search = QLineEdit()
        self.search.setPlaceholderText("Enter Manga Name...May take up to 5 seconds to load results...")
        self.search.setStyleSheet('font-size: 35px; height: 60px')
        mainLayout.addWidget(self.search)
        self.setLayout(mainLayout)

        self.search.returnPressed.connect(self.external_search)

        mainLayout.addWidget(self.manga_list)

    def external_search(self):
        #function gathers the search results from the given website we are accessing by inserting the user input directly into
        #the search bar on the given website (send_keys sends user input to the website)
        self.manga_list.clear()
        if self.mangas != 0:
            self.mangas.clear()
        self.mangas = driver.find_element(By.ID, "input-header-search")
        self.mangas.send_keys(self.search.text())
       
        self.get_manga_list()
    
    def get_manga_list(self):
        #function gathers the list returned by the website
        self.manga_list.clear()
        try:
            #waits for 5 seconds for the website to return search results
            WebDriverWait(driver, 5).until(
                    EC.visibility_of_element_located((By.CLASS_NAME, "search-result")))
        except TimeoutException as exception:
            print(exception)
        
        names = driver.find_elements(By.CLASS_NAME, "novel__item")
        for item in names:
            #if the current item in 'names' had a header tag_name, then the item is both added to 
            #'manga_list' (the title is added) and added to 'manga_dict'  (title and url)
            if item.find_element(By.XPATH, "./..").tag_name != "p":
                dict_value = item.find_element(By.PARTIAL_LINK_TEXT, '').get_attribute('href')
                self.manga_list.addItem(item.text)
                self.manga_dict.update({item.text:dict_value})

        self.get_dict()
    
    def get_dict(self):
        #returns the dictionary of manga (key:value) -> (manga-title:url)
        print(self.manga_dict)
        return self.manga_dict

if __name__ == '__main__':
    abs_path = os.path.dirname(__file__)
    option = Options()
    option.headless = False
    driver = webdriver.Firefox(options=option, service=Service(abs_path + "\geckodriver.exe"))
    driver.get("https://mangabuddy.com/")

    app = QApplication(sys.argv)
    srch = Search()
    dict = srch.get_dict()
    srch.show()
    sys.exit(app.exec_())