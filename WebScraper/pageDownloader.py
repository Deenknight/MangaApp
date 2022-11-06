import pageScraper as ps

import requests
import shutil





def downloadImages(urls, title, chapter):
    # Make a request for the specific image

    imType = getImageType(urls[0])

    for i in range(len(urls)):
        r = requests.get(urls[i], stream=True)

        if r.status_code == 200: # status_code == 200 if successful
            with open(f"{title}\\{chapter}\\{i+1}{imType}", 'wb') as f:
                r.raw.decode_content = True
                shutil.copyfileobj(r.raw, f)

def getImageType(link):
    return link[link.rindex("."):]

    

if __name__ == "__main__":

    url = "https://mangamirror.com/manga/19019-dangerous-convenience-store/chapter-2"
    title = "dangerous-convenience-store"
    chapter = 2

    imgs = ps.getPageUrls(url)

    downloadImages(imgs, title, chapter)
    
