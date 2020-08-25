num1 = int(input("enter value for num1"))
num2 = int(input("enter value for num2"))
lst = [1, 2, 3, 4, 5]

try:
    res = num1 / num2
    # it is an abnormal code or case
    print("result=", res)

except Exception as e:  # this code gives corrct reason for excptn

    num1 = int(input("enter value for num1"))
    num2 = int(input("enter value for num2"))
    try:
        res=num1/num2
        print("result=",res)

    except Exception as e:
        print(e.args)

finally:  #clean up processing

    print("we have database operation")

    print("file operation")

    print("process completed successfully")