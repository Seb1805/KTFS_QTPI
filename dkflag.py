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






#Draw the main board
drawMainBoard()


#Corner 1 Example
# sense.set_pixel(0,1,(255,0,0))
# sense.set_pixel(1,0,(255,0,0))
# sense.set_pixel(1,1,(255,0,0))
# sense.set_pixel(0,0,(255,0,0))




