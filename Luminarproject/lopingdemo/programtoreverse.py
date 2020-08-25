#258 852

num1=int(input("enter the number"))

reverse=0
#258
while(num1!=0): #25!=0  2!=0  0!=0
    #we have to fetch last digit
    #rem=>258%10=8,25%10=5,2%10=2
    rem=num1%10
    reverse=(reverse*10)+rem # reverse=>(0*10)+8=8,(8*10)+5=85,(85*10)+2=852

    num1=num1//10  #258//10=25, 25//10=2, 2//10=0
print(reverse)