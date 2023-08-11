from sense_hat import SenseHat

sense = SenseHat()
orientation = sense.get_orientation()
print("p: {pitch}, r: {roll}, y: {yaw}".format(**orientation))

# alternatives
print(sense.orientation)
