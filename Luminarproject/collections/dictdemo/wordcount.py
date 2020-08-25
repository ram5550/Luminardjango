line="hai hello hai hello"

words=line.split(" ")  #['hai', 'hello', 'hai', 'hello']
print(words)
dict={}  #empty
for word in words:
    if(word not in dict):
        dict[word]=1
    else:
        dict[word]+=1
print(dict)
