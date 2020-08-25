
import re
#pattern="a+"
#pattern="a*" #any number of including 0 no.of a
#pattern="a?"
#pattern="a{2}" #chck for 2 number of a
pattern="a{2,3}" #chck for min 2 no.of a max 3 no.of a

matcher= re.finditer(pattern,"aabaaaabbabbaaaa")
count=0
for match in matcher:
    print(match.start())
    print(match.group())

    count+=1
print("count",count)