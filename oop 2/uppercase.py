class String:
    def __init__(self):
       self.str1=""

    def get_string(self):
        self.str1=input("Enter a string: ")
    
    def printing(self):
        print(f"The changed string is {self.str1.upper()}")
    
str1=String()

str1.get_string()
str1.printing()