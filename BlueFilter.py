from PIL import Image,ImageDraw
carol = Image.open('BandW.png')
pixel = carol.load()
for x in range(carol.width):
    for y in range(carol.height):
        if pixel[x,y][0] < 15:
            ImageDraw.Draw(carol).point((x,y),(0,0,10*pixel[x,y][2]))

carol.save('BandW2.png')
