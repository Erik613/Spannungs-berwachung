import serial

with serial.Serial('COM3', 9600, ) as ser:
    x = ser.read()
    print(x)
