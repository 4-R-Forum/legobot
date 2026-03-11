def turn_heading_test():
    global heading_dev, heading_thold, go
    while heading_dev != 0:
        while heading_dev < -heading_thold or heading_dev > heading_thold:
            if heading_dev < -heading_thold:
                # Turn right
                MotorDriver.MotorRun(Motor.A, Dir.forward, 8)
                MotorDriver.MotorRun(Motor.B, Dir.backward, 8)
                go = 1
                heading_dev += 1
            elif heading_dev > heading_thold:
                # Turn left
                MotorDriver.MotorRun(Motor.A, Dir.backward, 8)
                MotorDriver.MotorRun(Motor.B, Dir.forward, 8)
                go = -1
                heading_dev -= 1
        MotorDriver.MotorStop(Motor.A)
        MotorDriver.MotorStop(Motor.B)
        go = 0
        break
