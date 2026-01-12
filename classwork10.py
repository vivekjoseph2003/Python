from abc import ABC,abstractmethod
class User(ABC):
    CURRENT_YEAR=2025
    
    def __init__(self,name,join_year):
        self.name=name
        self.join_year=join_year

    def years_on_platform(self):
        return User.CURRENT_YEAR-self.join_year

    @abstractmethod
    def role(self):
        pass

    def display_info(self):
        print(self.name+" is a "+self.role()+" and has been using the platform for "+str(self.years_on_platform())+" years.")

class Customer(User):
    def role(self):
        return "Customer"


class Vendor(User):
    def role(self):
        return "Vendor"

customer=Customer("Harry",2020)
vendor=Vendor("Chris",2018)
customer.display_info()
vendor.display_info()
