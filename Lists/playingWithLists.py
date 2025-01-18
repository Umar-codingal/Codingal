lst= [1,2,3,8,0,49,4,6,4,2,84,1,6,4,6,8,4,6,3,4,9,4,6,4,6,8,4,7,5,6,1,6]
ctr=0
print("Original list = ",lst)

for i in lst:
    ctr+=1

print("The sum of the list is ", ctr )

avg= ctr/len(lst)

print("Sum = ", ctr)
print("average = ", avg)

lst.sort()

max=lst[-1]
min = lst[0]

print("Gretest value in the ist is", max)
print("Lowest value in the list is ", min)