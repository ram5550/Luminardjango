#multiplication table of a number 1*2

number=int(input("enter number to print multiplication table"))

i=1

while(i<=10):
    res=i*number
    print(i,"*",number,"=",res)
    i+=1