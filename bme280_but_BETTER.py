import smbus2
import bme280

# Define I2C bus and BME280 address
bus = smbus2.SMBus(1)
address = 0x76

# Initialize the BME280 sensor
bme280.setup(bus, address)

# Read temperature, humidity, and pressure data
data = bme280.readData()
temp = data.temperature
hum = data.humidity
pres = data.pressure

print("Temperature: {:.2f} C".format(temp))
print("Humidity: {:.2f} %".format(hum))
print("Pressure: {:.2f} hPa".format(pres))
