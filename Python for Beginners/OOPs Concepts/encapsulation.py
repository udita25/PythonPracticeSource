class BankAccount:
    def __init__(self, account_holder, initial_balance):
        self.account_holder = account_holder          # Public attribute
        self.__balance = initial_balance              # Private attribute

    # Public method to view the balance
    def get_balance(self):
        print(f"{self.account_holder}'s Balance: ₹{self.__balance}")

    # Public method to deposit money
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited ₹{amount}. New Balance: ₹{self.__balance}")
        else:
            print("Deposit amount must be positive!")

    # Public method to withdraw money
    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrawn ₹{amount}. Remaining Balance: ₹{self.__balance}")
        else:
            print("Invalid withdrawal amount or insufficient balance!")

# Creating an object of BankAccount
account1 = BankAccount("Alice", 5000)

# Accessing public method
account1.get_balance()

# Trying to access private variable (Will raise an AttributeError)
# print(account1.__balance)  -  Not allowed

# Correct way: Use methods
account1.deposit(1500)
account1.withdraw(2000)

# Trying to access private variable using name mangling (Not recommended)
print(account1._BankAccount__balance)  #Technically works, but not safe
