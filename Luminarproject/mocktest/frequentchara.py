#Q1)
pattern="ABABABCAA"
print(pattern)

dict={}
for char in pattern:
    if(char in dict):
        dict[char]+=1
    else:
        dict[char]=1
print(dict)
result=max(dict,key=dict.get)
print(result)