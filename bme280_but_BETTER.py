import smbus2
import bme280

# Define I2C bus and BME280 address
bus = smbus2.SMBus(1)
address = 0x76

# Load calibration parameters from the BME280 sensor
calibration_params = bme280.load_calibration_params(bus, address)

# Initialize the BME280 sensor with the loaded calibration parameters
bme280_data = bme280.sample(bus, address, calibration_params)

# Read temperature, humidity, and pressure data
temp = bme280_data.temperature
hum = bme280_data.humidity
pres = bme280_data.pressure

print("Temperature: {:.2f} C".format(temp))
print("Humidity: {:.2f} %".format(hum))
print("Pressure: {:.2f} hPa".format(pres))
