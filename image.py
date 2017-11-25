from PIL import Image


def merge_captcha():
    newImage = Image.new('RGBA', (320, 130))
    newImage.paste(Image.open('B.png'), (0, 0))
    newImage.paste(Image.open('A.png'), (0, 100))
    newImage.save('C.png')
