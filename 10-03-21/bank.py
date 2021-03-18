import random
import yaml
import csv
import json
import os


class BankAccount:
    def __init__(self, balance, account_file):
        self.account_file = account_file
        if os.path.exists(account_file):
            with open(account_file) as f:
                self.balance = int(f.read())
        else:
            self.balance = balance
            with open(account_file, "w") as f:
                f.write(str(self.balance))

    def deposit(self,  amount):
        self.balance += amount
        with open(self.account_file, "w") as f:
            f.write(str(self.balance))

    def withdraw(self, amount):
        if self.balance - amount < 0:
            print("Can't withdraw money")
            return
        self.balance -= amount
        with open(self.account_file, "w") as f:
            f.write(str(self.balance))

    def get_balance(self):
        print(self.balance)
        return self.balance


smetka1 = BankAccount(1500, "smetka1.txt")
smetka1.withdraw(500)
smetka2 = BankAccount(1500, "smetka2.txt")
smetka2.deposit(1500)