#Fibonacci

num=int(input("enter number"))  #5
num1=0
num2=1
for i in range(num):
    print(num1)  #0  1  1  2  3
    temp=num1    #temp=0  temp=1  temp=1  temp=2
    num1=num2    #num1=1,  num1=1  num1=2  num1=3
    num2=temp+num2   #num2=0+1,  num2=1+1  num2=1+2  num2=2+3