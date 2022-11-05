from bs4 import BeautifulSoup

import requests
import shutil


class ChapterScraper():
    def __init__(self, title='mbx12-dangerous-convenience-store') -> None:
        self.title = title
        pass

    def getChapters(self):
        '''
        gonna say right now some of titles in the url are acutally 
        austitic like scott, probably be a problem later
        '''

        # load the page into html_text
        html_text = requests.get(f"https://mangabuddy.com/{self.title}")

        # parse the text using the lxml parser
        soup = BeautifulSoup(html_text.text, 'lxml')
        # print(soup)

        # Find chapters

        for ultag in soup.find_all('ul', {'class': 'chapter-list'}):
            for litag in ultag.find_all('li'):
                print(litag.get('id'))

        '''
        You would think this solution is faster but for some fucking
        its a lot slower so fuck you
        
        ultag = soup.find('ul', {'class': 'chapter-list'})
        for litag in ultag.find_all('li'):
            print(litag.get('id'))
        '''


...

# [imgAlts.append(alt.attrs['alt']) for alt in images]

# print(imgAlts)


if __name__ == "__main__":
    ChapterScraper = ChapterScraper()
    ChapterScraper.getChapters()
