#print second largest

num1=int(input("enter value for num1")) #10
num2=int(input("enter value for num2")) #20
num3=int(input("enter value for num3")) #15


if((num1>num2)&(num1>num3)):
    if(num2>num3):
        print("second largest",num2)
    else:
        print("second largest",num3)
elif((num2>num1)&(num2>num3)):
    if(num1>num3):
        print("second largest",num1)
    else:
        print("second largest",num3)
elif((num3>num1)&(num3>num2)):
    if(num1>num2):
        print("second largest",num1)
else:
    print("second largest",num2)

