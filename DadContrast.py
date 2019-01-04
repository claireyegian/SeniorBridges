#Claire Yegian
#DadContrast.py - dad contrast enhancement filter

from PIL import Image,ImageDraw

def FixRGB(val):
    if val < 0:
        return(0)
    elif val > 255:
        return(255)
    else:
        return val

image = Image.open('DadLowContrast.png')
pixel = image.load()
for x in range(image.width):
    for y in range(image.height):
        R = pixel[x,y]
        if R < 128:
            R = FixRGB(R - (abs(R-128)//2) + 20)
        elif R > 127:
            R = FixRGB(R + ((R-127)//17) + 20)
        ImageDraw.Draw(image).point((x,y),R)

image.save('DadContrast5.png')
