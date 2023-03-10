
from datetime import date as dt
from datetime import timedelta
from enum import Enum

class ATYP(Enum):
    savings = 1
    checking = 2
    other = 3


# class Frequency():
#     # there should be 
#     def __init__():
#         pass

class Recurring_Expence():
    def __init__(self, start_date: dt, value: float) -> None:
        self.start_date = start_date
        self.frequency = 7
        self.value = value

class Income:
    def __init__(self, start_date: dt, value: float) -> None:
        self.start_date = start_date
        self.frequency = 7
        self.value = value
    
    def __str__(self) -> str:
        return f"Start date: {self.start_date}"

class Account:
    def __init__(self, balance: float = 0.0) -> None: #, actType = ATYP.savings):
        self.balance = balance
        self.incomes: [Income] = []
        self.recurring_expences: [Recurring_Expence] = []

    def add_income(self, income:Income) -> None:
        self.incomes.append(income)
    
    def add_recurring_expence(self, expence: Recurring_Expence) -> None:
        self.recurring_expences.append(expence)

    # def modify(self) -> None:
    #     pass

    def update(self, date: dt) -> None:
        for income in self.incomes:
            diff = date - income.start_date
            if diff.days%income.frequency == 0:
                self.balance += income.value
            # print(diff.days)
        for expense in self.recurring_expences:
            diff = date - expense.start_date
            if diff.days%expense.frequency == 0:
                self.balance -= expense.value


