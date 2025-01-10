def add(p,q):
    return (p+q)

def sub(p,q):
    return p-q

def multi(p,q):
    return p*q

def div(p,q):
    return p/q

def mod(p,q):
    return p%q

p=int(input("Enter the first number: "))
q= int(input("Enter the second number: "))

print(" select a choice (A)ddition/(S)ubstraction/(M)ultiplication/(D)ivision/(R)emainder")

a = input("Enter the first letter only:")
choice = a.upper()


if choice == "A":
    print(add(p,q))
elif choice == "S":
    print(sub(p,q))
elif choice == "M":
    print(multi(p,q))
elif choice == "D":
    print(div(p,q))
elif choice == "R":
    print(mod(p,q))
else:
    print("enter a valid input")