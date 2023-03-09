# import datetime as dt
from datetime import date, timedelta
from enum import Enum

# for i in range(90):
#     print(date.today() + timedelta(days=i))

class ATYP(Enum):
    savings = 1
    checking = 2
    other = 3

class Account:
    def __init__(self, balance: float = 0.0): #, actType = ATYP.savings):
        self.balance = balance
        # self.type = actType

class Income:
    def __init__(self, frequency):
        self.frequency = frequency

def print_remaining_days():
    current_day = date.today()
    while current_day.month == date.today().month:
        print(current_day)
        current_day += timedelta(days=1)




def number_of_days_in(month:int = 1, year:int = 2023) -> int:
    return number_of_days_from_date(date(year, month, 1))

def number_of_days_from_date(dt: date = date.today()) -> int:
    return (dt.replace(month = dt.month % 12 + 1, day = 1)-timedelta(days=1)).day


# ATYP = Enum('ATYP', ['savings', 'checking', 'other'])

# account = Account(balance=1000, actType=ATYP.savings)
account = Account(balance=1000)

# print(number_of_days_in(month=1, year=2022))

for y in range(4):
    for m in range(1,13):
        print(number_of_days_in(month=m, year=2020+y))
    print("\n")


# print(list(ATYP))
# print(ATYP.savings.value)

# print(type(date.today()))

# for i in range(1,13):
#     dt = date(2024, i, 25)
#     monkey = (dt.replace(month = dt.month % 12 +1, day = 1)-timedelta(days=1)).day
#     print(monkey)



# print(number_of_days())



# current_day = date.today()
# while current_day.month == date.today().month:
#     # account.balance += account.balance
#     print(current_day, account.balance, account.type)
#     current_day += timedelta(days=1)


    
