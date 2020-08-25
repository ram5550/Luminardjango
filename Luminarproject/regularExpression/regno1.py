from re import *
f=open("regno","r")
lst=[]


for data in f:
    data=data.rstrip("\n")
    rule = '[Kk][Ll][0-9]{2}[a-z]{2}\d{4}'
    matcher=fullmatch(rule,data)
    if(matcher!=None):
        lst.append(data)
    else:
        pass
print(lst)


