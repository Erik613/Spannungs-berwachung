import serial
import traceback
import datetime

a = 0

while True:
    with open("log.txt", "a") as log:
        try:
            with serial.Serial('COM3', 9600, ) as ser:
                x = ser.read()
                if float(x) > 1:
                    b = datetime.datetime.now().strftime("%d.%m.%Y - %H:%M:%S")
                    print(b + " | " + str(float(x)))
                    log.write(str(b) + " | " + str(float(x)) + "\n")
                else:
                    print("Messung beendet")
                    log.write(str(b) + " | " + str(float(x)) + " Messung beendet""\n")
                    break

                a = 0
        except serial.serialutil.SerialException:
            a += 1
            if a == 1:
                c = datetime.datetime.now().strftime("%d.%m.%Y - %H:%M:%S"), "| Hardware wurde Entfernd"
                print(c)
                log.write(str(c))
                traceback.print_exc()
                a = 2
        except:
            pass
