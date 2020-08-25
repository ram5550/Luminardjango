#validte abc12@gmail.com

from re import *

rule='\w*@gmail.com'
id=input("enter gmail id")

matcher=fullmatch(rule,id)

if(matcher!=None):
    print("valid mail id")
else:
    print('invalid mail id')