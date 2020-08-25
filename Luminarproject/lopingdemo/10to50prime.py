#prime or not

low=int(input("enter a low limit number"))
upp=int(input("enter a upp limit number"))

for i in range(low,upp+1):
    flag = 0
    for j in range(2,i):
        if(i%j==0):
            flag=1
            break
    if(flag==0):
        print("prime",i)

