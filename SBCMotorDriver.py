from microbit import *

# Define motor and servo pins
PWMA = pin8
AIN1 = pin13
AIN2 = pin12
PWMB = pin16
PIN1 = pin14
PIN2 = pin15
S0_PIN = pin0
S1_PIN = pin1
S2_PIN = pin2

# Set PWM frequency
PWMA.set_analog_period(1)  
PWMB.set_analog_period(1) 
S0_PIN.set_analog_period(20) 
S1_PIN.set_analog_period(20) 
S2_PIN.set_analog_period(20) 

def motor_run(motor: int, direction: int, speed: int):
    duty = min(max(speed * 64 - 1, 0), 1023)  # Map 0-16 to 0-1023
    
    if motor == 1:
        PWMA = duty
        if direction == 1:
            AIN1 = 0
            AIN2 = 1
        else:
            AIN1 = 1
            AIN2 = 0
    else:
        PWMB = duty
        if direction == 1:
            PIN1 = 0
            PIN2 = 1
        else:
            PIN1 = 1
            PIN2 = 0

def motor_stop(motor:int):
    if motor == 1:
        PWMA = 0
    else:
        PWMB = 0


