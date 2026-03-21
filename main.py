from microbit import *
import log, time
import mpu6050
pdca = "G3.1.4"
duration_s = 5

def log_compass():
    sleep(200)
    heading_cw = compass.heading()
    heading_ccw = (-heading_cw + 180) % 360 - 180
    log.add({'heading_ccw':heading_ccw})


# Global Setup
compass.calibrate()
# wait until logo pressed


display.show("Touch Logo to Start") 
while not pin_logo.is_touched():
    display.show(pdca)

mpu6050.init_mpu6050()
# Perform dynamic calibration while robot is stationary
mpu6050.calibrate_gyro()

# reset log
log.delete()
log.set_labels('ang_vel','acc_yaw','dev','t_heading','heading_ccw','h_err','pA','pB','ms','comp_ms')
# main code #

display.scroll("A=CAL B=TURN")

# Wait for a mode selection.
while not (button_a.is_pressed() or button_b.is_pressed()):
    sleep(50)

if button_a.is_pressed():
    # Simple calibration/test routine:
    # - Use a single cm_per_sec constant and iterate based on measured distance.
    # - After each run, measure actual distance and adjust cm_per_sec externally (or rerun with edits).
    target_heading = mpu6050.compass_heading_ccw_pm180()
    power = 6
    cm_per_sec = 20.0
    Kp = 0.1

    for dist_cm in (25, 50, 100):
        display.scroll("D" + str(dist_cm))
        sleep(300)
        # Hold current heading and drive forward.
        mpu6050.move(target_heading, dist_cm, MotorPower=power, cm_per_sec=cm_per_sec, Kp=Kp)
        sleep(800)
        display.scroll("MEASURE")
        mpu6050.log_compass(duration_s)

    display.show(Image.YES)
else:
    # Existing turn test sequence
    mpu6050.turn(30, 3)
    sleep(300)
    mpu6050.turn(60, 3)
    sleep(300)
    mpu6050.turn(-30, 3)
    sleep(300)
    mpu6050.turn(-60, 3)
    display.show(Image.YES)
