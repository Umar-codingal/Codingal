CP=int(input("Enter the Cost price: "))
MRP=int(input("Enter the MRP: "))
SP=int(input("Enter the selling price: "))

if (SP-CP>0):
    print(F"The profit is ₹{SP-CP} ")
else:
    print("It's a loss")

dis= ((MRP-SP)/MRP)*100

if dis > 0:
    print(f"You've got {dis}% discount")
else:
    print("No discount was given")