import json
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
    def withdraw(self, amount):
        if amount>self.balance:
            print("Insufficient funds")
        self.balance -= amount
def load_account_details():
    with open("balance.json") as f:
        return
def save_account_data(data):
    with open("balance.json","w") as f:
        json.dumpclass, f, indent=4