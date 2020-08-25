# def add(num1,num2):
#     return num1+num2
#
# add(10,30)

#variable length argument method

# def printVal(name,location):
#     print(name)
#     print(location)
#
# printVal("ajay","kakkanad","aluva")

def add(**args):
    #args={"num1":10,"num2":20,"num3":40,"num4":50,"num5":60}
    print(args)
    result=0
    for k,v in args.items():
        result+=v
    print("res=",result)

add(num1=10,num2=20,num3=40,num4=50,num5=60)