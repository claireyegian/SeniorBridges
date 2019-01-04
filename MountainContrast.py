#Claire Yegian
#MountainContrast.py - mountain photo contrast enhancing filter

from PIL import Image,ImageDraw

def FixRGB(val):
    if val < 0:
        return(0)
    elif val > 255:
        return(255)
    else:
        return val

image = Image.open('MountainOverExposed.png')
pixel = image.load()
for x in range(image.width):
    for y in range(image.height):
        R = pixel[x,y]
        if R < 96:
            R = FixRGB(R - (abs(R-128)//50))
        elif R > 95:
            R = FixRGB(R + (R-95))
        ImageDraw.Draw(image).point((x,y),(R))

image.save('Mountain6.png')



#contrast decreasing filter
from PIL import Image,ImageDraw

def FixRGB(val):
    if val < 0:
        return(0)
    elif val > 255:
        return(255)
    else:
        return val

image = Image.open('Mountain.png')
pixel = image.load()
for x in range(image.width):
    for y in range(image.height):
        R = pixel[x,y]
        if R < 128:
            R = FixRGB(R - 30)
        elif R > 127:
            R = FixRGB(R - 50)
        ImageDraw.Draw(image).point((x,y),(R))

image.save('MountainOverExposed1.png')
