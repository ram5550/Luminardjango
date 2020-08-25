
num=int(input("enter a number"))

sum=0
while(num!=0):
    mul=num%10
    sum=sum+(mul**3)
    num=num//10
print(sum)