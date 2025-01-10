import random
print("Welcome to Rock paper Scissors")
input=input("Choose anything (rock,paper,scissors):")
input=input.upper()

options=["rock","paper","scissors"]
comp=random.choice(options)
comp=comp.upper()

if input==comp:
    print("Tie")
elif input == "ROCK":
    if comp == "PAPER":
        print("You lose :(")
    else:
        print("You win!")
elif input == "PAPER":
    if comp=="ROCK":
        print("You Win!")
    else:
        print("You lose:(")
elif input == "SCISSORS":
    if comp == "ROCK":
        print("You lose:(")
    else:
        print("You win!")
else:
    print("Invaild input")