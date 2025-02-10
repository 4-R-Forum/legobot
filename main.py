from microbit import *
import log, time, gc
import sbcmotorcontroller

MPU6050_ADDR = 0x68
def init_mpu6050():
    # Function to initialize MPU-6050
    global MPU6050_ADDR
    i2c.write(MPU6050_ADDR, bytearray([0x6B, 0]))  # Wake up MPU-6050
def read_mpu6050(register):
        # function to  Read 16-bit raw data from 6050 register
        i2c.write(MPU6050_ADDR, bytearray([register]))  
        raw = i2c.read(MPU6050_ADDR, 2)   # read 2 bytes
        value = (raw[0] << 8) | raw[1]  # Combine High Byte and Low Byte
        # Convert to signed 16-bit integer
        if value > 32767:
            value -= 65536 
        return value
def get_yaw_velocity():
    #Function to get yaw velocity (°/s)
    return read_mpu6050(0x47) / 131.0  # Convert raw data to °/s 

# Global Setup
init_mpu6050()
log.set_labels('ang_vel','acc_yaw','dev','this_time','last_time','mem_free', 'mem_alloc')
# Issues sharing enums/Class between modules, use int
MotorA = 1
MotorB = 2
DirFWD = 1
DirBCK = 2

# Parameters for single test
HeadingChange = -30 # degrees
StopReadDelay = 100 # ms
MotorPower = 4 # max 16, so 4 = 25%
sample_rate = 100 # 0.1 sec, works well

def turn_heading_test():
    HeadingDev = 0 - HeadingChange
    yaw_angle = 0
    start_time = time.ticks_ms()   # Get initial time in milliseconds
    last_time = start_time
    log.add({
    'ang_vel': 0,
    'acc_yaw': 0,
    'dev': HeadingChange,
    'this_time':start_time,
    'last_time':last_time,
    'mem_free': gc.mem_free(),
    'mem_alloc': gc.mem_alloc()
    })
    while True:
        if HeadingDev < 0:
            # turn left, CCW, angvel +ve
            Adir = DirFWD
            Bdir = DirBCK
        else:
            # turn right, CW, angvel -ve
            Adir = DirBCK
            Bdir = DirFWD
        sbcmotorcontroller.motor_run(MotorA, Adir, MotorPower)
        sbcmotorcontroller.motor_run(MotorB, Bdir, MotorPower)
        # Read yaw rate
        ang_vel = get_yaw_velocity()      
        # Integrate yaw rate to update heading
        this_time = time.ticks_ms()
        yaw_angle += ang_vel * (this_time  - last_time) / 1000 # dt +ve
        # Normalize to ±180° format
        yaw_angle = (yaw_angle + 180) % 360 - 180
        HeadingDev = HeadingChange - yaw_angle
        # Log heading change
        # print("AngVel (°/s)", ang_vel, ", Yaw (°):",yaw_angle)
        log.add({
        'ang_vel': ang_vel,
        'acc_yaw': yaw_angle,
        'dev': HeadingDev,
        'this_time':this_time,
        'last_time':last_time,
        'mem_free': gc.mem_free(),
        'mem_alloc': gc.mem_alloc()
        })
        if HeadingDev > 0:
            break
        sleep(sample_rate)  # Adjust sample rate
     
    sbcmotorcontroller.motor_stop(MotorA)
    sbcmotorcontroller.motor_stop(MotorB)
 
# main code #
display.show("G1.4.0")
display.clear()
log.delete()
gc.collect() # free memory
turn_heading_test()
display.show(Image.YES)