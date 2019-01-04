#Claire Yegian
#ContrastFilter1.py - increases contrast

from PIL import Image,ImageDraw

def FixRGB(val):
    if val < 0:
        return(0)
    elif val > 255:
        return(255)
    else:
        return val

image = Image.open('LowContrastImage.png')
pixel = image.load()
for x in range(image.width):
    for y in range(image.height):
        R = pixel[x,y][0]
        G = pixel[x,y][1]
        B = pixel[x,y][2]
        if R < 128:
            R = FixRGB(R - (abs(R-128)//4))
            G = FixRGB(G - (abs(G-128)//4))
            B = FixRGB(B - (abs(B-128)//4))
        elif R > 127:
            R = FixRGB(R + ((R-127)//10))
            G = FixRGB(G + ((G-127)//10))
            B = FixRGB(B + ((B-127)//10))
        ImageDraw.Draw(image).point((x,y),(R,G,B))

image.save('RegularImage.png')
