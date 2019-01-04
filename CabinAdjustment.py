#Claire Yegian
#CabinAdjustment.py - gets rid of light spot in cabin photo

from PIL import Image,ImageDraw

def FixRGB(val):
    if val < 0:
        return(0)
    elif val > 255:
        return(255)
    else:
        return val

image = Image.open('Cabin.png')
pixel = image.load()
for x in range(515,895):
    for y in range(90,525):
        R = FixRGB(pixel[x,y]-1)
        ImageDraw.Draw(image).point((x,y),R)
for x in range(525,885):
    for y in range(100,515):
        R = FixRGB(pixel[x,y]-1)
        ImageDraw.Draw(image).point((x,y),R)
for x in range(535,875):
    for y in range(110,505):
        R = FixRGB(pixel[x,y]-1)
        ImageDraw.Draw(image).point((x,y),R)
A = 550
B = 860
C = 125
D = 490
while A <= 705:
    for x in range(A,B):
        for y in range(C,D):
            R = FixRGB(pixel[x,y]-1)
            ImageDraw.Draw(image).point((x,y),R)
    A += 5
    B -= 5
    C += 5
    D -= 5

image.save('CabinBox2.png')
