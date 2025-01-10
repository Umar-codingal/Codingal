number = int(input("Enter a number: "))

if number < 0:
    number = -number


if number == 0:
    digit_count = 1
else:
    digit_count = 0

    
    while number > 0:
        number //= 10  
        digit_count += 1


print("The number of digits is:", digit_count)
