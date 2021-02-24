import random
import string

def id_generator(size=8, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

class BankAccount:
    def __init__(self, balance, name):
        self.balance = balance
        self.name = name
        self.id = id_generator()

    def deposit(self,  amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance - amount < 0:
            print("Can't withdraw money")
            return
        self.balance -= amount

    def get_balance(self):
        print(self.balance)
        return self.balance

class User:
    def __init__(self, name):
        self.name = name
        self.bank_accounts = []
        self.add_bank_account(1500, "Main")

    def add_bank_account(self, ammount, b_name):
        b = BankAccount(ammount, b_name)
        self.bank_accounts.append(b)

    def send_money(self, src, dst, amt):
        for i in self.bank_accounts:
            if i.id == dst:
                for j in self.bank_accounts:
                    if j.id == src:
                        j.withdraw(amt)
                        break
                i.deposit(amt)
                break
        raise ValueError("INVALID SRC/DST")



acc = User("Kaloyan")

print(acc.bank_accounts[0].id)
acc.add_bank_account(1500, "DST")
print(acc.bank_accounts[1].id)


acc.send_money(input("SRC: "), input("DST: "), 500)

acc.bank_accounts[0].get_balance()
acc.bank_accounts[1].get_balance()