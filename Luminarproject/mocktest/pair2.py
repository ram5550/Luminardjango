#Q)2

list=[2,3,4]
list2=[]
u=len(list)-1
for i in range(0,u):
    num=list[i],list[i+1]
    if(list not in list2):
        list2.append(num)
    num1=list[0],list[u]
    if(num1 not in list2):
        list2.append(num1)
print(list2)