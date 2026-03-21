PDCA-3.2 Legobot

# Goal
-  Change to a turn_to_target(heading) first them move(distance) strategy

## PLAN
- Using Cursor 2.4.37
- [ ] replace move with move(distance, motor_power, cm_sec ). Prompt:
Previous tests concluded 
1. clearly compass reading stabilizes stdDev = 2.5 deg, so averaging several reading will improve accuracy
2. compass readings are all above target heading by 14, 18, 27 degrees, gets worse with distance or time. don't even log complass while motors are running.
Please u


## DO

## CHECK

## ACT
