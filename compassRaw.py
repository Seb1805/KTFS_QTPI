from sense_hat import SenseHat

sense = SenseHat()
raw = sense.get_compass_raw()
print("x: {x}, y: {y}, z: {z}".format(**raw))

# alternatives
print(sense.compass_raw)