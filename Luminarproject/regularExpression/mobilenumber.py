#validate all mobile number

from re import *

rule='\d{10}' #'[0-9]'='\d'
mobno=input("enter mob no")
matcher=fullmatch(rule,mobno)

if(matcher!=None):
    print("valid mob no")

else:
    print("invalid mob no")