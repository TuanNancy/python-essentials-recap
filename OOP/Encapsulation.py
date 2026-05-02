class BankAccount:
    def __init__(self, balance):
        self.__balance = balance # _ _ = private, khong the truy cap tu ben ngoai
    
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
    
    def withdraw(self, amount):
        if amount > self.__balance:
            print("So du khong du")
        else:
            self.__balance -= amount
    def get_balance(self):
        return self.__balance
    @property
    def balance(self):
        return self.__balance
    
acc = BankAccount(1000)
acc.deposit(500)
print(acc.get_balance())
print(acc.balance) # dung nhu thuoc tinh, khong can goi ham ()