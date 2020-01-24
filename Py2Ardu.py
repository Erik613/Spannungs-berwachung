import serial
import traceback
import datetime
import struct


with open("log.csv", "a") as log:
    time = datetime.datetime.now().strftime("%d.%m.%Y um %H:%M:%S")
    print("Messung Startet am " + str(time) + "\n")
    log.write("Messung Startet am " + str( time) + "\n")
    while True:
        try:
            with serial.Serial('COM3', 9600, ) as ser:
                x = ser.read(4)
                bytes(x).decode('UTF-8')
                x = float(x)
                if x > 8:
                    b = datetime.datetime.now().strftime('"%H:%M:%S"')
                    print(b + " | " + str(x))
                    log.write(str(b) + " ; " + '"' +str(x)+ '"' + "\n")
                else:
                    print("Messung erfolgreich beendet am " + str(time) + "\n")
                    log.write(str(b) + " ; " + '"' + str(x)+ '"' +"\n""Messung erfolgreich beendet am " + str(time) + "\n""\n")
                    break

        except serial.serialutil.SerialException:
                c = datetime.datetime.now().strftime("%d.%m.%Y - %H:%M:%S")
                print(c + " | Hardware wurde Entfernd")
                log.write(str(c) + " | Hardware wurde Entfernd""\n""Messung wird vorzeitig beendet""\n""\n")
                break
        except Exception:
            pass
