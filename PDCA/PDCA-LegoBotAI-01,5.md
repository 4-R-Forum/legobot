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

## CHECK

1.5.0
- with motor power =3 and -60 log at _Gus2B\1-Projects\LegoBot\Gyro-PDCA-1.5.2.xlsx"
- looks like delay between motor starts and stops affect result, consider options to mitigate
- mdtor powers 1 and 2 tend to not turn enough, 3 seems OK with ang_vel ~ 2 deg/sec
