class flashcards:
    def __init__(self,word,meaning):
        self.word=word
        self.meaning=meaning
    def __str__(self):
        return self.word+("+self.meaning+") 
flash=[]
print ("welcome to flashcard application")
while (True):    
    word= input ("enter a name for the flashcards") 
    meaning=input("enter the meaning")
    flash.append(flashcards(word,meaning)) 
    option=int(input("enter 0 if you want to add another flashcard,otherwise enter 1" ))
    if(option):
        break 
print ("your flashcards")
for i in flash:
    print("<",i)