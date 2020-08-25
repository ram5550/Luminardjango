from re import *

#predefinedcharacterset

#pattern='[a-z]' #chck for lowercase a to z characters
#pattern='[A-Z]'  #chck for uppercase A to Z characters
#pattern='[a-zA-Z]'
#pattern='[a-kA-Z]'
#pattern='[0-9]'
#pattern='[^0-9]' # ^ --> THIS SYMBOL MEANS EXCEPT
#pattern='[^a-zA-Z0-9]' #special characters only

matcher=finditer(pattern,"abx 7Zxy@#%")

for match in matcher:
    print(match.start())
    print(match.group())