from PIL import Image
import os
import test

'''
basically call processImg() and it will take all the images from test.py and 
combine them into one image called "img.png"
'''


class Cropper:

    def cropSides(self, inImage):  # general purpose, for inbetween imgs
        path = rf'C:\Users\Julian\repos\hackED beta\project\MangaApp\WebScraper\manga\{inImage}'
        image = Image.open(path)
        height = image.height
        return image.crop((170, 0, 1069, height))
        # newImage.save(path)

    def cropTop(self, inImage):  # for first img
        path = rf'C:\Users\Julian\repos\hackED beta\project\MangaApp\WebScraper\manga\{inImage}'
        image = Image.open(path)
        height = image.height
        return image.crop((170, 453, 1069, height))

    def cropBottom(self, inImage):  # for last img
        path = rf'C:\Users\Julian\repos\hackED beta\project\MangaApp\WebScraper\manga\{inImage}'
        image = Image.open(path)
        height = image.height
        return image.crop((170, 0, 1069, height))


def processImg():  # crop all images and then combine them at the end
    crop = Cropper()
    dir_path = r'C:\Users\Julian\repos\hackED beta\project\MangaApp\WebScraper\manga'
    image = []
    img2 = None
    for path in os.listdir(dir_path):
        if os.path.isfile(os.path.join(dir_path, path)):
            image.append(path)

    for i in image:
        if i == image[0]:
            img1 = crop.cropTop(i)
        elif i == image[-1]:
            img2 = crop.cropBottom(i)
        else:
            img2 = crop.cropSides(i)
        if img2 != None:
            dst = Image.new('RGB', (img1.width, img1.height + img2.height))
            dst.paste(img1, (0, 0))
            dst.paste(img2, (0, img1.height))
            img1 = dst

    dst.save(
        r'C:\Users\Julian\repos\hackED beta\project\MangaApp\WebScraper\manga\img.png')


def preClean():
    import os
    import shutil
    folder = r'C:\Users\Julian\repos\hackED beta\project\MangaApp\WebScraper\manga'
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
    preClean()
    url = "https://mangabuddy.com/mbx13-chainsaw-man/chapter-108-5"
    test.openUrl(url)
    processImg()
    pass
