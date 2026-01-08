class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def show_details(self):
        print("Name:",self.name)
        print("Age:",self.age)

class Employee(Person):
    def __init__(self,name,age,employee_id):
        super().__init__(name,age)
        self.employee_id=employee_id

    def show_details(self):
        print("Name:",self.name)
        print("Age:",self.age)
        print("Employee ID:",self.employee_id)

class PartTime(Person):
    def __init__(self,name,age,working_hours):
        super().__init__(name,age)
        self.working_hours=working_hours
    
    def show_details(self):
        print("Name:",self.name)
        print("Age:",self.age)
        print("Working Hours:",self.working_hours)

class Consultant(Employee,PartTime):
    def __init__(self, name, age,employee_id,working_hours,project_name):
        Employee.__init__(self,name,age,employee_id)
        PartTime.__init__(self,name,age,working_hours)
        self.project_name=project_name
    
    def show_details(self):
        print("Name:",self.name)
        print("Age:",self.age)
        print("Employee ID:",self.employee_id)
        print("Working Hours:",self.working_hours)
        print("Project Name:",self.project_name)

person1=Person("Harry",32)
employee1=Employee("Chris",35,"A123")
parttime1=PartTime("Charlie",25,20.5)
consultant1=Consultant("Diana",40,"B123",10.0,"Project")

print("Person Details:")
person1.show_details()
print("\nEmployee Details:")
employee1.show_details()
print("\nPart-Time Details:")
parttime1.show_details()
print("\nConsultant Details:")
consultant1.show_details()