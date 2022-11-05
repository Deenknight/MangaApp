from bs4 import BeautifulSoup

import requests
import shutil


class webScraper():
    def __init__(self) -> None:
        pass
        
    def getChapter(self, chaterNum=0):
        
        # load the page into html_text
        html_text = requests.get("https://mangabuddy.com/mbx12-dangerous-convenience-store/chapter-{chapterNum}")
        
        # parse the text using the lxml parser
        soup = BeautifulSoup(html_text.text, 'lxml')


        # Find image
        images = soup.findAll('img')
        firstImage = images[2]
        imgAlts = []

        [imgAlts.append(alt.attrs['alt']) for alt in images]

        print(imgAlts)
        """ urlBase = "https:"

        # Make a request for the specific image
        r = requests.get(urlBase + imgURL, stream=True)

        if r.status_code == 200: # status_code == 200 if successful
            with open("imgs\\img.png", 'wb') as f:
                r.raw.decode_content = True
                shutil.copyfileobj(r.raw, f) """





if __name__ == "__main__":
    webScraper = webScraper()
    webScraper.getChapter(0)
