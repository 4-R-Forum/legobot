PDCA-LegoBotAI-1.4

# Purpose

Field test making a turn with motors and gyro, resolve issues:
- signed angular velocity
- log duration appears to be less than actual
- headingDev appears to start at 0 and increase negatively, should appoach zero
- bot hunts and never stops
- need combined sw and field unit tests

## PLAN

- Log shows same pattern as others acc never decreases, does angVel have sign?
- Investigate and fix for successful field test
- Process using MicroPython editor and VSCode still prone to fumbles. Improve and document

# DO

- see 1.4-Notes.txt
- changing to  while True ... break, makes big improvement
- truncated log probably not memory
- process documention started

# CHECK
- turn_heading_test now turns and stops, with +- headingChange

# ACT
- improve while logic
- reduce angular velocity
- streamline logging
- ready for unit tests
- update process