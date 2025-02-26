class flashcard:
    def __init__(self, word,meaning):
        self.word=word
        self.meaning=meaning
    def __str__(self):
         return f"{self.word}"+(f"{self.meaning}")
    
flash=[]
print("Welcome to flash card application")

while(True):
    word=input("Enter the word: ")
    meaning=input("Enter the meaning of the word:")
    flash.append(flashcard(word, meaning))
    option= int(input("Enter 0 to continue or enter 1: "))

    if option:
        break


print("\n your Flash card")

for i in flash:
    print(">",i)