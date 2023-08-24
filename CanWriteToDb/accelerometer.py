from sense_hat import SenseHat
import mariadb_cl as db
import requests #used to make api call
import json #json lib

sense = SenseHat()
accel_only = sense.get_accelerometer()

BASE_ADDRESS = 'http://192.168.3.213:5000'
prefix = 'Accelerometer'
FULL_PATH = BASE_ADDRESS + '/' + prefix

# print("p: {pitch}, r: {roll}, y: {yaw}".format(**accel_only))

# alternatives
# while True:
#     print(sense.accel)


while True:
    sense = SenseHat()
    raw = sense.get_accelerometer()
    
 
    testStr = '{"Pitch" :' + str(raw["pitch"]) + ', "Roll" :' + str(raw["roll"]) + ', "Yaw" :' + str(raw["yaw"]) + '}' # CANCER
    #strIns = f'"Pitch": {raw["pitch"]},"Roll" : {raw["roll"]},"Yaw": {raw["yaw"]}'
    print(testStr)
    #json_object = json.dumps(raw)
    json_object = json.loads(testStr)
    print(json_object)
    x = requests.post(FULL_PATH,json = json_object)
    print(x)
    #db.insertData('Accelerometer','Roll,Pitch,Yaw',strIns)

# print(sense.accelerometer)