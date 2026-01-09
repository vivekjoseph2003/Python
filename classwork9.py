class Vehicle:
    def __init__(self,_vehicle_id,_base_rate):
        self._vehicle_id=_vehicle_id
        self._base_rate=_base_rate

    def display_details(self):
        return "Vehicle ID:{},Base Rate:{}".format(self._vehicle_id,self._base_rate)
    def rental_charge(self):
        return 0.0
    
class Car(Vehicle):
    def __init__(self,_vehicle_id,_base_rate,num_seats):
        super().__init__(_vehicle_id,_base_rate)
        self.num_seats=num_seats

    def rental_charge(self):
        return self._base_rate*self.num_seats

class Bike(Vehicle):
    def __init__(self,vehicle_id,base_rate,bike_type):
        super().__init__(vehicle_id,base_rate)
        self.bike_type=bike_type

    def rental_charge(self):
        return self._base_rate*0.5

def calculate_rental(vehicle):
    return vehicle.rental_charge()

car=Car("CAR001",100.00,4)
bike=Bike("BIKE001",100.00,"Scooter")
print(car.display_details())
print("Car Rental Charge:",calculate_rental(car))
print(bike.display_details())
print("Bike Rental Charge:",calculate_rental(bike))