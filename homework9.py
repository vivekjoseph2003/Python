class Account:
    def __init__(self,name,balance):
        self._name=name
        self._balance=balance

    def __add__(self,other):
        return self._balance+other._balance
    
class SavingsAccount(Account):
    def calculate_interest(self):
        return self._balance*0.05
    def display_details(self):
        return "Account Holder:{},Balance:{},Interest:{}".format(self._name,self._balance,self.calculate_interest())

    
class CurrentAccount(Account):
    def calculate_interest(self):
        return self._balance*0.02
    def display_details(self):
        return "Account Holder:{},Balance:{},Interest:{}".format(self._name,self._balance,self.calculate_interest())

savings=SavingsAccount("Ravi",10000)
current=CurrentAccount("Anjali",15000)

print(savings.display_details())
print(current.display_details())
total_balance=savings+current
print("Total:",total_balance)
