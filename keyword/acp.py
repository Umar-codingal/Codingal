print("Hi, YOu have some amount pending let's check")
payed=int(input("Enter the amount you payed: "))
bill= int(input("Enter the total amount to be payed: "))

if payed < bill:
    print(f"Amount due is {bill-payed}")
elif payed == bill:
    print("perfectly payed")
    pass
else:
    print("You payed extra amount")

