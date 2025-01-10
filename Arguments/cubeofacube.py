def cube_root(num):
    return num ** (1/3)

def cube(n):
    return n *n*n

num = int(input("Enter a number:"))


if cube_root(num)%1 == 0:
    print(cube(num))
else:
    print("Enter a cube number")
