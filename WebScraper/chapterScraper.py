from bs4 import BeautifulSoup

import requests
import shutil


class ChapterScraper:

    def findChapters(self, title):
        '''
        gonna say right now some of titles in the url are acutally 
        austitic like scott, probably be a problem later
        '''
        chapterDict = {}
        # load the page into html_text
        html_text = requests.get(f"https://mangabuddy.com/{title}")

        # parse the text using the lxml parser
        soup = BeautifulSoup(html_text.text, 'lxml')

        # Find chapters
        for ultag in soup.find_all('ul', {'class': 'chapter-list'}):
            for litag in ultag.find_all('li'):
                titleTag = litag.find('a').get('title')
                link = litag.find('a').get('href')
                chapterDict[titleTag] = link
        '''
        YES I KNOW THAT 2 FOR LOOPS IS REALLY STUPID BUT FOR SOME REASON 
        DOING IT THIS WAY IS FASTER, WHY? FUCK YOU
        '''

        self.chapterDict = chapterDict

    def getNames(self):  # Returns ALL names
        return list(self.chapterDict.keys())

    def getLink(self, name):  # returns link associated to name
        return self.chapterDict[name]


if __name__ == "__main__":
    cs = ChapterScraper()
    cs.findChapters(title='mbx12-dangerous-convenience-store')
    names = cs.getNames()
    link = cs.getLink(names[1])
    print(names[1])
    print(link)
