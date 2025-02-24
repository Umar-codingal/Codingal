from abc import ABC,abstractmethod


class Animal(ABC):

    def move(self):
        pass


class Human(Animal):

    def move(self):
        print("I can walk and run")

class Snake(Animal):
    print("I can slither")

class lion(Animal):
    def move(self):
        print("I can roar")


h=Human()
h.move()

l=lion()
l.move()

s=Snake()
s.move()

