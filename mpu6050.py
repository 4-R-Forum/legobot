from microbit import *
import log, time
import sbcmotorcontroller

MPU6050_ADDR = 0x68
gz_bias = 242

def init_mpu6050():
    # Function to initialize MPU-6050
    #global MPU6050_ADDR
    i2c.init()
    i2c.write(MPU6050_ADDR, bytearray([0x6B, 0]))  # Wake up MPU-6050
def read_mpu6050(register):
        # function to  Read 16-bit raw data from 6050 register
        i2c.write(MPU6050_ADDR, bytearray([register]))  
        raw = i2c.read(MPU6050_ADDR, 2)   # read 2 bytes
        return raw
def get_yaw_velocity(bias,alpha,last_value,rotation):
    # Function to get yaw velocity (°/s) with bias correction and smoothing
    raw =  read_mpu6050(0x47)
    value = (raw[0] << 8) | raw[1]  # Combine High Byte and Low Byte
    signed_value = value - bias # apply bias measured in breadboard-03.py
    # Convert to signed 16-bit integer
    if signed_value > 32767:
        signed_value = value - 65536
    filtered_value = (alpha * signed_value) + ((1 - alpha) * last_value)
    ang_vel = filtered_value / 131.0  # convert signed value to °/s 
    if rotation == "cw":
        ang_vel = - ang_vel
    return ang_vel 
def dev_update(change, yaw):
    # CCW = +ve counter-intuitive
    return change - yaw
def turn_complete(change, dev):
    # CCW = +ve counter-intuitive
    if change > 0:
        if dev <= 0:
            return True
        else:
            return False
    elif change < 0:
        if dev >= 0:
            return True
        else:
            return False
def log_break():
        log.add({
        'ang_vel': 0,
        'acc_yaw': 0,
        'dev': 0
        })
def turn_heading_test(HeadingChange, MotorPower, sample_rate,rotation):
    # set variables for test
    yaw_angle = 0
    HeadingDev =  dev_update(HeadingChange, yaw_angle)
    start_time = time.ticks_ms()   # Get initial time in milliseconds
    last_time = start_time
    alpha = 0.5  # Smoothing factor (adjust as needed)
    ang_vel = 0 # start at 0 stationary
    log.add({
    'ang_vel': 0,
    'acc_yaw': 0,
    'dev': HeadingDev
    })
    while True:
        # Set motor directions, start fwd motor first
        # CCW = +ve counter-intuitive
        if HeadingDev > 0:
            # turn right, CW, angvel -ve
            Adir = sbcmotorcontroller.DirFWD
            Bdir = sbcmotorcontroller.DirBCK
            sbcmotorcontroller.motor_run(sbcmotorcontroller.MotorA, Adir, MotorPower)
            sbcmotorcontroller.motor_run(sbcmotorcontroller.MotorB, Bdir, MotorPower)
        else:
            # turn left, CCW, angvel +ve
            Adir = sbcmotorcontroller.DirBCK
            Bdir = sbcmotorcontroller.DirFWD
            sbcmotorcontroller.motor_run(sbcmotorcontroller.MotorB, Bdir, MotorPower)
            sbcmotorcontroller.motor_run(sbcmotorcontroller.MotorA, Adir, MotorPower)
       
        # Read yaw rate, using function updated from breadboard-02 1.6
        ang_vel = get_yaw_velocity(gz_bias,alpha,ang_vel,rotation)
        # Integrate yaw rate to update heading
        this_time = time.ticks_ms()
        yaw_angle += ang_vel * (this_time  - last_time) / 1000 # dt +ve
        # Normalize to ±180° format
        yaw_angle = (yaw_angle + 180) % 360 - 180

        HeadingDev = dev_update(HeadingChange, yaw_angle) # ///TODO Test
        log.add({
        'ang_vel': ang_vel,
        'acc_yaw': yaw_angle,
        'dev': HeadingDev
        })
        if turn_complete(HeadingChange,HeadingDev): # /// TODO Test
            break
        sleep(sample_rate)  # Adjust sample rate

    if HeadingDev < 0: 
        # avoid turning wrong way on stop
        sbcmotorcontroller.motor_stop(sbcmotorcontroller.MotorA)
        sbcmotorcontroller.motor_stop(sbcmotorcontroller.MotorB)
    else:
        sbcmotorcontroller.motor_stop(sbcmotorcontroller.MotorB)
        sbcmotorcontroller.motor_stop(sbcmotorcontroller.MotorA)
    