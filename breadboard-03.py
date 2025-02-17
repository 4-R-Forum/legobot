from microbit import *
import struct

MPU6050_ADDR = 0x68
GYRO_ZOUT_H = 0x47

def init_mpu6050():
    # Function to initialize MPU-6050
    global MPU6050_ADDR
    i2c.write(MPU6050_ADDR, bytearray([0x6B, 0]))  # Wake up MPU-6050

# Collect multiple stationary readings
num_samples = 100
bias_sum = 0
init_mpu6050()

for _ in range(num_samples):
    i2c.write(MPU6050_ADDR, bytearray([GYRO_ZOUT_H]))
    raw_data = i2c.read(MPU6050_ADDR, 2)
    GyZ = struct.unpack(">h", raw_data)[0]
    bias_sum += GyZ
    sleep(10)  # 10ms delay

gyro_bias = bias_sum / num_samples  # Calculate bias

display.show(gyro_bias)