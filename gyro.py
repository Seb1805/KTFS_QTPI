from sense_hat import SenseHat

sense = SenseHat()



# while True:
#     raw = sense.get_compass_raw()
#     print("x: {x}, y: {y}, z: {z}".format(**raw))
#     print(sense.compass_raw)
# alternatives





sense = SenseHat()
raw = sense.get_gyroscope_raw()
print("x: {x}, y: {y}, z: {z}".format(**raw))

# alternatives
print(sense.gyro_raw)
print(sense.gyroscope_raw)
