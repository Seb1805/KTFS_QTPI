from sense_hat import SenseHat
import mariadb_cl as db
import time

sense = SenseHat()


while True:
    temp = sense.get_temperature()
    db.insertData('Temperature','Temperature',temp)
    time.sleep(5)

print("Temperature: %s C" % temp)

# alternatives
print(sense.temp)
print(sense.temperature)

