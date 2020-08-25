f=open("movies.csv","r")
dict={}

for lines in f:
    #print(lines)
    #break
    data=lines.rstrip("\n").split(",")
    movies=data[1]
    rate=data[3]
    if(rate not in dict):
        dict[rate]=1
    else:
        dict[rate]+=1
for k,v in dict.items():
    print("Rating",k,"-",v,"Movies")