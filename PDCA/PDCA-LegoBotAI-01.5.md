PDCA-LegoBotAI-1.5

# Purpose
- improve while logic
- reduce angular velocity
- streamline logging
- ready for unit tests
- update process

## PLAN
- make min changes in main
- bench test +- 30

## DO

1.5.0
- min changes
- -30 and -60
1.5.1
- generalize changes
- add parameters to turn_heading_test
- mutiple tests in unit test module
1.5.2
- log raw, value
- bench test


## CHECK
  
1.5.0
- with motor power =3 and -60 log at _Gus2B\1-Projects\LegoBot\Gyro-PDCA-1.5.2.xlsx"
- looks like delay between motor starts and stops affect result, consider options to mitigate
    - start motor in direction of change first
    - stop motor in direction of change last
- motor powers 1 and 2 tend to not turn enough, 3 seems OK with ang_vel ~ 2 deg/sec

1.5.1
- 4 tests mostly successful
- no -ve ang_acc. Why1?
- +ve Heading change approx correct
- -ve about half way. Why2?
- bot turns wrong way on all turns. Why3?
- see log 1.5.3 and video

1.5.2
- 
- it looks like gyro is returning ang_vel of +2 +- 0.1 deg/sec regardless of actual, see _Gus2B\1-Projects\LegoBot\microbit (19).csv"
- even when not rotating, see 1.5.2.1.xlsx using LegobotAI-Gyro-01.py
- this explains Why1, ang_vel is always +ve
- and Why2, bot does not know actual ang_vel

## ACT
- Check microbit voltage on bot and 6050, 3.3 or 5?
- Breadboard test of microbit with only MPU6050
