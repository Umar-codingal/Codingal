class vehicle():
    def __init__(self,model,speed):
        self.model=model
        self.speed=speed

car1=vehicle("TOYOTA",220)
car2= vehicle("mercedes",280)

print(f"{car1.model} has the max speed of {car1.speed}")
print(f"{car2.model} has the max speed of {car2.speed}")