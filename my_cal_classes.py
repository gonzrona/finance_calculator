
from datetime import date as dt
from datetime import timedelta
from enum import Enum

class RCat(Enum):
    expense = 0
    income = 1

class FCat(Enum):
    xdays = 0
    onday = 1


class Frequency():
    # Options
    #   daily 
    #   weekly
    #   monthly
    #   yearly
    #   specific day of the month
    def __init__(self, origin: dt, ) -> None:
        self.origin = origin

    def check_date(self, date: dt) -> bool:
        return True if (date - self.origin).days%income.frequency == 0 else True

class Recurring():
    # def __init__(self, category: RCat, name: str, origin: dt, amount: float, frequency_category: FCat) -> None:
    def __init__(self, category: RCat, name: str, origin: dt, amount: float) -> None:
        self.category = category
        self.name = "name"
        self.origin = origin
        self.frequency = 7
        self.amount = amount
    
    def to_dictionary(self) -> dict:
        return {"category":self.category.name, "name":self.name, "start date": self.origin.__str__(), "frequency": self.frequency, "amount": self.amount}

    def __str__(self) -> str:
        return self.to_dictionary().__str__()


class Income(Recurring):
    def __init__(self, name: str, origin: dt, amount: float) -> None:
        super().__init__(category = RCat.income, name = name, origin = origin, amount = amount)

class Expense(Recurring):
    def __init__(self, name: str, origin: dt, amount: float) -> None:
        super().__init__(category = RCat.expense, name = name, origin = origin, amount = amount)


class Account:
    def __init__(self, balance: float = 0.0) -> None:
        self.balance = balance
        self.incomes: [Income] = []
        self.recurring_expences: [Expense] = []

    def add_income(self, income:Income) -> None:
        self.incomes.append(income)
    
    def add_recurring_expence(self, expence: Expense) -> None:
        self.recurring_expences.append(expence)

    def update(self, date: dt) -> None:
        for income in self.incomes:
            diff = date - income.origin
            if diff.days%income.frequency == 0:
                self.balance += income.amount
            # print(diff.days)
        for expense in self.recurring_expences:
            diff = date - expense.origin
            if diff.days%expense.frequency == 0:
                self.balance -= expense.amount


account = Account(balance=617.73)
account.add_income(Income(name="SoFi", origin=dt(2023,3,8), amount=1220))

for i in range(20):
    date = dt.today() + timedelta(days=i)
    account.update(date)
    print(date, account.balance)