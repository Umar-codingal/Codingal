a = int(input("Enter the first number (a): "))
b = int(input("Enter the second number (b): "))
c = int(input("Enter the third number (c): "))

print(f"Before swapping: a = {a}, b = {b}, c = {c}")


d = a
a = b
b = c
c = d


print(f"After swapping: a = {a}, b = {b}, c = {c}")
