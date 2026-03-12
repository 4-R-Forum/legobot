PDCD-01.8

# Purpose
- put use of compass readings on hold, may be necessary to abandon
- refactor gyro functions as separate module
- use gyro module to collect data for microbit AI by repeating turn_heading_test

## PLAN
- remount 6050 in clip
- create gyro module
- change rotation for 6050 mounted chipside down
- main repeat multiple tests, use available memory

## DO
- 6050 remounted chipside down, 2 screws in controller bracket
- Project 1.8.0 created and  successfully tested with code from 1.7.5
- 6050 module created, updated for chipside down
- main now loops over same 4 turn tests, 10 times

## CHECK
- run Project 1.8.1 , log in \1-Projects\LegoBot\microbit (28).csv, hex in \hex\L-1.8.1.hex commit 1.8.1
