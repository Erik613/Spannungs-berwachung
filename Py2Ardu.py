import serial

while True:
    with serial.Serial('COM3', 9600, ) as ser:
        x = ser.read()
        try:
            print(int(x))
        except:
            pass