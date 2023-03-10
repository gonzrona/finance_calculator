
from datetime import date as dt
from datetime import timedelta
from enum import Enum

class ATYP(Enum):
    savings = 1
    checking = 2
    other = 3

class RCat(Enum):
    expense = 0
    income = 1


class Frequency():
    # Options
    #   daily 
    #   weekly
    #   monthly
    #   yearly
    #   specific day of the month
    def __init__(self) -> None:
        pass

# class Type(Enum):
#     expense = 1
#     checking = 2
#     other = 3

class Recurring():
    def __init__(self, category: RCat, name: str, start_date: dt, amount: float) -> None:
        self.category = category
        self.name = "name"
        self.start_date = start_date
        self.frequency = 7
        self.amount = amount
    
    def to_dictionary(self) -> dict:
        return {"category":self.category.name, "name":self.name, "start date": self.start_date.__str__(), "frequency": self.frequency, "amount": self.amount}

    def __str__(self) -> str:
        return self.to_dictionary().__str__()


class IncomeTest(Recurring):
    def __init__(self, name: str, start_date: dt, amount: float) -> None:
        super().__init__(category = RCat.income, name = name, start_date = start_date, amount = amount)





# class Expence(Recurring):
#     def __init__(self, start_date: dt, value: float, ) -> None:
#         self.type = "Expense"

# class Income(Recurring):
#     self.type = "Income"

class Recurring_Expence():
    def __init__(self, start_date: dt, value: float) -> None:
        self.name = "RE"
        self.start_date = start_date
        self.frequency = 7
        self.value = value

class Income():
    def __init__(self, start_date: dt, value: float) -> None:
        self.name = "I"
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


