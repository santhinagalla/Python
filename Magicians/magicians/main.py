import sys
import traceback
from schedular import AppointmentSchedular
from db import readAllMagicians, readAllHolidays, writeAppointmentsToJson, readAppointmentsFromJson

def quit():
    sys.exit(0)

def displayChoices():
    print("Your choices are:")
    print("\t1. S - Schedule")
    print("\t2. C - Cancel")
    print("\t3. T - Status")
    print("\t4. Q - Quit")

def main():
    # printSchedule()
    appointmentSchedular = AppointmentSchedular()

    while True:
        displayChoices()
        try:
            command = input("Enter your command: ").strip().upper()[0]
            if command == "S":
                appointmentSchedular.schedule()
            elif command == "C":
                appointmentSchedular.cancel()
            elif command == "T":
                appointmentSchedular.status()
            elif command == "Q":
                appointmentSchedular.save()
                quit()
        except Exception as e:
            print("** Exception occured")
            print(e)
            traceback.print_tb(e.__traceback__)
        finally:
            print("\n\n")

main()
