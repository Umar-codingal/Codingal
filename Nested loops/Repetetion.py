Str=input("Enter a string: ")
char=input("Enter a character in your string: ")

i=0
count=0

while (i<len(Str)):
    if Str[i]==char:
        count = count + 1
    i = i+1

print(f"The character, {char} is repeated {count} times.")

