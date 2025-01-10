word=input("Enter a word: ")

x=word.upper()

for i in x :
    if i == "A":
        print("A is found")
        break
    else:
        print("A not found")