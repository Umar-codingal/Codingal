import math 

lst1=[1,4,5,9,25,121,44,6,7,8]

lst2=[]


for i in lst1:
    if type(math.sqrt(i))==float:   
     pass
     if math.sqrt(i)%10==0:
        lst2.append(i)  
     
    
print(lst2)




