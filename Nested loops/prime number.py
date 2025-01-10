lower=int(input("Enter the lower value of the range: "))
upper=int(input("Enter the highest value in the range: "))
print(f"Number in the range, {lower} to {upper} are: ")

for num in range(lower,upper +1 ):
    for i in range(2,num):
        if num%i == 0:
          break
    else:
           print(num)
       