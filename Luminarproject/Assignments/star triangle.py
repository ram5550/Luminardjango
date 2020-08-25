#Star Triangle

num=int(input("enter the number"))
for i in range(0,num): #if num is 4 then range will be (0,4)
    for j in range(0,num-i-1):  #if num=4 then (0,4-0-1) (0,4-1-1) (0,1)
        print(end=" ")
    for j in range(0,i+1):    #(0,1) (0,2) (0,3)
        print("*",end=" ")
    print()

