# Data-handler-practice-
This is a mock data handler the goal is to take in hex data from a csv file acting as a serial buffer, parse it, log it, and do some form of manipulation to it. 

# mock data sheet
Slave Address: 0x01
Function Code: 0x03 (Read Holding Registers)
Byte Count: 0x08 (4 registers, each 2 bytes)
Register 0x0001: Temperature (°C ×10), bytes [3–4]
Register 0x0002: Humidity (%RH ×10), bytes [5–6]
Register 0x0003: Pressure (kPa ×100), bytes [7–8]
Register 0x0004: Vibration Level (mm/s ×100), bytes [9–10]
CRC: Omitted in this example
All values are unsigned integers
To convert raw values to real units, divide by their respective scale factors (10, 10, 100, 100)
Packets are in Modbus RTU response format, no delimiters, space-separated hex for readability

packet breakdown
01 03 08 01 2C 00 FA 27 10 00 64
01        → Slave Address = 1  
03        → Function Code = 3 (Read Holding Registers)  
08        → Byte Count = 8 (4 registers × 2 bytes each)

01 2C     → Temperature = 0x012C = 300 → 30.0 °C  
00 FA     → Humidity    = 0x00FA = 250 → 25.0 %RH  
27 10     → Pressure    = 0x2710 = 10000 → 100.00 kPa  
00 64     → Vibration   = 0x0064 = 100 → 1.00 mm/s



