import imageCrop as imc
import pageDownloader as pgd
import tempFileCreator as tfc
import chapterScraper as cs


def loadPages(chapter_name, chapter_url, save_dir_path):

    temp_path = tfc.createFolder()
    

    imc.preClean(save_dir_path)
    start, width = pgd.openUrl(chapter_url, temp_path, True)

    imc.processImg(temp_path, save_dir_path, start, width, chapter_name)

    tfc.delFolder()

def getChapters(title_url):
    return cs.findChapters(title_url)

    



if __name__ == "__main__":
    pass