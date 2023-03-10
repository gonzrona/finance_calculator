
from datetime import date as dt
from datetime import timedelta
from enum import Enum
import abc


class RCat(Enum):
    expense = 0
    income = 1






# class Frequency():
#     # Options
#     #   daily 
#     #   weekly
#     #   monthly
#     #   yearly
#     #   specific day of the month
#     def __init__(self, category: FCat, origin: dt) -> None:
#         self.category = category
#         self.origin = origin
#         self.days

#     def check(self, date: dt) -> bool:
#         return False
        # return True # if (date - self.origin).days%income.frequency == 0 else True


# class Frequency():
#     # def __init__(self, name: str) -> None:
#     #     self.name = name
#     @abc.abstractmethod
#     def check(self):
#         pass

# class onFrequency(Frequency):
#     def check(self) -> None:
#         pass



# class FCat(Enum):
#     weekly = 0
#     biweekly = 1
#     monthly = 2
#     yearly = 3
#     xdays = 4

class Frequency():
    @abc.abstractmethod
    def check(self, date: dt):
        pass

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



class Recurring():
    def __init__(self, name: str, amount: float, frequency: Frequency) -> None:
        # self.category = category
        self.name = "name"
        self.frequency = frequency
        self.amount = amount
    
    def to_dictionary(self) -> dict:
        return {"category":self.category.name, "name":self.name, "amount": self.amount}

    def __str__(self) -> str:
        return self.to_dictionary().__str__()

class OneTime():
    pass


class Account:
    def __init__(self, name:str, balance: float = 0.0) -> None:
        self.name = name
        self.balance = balance
        self.incomes: [Recurring] = []
        self.expences: [Recurring] = []

    def add_income(self, income:Recurring) -> None:
        self.incomes.append(income)
    
    def add_expence(self, expence:Recurring) -> None:
        self.expences.append(expence)

    def update(self, date: dt) -> None:
        for income in self.incomes:
            if income.frequency.check(date=date): self.balance += income.amount
        for expense in self.expences:
            if expense.frequency.check(date=date): self.balance -= expense.amount


checking = Account(name="Checking", balance=617.73)
checking.add_income(Recurring(name="INL", amount=920, frequency=Weekly(day="Wednesday")))
checking.add_expence(Recurring(name="Grocery", amount=100, frequency=Weekly(day="Sunday")))
checking.add_expence(Recurring(name="Mortgage", amount=1000, frequency=Monthly(day=1)))
checking.add_expence(Recurring(name="Private Loans", amount=600, frequency=Monthly(day=7)))
checking.add_expence(Recurring(name="Gas", amount=80, frequency=Monthly(day=22)))
checking.add_expence(Recurring(name="City", amount=130, frequency=Monthly(day=22)))
checking.add_expence(Recurring(name="Internet", amount=20, frequency=Monthly(day=7)))

savings = Account(name="Savings", balance=10113.62)
savings.add_income(Recurring(name="INL", amount=300, frequency=Weekly(day="Wednesday")))


for i in range(60):
    date = dt.today() + timedelta(days=i)
    checking.update(date)
    savings.update(date)
    print(date, "{:.2f}".format(checking.balance), "{:.2f}".format(savings.balance))