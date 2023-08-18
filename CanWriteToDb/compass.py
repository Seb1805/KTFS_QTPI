from sense_hat import SenseHat
import CanWriteToDb.mariadb_cl as db

sense = SenseHat()

#print("North: %s" % north)

# alternatives
while True:
    north = sense.get_compass()
    db.insertData('Compass','DegreesToNorth',north)
    #print(sense.compass)