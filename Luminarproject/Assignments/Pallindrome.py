#Palindrome
#123321

num1=int(input("enter the number")) #123321
temp=num1
reverse=0
while(num1!=0):
    rem=num1%10
    #rem=>123321%10=1,12332%10=2,1233%10=3,123%10=3,12%10=2,1%10=1
    reverse=(reverse*10)+rem
    # reverse=>(0*10)+1=1,(1*10)+2=12,(12*10)+3=123,(123*10)+3=1233,(1233*10)+2=12332,(12332*10)+1=123321
    num1=num1//10
    #123321//10=12332,12332//10=1233,1233//10=123,123//10=12,12//10=1,1//10=0
if (temp==reverse):
    print("the number is palindrome")
else:
    print("the number is not palindrome")
