def wordMatch(Words):
    ctr=0
    lst=[]
    for i in Words:
        if len(i)>1 and i[0]==i[-1]:
            ctr += 1
            lst.append(i)
    print(lst)
    return ctr

count=wordMatch(["ece","wfe","wfrwr","3564","45848484"])
print(count)
