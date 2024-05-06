heading_T = 0
heading_thold = 0

def on_button_pressed_a():
    global heading_T, heading_thold
    if True:
        basic.show_string("4<5<5")
    heading_T = 0
    heading_thold = 5
    while True:
        basic.show_number(input.compass_heading())
        if True:
            basic.show_string("Y")
        else:
            basic.show_string("N")
        if input.button_is_pressed(Button.B):
            break
input.on_button_pressed(Button.A, on_button_pressed_a)

def TurnHeading(target: number):
    while input.compass_heading() - target < 0 - heading_thold or input.compass_heading() - target > heading_thold:
        if input.compass_heading() - target < 0 - heading_thold:
            # turn right
            MotorDriver.motor_run(Motor.A, Dir.FORWARD, 8)
            MotorDriver.motor_run(Motor.B, Dir.BACKWARD, 8)
        else:
            # turn left
            MotorDriver.motor_run(Motor.A, Dir.BACKWARD, 8)
            MotorDriver.motor_run(Motor.B, Dir.FORWARD, 8)
    MotorDriver.motor_stop(Motor.A)
    MotorDriver.motor_stop(Motor.B)
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
    basic.show_string("B")
    MotorDriver.motor_run(Motor.B, Dir.FORWARD, 10)
    basic.pause(2000)
    MotorDriver.motor_stop(Motor.B)
    basic.show_icon(IconNames.YES)
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_logo_pressed():
    global heading_T, heading_thold
    basic.show_string("L8")
    basic.pause(1000)
    basic.clear_screen()
    heading_T = 0
    heading_thold = 5
    basic.show_number(heading_T)
    TurnHeading(0)
    for index in range(4):
        Forth()
        heading_T += 90
        basic.show_number(heading_T)
        TurnHeading(heading_T)
    basic.show_icon(IconNames.YES)
input.on_logo_event(TouchButtonEvent.PRESSED, on_logo_pressed)
