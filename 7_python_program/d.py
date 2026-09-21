# Handle possible exceptions in the practical 6_a (Create a class account with necessary methods – showBalance, withdraw, deposit and transfer. Also, implement necessary getters and setters. Instantiate 2 objects of that class and show different method calls using them)

class BankAccount:
    def __init__(self, account_number, account_holder, balance):
        self._account_number = account_number
        self._account_holder = account_holder

        if balance < 0:
            raise ValueError("Initial balance cannot be negative")
        self._balance = balance

    # ---------- Getters ----------
    @property
    def account_number(self):
        return self._account_number

    @property
    def account_holder(self):
        return self._account_holder

    @property
    def balance(self):
        return self._balance

    # ---------- Setters ----------
    @account_holder.setter
    def account_holder(self, new_name):
        if not isinstance(new_name, str) or new_name.strip() == "":
            raise ValueError("Account holder name cannot be empty")
        self._account_holder = new_name

    @balance.setter
    def balance(self, new_balance):
        if new_balance < 0:
            raise ValueError("Balance cannot be negative")
        self._balance = new_balance

    # ---------- Methods ----------
    def show_balance(self):
        return self._balance

    def withdraw(self, amount):
        try:
            if not isinstance(amount, (int, float)):
                raise TypeError("Withdrawal amount must be a number")
            if amount <= 0:
                raise ValueError("Withdrawal amount must be greater than zero")
            if amount > self._balance:
                raise ValueError("Insufficient balance")

            self._balance -= amount
            return {"status": "success", "message": f"Withdrawn {amount}. New balance is {self._balance}"}

        except (TypeError, ValueError) as e:
            return {"status": "failure", "message": str(e)}

    def deposit(self, amount):
        try:
            if not isinstance(amount, (int, float)):
                raise TypeError("Deposit amount must be a number")
            if amount <= 0:
                raise ValueError("Deposit amount must be greater than zero")

            self._balance += amount
            return {"status": "success", "message": f"Deposited {amount}. New balance is {self._balance}"}

        except (TypeError, ValueError) as e:
            return {"status": "failure", "message": str(e)}

    def transfer(self, amount, recipient_account):
        try:
            if not isinstance(recipient_account, BankAccount):
                raise TypeError("Recipient must be a valid BankAccount object")
            if not isinstance(amount, (int, float)):
                raise TypeError("Transfer amount must be a number")
            if amount <= 0:
                raise ValueError("Transfer amount must be greater than zero")
            if amount > self._balance:
                raise ValueError("Insufficient balance")

            self._balance -= amount
            recipient_account.deposit(amount)
            return {
                "status": "success",
                "message": f"Transferred {amount} to {recipient_account.account_holder}. New balance is {self._balance}"
            }

        except (TypeError, ValueError) as e:
            return {"status": "failure", "message": str(e)}


if __name__ == "__main__":
    try:
        account1 = BankAccount("123456", "Alice", 1000)
        account2 = BankAccount("654321", "Bob", 500)
    except ValueError as e:
        print(f"Error creating account: {e}")
        exit()

    print(account1.show_balance())
    print(account1.deposit(200))
    print(account1.withdraw(150))
    print(account1.transfer(300, account2))
    print(account2.show_balance())

    print("\n--- Testing invalid cases ---")
    print(account1.withdraw(-50))         
    print(account1.withdraw(999999))      
    print(account1.deposit("abc"))        
    print(account1.transfer(100, "not_an_account"))  
    try:
        account1.balance = -500            
    except ValueError as e:
        print(f"Error: {e}")

    try:
        account1.account_holder = ""      
    except ValueError as e:
        print(f"Error: {e}")