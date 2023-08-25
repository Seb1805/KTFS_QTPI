from sense_hat import SenseHat
import requests 
import json
import time

#Base address of API
BASE_ADDRESS = 'http://192.168.3.213:5000'

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
    requests.post(f'{BASE_ADDRESS}/{path_api}',json = json_object)


#Loop that calls the various sensors
while True:
    #Miljø
    PostSensorData('Temperature', sense.get_temperature, lambda data : '{"Temperature" :' + str(data) + '}')
    PostSensorData('Pressure', sense.get_pressure, lambda data : '{"PressureInHectoPascal" :' + str(data) + '}')
    PostSensorData('Humidity', sense.get_humidity, lambda data : '{"Humidity" :' + str(data) + '}')
    time.sleep(10)
    #IMU DegreesToNorth
    PostSensorData('Accelerometer',sense.get_accelerometer, lambda data : '{"Pitch" :' + str(data["pitch"]) + ', "Roll" :' + str(data["roll"]) + ', "Yaw" :' + str(data["yaw"]) + '}')
    PostSensorData('Compass',sense.get_compass, lambda data : '{"DegreesToNorth" :' + str(data) + '}')
    #PostSensorData('Accelerometer',sense.get_accelerometer, lambda data : '{"Pitch" :' + str(data["pitch"]) + ', "Roll" :' + str(data["roll"]) + ', "Yaw" :' + str(data["yaw"]) + '}')
    #PostSensorData('Accelerometer',sense.get_accelerometer, lambda data : '{"Pitch" :' + str(data["pitch"]) + ', "Roll" :' + str(data["roll"]) + ', "Yaw" :' + str(data["yaw"]) + '}')

