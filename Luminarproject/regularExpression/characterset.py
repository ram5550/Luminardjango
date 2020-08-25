from re import *

pattern='[abc]' #chck for either a,b,c

matcher=finditer(pattern,"abx 7Zxy@")

for match in matcher:
    print(match.start())
    print(match.group())