Claires-MacBook-Air:SeniorBridges claireyegian$ source bin/activate
#activates virtual environment
(SeniorBridges) Claires-MacBook-Air:SeniorBridges claireyegian$ python3
Python 3.7.1 (v3.7.1:260ec2c36a, Oct 20 2018, 03:13:28) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> from PIL import Image, ImageDraw
>>> image = Image.open('horse.png')
>>> px = image.load()
>>> px[20,19]
(198, 210, 226, 255)
>>> px[0,0]
(155, 179, 213, 255)
>>> px[200,200]
(14, 12, 13, 255)
>>> px[0,0][:3] #only takes first 3
(155, 179, 213) #tuple - basically a list but cannot be changed
>>> ImageDraw.Draw(image).point((50,50),(255,255,255))
#changes specific pixel to specific color (pixel 50,50 to white)
>>> for x in range (50,100): #creates a white box on the image
        for y in range (50,100):
            ImageDraw.Draw(image).point((x,y),(255,255,255))
>>> image.save('horsebox.png') #saves image
>>> image.width #gives width of image in pixels
>>> image.height #gives height of image in pixels
>>> for x in range(image.width):
...     for y in range(image.height):
...             ImageDraw.Draw(image).point((x,y),(px[x,y][0]//2,px[x,y][1]//2,px[x,y][2]//2))
#double slash because the pixels can only be in integer format
#add fix function
