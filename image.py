from PIL import Image


def merge_captcha():
    newImage = Image.new('RGBA', (320, 160))
    newImage.paste(Image.open('B.png'), (0, 0))
    newImage.paste(Image.open('hint.png'), (0, 100))
    newImage.paste(Image.open('A.png'), (0, 130))
    newImage.save('C.png')


if __name__ == '__main__':
    merge_captcha()
