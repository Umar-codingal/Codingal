import array as a

ab=a.array("i",[1,2,3,5,2,2,2,2,2,1,3,3,3,3,3,3,3,2])
print(type(ab))

b=ab.count(2)
print(b)

ab.reverse()
print(ab)