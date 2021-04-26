import json
import pathlib
import os
from collections import OrderedDict

py_script_directory = pathlib.Path(__file__).parent.absolute()
working_directory = pathlib.Path().absolute()

db_folder = str(py_script_directory) + os.sep

def __readLines(db_file):
    lines = list()
    with open(db_file, "r+") as file:
        for line in file:
            # Remove newline character
            lines.append(line.rstrip('\n'))
    # Use ordered dict to remove duplicates and keep the order
    return list(OrderedDict.fromkeys(lines))

def readAllMagicians():
    __db_file = db_folder + "Magicians.dat"
    magicians = __readLines(__db_file)
    return magicians


def readAllHolidays():
    __db_file = db_folder + "Holidays.dat"
    holidays = __readLines(__db_file)
    return holidays

def writeAppointmentsToJson(bookings_holidays, bookings_magicians, waiting_list):
    __db_file = db_folder + "Schedule.dat"
    out_dict = {"bookings_by_holidays": bookings_holidays, "bookings_by_magicians":bookings_magicians, "waiting_list": waiting_list}
    with open(__db_file, "w", encoding="utf-8") as file:
        json.dump(out_dict, file, indent=4)
    
def readAppointmentsFromJson():
    __db_file = db_folder + "Schedule.dat"
    
    # If previous bookings data not available
    if not os.path.exists(__db_file):
        return {},{},{}
    
    with open(__db_file, "r", encoding="utf-8") as file:
        json_appointments = json.load(file)
    
    bookings_holidays = json_appointments.get("bookings_by_holidays", {})
    bookings_magicians = json_appointments.get("bookings_by_magicians", {})
    waiting_list = json_appointments.get("waiting_list", {})
    return bookings_holidays, bookings_magicians, waiting_list
