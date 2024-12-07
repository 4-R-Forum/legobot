function calc_h_dev2 (cur: number, tgt: number) {
	
}
// tests calc_h_dev
function unit_1 () {
    calc_h_dev(45, 0)
    TurnHeading()
    basic.pause(500)
    basic.showNumber(heading_dev)
    calc_h_dev(135, 0)
    TurnHeading()
    basic.pause(500)
    basic.showNumber(heading_dev)
    calc_h_dev(225, 0)
    TurnHeading()
    basic.pause(500)
    basic.showNumber(heading_dev)
    calc_h_dev(315, 0)
    TurnHeading()
    basic.pause(500)
    basic.showNumber(heading_dev)
}
function stopMotors () {
    MotorDriver.MotorStop(Motor.A)
    MotorDriver.MotorStop(Motor.B)
}
function goFwd (speed: number, dist: number) {
	
}
input.onButtonPressed(Button.A, function () {
    unit_1()
})
function calc_h_dev (cur: number, tgt: number) {
    diff = tgt - cur
    if (diff > 0) {
        if (diff > 180) {
            heading_dev = 180 - diff
        } else {
            heading_dev = diff
        }
    } else {
        if (diff < -180) {
            heading_dev = 360 + diff
        } else {
            heading_dev = diff
        }
    }
}
function unit_21 (num: number) {
    heading_dev = num
    compReading = input.compassHeading()
    TurnHeading()
    datalogger.log(
    datalogger.createCV("compass", compReading),
    datalogger.createCV("dev", heading_dev),
    datalogger.createCV("turn_ms", turn_ms),
    datalogger.createCV("turn_dir", turn_dir)
    )
}
function TurnHeading () {
    if (heading_dev > heading_thold) {
        turn_dir = "R"
        // Dev +ve
        // Turn Right, ClockWise
        basic.showLeds(`
            . . . . .
            . . . . .
            . . . . #
            . . . . .
            . . . . .
            `)
        // turn right
        MotorDriver.MotorRun(Motor.A, Dir.backward, turnSpeed)
        MotorDriver.MotorRun(Motor.B, Dir.forward, turnSpeed)
        basic.pause(turn_ms)
        stopMotors()
    }
    if (heading_dev < 0 - heading_thold) {
        turn_dir = "L"
        // Dev -ve
        // Turn Left, AntiClockwise
        basic.showLeds(`
            . . . . .
            . . . . .
            # . . . .
            . . . . .
            . . . . .
            `)
        // turn left
        MotorDriver.MotorRun(Motor.A, Dir.forward, turnSpeed)
        MotorDriver.MotorRun(Motor.B, Dir.backward, turnSpeed)
        basic.pause(turn_ms)
        stopMotors()
    }
    // within range
    if (heading_dev >= 0 - heading_thold && heading_dev <= heading_thold) {
        if (heading_dev >= 0 - 2 && heading_dev <= 2) {
            turn_dir = "S"
            // Spot on, within 2 deg
            basic.showLeds(`
                . . . . .
                . . . . .
                . . # . .
                . . . . .
                . . . . .
                `)
        } else {
            turn_dir = "S"
            // Within threshold
            basic.showLeds(`
                . . . . .
                . . . . .
                . # # # .
                . . . . .
                . . . . .
                `)
        }
    }
    stopMotors()
}
function Forth () {
    MotorDriver.MotorRun(Motor.A, Dir.backward, 10)
    MotorDriver.MotorRun(Motor.B, Dir.backward, 10)
    basic.pause(2000)
    MotorDriver.MotorStop(Motor.A)
    MotorDriver.MotorStop(Motor.B)
}
input.onButtonPressed(Button.AB, function () {
    input.calibrateCompass()
    n = 1
    basic.showIcon(IconNames.Square)
})
// tests turn right and left
function unit_2 () {
    turnSpeed = 4
    turn_ms = 1000
    unit_21(16)
    unit_21(-16)
    unit_21(90)
    unit_21(-90)
}
input.onButtonPressed(Button.B, function () {
    unit_2()
})
input.onLogoEvent(TouchButtonEvent.Pressed, function () {
    basic.showString("L16")
    datalogger.deleteLog(datalogger.DeleteType.Fast)
    turnSpeed = 4
    heading_T = 0
    heading_thold = 5
    // 50 ms per degree
    turn_rate = 25
    compReading = input.compassHeading()
    calc_h_dev(compReading, heading_T)
    while (Math.abs(heading_dev) > 1) {
        compReading = input.compassHeading()
        calc_h_dev(compReading, heading_T)
        // ms / deg
        turn_ms = Math.abs(heading_dev) + turn_rate
        datalogger.log(
        datalogger.createCV("compass", compReading),
        datalogger.createCV("dev", heading_dev),
        datalogger.createCV("turn_ms", turn_ms),
        datalogger.createCV("turn_dir", turn_dir)
        )
        TurnHeading()
    }
    basic.showIcon(IconNames.Yes)
})
let turn_rate = 0
let heading_T = 0
let n = 0
let turnSpeed = 0
let heading_thold = 0
let turn_dir = ""
let turn_ms = 0
let compReading = 0
let diff = 0
let heading_dev = 0
basic.showIcon(IconNames.SmallDiamond)
basic.forever(function () {
	
})
