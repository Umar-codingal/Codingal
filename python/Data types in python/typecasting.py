a= 125
b= "23145698"
c= 12.05
d= True

print("the type of a is", type(a))
a += float(a)
print("The new type of a is", type(a))

print("the type of b is", type(b))
print("The new type of b is not possible", type(b))

print("the type of c is", type(c))
c += int(c)
print("The new type of  cis", type(c))

print("the type of d is", type(d))
print("The new type of d is not possible", type(d))