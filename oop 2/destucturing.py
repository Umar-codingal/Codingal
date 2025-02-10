class Employee:
    def __init__(self):
       print("Employee created") 

    def __del__(self):
        print("Employee deleted")

def createObj():
        print('Making object...')
        obj=Employee()
        print("Function end")
        return obj


print("Running function")
obj=createObj()
print("Programme end..")