PDCA-LegoBotAI-01.1

# Purpose

Create a MicroPython function which reads gyroscope and logs calculated readings

# PLAN
- convert power and motor connnections to DuPont
- connect gyro using existing patch DuPont
- follow ChatGPT suggestion
- write code in mbit MicroPython Editor
- test with gyro loosely attached
- review log

#DO31 wire = MA1, 41 wire = MB1


MPU-6050 Pinout recommended by ChatGPT
from left
- vcc Green 3V3
- GND YELLOW GND
- SCL Orange 19
- SDA Red 20
- XDA Yellow
- XCL Orange
- ADO Red
- INT Brown

Sample code from ChatGPT in mbit MicroPython Editor
in repo LegoBot/Gyro Commit a983278

# CHECK
- First run collected yaw data. Wow!, see Gyro-PDCA-1.1.xslx
- Gyro board has power indicator

# ACT

1. Incorporate POC code into L17 for field test with compass, 
2. Mount gyro board, plastic standoff?
3. Field test
