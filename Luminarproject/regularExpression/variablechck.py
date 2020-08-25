#1)first character is an alphabet and it should be with a-k
#2)second should be a digit and it must divisible by 3
#3)and then any numbr of character

from re import *
rule='[a-k][369][a-zA-Z0-9]*' #THIS ORDER MUST *->any chara inside that bracket

varname=input("enter variable name")

matcher=fullmatch(rule,varname)

if(matcher !=None):
    print("valid")

else:
    print("invalid")