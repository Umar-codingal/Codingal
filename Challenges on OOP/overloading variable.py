class A:
    def __init__(self,a):
        self.a=a

    def __lt__(self,other):
        if (self.a<other.a):
            return "Ob 1 is smaller tha ob2"     
           
        else:
            return "Ob 2 is smaller tha ob1"
        
    def __eq__(self,other):
        if (self.a<other.a):
            return"Equal"
        else:
            return"Not equal"
        

ob1=A(2)
ob2=A(5)
print("Passed values:",ob1.a,ob2.a)

print(ob1<ob2)


