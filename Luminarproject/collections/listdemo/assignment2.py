lst=[10,10,20,20,30,31,31]
newlist=[]
for i in lst:
    if i not in newlist:
        newlist.append(i)
print(newlist)