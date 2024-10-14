import serial
import random 
import time

serial_port = '/dev/ttyUSB0'
baud_rate = 115200
ser = serial.Serial(serial_port, baud_rate, timeout=1)
start_time = time.time()
duration=15

try:
    while True:
        elapsed_time = time.time() - start_time
        if elapsed_time >= duration:
            break
        data = 0x34
        data2 = 0xAA
        ser.write(bytes([data]))
        ser.write(bytes([data2]))
        print(f"Sent: 0x{data:02X}, 0x{data2:02X}")
        time.sleep(0.5)

except KeyboardInterrupt:
    print ("Program stopped by user")

finally:
    ser.close()

