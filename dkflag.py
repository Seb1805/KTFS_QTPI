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


def checkSpace(x,y):
    col = (x-1)*3
    row = (y-1)*3
    arg = first_list[row*8 + col]
    if(arg == [0,0,0]):
        return True
    return False


botCol = (0,0,128)
humanCol = (128,0,0)
blinkCol = (245,8,18)

#Draw the main board
drawMainBoard()


#Start in (2,2)

playing = True
player1 = True


while playing:
    curPosX = 2
    curPosY = 2
    first_list = sense.get_pixels()
    while player1:

        sense.set_pixels(first_list)
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
                elif event.direction == "left":
                    if(curPosX > 1):
                        curPosX-=1
                elif event.direction == "up":
                    if(curPosY > 1):
                        curPosY-=1
                elif event.direction == "down":
                    if(curPosY < 3):
                        curPosY+=1
                elif event.direction == "middle":
                    if checkSpace(curPosX,curPosY):
                        fillSpace(curPosX,curPosY,humanCol)
                        first_list = sense.get_pixels()
                        player1 = not player1
    
    curPosX = 2
    curPosY = 2
    first_list = sense.get_pixels()

    while not player1:


        sense.set_pixels(first_list)
 

        fillSpace(curPosX,curPosY,botCol)
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
                elif event.direction == "left":
                    if(curPosX > 1):
                        curPosX-=1
                elif event.direction == "up":
                    if(curPosY > 1):
                        curPosY-=1
                elif event.direction == "down":
                    if(curPosY < 3):
                        curPosY+=1
                elif event.direction == "middle":
                    if checkSpace(curPosX,curPosY):
                        fillSpace(curPosX,curPosY,botCol)
                        first_list = sense.get_pixels()
                        player1 = not player1
    



def checkWin():
    winList = sense.get_pixels():
    pos1 = winList[0];
    pos2 = winList[3];
    pos3 = winList[6];
    pos4 = winList[24];
    pos5 = winList[27];
    pos6 = winList[30];
    pos7 = winList[48];
    pos8 = winList[51];
    pos9 = winList[54];

    if(pos1 == pos2 == pos3)
        return True
    else if (pos3 == pos4 == pos5)
        return True
    else if (pos6 == pos7 == pos8)
        return True
    else if(pos1 == pos4 == pos7)
        return True
    else if (pos2 == pos5 == pos8)
        return True
    else if (pos3 == pos6 == pos9)
        return True
    else if (pos1 == pos5 == pos9)
        return True
    else if (pos3 == pos5 == pos7)
        return True
    return False