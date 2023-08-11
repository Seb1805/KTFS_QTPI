from sense_hat import SenseHat

sense = SenseHat()
raw = sense.get_accelerometer_raw()
print("x: {x}, y: {y}, z: {z}".format(**raw))

# alternatives
print(sense.accel_raw)
print(sense.accelerometer_raw)