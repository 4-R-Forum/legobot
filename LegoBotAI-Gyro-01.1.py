from microbit import i2c, sleep, running_time
import struct, log
from microbit import *
import log

MPU6050_ADDR = 0x68

# Initialize MPU-6050, 
def init_mpu6050():
    i2c.write(MPU6050_ADDR, bytearray([0x6B, 0]))  # Wake up MPU-6050

# Setup log columns
log.set_labels('yaw')

# Read 16-bit raw data from a register
def read_mpu6050(register):
    i2c.write(MPU6050_ADDR, bytearray([register]))  
    data = i2c.read(MPU6050_ADDR, 2)  
    return struct.unpack(">h", data)[0]  

# Get yaw velocity (°/s)
def get_yaw_velocity():
    return read_mpu6050(0x47) / 131.0  # Convert raw data to °/s

# Initialize sensor
init_mpu6050()

# Variables for integration
yaw_angle = 0.0  # Initial heading
last_time = running_time()  # Get initial time in milliseconds

while True:
    # Read yaw rate
    yaw_rate = get_yaw_velocity()
    
    # Get current time and compute time difference (dt in seconds)
    current_time = running_time()
    dt = (current_time - last_time) / 1000.0  # Convert ms to s
    last_time = current_time  # Update last time
    
    # Integrate yaw rate to update heading
    yaw_angle += yaw_rate * dt  

    # Normalize to ±180° format
    yaw_angle = (yaw_angle + 180) % 360 - 180  

    # Log heading change
    print("Yaw (°):", yaw_angle)
    log.add({
      'yaw': yaw_angle
    })
    
    
    sleep(100)  # Adjust sample rate

