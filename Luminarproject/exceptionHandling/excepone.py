#exception handling
#try:
    #doubtful code
#except:
    #handling code

num1=int(input("enter value for num1"))
num2=int(input("enter value for num2"))
lst=[1,2,3,4,5]

try:
    res=num1/num2
#it is an abnormal code or case
    print("result=",res)


    print("we have database operation")

    print("file operation")

    print("process completed successfully")

except Exception as e: #this code gives corrct reason for excptn
    print(e.args)

try:
    pos = int(input("enter index position"))
    print(lst[pos])

except Exception as e:
    print(e.args)