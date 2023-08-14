from sense_hat import SenseHat
import mariadb_cl as db


sense = SenseHat()

# print("Pressure: %s Millibars" % pressure)

# alternatives
while True:
    pressure = sense.get_pressure()
    # print("Pressure: %s Millibars" % pressure)
    # print(sense.pressure)
    db.insertData('Pressure','PressureInHectoPascal', pressure)


