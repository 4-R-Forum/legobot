# PDCA-LegoBot-2.2

## Goal

- Ready for field test POC, stop motor to read compass
- Start from myPy-POC-2

## PLAN

- Restructure L14 for reading compass while motors not moving
- Strategy for same
- Test and debug strategy in code
- Connecton marking for correct movement on move and turn

## DO

- Restructured code in L15
    - A, B inc,dec pause to find decay time from motor
    - Test and fix L15

## CHECK

- Good result at "C:\Users\ghodg\OneDrive\_Gus2B\1-Projects\LegoBot\microbit (2).xlsx" Chart 5
    - Calc_h_dev correct and turning correctly
    - problem when target achieved, keeps turning!

## ACT

- POC2 calc turn duration based on Calc_h_dev
- stop turning on target achieved
