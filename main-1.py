from microbit import *
import struct, log, time
# import sbcmotorcontroller

## SBC Motor Controller
# Define motor and servo pins
PWMA   = pin8  # Analog Motor A
AIN1   = pin13 # Digital
AIN2   = pin12 # Digital
PWMB   = pin16 # Analog Motor B
BIN1   = pin14 # Digital
BIN2   = pin15 # Digital
S0_PIN = pin0  # Analog Servo1
S1_PIN = pin1  # Analog Servo2
S2_PIN = pin2  # Analog Servo3

def motor_run(motor: int, direction: int, speed: int):
    duty = min(max(speed * 64 - 1, 0), 1023)  # Map 0-16 to 0-1023
    global AIN1, AIN2, BIN1, BIN2, PWMA, PWMB
    if motor == 1:
        #Pins.analogWritePin(PWMA, duty)
        PWMA.write_analog(duty)
        PWMA.set_analog_period(1)
        if direction == 1:
            AIN1.write_digital(0)
            AIN2.write_digital(1)
        else:
            AIN1.write_digital(1)
            AIN2.write_digital(0)
    else:
        PWMB.write_analog(duty)
        PWMB.set_analog_period(1)
        if direction == 1:
            BIN1.write_digital(0)
            BIN2.write_digital(1)
        else:
            BIN1.write_digital(1)
            BIN2.write_digital(0)

def motor_stop(motor:int):
    if motor == 1:
        PWMA.write_analog(0)
    else:
        PWMB.write_analog(0)

## end of SBC MotorController

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
# Issues sharing enums/Class between modules, use int
MotorA = 1
MotorB = 2
DirFWD = 1
DirBCK = 2

# Parameters for single test
HeadingChange = 90 # degrees
StopReadDelay = 100 # ms
MotorPower = 4 # 40%
# from L15 test turn with motor power 4 is 4 deg per second = 250 ms per degree
# so expected duratiopn in this test = 90 * 250 = 22500 ms
# ExpectedDuration = 22500
sample_rate = 100 # 0.1 sec

def turn_heading_test():
    HeadingDev = 0 - HeadingChange
    yaw_angle = 0
    start_time = time.ticks_ms()   # Get initial time in milliseconds
    last_time = start_time
    Adir = 0
    
    while HeadingDev != 0:
        
        if HeadingDev < 0:
            # turn right
            Adir = DirFWD
            Bdir = DirBCK
        else:
            # turn left
            Adir = DirBCK
            Bdir = DirFWD
        motor_run(MotorA, Adir, MotorPower)
        motor_run(MotorB, Bdir, MotorPower)
        # Read yaw rate
        ang_vel = get_yaw_velocity()      
        # Integrate yaw rate to update heading
        this_time = time.ticks_ms()
        yaw_angle += ang_vel * (this_time  - last_time) / 1000
        # Normalize to ±180° format
        yaw_angle = (yaw_angle + 180) % 360 - 180
        HeadingDev = 0 - yaw_angle
        # Log heading change
        print("AngVel (°/s)", ang_vel, ", Yaw (°):",yaw_angle)
        log.add({
        'ang_vel': ang_vel,
        'acc_yaw': yaw_angle
        })
        sleep(sample_rate)  # Adjust sample rate
     
    motor_stop(MotorA)
    motor_stop(MotorB)
 
# main code #
display.show("G1.3.2")
display.clear()
log.delete()
turn_heading_test()
display.show(Image.YES)