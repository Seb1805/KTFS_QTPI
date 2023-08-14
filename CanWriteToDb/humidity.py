from sense_hat import SenseHat


#import
import mariadb_cl as db

sense = SenseHat()
humidity = sense.get_humidity()
# print("Humidity: %s %%rH" % humidity)

# # alternatives
# print(sense.humidity)
while True:
    humidity = sense.get_humidity()
    db.insertData('Humidity','Humidity',humidity)