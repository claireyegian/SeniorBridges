#Claire Yegian
#MargoRedFilter.py - turns Margo image red

from PIL import Image,ImageDraw

pix = Image.open('Margo.png')
pix2 = Image.open('BandW.png')
pixel = pix.load()
for x in range(pix.width):
    for y in range(pix.height):
        D = 250
        E = 255
        while D >= 0:
            if pixel[x,y] >= D and pixel[x,y] <= E:
                ImageDraw.Draw(pix2).point((x,y),(pixel[x,y],0,0))
            D -= 5
            E -= 5

pix2.save('Margo4.png')
