class Account:
    def __init__(self, name, acc_no, balance):
        self.customer_name = name
        self.accountNumber = acc_no
        self.acc_balance = balance

    def print_details(self):
        print(self.customer_name)
        print(self.accountNumber)
        print(self.acc_balance)
        print("----------------------")

    def deposit(self, amount):
        self.acc_balance += amount
        print(f"Deposited KES {amount}. New Balance is {self.acc_balance}")

    def withdraw(self, amount):
        if self.acc_balance >= amount:
            self.acc_balance - amount
        else:
            print("Insufficient funds in the account!!!")

    def check_balance(self):
        print(f"Account {self.accountNumber} has KES {self.acc_balance}")


p1 = Account("Awino", 3238137, 70000)

p1.deposit(20000)
p1.withdraw(1000000)
p1.check_balance()
