atten=int(input("Enter the attendence in percentage: "))
medic=input("Was there any medical reason True or False: ")

if atten<75:
    print("Atendence amount not fulfilled")
    if medic.upper == "TRUE":
        print("we will check with the authorities and come back top you.")
    else:
        print("Sorry! You are not eligible")
else:
    print("Exam date is 12.5.24")

