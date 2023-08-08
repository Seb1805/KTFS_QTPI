from sense_hat import SenseHat
import time
from PIL import Image
import os

# Open image file

sense = SenseHat()
image_file = os.path.join(
os.sep,"/home","ktfs/SenseHAT","2.png")                                                                                                                                                                                                                        
img = Image.open(image_file)

sense.load_image(image_file)

print(image_file)
# Generate rgb values for image pixels
rgb_img = img.convert('RGB')
image_pixels = list(rgb_img.getdata())

# Get the 64 pixels you need
