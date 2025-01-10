unt=int(input("Enter the number of units used by you  in a month: "))

amt=0
tax=0

if (unt<50):
    amt=unt*2.60
    tax=25
elif(unt<=100):
    amt=130+(unt-50)*3.25
else:
    print("price is the same as the last year.")

bill=amt+tax

print(bill)