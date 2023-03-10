
from datetime import date as dt
from datetime import timedelta
from enum import Enum
import abc


class Frequency():
    @abc.abstractmethod
    def check(self, date: dt):
        pass

class Once(Frequency):
    def __init__(self, date: dt) -> None:
        self.date = date
    def check(self, date: dt) -> bool:
        return True if self.date == date else False

class Weekly(Frequency):
    def __init__(self, day: str) -> None:
        self.day = day
    def check(self, date: dt) -> bool:
        return True if self.day == f'{date:%A}' else False

        
# class BiWeekly(Frequency):
#     def __init__(self):
#         pass

class Monthly(Frequency):
    def __init__(self, day: int) -> None:
        self.day = day
    def check(self, date: dt) -> bool:
        return True if self.day == date.day else False

# class Yearly(Frequency):
#     def __init__(self):
#         pass

# class Days(Frequency):
#     def __init__(self):
#         pass


class APY():
    def __init__(self, rate:float, frequency:Frequency) -> None:
        self.rate = rate
        self.frequency = frequency
        self.accrued = 0.0

    def update(self, date:dt, principal:float) -> float:
        if self.frequency.check(date=date):
            total = self.accrued
            self.accrued = 0.0
            return total
        else:
            days = 366 if date.year%4==0 else 365
            self.accrued += principal*self.rate/days
            return 0.0
        


class Recurring():
    def __init__(self, name:str, amount:float, frequency:Frequency) -> None:
        self.name = "name"
        self.frequency = frequency
        self.amount = amount

    def __str__(self) -> str:
        return {"category":self.category.name, "name":self.name, "amount": self.amount}.__str__()

class OneTime(Recurring):
    def __init__(self, name:str, amount:float, frequency:Frequency) -> None:
        super().__init__(name=name, amount=amount, frequency=frequency)


class Account:
    def __init__(self, name:str, balance:float, apy:APY) -> None:
        self.apy = apy
        self.name = name
        self.balance = balance
        self.incomes: [Recurring] = []
        self.expences: [Recurring] = []

    def add_income(self, income:Recurring) -> None:
        self.incomes.append(income)
    
    def add_expence(self, expence:Recurring) -> None:
        self.expences.append(expence)

    def update(self, date: dt) -> None:
        self.balance += self.apy.update(date=date, principal=self.balance)
        for income in self.incomes:
            if income.frequency.check(date=date): self.balance += income.amount
        for expense in self.expences:
            if expense.frequency.check(date=date): self.balance -= expense.amount


checking = Account(name="Checking", balance=617.73, apy=APY(rate=.025, frequency=Monthly(day=1)))
checking.add_income(Recurring(name="INL", amount=920, frequency=Weekly(day="Wednesday")))
checking.add_expence(Recurring(name="Grocery", amount=100, frequency=Weekly(day="Sunday")))
checking.add_expence(Recurring(name="Mortgage", amount=1000, frequency=Monthly(day=1)))
checking.add_expence(Recurring(name="Private Loans", amount=600, frequency=Monthly(day=7)))
checking.add_expence(Recurring(name="Gas", amount=80, frequency=Monthly(day=22)))
checking.add_expence(Recurring(name="City", amount=130, frequency=Monthly(day=22)))
checking.add_expence(Recurring(name="Internet", amount=20, frequency=Monthly(day=7)))

checking.add_expence(OneTime(name="St Patricks", amount=400, frequency=Once(dt(2023,3,17))))

# principal=9487.44

savings = Account(name="Savings", balance=10113.62, apy=APY(rate=.0375, frequency=Monthly(day=1)))
savings.add_income(Recurring(name="INL", amount=300, frequency=Weekly(day="Wednesday")))


for i in range(60):
    date = dt.today() + timedelta(days=i)
    checking.update(date)
    savings.update(date)
    print(date, "{:.2f}".format(checking.balance), "{:.2f}".format(savings.balance), "{:.2f}".format(savings.balance + checking.balance))