inp=input("Enter a charcter: ")

alpha = False


if ('a' <= inp <= 'z') or ('A' <= inp <= 'Z'): 
    alpha=True 

if alpha:
    print("The text contains alphabetic characters.")
else:
    print("The text does not contain any alphabetic characters.")
