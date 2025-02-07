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
- crimp Dupont motor connections

## CHECK

- Simulator logs one zero reading and shows OK image and ends with "dirty" message
