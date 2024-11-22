debug = 0
heading_dev = 0
heading_T = 0
heading_thold = 0
go = 0

def on_button_pressed_a():
    global debug
    debug = 0
input.on_button_pressed(Button.A, on_button_pressed_a)

def calc_h_dev(cur: number, tgt: number):
    global heading_dev
    if cur - tgt > 180:
        heading_dev = cur - tgt - 360
    else:
        heading_dev = cur - tgt
def TurnHeading(target: number):
    while True:
        calc_h_dev(input.compass_heading(), heading_T)
        if heading_dev < 0 - heading_thold:
            basic.show_leds("""
                . . . . .
                . . . . .
                . . . . #
                . . . . .
                . . . . .
                """)
            # turn right
            MotorDriver.motor_run(Motor.A, Dir.FORWARD, 8)
            MotorDriver.motor_run(Motor.B, Dir.BACKWARD, 8)
        if heading_dev > heading_thold:
            basic.show_leds("""
                . . . . .
                . . . . .
                # . . . .
                . . . . .
                . . . . .
                """)
            # turn left
            MotorDriver.motor_run(Motor.A, Dir.BACKWARD, 8)
            MotorDriver.motor_run(Motor.B, Dir.FORWARD, 8)
        # within range
        if heading_dev >= 0 - heading_thold and heading_dev <= heading_thold:
            if heading_dev >= 0 - 2 and heading_dev <= 2:
                basic.show_leds("""
                    . . . . .
                    . . . . .
                    . . # . .
                    . . . . .
                    . . . . .
                    """)
            else:
                basic.show_leds("""
                    . . . . .
                    . . . . .
                    . # # # .
                    . . . . .
                    . . . . .
                    """)
            MotorDriver.motor_stop(Motor.A)
            MotorDriver.motor_stop(Motor.B)
            break
def TurnHeadingtest():
    global go, heading_dev
    while heading_dev != 0:
        while heading_dev < 0 - heading_thold or heading_dev > heading_thold:
            if heading_dev < 0 - heading_thold:
                # turn right
                MotorDriver.motor_run(Motor.A, Dir.FORWARD, 8)
                MotorDriver.motor_run(Motor.B, Dir.BACKWARD, 8)
                go = 1
                heading_dev += 1
            if heading_dev > heading_thold:
                # turn left
                MotorDriver.motor_run(Motor.A, Dir.BACKWARD, 8)
                MotorDriver.motor_run(Motor.B, Dir.FORWARD, 8)
                go = -1
                heading_dev += -1
        MotorDriver.motor_stop(Motor.A)
        MotorDriver.motor_stop(Motor.B)
        go = 0
        break
def Forth():
    MotorDriver.motor_run(Motor.A, Dir.FORWARD, 10)
    MotorDriver.motor_run(Motor.B, Dir.FORWARD, 10)
    basic.pause(2000)
    MotorDriver.motor_stop(Motor.A)
    MotorDriver.motor_stop(Motor.B)

def on_button_pressed_ab():
    basic.show_icon(IconNames.SMALL_DIAMOND)
    input.calibrate_compass()
    basic.show_icon(IconNames.SQUARE)
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    global debug
    debug = 1
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_logo_pressed():
    global heading_T, heading_thold
    basic.show_string("L13")
    basic.pause(1000)
    basic.clear_screen()
    datalogger.delete_log(datalogger.DeleteType.FULL)
    heading_T = 0
    heading_thold = 10
    if debug == 1:
        basic.show_number(input.compass_heading())
        basic.show_number(heading_T)
        calc_h_dev(input.compass_heading(), heading_T)
        basic.show_number(heading_dev)
    TurnHeading(0)
    for index in range(4):
        if heading_T == 0:
            basic.show_string("N")
        if heading_T == 90:
            basic.show_string("E")
        if heading_T == 180:
            basic.show_string("S")
        if heading_T == 270:
            basic.show_string("W")
        Forth()
        heading_T += 90
        if heading_T == 360:
            heading_T = 0
        TurnHeading(heading_T)
    basic.show_icon(IconNames.YES)
input.on_logo_event(TouchButtonEvent.PRESSED, on_logo_pressed)

def on_forever():
    calc_h_dev(input.compass_heading(), heading_T)
    datalogger.log(datalogger.create_cv("compass", input.compass_heading()),
        datalogger.create_cv("target", heading_T),
        datalogger.create_cv("dev", heading_dev))
basic.forever(on_forever)
