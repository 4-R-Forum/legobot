
from microbit import *
import struct, log, time

MPU6050_ADDR = 0x68

# Initialize MPU-6050
def init_mpu6050():
    i2c.write(MPU6050_ADDR, bytearray([0x6B, 0]))  # Wake up MPU-6050

# Global Setup
init_mpu6050()
log.set_labels('yaw')


# Parameters for single test
HeadingChange = 90 # degrees
StopReadDelay = 100 # ms
MotorPower = 4 # 40%
# from L15 test turn with motor power 4 is 4 deg per second = 250 ms per degree
# so expected duratiopn in this test = 90 * 250 = 22500 ms
ExpectedDuration = 22500
sample_rate = 100 # 0.1 sec


def log_yaw(sample_rate):
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
        
        # Get current time and compute time difference (dt in seconds)
        
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

def test_turn ():
    global turnSpeed, heading_T, heading_thold, compReading
    basic.show_string("L15")
    datalogger.delete_log(datalogger.DeleteType.FAST)
    turnSpeed = 4
    heading_T = 0
    heading_thold = 5
    while True:
        compReading = input.compass_heading()
        calc_h_dev(compReading, heading_T)
        datalogger.log(datalogger.create_cv("compass", compReading),
            datalogger.create_cv("target", heading_T),
            datalogger.create_cv("dev", heading_dev),
            datalogger.create_cv("interval", n))
        TurnHeading(heading_T)
        if heading_dev > heading_thold and heading_dev < 0 - heading_thold:
            break
        basic.pause(1000 * n)
    basic.show_icon(IconNames.YES)    


log_yaw(100)
