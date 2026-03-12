from microbit import *

MPU6050_ADDR = 0x68  # MPU-6050 I2C address
GYRO_CONFIG = 0x1B   # Gyroscope configuration register

i2c.write(MPU6050_ADDR, bytearray([GYRO_CONFIG]))  # Request register
fs_sel_value = i2c.read(MPU6050_ADDR, 1)[0]  # Read 1 byte