character = input("Enter a character: ")


if len(character) != 1:
    print("Please enter only a single character.")
else:
    ascii_value = ord(character)
    print(f"The ASCII value of '{character}' is {ascii_value}.")

