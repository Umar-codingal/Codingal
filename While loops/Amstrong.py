num=int(input("Enter a number: "))

result=0

while num>=0:
    sum = num%10
    temp2=sum**3
    sum2=num%100
    temp3=sum2//10
    sum3= temp3**3
    temp4= num//100
    sum4= temp4**3
    result=sum4+sum3+temp2
    break


if num==result:
    print("it's an armstrong number")

else:
    print("it's a normal number")

    


