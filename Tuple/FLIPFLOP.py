def palind(r):
    e= len(r)-1
    c=0
    while(e<c):
        if (r[0]!=r[e]):
            return False
        e+=-1
        c+=1
    return True

r=(1,2,3,3,2,1)

if palind(r):
    print("True")
else:
    print("False")