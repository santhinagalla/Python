import time
import datetime
class Time:
    def __init__(self,hour,minute,second):
        self.__hour = hour
        self.__minute = minute
        self.__second = second
    
    @property
    def hour(self):
        return self.__hour

    @property
    def minute(self):
        return self.__minute
    
    @property
    def second(self):
        return self.__second

    def __str__(self):
        return "{hour}:{minute}:{second}".format(hour=self.hour,minute=self.minute,second=self.second)
    
    def display(self):
        return "{hour}:{minute}:{second}".format(hour=self.hour,minute=self.minute,second=self.second)

class SavingsAccount:
    def __init__(self,annualInteRestrate,savingsBalance,updatedTime):
        self.__annualInteRestrate = annualInteRestrate
        self.__savingsBalance = savingsBalance
        self.__updatedTime = updatedTime
    
    @property
    def annualInterestRate(self):
        return self.__annualInteRestrate
    
    @annualInterestRate.setter
    def annualInterestRate(self, newInterestRate):
        self.__annualInteRestrate = newInterestRate

    @property
    def savingsBalance(self):
        return self.__savingsBalance

    @property
    def updatedTime(self):
        return self.__updatedTime
    
    def __str__(self):
        return "Balance:{balance}, updated:{update_time}".format(balance=self.savingsBalance, update_time=str(self.updatedTime))

    def calculateMonthlyInterest(self):
        interest = (self.__savingsBalance * self.__annualInteRestrate ) / 12
        self.__savingsBalance += interest
        now = datetime.datetime.now()
        self.__updatedTime = Time(now.hour, now.minute, now.second)
