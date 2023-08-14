from sense_hat import SenseHat
import mariadb_cl as db

sense = SenseHat()
accel_only = sense.get_accelerometer()
# print("p: {pitch}, r: {roll}, y: {yaw}".format(**accel_only))

# alternatives
# while True:
#     print(sense.accel)

while True:
    sense = SenseHat()
    raw = sense.get_accelerometer()
    print(raw)
    strIns = f'{raw["roll"]},{raw["pitch"]},{raw["yaw"]}'
    db.insertData('Accelerometer','Roll,Pitch,Yaw',strIns)

# print(sense.accelerometer)