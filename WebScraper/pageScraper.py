from bs4 import BeautifulSoup

import requests
import shutil


class pageScraper():
    def __init__(self, title):
        self.mangaTitle = title

    def setTitle(self, title):
        self.mangaTitle = title

    def getPageUrls(self, chapter=0):
        
        # load the page into html_text
        html_text = requests.get(f"https://mangabuddy.com/mbx12-dangerous-convenience-store/chapter-{chapter}")
        
        # parse the text using the lxml parser
        soup = BeautifulSoup(html_text.text, 'lxml')


        # Find the div that holds the images
        mainDiv = soup.find("div", id="chapter-images")

        imgSrcs = []
        for div in mainDiv.find_all('div'):
            try:
                if 'chapter-image' in div.attrs['class']:
                    contents = str(div.contents[0]).split()
                    url = [item for item in contents if item.startswith("data-src")]
            
                    
                    imgSrcs.append(url[0][10:-1])
            except KeyError:
                continue
        
        return imgSrcs
    





if __name__ == "__main__":
    pageScraper = pageScraper("mbx12-dangerous-convenience-store")
    pageScraper.getPageUrls(chapter=0)
