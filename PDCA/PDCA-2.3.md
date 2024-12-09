# PDCA-2.3

## Goal

- POC2 calc turn duration based on Calc_h_dev
- stop turning on target achieved

## PLAN

- New version L16 [OK]
- Set run time for turn_heading head_dev / 4 deg/sec [OK] 
- change main loop from while true to while heading dev > 0 [OK]
- remove parameter from turn_heading, it uses global var [OK]

Steps to avoid git merge errors between MakeCode and VSCode

- Code and test L16
- Local changes PDCA in MakeCode, to drive work
- Commit from MakeCode
- Pull in VSCode, overwrites main files
- Commit and Push in VSCode, PDCAs will be ignored by MakeCode

## DO

- L16 Created
    - tested in MakeCode debugger, very useful
- Field test
    - unit tests extended
    - fixed logic errors
    - ms/deg of move varies 0 to 30, mode 5, mean 8
- Test plan to avoid merge errors



## CHECK

- see microbit2 thru 10 charts
- test git steps

## ACT

- use turn_rate = 10 ms/deg
- make unit tests part of process for testing software/hardware combo
- ready for POC 3, move and turn functions
- Edit MakeCode in multiple Edge tabs causes git issues, avoid carefully
- consider branch and pull request to merge changes to master