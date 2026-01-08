class Employee:
    def __init__(self,name,role):
        self.name=name
        self.role=role

    def display(self):
        print("Name:",self.name)
        print("Role:",self.role)

class Trainer(Employee):
    def __init__(self,name,role,specialization):
        super().__init__(name,role)
        self.specialization=specialization

    def display(self):
        print("Name:",self.name)
        print("Role:",self.role)
        print("Specialization:",self.specialization)

class YogaInstructor(Employee):
    def __init__(self,name,role,yoga_style):
        super().__init__(name,role)
        self.yoga_style=yoga_style

    def display(self):
        print("Name:",self.name)
        print("Role:",self.role)
        print("Yoga Style:",self.yoga_style)

class MultiTrainer(Trainer,YogaInstructor):
    def __init__(self,name,role,specialization,yoga_style):
        Trainer.__init__(self,name,role,specialization)
        YogaInstructor.__init__(self,name,role,yoga_style)

    def display(self):
        print("Name:",self.name)
        print("Role:",self.role)
        print("Specialization:",self.specialization)
        print("Yoga Style:",self.yoga_style)

employee1=Employee("Harry","Receptionist")
trainer1=Trainer("Chris","Trainer","Weightlifting")
yogainstructor1=YogaInstructor("Leo","Yoga Instructor","Style")
multitrainer1=MultiTrainer("Theo","Trainer & Yoga Instructor","Cardio","Style")

print("Employee Details:")
employee1.display()
print("\nTrainer Details:")
trainer1.display()
print("\nYoga Instructor Details:")
yogainstructor1.display()
print("\nMulti-Trainer Details:")
multitrainer1.display()