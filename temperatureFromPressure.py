from sense_hat import SenseHat

sense = SenseHat()
temp = sense.get_temperature_from_pressure()
print("Temperature: %s C" % temp)