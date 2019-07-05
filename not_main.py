from math import *
from PIL import Image

size = (400,400)
pi = 3.14
diam = 201
rad = int(diam/2)
Ax0 = 150
Ay0 = 150
Acolor = (0,128,255)

dx = 21
dy = 41
tx = int(dx/2)
ty = int(dy/2)
Bx0 = 0
By0 = 0
Bcolor = (255,0,0)

img = Image.new( 'RGB', size, "white")
pixels = img.load()
Sumcolor = (128,194,255)

def trCoord(x,y):
    x = int(x+diam/2)
    y = int(y+diam/2)
    return x,y

def addPixel(x,y,color):
    x,y = trCoord(x,y)
    pixels[x,y] = color

def getPixelColor(x,y):
    x,y = trCoord(x,y)
    return pixels[x,y]


for i in range(-rad,rad):
    for j in range(-rad,rad):
        if i**2 + j**2 < rad**2:
            addPixel(i+Ax0,j+Ay0,Acolor)

BCoord = []
t = radians(20)
for i in range(-dx,dx):
    for j in range(-dy,+dy):
        if abs(i-Bx0) < tx and abs(j-By0) < ty:
            addPixel(int(i*cos(t)) - int(j*sin(t)),int(i*sin(t))+int(j*cos(t)),Bcolor)
            #addPixel(int(r*cos(t)+0.5),int(r*sin(t)+0.5),Bcolor)
            #addPixel(i,j,Bcolor)
            BCoord.append((int(i*cos(t)) - int(j*sin(t)),int(i*sin(t))+int(j*cos(t))))
            #BCoord.append((int(r*cos(t)+0.5),int(r*sin(t)+0.5)))
            #BCoord.append((i,j))
for i in range(-dx,dx):
    for j in range(-dy,dy):
        if getPixelColor(i+1, j) == Bcolor and \
        getPixelColor(i-1, j) == Bcolor and \
        getPixelColor(i, j+1) == Bcolor and getPixelColor(i, j-1) == Bcolor:
            addPixel(i,j,Bcolor)

def MinkowskiSum(x,y):
    for (bx,by) in BCoord:
        nx = x + bx
        ny = y + by
        if getPixelColor(nx,ny) != Acolor:
            addPixel(nx,ny,Sumcolor)

for i in range(-rad,rad):
    for j in range(-rad,rad):
        #For Circle
        if (i**2 + j**2 < rad**2) and (i**2 + j**2 > (rad-2)**2):
            MinkowskiSum(i+Ax0,j+Ay0)
img.show()
