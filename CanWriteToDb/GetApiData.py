from sense_hat import SenseHat
import mariadb_cl as db
import requests #used to make api call
import json #json lib
import time



BASE_ADDRESS = 'http://192.168.3.213:5000'
 


def tempfuntion(path_api):
    global BASE_ADDRESS
    # data = get_data_func()

    # json_str = format_json_func(data)
    
    # json_object = json.loads(json_str)
    x = requests.get(f'{BASE_ADDRESS}/{path_api}/3',)
    print(x.status_code)
    #requests.post(BASE_ADDRESS + "/" + path_api,json = json_object)
    if x.status_code == 200:
        print (x.json())
    #print(x.body)

while True:
    #Miljø
    tempfuntion('Temperature')
    tempfuntion('Pressure')
    tempfuntion('Humidity')
    time.sleep(5)
    #IMU DegreesToNorth
    # tempfuntion('Accelerometer',sense.get_accelerometer, lambda data : '{"Pitch" :' + str(data["pitch"]) + ', "Roll" :' + str(data["roll"]) + ', "Yaw" :' + str(data["yaw"]) + '}')
    # tempfuntion('Compass',sense.get_compass, lambda data : '{"DegreesToNorth" :' + str(data) + '}')
    #tempfuntion('Accelerometer',sense.get_accelerometer, lambda data : '{"Pitch" :' + str(data["pitch"]) + ', "Roll" :' + str(data["roll"]) + ', "Yaw" :' + str(data["yaw"]) + '}')
    #tempfuntion('Accelerometer',sense.get_accelerometer, lambda data : '{"Pitch" :' + str(data["pitch"]) + ', "Roll" :' + str(data["roll"]) + ', "Yaw" :' + str(data["yaw"]) + '}')

