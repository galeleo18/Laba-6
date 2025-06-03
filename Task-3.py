class BankAccount:
    def __init__(self,balance = 0):
        self.__balance = balance

    def deposit(self,amount):
        self.__balance += amount

    def withdraw(self,amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Недостаточно средств.")

    def get_balance(self):
        return self.__balance

account = BankAccount()
dep = int(input("Сколько внести на счёт? "))
account.deposit(dep)

wd = int(input("Сколько снять со счёта? "))
account.withdraw(wd)
print("Баланс", account.get_balance())