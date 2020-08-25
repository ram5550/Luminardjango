from re import *

#predefinedcharacter

#pattern="\s"  #it will check for spaces
#pattern="\d"  #it will check for digit[0-9]
#pattern="\D"  #it will check except the digits=[^0-9]
#pattern="\w"  #it will check for all words no special characters means'[a-zA-Z0-9]'
#pattern="\W"   #it will check except words that means special chara

matcher=finditer(pattern,"abx 7Zxy@#%")

for match in matcher:
    print(match.start())
    print(match.group())