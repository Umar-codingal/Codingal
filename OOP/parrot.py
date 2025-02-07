class parrot():
    def __init__(self,breed,name,age):
        self.name=name
        self.breed = breed
        self.age=age

par1=parrot("Macaw","coco",5)
par2=parrot("African grey ","alex",10)

print(f"{par1.name} is a {par1.breed} and is {par1.age} years old")
print(f"{par2.name} is a {par2.breed} and is {par2.age} years old")