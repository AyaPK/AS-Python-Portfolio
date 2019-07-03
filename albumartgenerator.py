from PIL import Image, ImageDraw, ImageFont
from urllib.request import urlopen
import random
import string

enWords = open("C:\\Users\\Administrator\\Documents\\Words.txt", "r")
wordList = enWords.readlines()


def generateName():
    rand = random.randint(0, len(wordList) - 1)
    name = wordList[rand]
    while name[0] in string.ascii_letters.lower():
        rand = random.randint(0, len(wordList) - 1)
        name = wordList[rand]
    return name
def fullName():
    name = generateName()
    name = name.replace("\n", "")
    return name
artistName = fullName()+" "+fullName()

def pullAlbumWord():
    rand = random.randint(0, len(wordList) - 1)
    name = wordList[rand]
    while name[0] not in string.ascii_letters.lower():
        rand = random.randint(0, len(wordList) - 1)
        name = wordList[rand]
    return name
def makeFullAlbumName():
    wordcount = random.randint(1,5)
    for x in range(0,wordcount):
        albumname = pullAlbumWord()+" "
    albumname = albumname.replace("\n", "")
    albumname = albumname.replace(albumname[0], albumname[0].upper())
    return albumname
albumName = makeFullAlbumName()


fontpath = "C:\\Users\\Administrator\\PycharmProjects\\PyGameTest\\venv\\Lib\\site-packages\\pygame\\tests\\fixtures\\fonts\\test_fixed.otf"
titlefont = ImageFont.truetype(fontpath, 40)
namefont = ImageFont.truetype(fontpath, 80)
W, H = (800,800)
bgImage = Image.open(urlopen("https://picsum.photos/800/800"))
## bgImage = Image.open("C:\\Users\\Administrator\\Documents\\bg1.jpg")
frame = Image.new("RGBA", (800, 800), (0, 0, 0, 0,))
frame.paste(bgImage)
output = ImageDraw.Draw(frame)
arw, arh = output.textsize(artistName, font=namefont)
alw, alh = output.textsize(albumName, font=titlefont)
titleheight = random.randint(2,7)*100
output.text(((W-arw)/2,50), artistName, fill=(255,255,255), font=namefont)
output.text(((W-alw)/2, titleheight), albumName, fill=(255,255,255), font=titlefont)

frame.show()
