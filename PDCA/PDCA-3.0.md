LegoBot PDCA-3.0

# Goal

Restart legobot work, starting from 2.3, with goal of transfering to a new project on Keystudio Mbit or XRP base.

## Recap on project status.
1. We know compass cannot work while motors are powered on.
2. Gyro is attempting to integrate ang-vel to determine heading
3. Code is MicroPython
    - edited in https://python.microbit.org/v/3 , which has no git integration
    - pythong code in main, mpu6050 and sbcmotorcontroller .py
    - as well as copy pasted to C:\Repos\legobot\work\PCode-1.8.1.py
4. What conclusions can we draw from "microbit2 thru 10 charts" referred tp in PCDA-2.3?
    - The function is defined as:
        def turn_heading_test(HeadingChange, MotorPower, sample_rate, rotation)
        - Gemini suggests testing for bias instead of using hard coded value
    
## PLAN
- [ ] Retest 3 py files on LegoBot at G3.0

## CHECK
- With help from Gemini in Repo. No GYRO, NO I12C
- Check Wiring
    - 6050 VCC  Green  SBC 3V3
    - 6050 GND  Yellow SBC GND
    - 6050 SLC  Red    SBC P19 Wires reversed, Corrected
    - 6050 SDA  Orange SBC P20 Wires reversed, Corrected
- Need to calibrate compass on prompt
- test completed successfully
- **Test Analysis (Gyro Integration Fix):**
    - **Direction:** Fixed. Positive targets result in positive angular velocity.
    - **Integration:** Fixed. `acc_yaw` correctly tracks velocity over time.
    - **Performance:**
        - Target 30: Error ~0.1° (Excellent)
        - Target 60: Error +6.5° (Overshoot). Start anomaly observed (brief -ve rotation).
        - Overshoot caused by 80ms loop latency at ~100°/s (approx 8° per loop).
- **Test Analysis (Compass Test):**
    - **Gyro:** Remains consistent.
        - +30 Target -> +30.5 deg (0.5 overshoot)
        - +60 Target -> +64.5 deg (4.5 overshoot)
        - -30 Target -> -30.3 deg (0.3 overshoot)
        - -60 Target -> -63.9 deg (3.9 overshoot)
    - **Compass:** Unusable/Inconsistent. Delta between readings does not match executed turn (e.g., +60 turn showed +151 compass change).

- Shelve compass investigation. Focused on improving turn accuracy.

- Implement proportional control in `turn_heading_test` to reduce overshoot.
    - Motor power will now be proportional to the remaining heading deviation (`HeadingDev`).
    - This will make the robot slow down as it approaches the target heading.
    - Introduce `P_GAIN` and `MIN_POWER` constants for tuning.
- **Test Analysis (Proportional Control Attempt 1):**
    - Result: Overshoot worsened (e.g., Target 60 overshoot ~10°). Velocity increased during turn.
    - Cause 1: `MIN_POWER` (4) was > `MotorPower` (3). Logic `max(MIN, min(MAX, calc))` forced power to 4 continuously.
    - Cause 2: `P_GAIN` (2.5) was too high. Braking would only trigger at <1.2° error, which is smaller than the loop latency distance (~8-10°).
    - **Fix:** Decrease `MIN_POWER` to 1. Decrease `P_GAIN` to 0.2 to start braking at ~15° error.
- **Test Analysis (Proportional Control Attempt 2):**
    - Result: Improvement. Target 60 overshoot reduced to 1.2°. Target 30 overshoot ~3.2°.
    - Observation: Velocity dropped from ~90°/s to ~75°/s.
    - Issue: 80ms loop time is too slow. At 75°/s, robot travels ~6° per loop (blind spot).
    - Issue: `P_GAIN` 0.2 brakes at <5°, which is inside the blind spot.
    - **Fix:** Reduce `P_GAIN` to 0.1 (brake at 10°). Reduce `sample_rate` in `main.py` to 20ms.
- **Test Analysis (Stall at Power 1):**
    - **Issue:** Robot turns incomplete. Data shows `ang_vel` dropping to ~0 with `dev` remaining at ~15°.
    - **Cause:** `P_GAIN` (0.1) reduced power to `int(0.1 * 17) = 1`. `MIN_POWER` was 1. Motor Speed 1 is insufficient to move the robot under load.
    - **Fix:** Increase `MIN_POWER` to 2.
- **Test Analysis (Tuning Complete):**
    - **Result:** Excellent. Overshoot is consistently < 1.1°. Stall is resolved.
    - **Parameters:** `MIN_POWER=2`, `P_GAIN=0.1`, `sample_rate=20ms` are the final tuned values.
    - **Conclusion:** The proportional control turning logic is now reliable and accurate.
- **ACT (Refactor):**
    - Refactor the code for clarity and usability.
    - In `mpu6050.py`, rename `turn_heading_test` to `turn` and make `sample_rate` an internal constant.
    - In `main.py`, simplify the main loop by removing now-unnecessary global variables and updating calls to the new `turn` function.

## ACT

- Investigate magnetic field decay and compass reliability
- Investigate and calibrate  move fwd/back