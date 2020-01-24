import serial
import datetime
import traceback
import sys


def user_input():
    end_value = input("End Wert Angeben ")
    try:
        while True:
            end_value = int(end_value)
            measurement(end_value)
    except ValueError:
        print("Bitte eine Zahl eingeben")
        user_input()
    except Exception:
        print(traceback.print_exc())
        user_input()

def get_value():
    with serial.Serial('COM3', 9600, ) as ser:
        x = ser.read(4)
        bytes(x).decode('UTF-8')
        return float(x)

def measurement(end_value):
    with open("log.csv", "a") as log:
        time = datetime.datetime.now().strftime("%d.%m.%Y um %H:%M:%S")
        print("Messung Startet am " + str(time) + "\n")
        log.write("Messung Startet am " + str(time) + "\n")
        try:
            while (x:= get_value()) > end_value:
                b = datetime.datetime.now().strftime('"%H:%M:%S:%f"')
                print(b + " | " + str(x))
                log.write(str(b) + " ; " + '"' + str(x) + '"' + "\n")
            print("Messung erfolgreich beendet am " + str(time) + "\n")
            log.write(str(b) + " ; " + '"' + str(x) + '"' + "\n""Messung erfolgreich beendet am " + str(
                time) + "\n""\n")
            sys.exit(1)

        except serial.serialutil.SerialException:
            c = datetime.datetime.now().strftime("%d.%m.%Y - %H:%M:%S")
            print(c + " | Hardware wurde Entfernd")
            print(traceback.print_exc())
            log.write(str(c) + " | Hardware wurde Entfernd""\n""Messung wird vorzeitig beendet""\n""\n")
            sys.exit(1)

        except ValueError:
            c = datetime.datetime.now().strftime("%d.%m.%Y - %H:%M:%S")
            print(c + " | Hardware wurde Entfernd")
            print(traceback.print_exc())
            log.write(str(c) + " | Hardware wurde Entfernd""\n""Messung wird vorzeitig beendet""\n""\n")
            sys.exit(1)

        except Exception:
            c = datetime.datetime.now().strftime("%d.%m.%Y - %H:%M:%S")
            print(c + " | Ein unerwarteter Fehler ist aufgetretten. Messung wird abgebrochen")
            print(traceback.print_exc())
            log.write(str(
                c) + " | Ein unerwarteter Fehler ist aufgetretten. Messung wird abgebrochen""\n""Messung wird vorzeitig beendet""\n""\n")
            sys.exit(1)

if __name__ == "__main__":
    user_input()
