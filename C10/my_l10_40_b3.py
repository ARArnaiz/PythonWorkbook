
class Transaction:
    balance = 0

    def __init__(self, amount):
        self.amount = amount
        Transaction.balance += amount


t1 = Transaction(100)
t2 = Transaction(-50)
t3 = Transaction(25)
print(Transaction.balance)