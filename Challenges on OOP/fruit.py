import random

class Quiz:
    def __init__(self):


        self.fruits={"apple":"red","grapes":"green","orange":"orange","Banana":"yellow"}

    def quiz(self):
         
         while(True):
            fruit, colour=random.choice(list(self.fruits.items()))
            print(f"What is the colour of {fruit}")
            userAnswer= input()
            if (userAnswer.lower()==colour):
                print("Correct")

            else:
                print("incorrect")


print("welcome")

Quiz().quiz()