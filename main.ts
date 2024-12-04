input.onButtonPressed(Button.AB, function () {
    input.calibrateCompass()
    n = 1
    basic.showIcon(IconNames.Square)
})
function calc_h_dev2 (cur: number, tgt: number) {
	
}
function stopMotors () {
    MotorDriver.MotorStop(Motor.A)
    MotorDriver.MotorStop(Motor.B)
}
function goFwd (speed: number, dist: number) {
	
}
input.onButtonPressed(Button.A, function () {
	
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
function TurnHeading (target: number) {
    if (true) {
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
        MotorDriver.MotorRun(Motor.A, Dir.forward, turnSpeed)
        MotorDriver.MotorRun(Motor.B, Dir.backward, turnSpeed)
        basic.pause(10 * Math.abs(heading_dev))
        stopMotors()
    }
    if (heading_dev < 0 - heading_thold) {
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
        MotorDriver.MotorRun(Motor.A, Dir.backward, turnSpeed)
        MotorDriver.MotorRun(Motor.B, Dir.forward, turnSpeed)
        basic.pause(10 * Math.abs(heading_dev))
        stopMotors()
    }
    // within range
    if (heading_dev >= 0 - heading_thold && heading_dev <= heading_thold) {
        if (heading_dev >= 0 - 2 && heading_dev <= 2) {
            // Spot on, within 2 deg
            basic.showLeds(`
                . . . . .
                . . . . .
                . . # . .
                . . . . .
                . . . . .
                `)
        } else {
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
input.onButtonPressed(Button.B, function () {
    n += -1
})
input.onLogoEvent(TouchButtonEvent.Pressed, function () {
    basic.showString("L15")
    datalogger.deleteLog(datalogger.DeleteType.Fast)
    turnSpeed = 4
    heading_T = 0
    heading_thold = 5
    while (true) {
        compReading = input.compassHeading()
        calc_h_dev(compReading, heading_T)
        datalogger.log(
        datalogger.createCV("compass", compReading),
        datalogger.createCV("target", heading_T),
        datalogger.createCV("dev", heading_dev),
        datalogger.createCV("interval", n)
        )
        TurnHeading(heading_T)
        if (heading_dev > heading_thold && heading_dev < 0 - heading_thold) {
            break;
        }
        basic.pause(1000 * n)
    }
    basic.showIcon(IconNames.Yes)
})
let compReading = 0
let heading_T = 0
let heading_thold = 0
let turnSpeed = 0
let heading_dev = 0
let diff = 0
let n = 0
basic.showIcon(IconNames.SmallDiamond)
basic.forever(function () {
	
})
