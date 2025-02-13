from microbit import *
import log, time, gc
import sbcmotorcontroller
pdca = "G1.5.2"

MPU6050_ADDR = 0x68
def init_mpu6050():
    # Function to initialize MPU-6050
    global MPU6050_ADDR
    i2c.write(MPU6050_ADDR, bytearray([0x6B, 0]))  # Wake up MPU-6050
def read_mpu6050(register):
        # function to  Read 16-bit raw data from 6050 register
        i2c.write(MPU6050_ADDR, bytearray([register]))  
        raw = i2c.read(MPU6050_ADDR, 2)   # read 2 bytes
        '''        
        value = (raw[0] << 8) | raw[1]  # Combine High Byte and Low Byte
        # Convert to signed 16-bit integer
        if value > 32767:
            value -= 65536 
        return value
        '''
        return raw
def get_yaw_velocity():
    #Function to get yaw velocity (°/s)
    return read_mpu6050(0x47) / 131.0  # Convert raw data to °/s 
def dev_update(change, yaw):
    if change > 0:
        return change -yaw
    else:
        return change + yaw
def turn_complete(change, dev):
    if change > 0:
        if dev < 0:
            return True
        else:
            return False
    elif change < 0:
        if dev > 0:
            return True
        else:
            return False

# Global Setup
init_mpu6050()
log.set_labels('ang_vel','acc_yaw','dev','raw','value','signed_value')
# Issues sharing enums/Class between modules, use int
MotorA = 1
MotorB = 2
DirFWD = 1
DirBCK = 2

def turn_heading_test(HeadingChange, MotorPower, sample_rate):
    HeadingDev = 0 - HeadingChange
    yaw_angle = 0
    start_time = time.ticks_ms()   # Get initial time in milliseconds
    last_time = start_time
    log.add({
    'ang_vel': 0,
    'acc_yaw': 0,
    'dev': HeadingChange,
    'raw': "",
    'value': "",
    'signed_value': ""
    })
    while True:
        # start fwd motor first, avoid turn wrong way
        if HeadingDev < 0:
            # turn left, CCW, angvel +ve
            Adir = DirFWD
            Bdir = DirBCK
            sbcmotorcontroller.motor_run(MotorA, Adir, MotorPower)
            sbcmotorcontroller.motor_run(MotorB, Bdir, MotorPower)
        else:
            # turn right, CW, angvel -ve
            Adir = DirBCK
            Bdir = DirFWD
            sbcmotorcontroller.motor_run(MotorB, Bdir, MotorPower)
            sbcmotorcontroller.motor_run(MotorA, Adir, MotorPower)
       
        # Read yaw rate
        # ang_vel = get_yaw_velocity() 
        raw =  read_mpu6050(0x47)
        value = (raw[0] << 8) | raw[1]  # Combine High Byte and Low Byte
        signed_value = value
        # Convert to signed 16-bit integer
        if value > 32767:
            signed_value = value - 65536
        ang_vel = signed_value / 131.0  # Convert raw data to °/s 
        # Integrate yaw rate to update heading
        this_time = time.ticks_ms()
        yaw_angle += ang_vel * (this_time  - last_time) / 1000 # dt +ve
        # Normalize to ±180° format
        yaw_angle = (yaw_angle + 180) % 360 - 180
        HeadingDev = dev_update(HeadingChange, yaw_angle) # ///TODO Test
        # Log heading change
        # print("AngVel (°/s)", ang_vel, ", Yaw (°):",yaw_angle) # for simulator test
        log.add({
        'ang_vel': ang_vel,
        'acc_yaw': yaw_angle,
        'dev': HeadingDev,
        'raw': raw,
        'value': value,
        'signed_value': signed_value
        })
        if turn_complete(HeadingChange,HeadingDev): # /// TODO Test
            break
        sleep(sample_rate)  # Adjust sample rate

    if HeadingDev < 0: 
        # avoid turning wrong way on stop
        sbcmotorcontroller.motor_stop(MotorA)
        sbcmotorcontroller.motor_stop(MotorB)
    else:
        sbcmotorcontroller.motor_stop(MotorB)
        sbcmotorcontroller.motor_stop(MotorA)
 
# main code #
display.show(pdca)
display.clear()
log.delete()
turn_heading_test(30, 3, 80)
sleep(2000)
turn_heading_test(60, 3, 80)
sleep(2000)
turn_heading_test(-30, 3, 80)
sleep(2000)
turn_heading_test(-60, 3, 80)
display.show(Image.YES)
