from sense_hat import SenseHat
import CanWriteToDb.mariadb_cl as db
import time


sense = SenseHat()

# print("Pressure: %s Millibars" % pressure)

# alternatives
while True:
    pressure = sense.get_pressure()
    # print("Pressure: %s Millibars" % pressure)
    # print(sense.pressure)
    db.insertData('Pressure','PressureInHectoPascal', pressure)
    time.sleep(5)


