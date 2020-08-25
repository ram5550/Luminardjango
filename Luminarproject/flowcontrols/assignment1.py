
#sorting

num1=int(input("enter value for num1"))#40
num2=int(input("enter value for num2"))#30
num3=int(input("enter value for num3"))#20

if((num1>num2)&(num1>num3)):
    if(num2>num3):
        print(num1,num2,num3,"sorted")
    else:
        print(num1,num3,num2,"sorted")
elif((num2>num1)&(num2>num3)):
    if(num1>num3):
        print(num2,num1,num3,"sorted")
    else:
        print(num2,num3,num1,"sorted")
elif((num3>num1)&(num3>num2)):
    if(num1>num2):
        print(num3,num1,num2,"sorted")
    else:
        print(num3,num2,num1)
else:
    print(num1,num2,num3,"All numbers are equal")