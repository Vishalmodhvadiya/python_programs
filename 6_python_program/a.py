# Create a class account with necessary methods – showBalance, withdraw, deposit and transfer. Also, implement necessary getters and setters. Instantiate 2 objects of that class and show different method calls using them

class BankAccount:
    def __init__(self, account_number, account_holder, balance):
        self._account_number = account_number
        self._account_holder = account_holder
        self._balance = balance

    @property
    def account_number(self):
        return self._account_number

    @property
    def account_holder(self):
        return self._account_holder

    @property
    def balance(self):
        return self._balance

    @account_holder.setter
    def account_holder(self, new_name):
        if new_name.strip == "":
            raise ValueError("Account name cannot be empty")
        self._account_holder = new_name

    @balance.setter
    def balance(self, new_balance):
        if new_balance < 0:
            raise ValueError("balance cannot be negative")
        self._balance = new_balance

    def show_balance(self):
        return self._balance

    def withdraw(self, amount):
        if amount <= self._balance:
            self.balance -= amount
            return {"status": "success", "message":f"withdrawn {amount}. new balance is {self.balance}"}
        else:
            return {"status": "failure", "message": "insufficient balance"}

    def deposit(self, amount):
        self.balance += amount
        return {"status": "success", "message": f"deposited {amount}. new balance is {self.balance}"}

    def transfer(self, amount, recipient_account):
        if amount <= self._balance:
            self.balance -= amount
            recipient_account.deposit(amount)
            return {"status": "success", "message": f"transferred {amount} to {recipient_account.account_holder}. new balance is {self.balance}"}
        else:
            return {"status": "failure", "message": "insufficient balance"}     


if __name__ == "__main__": 
    account1 = BankAccount("123456", "Alice", 1000)
    account2 = BankAccount("654321", "Bob", 500)

    print(account1.show_balance())  
    print(account1.deposit(200))    
    print(account1.withdraw(150))    
    print(account1.transfer(300, account2)) 

    print(account2.show_balance())  