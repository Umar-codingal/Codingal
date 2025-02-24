from abc import ABC,abstractmethod

class Absclass(ABC):


    def printing(self,x):
        print("passed value: ",x)

    
    @abstractmethod
    def task(self):
        print("We are inside Absclass")


class test(Absclass):
     def task(self):
        print("We are inside test class")

obj=test()
obj.task()
obj.printing(100)