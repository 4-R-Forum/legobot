let debug = 0
let heading_dev = 0
let heading_T = 0
let heading_thold = 0
let go = 0
input.onButtonPressed(Button.A, function () {
    debug = 0
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
    while (true) {
        calc_h_dev(input.compassHeading(), heading_T)
        if (heading_dev < 0 - heading_thold) {
            basic.showLeds(`
                . . . . .
                . . . . .
                . . . . #
                . . . . .
                . . . . .
                `)
            // turn right
            MotorDriver.MotorRun(Motor.A, Dir.forward, 8)
            MotorDriver.MotorRun(Motor.B, Dir.backward, 8)
        }
        if (heading_dev > heading_thold) {
            basic.showLeds(`
                . . . . .
                . . . . .
                # . . . .
                . . . . .
                . . . . .
                `)
            // turn left
            MotorDriver.MotorRun(Motor.A, Dir.backward, 8)
            MotorDriver.MotorRun(Motor.B, Dir.forward, 8)
        }
        // within range
        if (heading_dev >= 0 - heading_thold && heading_dev <= heading_thold) {
            if (heading_dev >= 0 - 2 && heading_dev <= 2) {
                basic.showLeds(`
                    . . . . .
                    . . . . .
                    . . # . .
                    . . . . .
                    . . . . .
                    `)
            } else {
                basic.showLeds(`
                    . . . . .
                    . . . . .
                    . # # # .
                    . . . . .
                    . . . . .
                    `)
            }
            MotorDriver.MotorStop(Motor.A)
            MotorDriver.MotorStop(Motor.B)
            break;
        }
    }
}
function TurnHeadingtest () {
    while (heading_dev != 0) {
        while (heading_dev < 0 - heading_thold || heading_dev > heading_thold) {
            if (heading_dev < 0 - heading_thold) {
                // turn right
                MotorDriver.MotorRun(Motor.A, Dir.forward, 8)
                MotorDriver.MotorRun(Motor.B, Dir.backward, 8)
                go = 1
                heading_dev += 1
            }
            if (heading_dev > heading_thold) {
                // turn left
                MotorDriver.MotorRun(Motor.A, Dir.backward, 8)
                MotorDriver.MotorRun(Motor.B, Dir.forward, 8)
                go = -1
                heading_dev += -1
            }
        }
        MotorDriver.MotorStop(Motor.A)
        MotorDriver.MotorStop(Motor.B)
        go = 0
        break;
    }
}
function Forth () {
    MotorDriver.MotorRun(Motor.A, Dir.backward, 10)
    MotorDriver.MotorRun(Motor.B, Dir.backward, 10)
    basic.pause(2000)
    MotorDriver.MotorStop(Motor.A)
    MotorDriver.MotorStop(Motor.B)
}
input.onButtonPressed(Button.AB, function () {
    basic.showIcon(IconNames.SmallDiamond)
    input.calibrateCompass()
    basic.showIcon(IconNames.Square)
})
input.onButtonPressed(Button.B, function () {
    debug = 1
})
input.onLogoEvent(TouchButtonEvent.Pressed, function () {
    basic.showString("L13")
    basic.pause(1000)
    basic.clearScreen()
    datalogger.deleteLog(datalogger.DeleteType.Full)
    heading_T = 0
    heading_thold = 10
    if (debug == 1) {
        basic.showNumber(input.compassHeading())
        basic.showNumber(heading_T)
        calc_h_dev(input.compassHeading(), heading_T)
        basic.showNumber(heading_dev)
    }
    TurnHeading(0)
    for (let index = 0; index < 4; index++) {
        if (heading_T == 0) {
            basic.showString("N")
        }
        if (heading_T == 90) {
            basic.showString("E")
        }
        if (heading_T == 180) {
            basic.showString("S")
        }
        if (heading_T == 270) {
            basic.showString("W")
        }
        Forth()
        heading_T += 90
        if (heading_T == 360) {
            heading_T = 0
        }
        TurnHeading(heading_T)
    }
    basic.showIcon(IconNames.Yes)
})
basic.forever(function () {
	
})
