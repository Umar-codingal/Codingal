try:
    num=int(input("Enter a number: "))
    print("the number you chose is", num)

except ValueError as ex:
    print("Exception:" , ex)