import random
valid= True
number = str(random.randint(0,9))

print("I will generate a random number between 0 and 9 you have to guess it.YOu win when you get 1 hero")
guess= input("Guess the number: ")

while valid:
    if number == guess:
        print("You win!")
        break
    else:
        print("Try again")
        