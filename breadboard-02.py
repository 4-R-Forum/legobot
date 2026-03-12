from microbit import *
import log, music, time

MPU6050_ADDR = 0x68
def init_mpu6050():
    # Function to initialize MPU-6050
    global MPU6050_ADDR
    i2c.write(MPU6050_ADDR, bytearray([0x6B, 0]))  # Wake up MPU-6050
def read_mpu6050(register):
        # function to  Read 16-bit raw data from 6050 register
        i2c.write(MPU6050_ADDR, bytearray([register]))  
        raw = i2c.read(MPU6050_ADDR, 2)   # read 2 bytes
        return raw

log.delete()
log.set_labels('ang_vel','acc_yaw')
init_mpu6050()
sleep(8000)
music.play(music.BA_DING)
n = 0
start_time = time.ticks_ms()   # Get initial time in milliseconds
last_time = start_time
yaw_angle = 0
alpha = 0.5  # Smoothing factor (adjust as needed)
filtered_value = 0 # apply bias to starting point
while n < 15:
    raw =  read_mpu6050(0x47)
    value = (raw[0] << 8) | raw[1]  # Combine High Byte and Low Byte
    signed_value = value - 242 # apply bias measured in breadboard-03.py
    # Convert to signed 16-bit integer
    if signed_value > 32767:
        signed_value = value - 65536
    filtered_value = (alpha * signed_value) + ((1 - alpha) * filtered_value)
    ang_vel = signed_value / 131.0  # convert signed value to °/s 
    # Integrate yaw rate to update heading
    this_time = time.ticks_ms()
    yaw_angle += ang_vel * (this_time  - last_time) / 1000 # dt +ve
    # Normalize to ±180° format
    yaw_angle = (yaw_angle + 180) % 360 - 180
    n += 1
    log.add({
    'ang_vel': ang_vel,
    'acc_yaw': yaw_angle
    })    
    sleep(100)

display.show(Image.YES)

