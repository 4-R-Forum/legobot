PDCA 1.7

# Purpose

- Apply bias and smoothing for desk/field test of bot
- consider investigating temp variation also

## PLAN
- Crimp motor wires to controller
- reassemble bot
- Refactor main.py for bias and smoothing
- test

## DO
- Review and update main.py
- motor wires crimped and bot reassemble
- test 1.7.2
    - see OneNote "PDCA-1.7 worksheet" this summarizes +ve and -ve values for code
    - result in PDCA-1.7.2.png, and PDCA-1.7.2.mp4
    - behavior in result looks correct, but direction of turn expected is R-R-L-L, actual is L-L-R-R, why?
    - expected magnitude of turn is  30 60 -30 -60, actual approx 30, 30, -30, -45
    - ACT from handwritten notes 3 places in main.py. Update PDCA-1.7 worksheet
- test 1.7.3
    - PDCA-1.7 worksheet updated
    - main.py retrieved from mbit using mbit-python VSCode extension
    - result in PDCA-1.7.3.png, looks perfect, contrary to 1.7.2 L-L-R-R is correct, CCW is +ve
    - angular acc, deviation and turn all share gyro convention CCW turn is +ve
    - now compass must follow same convention, compass reading 330 deg is +30, 30 deg reading is -30 deg
    - ACT read compass after motors stop
- test 1.7.4
    - compass and gyro readings readings in PDCA-1.7.4.png
        - -109 starting position
        - -58 turned  CCW +51, expected +30
        - +27 turned  CCW +85, expected +60
        - -31 turned  CCW -58, expected -30
        - -102 turned CCW -71, expected -60
    - magnetic compass in same place as microbit
        - magnetic compass is affected by proximity to motors and laptop
        - depending on rotation of motors it varies +- 70 deg
        - actual magnetic north is about -20 deg
        - this is a problem
    - ACT record actual turns in video

## CHECK
- test 1.7.5
    - record video 1-Projects\LegoBot\PDCA-1.7.5.mp4
    - measure actual turns, relative to top edgo of desk, CCW +ve
        - -2 start
        - +27, change +29
        - +70, change +53
        - +35, change -35
        - -6, change -41
   - all four compass readings are +ve, spurious

## ACT
- put use of compass readings on hold, may be necessary to abandon
- refactor gyro functions as separate module
- use gyro module to collect data for microbit AI by repeating turn_heading_test
        







