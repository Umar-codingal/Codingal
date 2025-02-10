class Dog():
    def __init__(self,breed,name,age):
        self.name=name
        self.breed = breed
        self.age=age

dog1=Dog("pomerian","tommy",2)

print(f"{dog1.name} is a {dog1.breed} and is {dog1.age} years old.")
print(f"{dog1.name} says Woof!")