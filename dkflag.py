from sense_hat import SenseHat
import time
from PIL import Image
import os

sense = SenseHat()


def drawMainBoard():
    # Open image file
    image_file = os.path.join(
    os.sep,"/home","ktfs/SenseHAT","4.png")                                                                                                                                                                                                                        
    img = Image.open(image_file)

    sense.load_image(image_file)
    rgb_img = img.convert('RGB')
    # Generate rgb values for image pixels
    image_pixels = list(rgb_img.getdata())

def fillSpace(x, y, color):

    col = (x-1)*3
    row = (y-1)*3


    sense.set_pixel(col, row, color) 
    sense.set_pixel(col + 1, row, color) 
    sense.set_pixel(col, row + 1, color) 
    sense.set_pixel(col, row + 1, color) 
    sense.set_pixel(col, row + 1, color) 
    sense.set_pixel(col + 1, row + 1, color) 


sense.set_rotation(180)

botCol = (0,0,128)
humanCol = (128,0,0)
blinkCol = (245,8,18)


#Draw the main board
drawMainBoard()

fillSpace(1,1,humanCol)
fillSpace(1,2,botCol)
fillSpace(2,1,humanCol)
fillSpace(3,1,humanCol)
fillSpace(3,1,botCol)
sense.set_pixel(3,7,botCol)
#Corner 1 Example
# sense.set_pixel(0,1,(255,0,0))
# sense.set_pixel(1,0,(255,0,0))
# sense.set_pixel(1,1,(255,0,0))
# sense.set_pixel(0,0,(255,0,0))


#Start in (2,2)


turn = True
curPosX = 2
curPosY = 2
while True:


    fillSpace(curPosX,curPosY,blinkCol)
    time.sleep(0.1)
    fillSpace(curPosX,curPosY,(0,0,0))
    time.sleep(0.1)
    #TODO: Set bool false when enter input detected

    for event in sense.stick.get_events():
        if event.action == 'pressed':
            print(event.direction)
            if event.direction == "right":
                if(curPosX < 3):
                    curPosX+=1
            else if event.direction == "left":
                if(curPosX > 1):
                    curPosX-=1
            else if event.direction == "up":
                if(curPosY < 3):
                    curPosY+=1
            else if event.direction == "down":
                if(curPosY > 1):
                    curPosY-=1

