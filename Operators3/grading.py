one=int(input("Enter you marks for the first subject: "))
two=int(input("Enter you marks for the second subject: "))
three=int(input("Enter you marks for the third subject: "))
four= int(input("Enter you marks for the fourth subject: "))
five= int(input("Enter you marks for the fifth subject: "))

tot = one+two+three+four+five
per = tot/500 *100

print("Your percantage are: ",per)
print("Your grade is: ")

if 95<=per<=100:
    print("A*")
elif 90<=per<=94.9:
    print("A")
elif 89<= per<= 85.9:
    print("A-")
elif 80<= per <= 84.9:
    print("B")
elif 70<= per <=79.9:
    print("C")
elif 60<= per<=69.9:
    print("D")
