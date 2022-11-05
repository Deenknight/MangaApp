from bs4 import BeautifulSoup

import requests
import shutil


class pageScraper():
    def __init__(self, title):
        self.mangaTitle = title

    def setTitle(self, title):
        self.mangaTitle = title

    def getPageUrls(self, chapter):

        html_text = requests.get(f"https://mangabuddy.com/mbx12-dangerous-convenience-store/chapter-{chapter}")
        
        # parse the text using the lxml parser
        soup = BeautifulSoup(html_text.text, 'lxml')


        # Find the div that holds the images
        mainDiv = soup.find("div", id="chapter-images")

        # initialize the list
        imgSrcs = []

        # sift through all the chapter image divs
        for img in mainDiv.find_all('img'):
            imgSrcs.append(f"https:{img.attrs['data-src']}")
        
        return imgSrcs

    





if __name__ == "__main__":
    c = 2

    pageScraper = pageScraper("mbx12-dangerous-convenience-store")
    # print(pageScraper.getPageUrls(c))
    print(pageScraper.getPageUrls(c))
