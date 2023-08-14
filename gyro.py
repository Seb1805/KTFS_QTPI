from sense_hat import SenseHat
import mariadb_cl as db
sense = SenseHat()



# while True:
#     raw = sense.get_compass_raw()
#     print("x: {x}, y: {y}, z: {z}".format(**raw))
#     print(sense.compass_raw)
# alternatives
while True:
    sense = SenseHat()
    raw = sense.get_gyroscope_raw()
    strIns = f'{raw["x"]},{raw["y"]},{raw["z"]}'
    db.insertData('Gyroscope','X,Y,Z',strIns)


# print("x: {x}, y: {y}, z: {z}".format(**raw))

# # alternatives
# print(sense.gyro_raw['x']) #Get x > x,y,z
# print(sense.gyroscope_raw)
