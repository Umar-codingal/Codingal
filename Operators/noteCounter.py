notes= int(input("Enter the amoount to withdraw: "))

hundred =int(notes/100)
fifties= int((notes%100)/50)
tens= int(((notes%100)%50)/10)


print("Number of 100 notes:" , hundred)
print("NUmber of 50 notes", fifties)
print("Number of 10 notes", tens)