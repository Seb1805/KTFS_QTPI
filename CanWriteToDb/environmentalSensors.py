from sense_hat import SenseHat
import mariadb_cl as db
import requests #used to make api call
import json #json lib
import time



BASE_ADDRESS = 'http://192.168.3.213:5000'

sense = SenseHat()


def tempfuntion(path_api, get_data_func, format_json_func):
    global BASE_ADDRESS
    data = get_data_func()

    json_str = format_json_func(data)
    
    json_object = json.loads(json_str)
    requests.post(f'{BASE_ADDRESS}/{path_api}',json = json_object)
    #requests.post(BASE_ADDRESS + "/" + path_api,json = json_object)

    print(json_str)

while True:
    #Miljø
    tempfuntion('Temperature', sense.get_temperature, lambda data : '{"Temperature" :' + str(data) + '}')
    tempfuntion('Pressure', sense.get_pressure, lambda data : '{"PressureInHectoPascal" :' + str(data) + '}')
    tempfuntion('Humidity', sense.get_humidity, lambda data : '{"Humidity" :' + str(data) + '}')
    time.sleep(5)
    #IMU DegreesToNorth
    tempfuntion('Accelerometer',sense.get_accelerometer, lambda data : '{"Pitch" :' + str(data["pitch"]) + ', "Roll" :' + str(data["roll"]) + ', "Yaw" :' + str(data["yaw"]) + '}')
    tempfuntion('Compass',sense.get_compass, lambda data : '{"DegreesToNorth" :' + str(data) + '}')
    #tempfuntion('Accelerometer',sense.get_accelerometer, lambda data : '{"Pitch" :' + str(data["pitch"]) + ', "Roll" :' + str(data["roll"]) + ', "Yaw" :' + str(data["yaw"]) + '}')
    #tempfuntion('Accelerometer',sense.get_accelerometer, lambda data : '{"Pitch" :' + str(data["pitch"]) + ', "Roll" :' + str(data["roll"]) + ', "Yaw" :' + str(data["yaw"]) + '}')

