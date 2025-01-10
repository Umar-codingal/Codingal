print("Welcome to divisibility checker")
a= int(input("Enter a number to be divided: "))
b= int(input("Enter a number to divide: "))

if a%b ==0:
    print(f"The number {a} is divisibe by {b} and the answer is {a/b}")
else:
    print(f"The number {a} is not divisibe by {b} and the answer is {a/b}")