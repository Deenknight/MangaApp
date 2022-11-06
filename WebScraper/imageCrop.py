from PIL import Image
import os
import pageDownloader as pgD
import tempFileCreator as tfc
import shutil
'''
basically call processImg() and it will take all the images from test.py and 
combine them into one image called "img.png"
'''


class Cropper:
    def __init__(self, path):
        self.path = path

    def setPath(self, path):
        self.path = path

    def cropSides(self, inImage, start, width):  # general purpose, for inbetween imgs
        
        image = Image.open(f"{self.path}\\{inImage}")
        height = image.height
        return image.crop((start, 5, start+width, height))
        # newImage.save(path)

    def cropTop(self, inImage, start, width):  # for first img
        
        image = Image.open(f"{self.path}\\{inImage}")
        height = image.height
        return image.crop((start, 453, start+width, height))

    def cropBottom(self, inImage, start, width):  # for last img
        
        image = Image.open(f"{self.path}\\{inImage}")
        height = image.height
        return image.crop((start, 5, start+width, height-100))


def processImg(temp_path, dir_path, start, width, chapter_name):  # crop all images and then combine them at the end
    crop = Cropper(temp_path)
    image = []
    img2 = None
    for path in os.listdir(temp_path):
        if os.path.isfile(os.path.join(temp_path, path)):
            image.append(path)

    for i in image:
        if i == image[0]:
            img1 = crop.cropTop(i, start, width)
        elif i == image[-1]:
            img2 = crop.cropBottom(i, start, width)
        else:
            img2 = crop.cropSides(i, start, width)
        if img2 != None:
            dst = Image.new('RGB', (img1.width, img1.height + img2.height))
            dst.paste(img1, (0, 0))
            dst.paste(img2, (0, img1.height))
            img1 = dst

    dst.save(
        f'{dir_path}\\{chapter_name}.png')


def preClean(folder):

    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (file_path, e))

    pass


if __name__ == "__main__":
    path = os.path.dirname(__file__)

    temp_path = tfc.createFolder()
    dir_path = os.path.join(path, "manga")

    preClean(dir_path)
    url = "https://mangabuddy.com/the-eminence-in-shadow/chapter-46"
    start, width = pgD.openUrl(url, temp_path, True)

    processImg(temp_path, dir_path, start, width)

    tfc.delFolder()
    pass
