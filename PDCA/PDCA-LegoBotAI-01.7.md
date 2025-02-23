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
    - result in PDCA-1.7.3.png, looks perfect
    - angular acc, deviation and turn all share gyro convention CCW turn is +ve
    - now compass must follow same convention, compass reading 330 deg is +30, 30 deg reading is -30 deg
    - ACT read compass after motors stop






