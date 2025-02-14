class Vehicle:
    def __init__(self,model,vehicle,tyres, mileage):
        self.model=model
        self.vehicle=vehicle
        self.tyres=tyres
        self.mileage=mileage


class bus(Vehicle):
    pass


bus1=bus("Traveller","Mini bus",4,7.5)
print(f"{bus1.model} is a {bus1.vehicle}, has {bus1.tyres} tyres and has a mileage of {bus1.mileage} km/l. ")