#print maximum number among 3 number

num1=int(input("enter value for num1"))#10
num2=int(input("enter valur for num2"))#20
num3=int(input("enter value for num3"))#30

if((num1>num2)&(num1>num3)):#(10>20)&(10>30)
    print("max=",num1)
elif((num2>num1)&(num2>num3)): #20>10 & 20>30
    print("max=",num2)
else:
    print("max=",num3)
