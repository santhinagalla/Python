
import os
import sys
from db import readAllMagicians, readAllHolidays, writeAppointmentsToJson, readAppointmentsFromJson
class AppointmentSchedular:
    def __init__(self):
        self.__magicians = readAllMagicians()
        self.__holidays = readAllHolidays()
        # Initialize from existing data or with empty lists
        self.__bookings_holidays, self.__bookings_magicians, self.__waiting_list = readAppointmentsFromJson() # dict(), dict(), dict()

    def schedule(self, customer_name=None, holiday_name=None):
        if customer_name is None: customer_name = input("Enter customer name: ")
        if holiday_name is None: holiday_name = input("Enter Holiday name: ")
        # Validate holiday name
        if holiday_name not in self.__holidays:
            raise ValueError("Please enter valid holiday name")
        
        # Get already booked magicians for that holiday
        appointments_for_holiday = self.__bookings_holidays.get(holiday_name, {})
        magicians_booked_for_holiday = list(appointments_for_holiday.values())
        
        # Validate customer already booked any magician
        existing_appointment_for_customer = appointments_for_holiday.get(customer_name)
        if existing_appointment_for_customer is not None:
            raise ValueError(f"An appointment already booked for '{customer_name}' with '{existing_appointment_for_customer}' on '{holiday_name}'. Please cancel existing appointment")


        # Get magicians not booked for that holiday
        magicians_not_booked_for_holiday = [ m for m in self.__magicians if m not in set(magicians_booked_for_holiday)]
        
        # If magicians not available add customer to waitlist
        if len(magicians_not_booked_for_holiday) < 1:
            waiting_list_for_holiday = self.__waiting_list.get(holiday_name, [])
            waiting_list_for_holiday.append(customer_name)
            self.__waiting_list[holiday_name] = waiting_list_for_holiday
            print(f"Magicians not available for '{holiday_name}'. Placed '{customer_name}' on waiting list.")
            self.__printSchedule()
            return
        
        # Book to first available magician
        magician = magicians_not_booked_for_holiday[0]
        appointments_for_holiday[customer_name] = magician

        # Keep the appointments sorted by customer name
        self.__bookings_holidays[holiday_name] = self.__sort(appointments_for_holiday)

        # Replicate same data in second data structure (magicians)
        # No need to do validation for double booking as done previously
        appointments_for_magician = self.__bookings_magicians.get(magician, {})
        appointments_for_magician[holiday_name] = customer_name
        self.__bookings_magicians[magician] = self.__sort(appointments_for_magician)
        
        print(f"Schedule confirmed for '{customer_name}' with '{magician}' on '{holiday_name}'.")
        self.__printSchedule()

    def __cancelFor(self, customer_name, holiday_name):
        # Remove from bookings_holidays
        appointments_for_holiday = self.__bookings_holidays.get(holiday_name, {})
        appointments_for_holiday.pop(customer_name, None)
        self.__bookings_holidays[holiday_name] = self.__sort(appointments_for_holiday)

        # Remove from bookings_magicians
        for magician in self.__bookings_magicians:
            appointments_for_magician = self.__bookings_magicians[magician]
            appointments_for_magician = {holiday:customer for (holiday, customer) in appointments_for_magician.items() if not (holiday == holiday_name and appointments_for_magician[holiday]==customer_name)}
            self.__bookings_magicians[magician] = self.__sort(appointments_for_magician)
    
    def cancel(self):
        customer_name = input("Enter customer name: ")
        holiday_name = input("Enter Holiday name: ")
        # Validate holiday name
        if holiday_name not in self.__holidays:
            raise ValueError("Please enter valid holiday name")

        self.__cancelFor(customer_name, holiday_name)

        # Make booking for waiting list customers
        # Get first waiting person in waiting list for holiday
        waiting_list_for_holiday = self.__waiting_list.get(holiday_name, [])
        
        # Return if there is no waiting list for that holiday
        if len(waiting_list_for_holiday) < 1:
            self.__printSchedule()
            return
        
        # Schedule for first customer in waiting list
        waiting_customer = waiting_list_for_holiday[0]
        self.schedule(waiting_customer, holiday_name)
        
        # Remove customer from waiting list
        waiting_list_for_holiday.pop(0)
        self.__waiting_list[holiday_name] = waiting_list_for_holiday

        self.__printSchedule()

    def __printDict(self, dict, headers):
        maxSizeCol1 = max(max([len(k) for k in dict]),10)
        maxSizeCol2 = max(max([len(v) for k,v in dict.items()]),10)
        colSizes = [maxSizeCol1, maxSizeCol2]
        formatStr = " | ".join(["{{:<{}}}".format(i) for i in colSizes])
        line = formatStr.replace(' | ','-+-').format(*['-' * i for i in colSizes])
        myList = [headers]

        for k,v in dict.items():
            myList.append([k,v])
        for item in myList: 
            print(formatStr.format(*item) + os.linesep + line)

    def status(self):
        self.__printSchedule()
        name = input("Enter magician name or holiday name: ")

        # If not found in holidays names, user had entered magician name
        if name in self.__holidays:
            bookings_for_holiday = self.__bookings_holidays.get(name, {})
            print(f"{os.linesep}Schedule for holiday '{name}':")
            self.__printDict(bookings_for_holiday, ["Customer", "Magician"])
        elif name in self.__magicians:
            bookings_for_magician = self.__bookings_magicians.get(name, {})
            print(f"{os.linesep}Schedule for magician '{name}':")
            self.__printDict(bookings_for_magician, ["Holiday", "Customer"])
        else:
            raise ValueError("Please enter valid magician name or holiday name")
    
    def __printSchedule(self):
        print(os.linesep+"Schedule:")
        # Find first column max length
        maxSize = max(len(x) for x in self.__magicians)

        sorted_holidays = sorted(self.__holidays)
        colSizes = [len(x)+5 for x in sorted_holidays] # Column width for holidays columns
        colSizes.insert(0, maxSize+5) # Column width for magician name column

        formatStr = ' | '.join(["{{:<{}}}".format(i) for i in colSizes])
        line = formatStr.replace(' | ','-+-').format(*['-' * i for i in colSizes])

        # Header rows
        myList = [sorted_holidays.copy()]
        myList[0].insert(0, "Magician/Holidays")

        for magician in self.__bookings_magicians:
            magician_appointments = self.__bookings_magicians.get(magician, {})
            customers = [magician_appointments.get(x, "") for x in sorted_holidays ]
            customers.insert(0, magician)
            myList.append(customers)

        for item in myList: 
            print(formatStr.format(*item) + os.linesep + line)
        
        print(os.linesep + "Waiting list:")
        myList = []
        for holiday in self.__waiting_list:
            customers = self.__waiting_list[holiday]
            myList.append(f"{holiday:<20} = [{', '.join([f'{x:<5}' for x in customers])}]")
        for item in myList: 
            print(item)

        
    def save(self):
        self.__printSchedule()
        writeAppointmentsToJson(self.__bookings_holidays, self.__bookings_magicians, self.__waiting_list)

    def __sort(self, dictionary):
        return dict(sorted(dictionary.items()))
