
from microbit import *
import struct, log, time

MPU6050_ADDR = 0x68
def init_mpu6050():
    # Function to initialize MPU-6050
    global MPU6050_ADDR
    i2c.write(MPU6050_ADDR, bytearray([0x6B, 0]))  # Wake up MPU-6050
def read_mpu6050(register):
        # function to  Read 16-bit raw data from 6050 register
        i2c.write(MPU6050_ADDR, bytearray([register]))  
        data = i2c.read(MPU6050_ADDR, 2)  
        return struct.unpack(">h", data)[0] 
def get_yaw_velocity():
    #Function to get yaw velocity (°/s)
    return read_mpu6050(0x47) / 131.0  # Convert raw data to °/s 

# Global Setup
init_mpu6050()
log.set_labels('ang_vel','acc_yaw')

# Parameters for single test
HeadingChange = 90 # degrees
StopReadDelay = 100 # ms
MotorPower = 4 # 40%
# from L15 test turn with motor power 4 is 4 deg per second = 250 ms per degree
# so expected duratiopn in this test = 90 * 250 = 22500 ms
# ExpectedDuration = 22500
sample_rate = 100 # 0.1 sec

def log_yaw():
    ### created for POC in PDCA-01.1
    ### unit test candidate ///TODO params for values to log
    # Read 16-bit raw data from a register
    def read_mpu6050(register):
        i2c.write(MPU6050_ADDR, bytearray([register]))  
        data = i2c.read(MPU6050_ADDR, 2)  
        return struct.unpack(">h", data)[0]  
    # Get yaw velocity (°/s)
    def get_yaw_velocity():
        return read_mpu6050(0x47) / 131.0  # Convert raw data to °/s
    # Variables for integration
    yaw_angle = 0.0  # Initial heading
    start_time = time.ticks_ms()   # Get initial time in milliseconds
    last_time = start_time
    while (time.ticks_diff(time.ticks_ms(), start_time) < ExpectedDuration) :
        # Read yaw rate
        yaw_rate = get_yaw_velocity()      
        # Integrate yaw rate to update heading
        this_time = time.ticks_ms()
        yaw_angle += yaw_rate * (this_time  - last_time) / 1000
        # Normalize to ±180° format
        yaw_angle = (yaw_angle + 180) % 360 - 180  
        # Log heading change
        print("Yaw (°):", yaw_angle)
        log.add({
        'yaw': yaw_angle
        })
        sleep(sample_rate)  # Adjust sample rate

def test_turn():
    log.delete()
    ### copied from log_yaw in PDCA-01.1
    ### unit test candidate ///TODO params for values to log

    # Variables for integration
    yaw_angle = 0.0  # Initial heading
    start_time = time.ticks_ms()   # Get initial time in milliseconds
    last_time = start_time
    while (time.ticks_diff(time.ticks_ms(), start_time) < 2000) : # Simultor test
    # while (time.ticks_diff(time.ticks_ms(), start_time) < 2000) : # Field test
        # Read yaw rate
        ang_vel = get_yaw_velocity()      
        # Integrate yaw rate to update heading
        this_time = time.ticks_ms()
        yaw_angle += ang_vel * (this_time  - last_time) / 1000
        # Normalize to ±180° format
        yaw_angle = (yaw_angle + 180) % 360 - 180  
        # Log heading change
        print("AngVel (°/s)", ang_vel, ", Yaw (°):",yaw_angle)
        log.add({
        'ang_vel': ang_vel,
        'acc_yaw': yaw_angle
        })
        sleep(sample_rate)  # Adjust sample rate
        
# main code #
display.show("G1.2")
display.clear()
test_turn()
display.show(Image.YES)