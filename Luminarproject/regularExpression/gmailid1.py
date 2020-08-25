from re import *
f=open("gmailid","r")
lst=[]

for data in f:
    data=data.rstrip("\n")
    rule='[a-z+A-Z+0-9]*@gmail.com'
    matcher=fullmatch(rule,data)
    if(matcher!=None):
        lst.append(data)
    else:
        pass
print(lst)