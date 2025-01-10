print("Welcome to Uber")
print("Choose your vehicle")
print("1. Car")
print("2. Two-wheeler")

moto=int(input("Enter the number of the vehicle you need"))

if moto == 1:
    print("Which cars do you want:")
    print("1. sedan")
    print("2. SUV")
    choice1=int(input("Enter the type of car you want:"))
    if choice1==1:
        print('Your honda city will be arriving soon')
    else:
        print("Your Innova will be arriving soon.")
elif moto==2:
     print("Which two-wheeler do you want:")
     print("1. Scooty")
     print("2. bike")
     choice2=int(input("Enter the type of bike you want:"))
     if choice2==1:
        print('Your activa will be arriving soon')
     else:
        print("Your splendor will be arriving soon.")     
else:
    print("Give a valid value.")


