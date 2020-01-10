import serial
import traceback
import datetime

a = 0

while True:
    with open("log.txt", "a") as log:
        try:
            with serial.Serial('COM3', 9600, ) as ser:
                x = ser.read()
                b = datetime.datetime.now().strftime("%d.%m.%Y - %H:%M:%S") , "|" , int(x)
                print(b)
                log.write(str(b)+"\n")

                a = 0
        except serial.serialutil.SerialException:
            a += 1
            if a == 1:
                print(datetime.datetime.now().strftime("%d.%m.%Y - %H:%M:%S"), "| Hardware wurde Entfernd")
                traceback.print_exc()
                a = 2
        except:
            pass
