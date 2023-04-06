import smbus
import time

# MPU-6050 register addresses
PWR_MGMT_1 = 0x6B
ACCEL_XOUT_H = 0x3B
ACCEL_YOUT_H = 0x3D
ACCEL_ZOUT_H = 0x3F
GYRO_XOUT_H = 0x43
GYRO_YOUT_H = 0x45
GYRO_ZOUT_H = 0x47

# Initialize I2C bus and MPU-6050
bus = smbus.SMBus(1)
bus.write_byte_data(0x68, PWR_MGMT_1, 0)

# Function to read 16-bit word from I2C device
def read_word_2c(addr):
    high = bus.read_byte_data(0x68, addr)
    low = bus.read_byte_data(0x68, addr + 1)
    val = (high << 8) + low

    if (val >= 0x8000):
        return -((65535 - val) + 1)
    else:
        return val

# Read and print accelerometer and gyroscope data
while True:
    accel_x = read_word_2c(ACCEL_XOUT_H)
    accel_y = read_word_2c(ACCEL_YOUT_H)
    accel_z = read_word_2c(ACCEL_ZOUT_H)
    gyro_x = read_word_2c(GYRO_XOUT_H)
    gyro_y = read_word_2c(GYRO_YOUT_H)
    gyro_z = read_word_2c(GYRO_ZOUT_H)

    print("accelerometer (x,y,z): ({},{},{})".format(accel_x, accel_y, accel_z))
    print("gyroscope (x,y,z): ({},{},{})".format(gyro_x, gyro_y, gyro_z))

    time.sleep(1.5)
