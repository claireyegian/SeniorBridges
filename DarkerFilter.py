#Claire Yegian
#DarkerFilter.py - darkens image

from PIL import Image,ImageDraw

def FixRGB(val):
    if val < 0:
        return(0)
    elif val > 255:
        return(255)
    else:
        return val

image = Image.open('RegularImage.png')
pixel = image.load()
for x in range(image.width):
    for y in range(image.height):
        R = FixRGB(pixel[x,y][0]-50)
        G = FixRGB(pixel[x,y][1]-50)
        B = FixRGB(pixel[x,y][2]-50)
        ImageDraw.Draw(image).point((x,y),(R,G,B))

image.save('DarkenedImage.png')
