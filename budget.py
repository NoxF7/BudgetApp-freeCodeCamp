from cgitb import text
from ctypes import sizeof
from pickle import FALSE, TRUE


class Category:
    name = ""
    total = 0
    ledger = []
    def __init__(self, name):
        self.name = name
        print(self.name, "constructed")
    def __str__(self):
        title = ""
        size = 15 - int(len(self.name)/2)
        for i in range(size):
            title = title + "*"
        title = title + self.name
        size = 30 - size - len(self.name)
        for i in range(size):
            title = title + "*"
        txt = title + "\n"
        for thisMovement in self.ledger:
            line = thisMovement["description"]
            txt = txt + line + "\n"
        return txt
    def deposit(self, amount, description="new deposit"):
        thisDeposit = {"amount" : amount, "description" : description}
        self.ledger.append(thisDeposit)
        self.total += amount
    def withdraw(self, amount, description="new withdraw"):
        if self.check_funds(amount):
            thisDeposit = {"amount" : 0-amount, "description" : description}
            self.ledger.append(thisDeposit)
            self.total -= amount
        else:
            return FALSE
    def get_balance(self):
        return self.total
    def transfer(self, amount, category):
        if self.check_funds(amount):
            description =  "Transfer to " + category.name
            self.withdraw(amount,  description)
            description =  "Transfer from " + category.name
            category.deposit(amount, description)
            return TRUE
        else:
            return FALSE
    def check_funds(self, amount):
        if amount <= self.total:
            return TRUE
        else:
            return FALSE




# def create_spend_chart(categories):