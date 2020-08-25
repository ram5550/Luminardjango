#Q5)

lst=[1,2,3,4]

element=int(input("enter number")) #6
lst.sort()
low=0
upp=len(lst)-1
while(low<=upp):
    num=lst[low]+lst[upp]

    if(num==element):
        print("pairs",lst[low],",",lst[upp])
        break
    elif(num>element):
        upp=upp-1

    else:
        low=low+1