from PIL import Image


def imageCropper(image=r'bob.png'):
    # Opens a image in RGB mode
    im = Image.open(image)
    # 170,1520,1069,16244 i want to crop to this
    # 0,0,1255,16293 res of full image
    height = im.height

    x1 = 170
    x2 = 1069
    y1 = 1520
    y2 = height - 49

    imCropped = im.crop((x1, y1, x2, y2))

    # Shows the image in image viewer
    imCropped.show()
    pass


if __name__ == "__main__":
    imageCropper()
    pass
