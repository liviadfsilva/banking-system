class Account:
    def __init__(self, number, client):
        self._balance = 0.0
        self.branch = "013"
        self._number = number
        self._client = client
        
    @classmethod
    def new_account(cls, client, number):
        return cls(number, client)
    
    @property
    def balance(self):
        return self._balance
    
    @property
    def number(self):
        return self._number
    
    @property
    def client(self):
        return self._client
    
    def withdrawal(self, amount):
        balance = self._balance
        not_enough_balance = amount > balance
        
        if not_enough_balance:
            print("You don't have enough balance.")
            
        elif amount <= balance:
            print("The transaction was successful. Thank you!")
            
        else:
            print("Something went wrong. Please try again.")
            
    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            print("The transaction was successful.")
        else:
            print("Something went wrong. Please try again.")
            
            
class CheckingAccount(Account):
    def __init__(self, number, client, limit=500, withdrawal_limit=3):
        super().__init__(number, client)
        self._limit = limit
        self._withdrawal_limit = withdrawal_limit
        self._withdrawals_today = 0
        
    def withdrawal(self, amount):
        reached_limit = amount > self._limit
        reached_withdrawal_limit = self._withdrawals_today >= self._withdrawal_limit
        
        if reached_limit:
            print(f"You can only withdraw up to {self._limit} at a time.")
            
        elif reached_withdrawal_limit:
            print("Sorry. You can only make a withdrawal up to 3x a day. Please try again tomorrow.")
            
        else:
            self._withdrawals_today += 1
            self._balance -= amount
            return super().withdrawal(amount)
        
    def __str__(self):
        return f"""\
            Branch:\t{self.branch}
            C/C:\t\t{self.number}
            Account Holder:\t{self.client}
        """