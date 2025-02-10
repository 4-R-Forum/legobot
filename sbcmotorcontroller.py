from microbit import *

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