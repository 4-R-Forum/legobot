PDCA-LegobotAI-01

# Purpose:

Take advantage of ML to speed up and streamline change of heading when stopping motors in order to read compass.

## PLAN

- External factors
  - HeadingChange
  - StopReadDelay
  - MotorPower
    - ExpetedDuration
  - Surface
  -BatteryPower (later)

- GlobalVariables
  - ExternalFactors
  - TimeTick

- Start with single turn test
- List all tests later

- For each test
  - log GlobalVariables
  - while turnDeg lt headingChange
    - calc angVel
    - calc tickDeg
    - turnDeg += tickDeg
    - log tick, angVel, tick, turnDeg

## DO
- Test Gyroscope alone first PDCA-:egoBotAI-01.1
- Incorporate POC for field test 1.2
 

