class MyClass:

    __privateVar=465


    def __privFun(self):
        print("i'm inside my class")

    def hello(self):
        print("Value of private variable is: ",MyClass.__privateVar)

foo=MyClass()
foo.hello()
foo.__privFun()