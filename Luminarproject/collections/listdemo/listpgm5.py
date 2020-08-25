lst=[1,2,3,4]
element=int(input("enter element"))
for i in lst:
    for j in lst:
        if(i+j==element):
            print(i,j)
        else:
            pass
