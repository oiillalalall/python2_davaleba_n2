class bankaccount:
    def __init__(self,owner,balance):
        self.owner = owner
        self.balance = balance

    def deposit(self,amount):
        self.balance = self.balance + amount

    def withdraw(self,amount):
        if self.balance >= amount:
            self.balance = self.balance - amount
            print(f"მოიხსნა, {amount}, დარჩენილი ბალანსი: {self.balance}")
        else:
            print(f"არ გაქ მაგდენი ძმა")

    def get_balance(self):
        print(f"ბალანსი: {self.balance}")
        return self.balance
