even=[]
odd=[]
list=[]
for i in range(50,100):
    list.append(i)
print(list)

for i in list:
    if(i%2==0):
        even.append(i)
    else:
        odd.append(i)
print("even",even)
print("odd",odd)