# wallet.py

class InsufficientAmount(Exception):
    pass


class Wallet(object):
    def __init__(self, initial_amount=0):
        self.balance = initial_amount
        if type(object) == (int or float):
            self.balance = object


    def spend_cash(self, amount):
        if type(amount) == (int or float):
            if self.balance < amount:
                raise InsufficientAmount("Insufficient Balance")
            else:
                self.balance -= amount


    def add_cash(self, amount):
        if type(amount) == (int or float):
            self.balance += amount
            
