#Claire Yegian
#ColorFilter.py - colorizes photo

from PIL import Image,ImageDraw
pix = Image.open('BandW.png')
pixel = pix.load()
for x in range(pix.width):
    for y in range(pix.height):
        if pixel[x,y][0] < 85:
            ImageDraw.Draw(pix).point((x,y),(0,0,pixel[x,y][2]))
        elif pixel[x,y][0] > 85 and pixel[x,y][0] < 170:
            ImageDraw.Draw(pix).point((x,y),(0,pixel[x,y][1],0))
        elif pixel[x,y][0] > 170:
            ImageDraw.Draw(pix).point((x,y),(pixel[x,y][0],0,0))

pix.save('BandW3.png')
