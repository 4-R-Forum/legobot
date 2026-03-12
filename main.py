from microbit import *
import log, time
import mpu6050
pdca = "G3.0"

def log_compass():
    sleep(200)
    heading_cw = compass.heading()
    heading_ccw = (-heading_cw + 180) % 360 - 180
    log.add({'heading_ccw':heading_ccw})


# Global Setup
#compass.calibrate()
# wait until logo pressed


display.show("Touch Logo to Start") 
while not pin_logo.is_touched():
    display.show(pdca)

mpu6050.init_mpu6050()
# Perform dynamic calibration while robot is stationary
mpu6050.calibrate_gyro()

# reset log
log.delete()
log.set_labels('ang_vel','acc_yaw','dev', 'heading_ccw')
# main code #

mpu6050.turn(30, 3)
#log_compass()
sleep(300)
mpu6050.turn(60, 3)
#log_compass()
sleep(300)
mpu6050.turn(-30, 3)
#log_compass()
sleep(300)
mpu6050.turn(-60, 3)
#log_compass()
display.show(Image.YES)
