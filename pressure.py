from sense_hat import SenseHat

sense = SenseHat()
pressure = sense.get_pressure()
print("Pressure: %s Millibars" % pressure)

# alternatives
while True:
    print("Pressure: %s Millibars" % pressure)
    print(sense.pressure)