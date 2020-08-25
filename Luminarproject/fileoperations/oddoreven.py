f=open("numbers","r")
lst=[]
for i in f:  #100\n
    lst.append(int(i))
even=[]
odd=[]
for i in lst:
    if(i%2==0):
        even.append(i)
    else:
        odd.append(i)

print(even)
print(odd)