#for pattern matching

#step1 we have to import re module

import re

matcher= re.finditer("ab","abababababababab")
count=0
for match in matcher:
    print(match.start())
    print(match.group())

    count+=1
print("count",count)