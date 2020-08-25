#Bubblesort

lst=[]
num=int(input("enter the limit"))
print("enter values")
for i in range(0,num):
    lst.append(int(input()))
print("Unsorted list",lst)  #[4 2 9]

for i in range(0,num-1):  #(0,2)
    for j in range(0,num-i-1):  #(0,3-0-1)  (0,3-1-1)
        if(lst[j]>lst[j+1]):  #4>2  4>9
            temp=lst[j]   #temp=4
            lst[j]=lst[j+1]  #lst[j]=2
            lst[j+1]=temp  #lst[j+1]=4
print("Sorted list is",lst) #[2,4,9]
