def on_button_pressed_ab():
    global n
    input.calibrate_compass()
    n = 1
    basic.show_icon(IconNames.SQUARE)
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def calc_h_dev2(cur: number, tgt: number):
    pass
def stopMotors():
    MotorDriver.motor_stop(Motor.A)
    MotorDriver.motor_stop(Motor.B)
def goFwd(speed: number, dist: number):
    pass
def calc_h_dev(cur2: number, tgt2: number):
    global diff, heading_dev
    diff = tgt2 - cur2
    if diff > 0:
        if diff > 180:
            heading_dev = 180 - diff
        else:
            heading_dev = diff
    else:
        if diff < -180:
            heading_dev = 360 + diff
        else:
            heading_dev = diff
def TurnHeading(target: number):
    if True:
        # Dev +ve
        # Turn Right, ClockWise
        basic.show_leds("""
            . . . . .
            . . . . .
            . . . . #
            . . . . .
            . . . . .
            """)
        # turn right
        MotorDriver.motor_run(Motor.A, Dir.FORWARD, turnSpeed)
        MotorDriver.motor_run(Motor.B, Dir.BACKWARD, turnSpeed)
        basic.pause(10 * abs(heading_dev))
        stopMotors()
    if heading_dev < 0 - heading_thold:
        # Dev -ve
        # Turn Left, AntiClockwise
        basic.show_leds("""
            . . . . .
            . . . . .
            # . . . .
            . . . . .
            . . . . .
            """)
        # turn left
        MotorDriver.motor_run(Motor.A, Dir.BACKWARD, turnSpeed)
        MotorDriver.motor_run(Motor.B, Dir.FORWARD, turnSpeed)
        basic.pause(10 * abs(heading_dev))
        stopMotors()
    # within range
    if heading_dev >= 0 - heading_thold and heading_dev <= heading_thold:
        if heading_dev >= 0 - 2 and heading_dev <= 2:
            # Spot on, within 2 deg
            basic.show_leds("""
                . . . . .
                . . . . .
                . . # . .
                . . . . .
                . . . . .
                """)
        else:
            # Within threshold
            basic.show_leds("""
                . . . . .
                . . . . .
                . # # # .
                . . . . .
                . . . . .
                """)
    stopMotors()

def on_button_pressed_a():
    pass
input.on_button_pressed(Button.A, on_button_pressed_a)

def Forth():
    MotorDriver.motor_run(Motor.A, Dir.BACKWARD, 10)
    MotorDriver.motor_run(Motor.B, Dir.BACKWARD, 10)
    basic.pause(2000)
    MotorDriver.motor_stop(Motor.A)
    MotorDriver.motor_stop(Motor.B)

def on_button_pressed_b():
    global n
    n += -1
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_logo_pressed():
    global turnSpeed, heading_T, heading_thold, compReading
    basic.show_string("L15")
    datalogger.delete_log(datalogger.DeleteType.FAST)
    turnSpeed = 4
    heading_T = 0
    heading_thold = 5
    while True:
        compReading = input.compass_heading()
        calc_h_dev(compReading, heading_T)
        datalogger.log(datalogger.create_cv("compass", compReading),
            datalogger.create_cv("target", heading_T),
            datalogger.create_cv("dev", heading_dev),
            datalogger.create_cv("interval", n))
        TurnHeading(heading_T)
        if heading_dev > heading_thold and heading_dev < 0 - heading_thold:
            break
        basic.pause(1000 * n)
    basic.show_icon(IconNames.YES)
input.on_logo_event(TouchButtonEvent.PRESSED, on_logo_pressed)

compReading = 0
heading_T = 0
heading_thold = 0
turnSpeed = 0
heading_dev = 0
diff = 0
n = 0
basic.show_icon(IconNames.SMALL_DIAMOND)

def on_forever():
    pass
basic.forever(on_forever)
