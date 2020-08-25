#Binarysearch

lst=[10,11,12,13,14,15,2,3,4]

lst.sort()
print(lst)
#[2,3,4,10,11,12,13,14,15]

low=0
upp=len(lst)-1
element=int(input("enter number to search"))#14
flg=0
while(low<=upp):#0<=9-1
    mid=(low+upp)//2 #(0+8)//2=4

    if(element>lst[mid]):#14>lst[4] 14>11
        low=mid+1 #low=4+1=5
    elif(element<lst[mid]):
        upp=mid-1
    elif(element==lst[mid]):
        flg+=1
        break
if(flg>0):
    print("element found")
else:
    print("element not found")
