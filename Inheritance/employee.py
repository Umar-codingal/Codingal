class Parent(object):
    def __init__(self,name,idnumber):
        self.name=name
        self.idnumber=idnumber

    def object(self):
        print(self.name)
        print(self.idnumber)

    
class Employee(Parent):
    def __init__(self,name,idnumber,salary, post):
        self.salary=salary
        self.post=post

        Parent.__init__(self,name,idnumber)

a=Employee("Wolfeschlegelsteinhausenbergerdorff","2805","₹2,00,000","Manager")

a.object()

