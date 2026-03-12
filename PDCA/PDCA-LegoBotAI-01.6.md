PDCA-1.6

# Purpose

- Check microbit voltage on bot and 6050, 3.3 or 5?
- Breadboard test of microbit with only MPU6050

# PLAN
- check voltage on board
- breadboard test, suggestions from ChatGPT

# DO

1.6.O
- voltage on bot confirmed: microbit 3.24v motorcontroller 7.86v (1.31 v per cell)
- breadboard
    - check range. It is zero, default, max sensitivity
    - check bias, also zero. Surprising!
    - 6050 in horizontal plane, log readings while stationary, breadboard-02.py
        - results in _Gus2B\1-Projects\LegoBot\Breadboard-02.xlsx
        - avg deg/sec = 1.855
    - check bias again breadboard-03
        - bias reported as 0
        - added init_6050() function and called in -03
        - bias reported as 247.4 = 247.4/131 = 1.888 deg/sec, +1.8% higher than breadboard-02
    - updated -02.py to apply bias of 245 raw
        - result in _Gus2B\1-Projects\LegoBot\Breadboard-02.xlsx
        - much better!
        - its clear that careful calibration of 6050, and smoothing is necessary
    - updated -02.py to apply smoothing
        - bias reduced to 242 raw
        - result in _Gus2B\1-Projects\LegoBot\Breadboard-02.3.xlsx
        - accumulated error over 2 sec is 2.4/2 = 1.2 deg/sec * 131 = 157 raw points, need to change bias?
    - let's see if we can log some rotation:
        - increase log time to 10 seconds, increase counter to 500
        - log only ang_vel and acc_yaw, so that data can be previewed in browser
        - on start program, wait 2 seconds, then rapid turn 90deg, wait to end
        - 1.6.1 Results in _Gus2B\1-Projects\LegoBot\PDCA-1.6.1.png. how to interpret this?
            - It's a bit confusing, can't readily determine where 'rapid turn 90deg' occurred.
            - Looks like there is chaos from 1.5 to 5.5 secs with rapid changes of ang_vel +- 180
                - then stable behavior acc_yaw at ~100 deg, is this the 90deg turn?
            - next steps, resolve:
                - could it be the gyro takes 5 secs or so to set up an stabilize
                - would longer reading intervals help
                - would higher alpha value work better
    1.6.2
    - new test steps, wait 8 seconds, rapid turn 90deg wait to 15 seconds
        - result PDCA-1.6.2.1.png
    - repeat with longer time intervals
        - 100 ms interval, result PDCA-1.6.2.2.png
    - repeat with different alpha values, start 0.5
        - 0.5 alpha, result PDCA-1.6.2.3.png
    - 3 results looks like ang_vel overshoots. try again 100ms, 0.5 alpha, slow move like robot
        - result PDCA-1.6.2.4.png, still overshoots to +250 deg/sec. Why?

    ## CHECK    
    - Ah! bias needs to be applied after converting to signed_value, looks like this may cause spurious overshoot
        - result in PDCA-1.6.2.5.png, no overshoot!
        - no need to wait 8 seconds

    ## ACT
    - Apply bias and smoothing for desk/field test of bot
    - consider investigating temp variation also