from microbit import *
import log, time, struct
import sbcmotorcontroller

MPU6050_ADDR = 0x68
gz_bias = 0

def init_mpu6050():
    # Function to initialize MPU-6050
    i2c.init()
    
    # Debug: Scan for I2C devices to confirm connection
    devices = i2c.scan()
    if MPU6050_ADDR not in devices:
        display.scroll("NO GYRO")
        if devices:
            display.scroll("FND:" + str(hex(devices[0])))
        else:
            display.scroll("NO I2C")
        # Halt execution here to prevent crash at line 18
        while True:
            display.show(Image.NO)
            sleep(500)
        
    i2c.write(MPU6050_ADDR, bytearray([0x6B, 0]))  # Wake up MPU-6050

def calibrate_gyro(samples=100):
    # Calculate bias by averaging stationary readings
    global gz_bias
    display.show("C") # Indicating Calibration
    bias_sum = 0
    for _ in range(samples):
        # Read raw Z-axis gyro data (Register 0x47)
        i2c.write(MPU6050_ADDR, bytearray([0x47]))
        raw = i2c.read(MPU6050_ADDR, 2)
        value = (raw[0] << 8) | raw[1]
        if value > 32767: value -= 65536
        value = -value # Invert for upside down mounting
        bias_sum += value
        sleep(5)
    gz_bias = bias_sum / samples
    display.clear()
    return gz_bias

def read_mpu6050(register):
        # function to  Read 16-bit raw data from 6050 register
        i2c.write(MPU6050_ADDR, bytearray([register]))  
        raw = i2c.read(MPU6050_ADDR, 2)   # read 2 bytes
        return raw
def get_yaw_velocity(bias,alpha,last_value):
    # Function to get yaw velocity (°/s) with bias correction and smoothing
    raw =  read_mpu6050(0x47)
    value = (raw[0] << 8) | raw[1]  # Combine High Byte and Low Byte
    
    # Convert to signed 16-bit integer
    if value > 32767: value -= 65536
    value = -value # Invert for upside down mounting

    # Scale to deg/s first (bias is in raw units)
    current_ang_vel = (value - bias) / 131.0
    
    # Apply filter on consistent units (deg/s)
    filtered_ang_vel = (alpha * current_ang_vel) + ((1 - alpha) * last_value)
    return filtered_ang_vel

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
def turn(HeadingChange, MotorPower):
    # set variables for test
    yaw_angle = 0
    start_time = time.ticks_ms()   # Get initial time in milliseconds
    last_time = start_time
    alpha = 0.5  # Smoothing factor (adjust as needed)
    ang_vel = 0 # start at 0 stationary

    # Proportional control constants for reducing overshoot. These will need tuning.
    P_GAIN = 0.1   # 0.1 * 30 deg = 3 (Max). Brake to Power 1 at <10 deg error.
    MIN_POWER = 2  # Must be < MotorPower. 1 is too weak (stall).

    # Tuned constant for loop delay
    sample_rate = 20
    HeadingDev =  dev_update(HeadingChange, yaw_angle)
    log.add({
    'ang_vel': 0,
    'acc_yaw': 0,
    'dev': HeadingDev
    })
    while True:
        # Logic: A positive HeadingDev means we need to turn Left (CCW)
        # to reach the target.
        if HeadingDev > 0:
            # Turn Left (CCW)
            # Assuming Motor A=Right, Motor B=Left
            # To turn Left: Right FWD, Left BCK
            Adir = sbcmotorcontroller.DirFWD 
            Bdir = sbcmotorcontroller.DirBCK 
        else:
            # Turn Right (CW)
            # To turn Right: Right BCK, Left FWD
            Adir = sbcmotorcontroller.DirBCK 
            Bdir = sbcmotorcontroller.DirFWD

        # --- Proportional Control Logic ---
        # Calculate power based on how far we are from the target.
        # This makes the robot slow down as it gets closer.
        error = abs(HeadingDev)
        calculated_power = int(P_GAIN * error)
        
        # Clamp power between a minimum to move and the max specified by the user.
        dynamic_power = max(MIN_POWER, min(MotorPower, calculated_power))
        sbcmotorcontroller.motor_run(sbcmotorcontroller.MotorA, Adir, dynamic_power)
        sbcmotorcontroller.motor_run(sbcmotorcontroller.MotorB, Bdir, dynamic_power)

        # Read yaw rate, using function updated from breadboard-02 1.6
        ang_vel = get_yaw_velocity(gz_bias,alpha,ang_vel)
        # Integrate yaw rate to update heading
        this_time = time.ticks_ms()
        dt = (this_time - last_time) / 1000.0
        yaw_angle += ang_vel * dt
        last_time = this_time # Important: Update last_time for next loop
        # Normalize to ±180° format
        yaw_angle = (yaw_angle + 180) % 360 - 180

        HeadingDev = dev_update(HeadingChange, yaw_angle)
        log.add({
        'ang_vel': ang_vel,
        'acc_yaw': yaw_angle,
        'dev': HeadingDev
        })
        if turn_complete(HeadingChange,HeadingDev):
            break
        sleep(sample_rate)  # Adjust sample rate

    sbcmotorcontroller.motor_stop(sbcmotorcontroller.MotorA)
    sbcmotorcontroller.motor_stop(sbcmotorcontroller.MotorB)
    