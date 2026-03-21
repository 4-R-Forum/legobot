PDCA 3.1 LegoBot

# Goal

- Investigate and calibrate  move fwd/back
- Investigate magnetic field decay and compass reliability


## PLAN
- Using Cursor 2.4.37
- [x] create function move(heading, distance) in 6050
- [x] create function log_compass(duration) in n 6050
- [x] create test for both in main

 ## DO
- Prompt for move function to agent
Please create a fuction in mpu6050.py with parameters heading representing and dist representing distance in centimeters. Vary motor power and move duration to achieve the distance. It will be necessary to create calibration tests for this purposes.
- Plan at C:\Users\ghodg\.cursor\plans\move-heading-distance_a70e4124.plan.md
- Bench test 1
- Field test 3.1 log at "C:\Users\ghodg\Downloads\microbit (32).csv"
- tests to 3.1.3
- Prompt for read_compass
Please creat a function in mpu6050.py with parameer duration in seconds. Value for duration to be set in main.py. Log compass reading at start and every one tenth of duration, total 11 readings. Default value for duration = 5 seconds
- Field test 3.1.4


## CHECK
- Bench test 3.0
    - ran compass calibraton
    - pressed A, motors ran 3 times
    - scrolling fonts difficult to read, need a checklist
    - log at "C:\Users\ghodg\Downloads\microbit (31).csv"
- Field test 3.1
    - kp = 0.2
    - press A, motors run 3 times, for progressive distances
    - bot swings side to side rapidly, not a straight line, need much lower kp
- Field test 3.1.1
    - kp = 0.05 ->
    - distances about right, not measured, path still wonky => decrease kp further
- Field test 3.1.2
    - kp = 0.02
    - distances ditto, path now veres right
    - one more try with Kp = 0.1, if that doesn't work, change to turn first then move. simpler and easier to test and correct
- Filed test 3.1.3
    - kp = 0.1
    - heading still changing but good enough to continue to test compass reliablilty
- Field test 3.1.4
    - log at "C:\Users\ghodg\Downloads\microbit (33).csv" saved as https://d.docs.live.net/c9fe7ec56ddc73db/_Gus2B/1-Projects/LegoBot-Gus2B/FieldTest-3.1.4.xlsx
    - clearly compass reading stabilizes stdDev = 2.5 deg, so averaging several reading will improve accuracy
    - compass readings are all above target heading by 14, 18, 27 degrees, gets worse with distance or time.
    - don't even log complass while motors are running

## ACT
-  Change to a turn_to_target(heading) first them move(distance) strategy