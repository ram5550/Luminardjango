#Q)4

line="hello hai hello hai"

words=line.split(" ")  #['hello','hai','hello,'hai']
print(words)
dict={}  #empty
for word in words:
    if(word not in dict):
        dict[word]=1
    else:
        dict[word]+=1
print(dict)
