from datetime import date, timedelta
from my_cal_classes import Account, Income, Recurring_Expence, Recurring, RCat, IncomeTest




def print_remaining_days():
    current_day = date.today()
    while current_day.month == date.today().month:
        print(current_day)
        current_day += timedelta(days=1)



# def is(months: int, dt: date):
#     pass
    # newmonth = ((( d.month - 1) + x ) % 12 ) + 1
    # newyear  = int(d.year + ((( d.month - 1) + x ) / 12 ))
    # return datetime.date( newyear, newmonth, d.day)


def number_of_days_in(month:int = 1, year:int = 2023) -> int:
    return number_of_days_from_date(date(year, month, 1))

def number_of_days_from_date(dt: date = date.today()) -> int:
    return (dt.replace(month = dt.month % 12 + 1, day = 1)-timedelta(days=1)).day


# ATYP = Enum('ATYP', ['savings', 'checking', 'other'])

# account = Account(balance=1000, actType=ATYP.savings)
account = Account(balance=617.73)
account.add_income(Income(start_date=date.today()-timedelta(days=1), value=1220))
account.add_recurring_expence(Recurring_Expence(start_date=date(2023,3,12), value=100))

for i in range(30):
    dt = date.today() + timedelta(days=i)
    account.update(dt)
    # print(dt, account.balance)


# Recurring(RCat.expense, "paycheck", date.today(), 1220.00)


print(Recurring(RCat.income, "paycheck", date.today(), 1220.00))

print(IncomeTest("paycheck", date.today(), 1220.00))

# dt = date.today() + 


# print(number_of_days_in(month=1, year=2022))

# for y in range(4):
#     for m in range(1,13):
#         print(number_of_days_in(month=m, year=2020+y))
#     print("\n")



# for i in range(90):
#     print(date.today() + timedelta(days=i))