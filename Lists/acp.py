start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))

squares = []
even_values = []
odd_values = []

for num in range(start, end + 1):
    square = num ** 2
    squares.append(square)
    if square % 2 == 0:
        even_values.append(square)
    else:
        odd_values.append(square)

print("Square values:", squares)
print("Even square values:", even_values)
print("Odd square values:", odd_values)