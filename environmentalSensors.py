from sense_hat import SenseHat
import requests 
import json
import time
import gc
import os
from dotenv import load_dotenv as denv

denv()

#Base address of API
BASE_ADDRESS = f'http://{os.getenv("SERVER_IP")}:{os.getenv("PORT")}'

sense = SenseHat()


def PostSensorData(path_api, get_data_func , format_json_func):
    """
    Post sensor data through the API

    Parameters
    ----------
    path_api: str
        a string with the path to the endpoint
    get_data_func: funcion
        the function used to get the data
    format_json_func: lambda
        the json format send to the database
    """

    #Tells the function to use the global constant BASE_ADDRESS instead of making a function scoped constant
    global BASE_ADDRESS
    data = get_data_func()
    #Applies the lambda on the data
    json_str = format_json_func(data)
    #Convert the string to a JSON object
    json_object = json.loads(json_str)
    #Send the post request to the API
    try:
        requests.post(f'{BASE_ADDRESS}/{path_api}',json = json_object)
    except requests.exceptions.ConnectionError:
        print('connection failed')
    # requests.post(f'{BASE_ADDRESS}/{path_api}',json = json_object)
    #print('APIet kører ikke, KLAPHAT')

#Loop that calls the various sensors
while True:
    #Miljø
    PostSensorData('Temperature', sense.get_temperature, lambda data : '{"Temperature" :' + str(data) + '}')
    PostSensorData('Pressure', sense.get_pressure, lambda data : '{"PressureInHectoPascal" :' + str(data) + '}')
    PostSensorData('Humidity', sense.get_humidity, lambda data : '{"Humidity" :' + str(data) + '}')
    #IMU DegreesToNorth
    PostSensorData('Accelerometer',sense.get_accelerometer, lambda data : '{"Pitch" :' + str(data["pitch"]) + ', "Roll" :' + str(data["roll"]) + ', "Yaw" :' + str(data["yaw"]) + '}')
    PostSensorData('Compass',sense.get_compass, lambda data : '{"DegreesToNorth" :' + str(data) + '}')
    PostSensorData('Orientation',sense.get_orientation, lambda data : '{"Pitch" :' + str(data["pitch"]) + ', "Roll" :' + str(data["roll"]) + ', "Yaw" :' + str(data["yaw"]) + '}')
    PostSensorData('Gyroscope',sense.get_gyroscope_raw, lambda data : '{"X" :' + str(data["x"]) + ', "Y" :' + str(data["y"]) + ', "Z" :' + str(data["z"]) + '}')
    gc.collect()
    time.sleep(60)

