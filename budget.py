from pickle import FALSE, TRUE


class Category:
    name = ""
    total = 0
    ledger = []
    def __init__(self, name):
        self.name = name
        print(self.name, "constructed")
    def deposit(self, amount, description="new deposit"):
        thisDeposit = {"ampount" : amount, "description" : description}
        self.ledger.append(thisDeposit)
        self.total += amount
    def withdraw(self, amount, description="new withdraw"):
        if self.check_funds(amount):
            thisDeposit = {"ampount" : 0-amount, "description" : description}
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