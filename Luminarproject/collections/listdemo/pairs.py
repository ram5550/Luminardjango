lst=[1,2,3,4]

element=int(input("enter value")) #4
lst.sort()
#[1,2,3,4]
# l     u
low=0
upp=len(lst)-1  #4-1=3  #3-1=2
while(low<=upp): #0<=3
    data=lst[low]+lst[upp] #1+4=5  #1+3=4

    if(data==element):
        print("pairs",lst[low],",",lst[upp])
        break
    elif(data>element): #5>4
        upp=upp-1
    else:
        low=low+1
