from sense_hat import SenseHat

sense = SenseHat()
north = sense.get_compass()
print("North: %s" % north)

# alternatives
while True:
    print(sense.compass)