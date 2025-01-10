
base = float(input("Enter the base number: "))
exponent = int(input("Enter the exponent (power): "))

result=1

if exponent >= 0:
    for i in range(exponent):
        result *= base
else:
    for i in range(-exponent):
        result *= base
    result = 1 / result  

print(f"{base} raised to the power of {exponent} is: {result}")
