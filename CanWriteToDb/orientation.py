from sense_hat import SenseHat
import CanWriteToDb.mariadb_cl as db

sense = SenseHat()
orientation = sense.get_orientation()
print("p: {pitch}, r: {roll}, y: {yaw}".format(**orientation))

# alternatives
print(sense.orientation)

while True:
    sense = SenseHat()
    raw = sense.get_orientation()
    strIns = f'{raw["roll"]},{raw["pitch"]},{raw["yaw"]}'
    db.insertData('Orientation','Roll,Pitch,Yaw',strIns)
