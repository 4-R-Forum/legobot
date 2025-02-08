PDCA-LegoBotAI-1.3

# Purpose

Field test makding a turn with motors, and log drift over several turns

## PLAN
- Mount 6050 on LegoBot
- update test_turn fucntion
- test with several turns to seek several headings with straight moves in between
- log drift at each stop

## DO
- Mount 6050
- Update main.py
- port sbcmotorcontroller from typescript to python
- create MicroPython code
- run in simulator
- Field test
1.3.1
- debug motor not working
- debug vacillating accumulated
- refactored sbcmotorcontroller.py in Mbit MicroPython editor using intellisense
- added sleep(sample_rate) to end of turn_heading test

1.3.3
- updated all-in-one main-1.py, noticed gray variable not used warnings in MicroPython editor
- refactored code in MixeoPython editor

1.3.4

- crimp Dupont motor connections

## CHECK

- Simulator logs one zero reading and shows OK image and ends with "dirty" message
- motors don't turn, turned bot manually
- data logged about 20 sec
- angular velocity logged, but accumulated vacillates +- 70

1.3.1
- all code in single py file, motors still don't run 
- sample rate 100ms resolves logged data

1.3.2
- logs data, but no motor movement
- L-16 runs motors so it still looks like issue with sbcmotorcontroller

1.3.3
- bench test, now motors are running!
- try now with separate sbcmotorcontroller.py 

1.3.4
- now with separate sbcmotocontroller, bench test successful, motors running
- field test, makes turn but does not complete successfully
- log in Gus2B/1-Projects/LegoBot/Gyro-PDCA-1.3.4.xlsx

## ACT
- Now we have a motor driver. Great.
- Log shows same pattern as others acc never decreases, does angVel have sign?
- Investigate and fix for successful field test
- Process using MicroPython editor and VSCode still prone to fubles. Improve and document