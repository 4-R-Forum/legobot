from microbit import *
import log, time
import mpu6050
pdca = "G1.8.0"

def log_compass():
    sleep(200)
    heading_cw = compass.heading()
    heading_ccw = (-heading_cw + 180) % 360 - 180
    log.add({'heading_ccw':heading_ccw})


# Global Setup
# wait until logo pressed
display.show(pdca)

display.show("R") 
while not pin_logo.is_touched():
    sleep(100)

mpu6050.init_mpu6050()
start_time = time.ticks_ms()   # Get initial time in milliseconds
last_time = start_time
yaw_angle = 0
alpha = 0.5  # Smoothing factor (adjust as needed)

# reset log
log.delete()
log.set_labels('ang_vel','acc_yaw','dev', 'heading_ccw')
# main code #


mpu6050.turn_heading_test(30, 3, 80,"cw")
sleep(500)
mpu6050.turn_heading_test(60, 3, 80,"cw")
sleep(500)
mpu6050.turn_heading_test(-30, 3, 80,"cw")
sleep(500)
mpu6050.turn_heading_test(-60, 3, 80,"cw")
display.show(Image.YES)
