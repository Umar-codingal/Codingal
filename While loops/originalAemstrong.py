num=int(input("Enter a number: "))


sum=0
temp=num

while temp>0:
    no = temp%10
    sum+=no**3
    temp//=10
    

if num==sum:
    print("it's an armstrong number")

else:
    print("it's a normal number")