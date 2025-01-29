# Maping
numbers1=[1,2,3]
numbers2=[4,5,6]
result=map(lambda x , y: y+x,numbers1,numbers2)
print(list(result))

lst=[1,2,3,5,8,7,9,6,4,6]

def sq(n):
    return n*n


result=list(map(sq,lst))
print(result)