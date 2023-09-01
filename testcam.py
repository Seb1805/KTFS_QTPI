#Imports
import argparse
import sys
import time
import cv2
from timeit import time
from picamera2 import Picamera2, Preview
from matplotlib import pyplot as plt

picam2 = Picamera2()
picam2.start_preview(Preview.QTGL)
picam2.start()
image = picam2.capture_array()

image = cv2.resize(image, (640, 480))    # 3280, 2464)
# image = cv2.cvtColor(image, 0)

plt.imshow(image)
plt.show()
time.sleep(30)