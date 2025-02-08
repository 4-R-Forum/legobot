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
- updated 


- crimp Dupont motor connections

## CHECK

- Simulator logs one zero reading and shows OK image and ends with "dirty" message
- motors don't turn, turned bot manually
- data logged about 20 sec
- angular velocity logged, but accumulated vacillates +- 70

1.3.1
- all code in single py file, motors still don't run 
- sample rate 100ms resolves logged data