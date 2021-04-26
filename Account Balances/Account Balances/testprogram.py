from interest_calculator import Time, SavingsAccount
import datetime
import time

def main():
    now = datetime.datetime.now()
    time1 = Time(now.hour,now.minute,now.second)
    time2 = Time(now.hour,now.minute,now.second)
    savings_account1 = SavingsAccount(0.015, 5000, time1)
    savings_account2 = SavingsAccount(0.015, 10000, time2)
    print("Initial balances: \nSaver1: Balance=", savings_account1.savingsBalance, "updated:", savings_account1.updatedTime.display())
    print("Saver2: Balance=", savings_account2.savingsBalance, "updated:", savings_account2.updatedTime.display())
    
    time.sleep(2)
    
    savings_account1.calculateMonthlyInterest()
    savings_account2.calculateMonthlyInterest()
    print("Balances after 1 month's interest applied at .015: \nSaver1: Balance=", savings_account1.savingsBalance, "updated:", savings_account1.updatedTime.display())
    print("Saver2: Balance=", savings_account2.savingsBalance, "updated:", savings_account2.updatedTime.display())
    time.sleep(2)

    savings_account1.annualInterestRate = 0.03
    savings_account2.annualInterestRate = 0.03
    savings_account1.calculateMonthlyInterest()
    savings_account2.calculateMonthlyInterest()
    print("Balances after 1 month's interest applied at .03: \nSaver1: Balance=", savings_account1.savingsBalance, "updated:", savings_account1.updatedTime.display())
    print("Saver2: Balance=", savings_account2.savingsBalance, "updated:", savings_account2.updatedTime.display())


main()
