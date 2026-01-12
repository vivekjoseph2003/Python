from abc import ABC,abstractmethod
class User(ABC):
    CURRENT_YEAR=2025

    def __init__(self,name,account_year):
        self.name=name
        self.account_year=account_year

    def account_age(self):
        return User.CURRENT_YEAR-self.account_year

    @abstractmethod
    def get_role(self):
        pass

class Admin(User):
    def get_role(self):
        return "Admin"

    def __str__(self):
        return self.name+" is an Admin user."

class Guest(User):
    def get_role(self):
        return "Guest"

    def __str__(self):
        return self.name+" is a Guest user."

admin = Admin("Chris",2019)
guest = Guest("Harry",2022)
print(admin.get_role())
print(admin.account_age())
print(admin)
print(guest.get_role())
print(guest.account_age())
print(guest)
